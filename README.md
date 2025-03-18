# -HandPoseNormalizer
HandPoseNormalizer - A powerful hand image processing pipeline that detects, normalizes, aligns, and centers hands using MediaPipe &amp; OpenCV. Perfect for gesture analysis, biometric research, and time-lapse visualization.

### **🚀 Hand Image Normalization & Alignment Pipeline**
# 🖐️ **Perfectly Aligned Hand Tracking & Analysis Tool**  

Do you have a **collection of hand images** captured at different angles, sizes, and positions? 📸 Do you want to **standardize them for precise analysis or cool visualizations**?  

This project **automatically detects, normalizes, aligns, and centers hands** in images—making them **consistent in size, orientation, and position**! Whether you're tracking **hand evolution over time**, preparing images for **biometric analysis**, or creating **smooth hand motion videos**, **this is the perfect tool for you!** 🎯  

---

## **✨ Features**
✔ **Fully Automated Pipeline** – Just give it a folder of hand images, and it does the rest!  
✔ **Hand Detection** – Uses **MediaPipe Hands** for accurate hand keypoint extraction.  
✔ **Size Normalization** – Standardizes hand size based on **middle finger length**.  
✔ **Rotation Alignment** – Ensures all hands are **perfectly oriented** with fingers pointing up.  
✔ **Hand Centering** – Moves hands to the **center of the frame**, keeping them perfectly aligned.  
✔ **Rotation Variants** – Generate images at different **rotation angles** for analysis.  
✔ **Customizable Parameters** – Adjust **reference hand size, rotation angles, and image dimensions**.  
✔ **Ready for Machine Learning** – Produces **clean, consistent data** for gesture recognition & biometrics.  
✔ **Supports Batch Processing** – Handles **hundreds of images in one go**.  

---

## **🔬 Use Cases**
🖐️ **Hand Motion Tracking** – Observe how a hand evolves over time.  
📊 **Biometric & Forensic Analysis** – Standardize hand data for fingerprint or palm recognition.  
🎨 **Art & Animation** – Generate **consistent hand references** for animation & design.  
🖥️ **Gesture Recognition & AI Training** – Clean dataset for **machine learning & deep learning models**.  
📱 **Sign Language Research** – Normalize hands for **gesture-based communication analysis**.  
🎥 **Smooth Time-Lapse Videos** – Create **morphing hand transformations over time**.  

---

## **📂 Folder Structure**
```
📁 dataset/photos              # Original input images  
📁 output/               # Processed images  
 ├── resized_photos/    # Step 1: Resized to a fixed dimension  
 ├── normalized_photos/ # Step 2: Hand size normalization  
 ├── aligned_photos/    # Step 3: Rotated so fingers always point up  
 ├── centered_photos/   # Step 4: Centered for perfect positioning  
```

---

## **🚀 How It Works**
The script follows **5 powerful steps** to transform any set of hand images into **perfectly aligned datasets**:  

### **1️⃣ Resize Images**
- Ensures all images have a **consistent starting size** for processing.  

### **2️⃣ Detect Hand Keypoints**
- Uses **MediaPipe Hands** to extract 21 keypoints **per hand**.  

### **3️⃣ Normalize Hand Size**
- Uses the **middle finger length** as a reference to ensure **size consistency**.  

### **4️⃣ Rotate Hands for Perfect Orientation**
- Rotates each hand so the **middle finger always points upwards**.  
- Can generate **multiple rotation variants** (0° to 360°).  

### **5️⃣ Center Hands in the Frame**
- Moves the hand to the **exact center** for precise alignment.  
- No more **hands cut off at the edges**!  

---

## **🛠 Installation & Setup**
### **📌 Prerequisites**
- Python 3.7+
- OpenCV (`cv2`)
- MediaPipe
- NumPy
- Matplotlib
- Natsort

### **📌 Install Dependencies**
```bash
pip install opencv-python mediapipe numpy matplotlib natsort
```

### **📌 Run the Script**
```bash
python process_hand_images.py
```
*(Make sure to update `image_folder` and `output_folder` paths inside the script.)*  

---

## **⚙ Configuration**
| Parameter        | Description                                      | Default |
|-----------------|--------------------------------------------------|---------|
| `image_folder`  | Path to the folder containing input images       | `"dataset/photos"` |
| `output_folder` | Path to save processed images                    | `"output"` |
| `rotate_angle`  | Rotation alignment angle (0-360°)                | `30` |
| `ref_length`    | Standard hand size (middle finger length in px) | `600` |
| `final_size`    | Output image size (width, height)                | `(1000, 1280)` |

*(Adjust these parameters in `process_hand_images()` to customize the processing.)*

---

## **📽️ Create Smooth Hand Transition Video**
Once all images are **standardized**, generate a **smooth time-lapse video**:
```bash
python frame2video.py
```

---

## **🌟 Example Results**
| **Before** 🟥 | **After** 🟩 |
|--------------|--------------|
| Hand images with **random sizes, angles, and positions** | **Perfectly aligned, normalized, and centered hands** |


---

🚀 **Standardize your hand images today – for AI, research, or just pure fun!** 🚀  

---
