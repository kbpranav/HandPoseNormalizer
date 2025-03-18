import cv2
import mediapipe as mp
import numpy as np
import os
import matplotlib.pyplot as plt
from natsort import natsorted

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def process_hand_images(image_folder, ref_image_path, output_folder, rotate_angle=30, ref_length=600):
    """
    Processes all images by:
    - Resizing to match the reference image dimensions.
    - Detecting keypoints using MediaPipe.
    - Normalizing hand size based on middle finger length.
    - Aligning the middle finger to point up.
    - Centering the hand in the image frame.

    Args:
        image_folder (str): Folder containing input images.
        ref_image_path (str): Path to the reference image.
        output_folder (str): Folder to save processed images.
        ref_length (int): Reference middle finger length in pixels for normalization.

    Returns:
        None
    """

    # Load the reference image to get dimensions
    # ref_image = cv2.imread(ref_image_path)
    ref_height, ref_width = 1280, 1000
    print(f"Reference Image Size: {ref_width}x{ref_height}")

    # Create output folders
    resized_folder = os.path.join(output_folder, "resized_photos")
    normalized_folder = os.path.join(output_folder, "normalized_photos")
    aligned_folder = os.path.join(output_folder, "aligned_photos")
    centered_folder = os.path.join(output_folder, "centered_photos")

    os.makedirs(resized_folder, exist_ok=True)
    os.makedirs(normalized_folder, exist_ok=True)
    os.makedirs(aligned_folder, exist_ok=True)
    os.makedirs(centered_folder, exist_ok=True)

    hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5)
    file_count = 0
    for filename in sorted(os.listdir(image_folder)):
        file_count += 1
        if not filename.endswith(('.jpg', '.jpeg', '.png')):
            continue  # Skip non-image files
        
        image_path = os.path.join(image_folder, filename)

        # Step 1: Resize images to reference dimensions
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error loading {filename}")
            continue

        resized_image = cv2.resize(image, (ref_width, ref_height))
        # resized_path = os.path.join(resized_folder, filename)
        # cv2.imwrite(resized_path, resized_image)

        # Convert to RGB for MediaPipe
        image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

        # Step 2: Detect hand keypoints
        results = hands.process(image_rgb)

        if not results.multi_hand_landmarks:
            print(f"No hand detected in {filename}")
            continue

        for hand_landmarks in results.multi_hand_landmarks:
            # Extract keypoints
            keypoints = []
            h, w, _ = resized_image.shape
            for lm in hand_landmarks.landmark:
                keypoints.append((lm.x * w, lm.y * h))  # Convert normalized coords to pixels

            keypoints = np.array(keypoints)
            mp_drawing.draw_landmarks(resized_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            # Step 3: Normalize hand size based on middle finger length
            knuckle = keypoints[9]
            fingertip = keypoints[12]
            current_length = np.linalg.norm(fingertip - knuckle)

            scale_factor = ref_length / current_length
            keypoints_scaled = knuckle + (keypoints - knuckle) * scale_factor

            transformation_matrix, _ = cv2.estimateAffinePartial2D(keypoints[:, None, :], keypoints_scaled[:, None, :])

            normalized_image = cv2.warpAffine(resized_image, transformation_matrix, (w, h), borderMode=cv2.BORDER_REPLICATE)
            # normalized_path = os.path.join(normalized_folder, filename)
            # cv2.imwrite(normalized_path, normalized_image)

            # Step 4: Align the middle finger to point up
            delta_x, delta_y = fingertip - knuckle
            current_angle = np.degrees(np.arctan2(delta_x, -delta_y))

            rotation_needed = current_angle - rotate_angle
            image_center = (w // 2, h // 2)

            rotation_matrix = cv2.getRotationMatrix2D(image_center, rotation_needed, 1)
            aligned_image = cv2.warpAffine(normalized_image, rotation_matrix, (w, h), borderMode=cv2.BORDER_REPLICATE)
            # aligned_path = os.path.join(aligned_folder, filename)
            # cv2.imwrite(aligned_path, aligned_image)

            # Step 5: Center the hand in the image frame
            keypoints_rotated = cv2.transform(keypoints_scaled.reshape(-1, 1, 2), rotation_matrix).reshape(-1, 2)
            new_centroid = np.mean(keypoints_rotated, axis=0)
            print(new_centroid)

            translation_x =  image_center[0] - new_centroid[0] 
            translation_y =  image_center[1] - new_centroid[1] 

            # print(f"Translation: {translation_x}, {translation_y}")

            translation_matrix = np.array([[1, 0, translation_x], [0, 1, translation_y]], dtype=np.float32)
            centered_image = cv2.warpAffine(aligned_image, translation_matrix, (w, h), borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))

            centered_path = os.path.join(centered_folder, f"image{file_count}_{rotate_angle}{os.path.splitext(filename)[1]}")
            cv2.imwrite(centered_path, centered_image)


            print(f"Processed and saved: {filename}")


    print("\nAll images have been processed successfully!")

# Run the function
image_folder = "dataset/photos"
ref_image_path = os.path.join(image_folder, os.listdir(image_folder)[0])
output_folder = "rotate_output"

os.makedirs(output_folder, exist_ok=True)

process_hand_images(image_folder, ref_image_path, output_folder, rotate_angle=30)

# for i in range(0, 360, 5):
#     process_hand_images(image_folder, ref_image_path, output_folder, rotate_angle=i)
