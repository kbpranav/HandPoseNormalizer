import cv2
import os

# Input and output directories
video_folder = "dataset/videos"  # Change this to your folder containing videos
output_folder = "dataset/extracted_frames"
os.makedirs(output_folder, exist_ok=True)

# Frame extraction settings
frame_interval = 0.5  # Save every 10th frame (adjust as needed)

# Process each video in the folder
for video_file in os.listdir(video_folder):
    if video_file.endswith((".mp4", ".avi", ".mov", ".mkv")):
        video_path = os.path.join(video_folder, video_file)
        cap = cv2.VideoCapture(video_path)
        count = 0
        frame_id = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            if count % frame_interval == 0:  # Save every nth frame
                frame_filename = f"{os.path.splitext(video_file)[0]}_frame{frame_id:04d}.jpg"
                frame_path = os.path.join(output_folder, frame_filename)
                cv2.imwrite(frame_path, frame)
                frame_id += 1

            count += 1

        cap.release()
        print(f"Frames extracted from {video_file}")

print("Frame extraction completed!")
