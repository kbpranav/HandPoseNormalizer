import cv2
import os
import numpy as np
from natsort  import natsorted

def blend_frames(frame1, frame2, alpha):
    """
    Blends two frames using a weighted sum (Cross-Dissolve effect).

    Args:
        frame1 (np.array): First image (starting frame).
        frame2 (np.array): Second image (next frame).
        alpha (float): Blending weight (0 to 1).

    Returns:
        np.array: Blended frame.
    """
    return cv2.addWeighted(frame1, 1 - alpha, frame2, alpha, 0)

def create_smooth_transition_video(image_folder, output_video_path, fps=10, transition_frames=5):
    """
    Creates a smooth transition video from centered hand images with blending.

    Args:
        image_folder (str): Path to the folder containing centered hand images.
        output_video_path (str): Path to save the output video.
        fps (int): Frames per second for the video.
        transition_frames (int): Number of intermediate frames between images.
    
    Returns:
        None
    """
    # Get list of images sorted by filename
    images = [img for img in os.listdir(image_folder) if img.endswith(('.jpg', '.png', '.jpeg'))]
    images = natsorted(images)
    print(images)

    if not images:
        print("No images found in the folder!")
        return

    # Load first image to get dimensions
    first_image_path = os.path.join(image_folder, images[0])
    first_image = cv2.imread(first_image_path)
    height, width, layers = first_image.shape

    # Define video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use MP4 format
    video = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    print(f"Creating video: {output_video_path} at {fps} FPS with {transition_frames} transition frames per step.")

    # Iterate over images and blend transitions
    for i in range(len(images) - 1):
        img1_path = os.path.join(image_folder, images[i])
        img2_path = os.path.join(image_folder, images[i + 1])

        frame1 = cv2.imread(img1_path)
        frame2 = cv2.imread(img2_path)

        if frame1 is None or frame2 is None:
            print(f"Skipping corrupted image: {images[i]}")
            continue
        
        # Resize to ensure consistency
        frame1 = cv2.resize(frame1, (width, height))
        frame2 = cv2.resize(frame2, (width, height))

        # Write original frame
        video.write(frame1)

        # Generate transition frames
        for j in range(1, transition_frames + 1):
            alpha = j / transition_frames
            blended_frame = blend_frames(frame1, frame2, alpha)
            video.write(blended_frame)

    # Add the final frame
    last_frame = cv2.imread(os.path.join(image_folder, images[-1]))
    last_frame = cv2.resize(last_frame, (width, height))
    video.write(last_frame)

    # Release video writer
    video.release()
    print(f"Smooth transition video saved successfully: {output_video_path}")

# Run the function to create the transition video
image_folder = "output/centered_photos/"
output_video_path = "output/smooth_hand_transition.mp4"
create_smooth_transition_video(image_folder, output_video_path, fps=10, transition_frames=2)
