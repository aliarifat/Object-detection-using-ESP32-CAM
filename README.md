# Object-detection-using-ESP32-CAM
# 🎯 Object Detection using ESP32-CAM

## 📖 Overview

Hello, friends! I hope you're all doing well. Today, we will explore an exciting image processing project using the ESP32-CAM for object detection.

This project combines **ESP32-CAM**, **OpenCV**, and **YOLO (You Only Look Once)** to build a real-time object detection system. The ESP32-CAM captures images and serves them over Wi-Fi, while a Python application processes these images to detect objects and draw bounding boxes.

The ESP32-CAM acts as a lightweight image server, and all heavy computation is handled on a computer, making this system efficient and beginner-friendly.

---

## 🚀 Applications

- 🏠 Home security systems  
- 🐾 Wildlife monitoring  
- 🏭 Industrial object tracking  
- 📦 Smart inventory systems  
- 🚗 Traffic monitoring  

---

## 🧩 System Architecture

The system consists of two main components:

### 🔹 ESP32-CAM
- Captures images using onboard camera  
- Runs a web server  
- Serves images via HTTP endpoint  

### 🔹 Computer (YOLO + OpenCV)
- Fetches images from ESP32-CAM  
- Processes images using YOLO  
- Detects objects and draws bounding boxes  

### 🔹 Data Flow
ESP32-CAM → WiFi HTTP Server → Python Client → OpenCV → YOLO → Object Detection Output

---

## 🔄 Workflow

### 1. ESP32-CAM Setup
- Connects to Wi-Fi  
- Starts HTTP server  
- Serves images at:
- 
---

## 🔄 Workflow

### 1. ESP32-CAM Setup
- Connects to Wi-Fi  
- Starts HTTP server  
- Serves images at:
- http://<ESP32_IP>/cam-hi.jpg
- 
### 2. Image Retrieval
- Python script fetches images continuously  
- Converts them into usable format  

### 3. Image Processing
- OpenCV decodes and processes images  
- Prepares frames for YOLO  

### 4. Object Detection
- YOLO detects objects in the image  
- Generates bounding boxes and labels  

### 5. Output Display
- Displays annotated frames  
- Prints detected objects in terminal  

---

## 🧰 Hardware Requirements

| Component | Quantity |
|----------|--------|
| ESP32-CAM Module | 1 |
| FTDI USB-to-Serial Converter | 1 |
| Jumper Wires | ~5 |
| Micro USB Cable | 1 |

---

## 🔌 Circuit Connections

| ESP32-CAM | FTDI |
|----------|------|
| VCC | 5V |
| GND | GND |
| U0R | TX |
| U0T | RX |
| IO0 | GND (for flashing) |

> ⚠️ After uploading code, disconnect IO0 from GND and reset the board.

---

## 💻 Project Files

- `esp32_cam_basic.ino` → ESP32-CAM firmware  
- `object_detection.py` → Python detection script  
- `YOLO/` → Folder containing model files  
- `yolov3.weights`  
- `yolov3.cfg`  
- `coco.names`  

---

## ⚙️ Setup Instructions

### 1. ESP32-CAM
- Install ESP32 board in Arduino IDE  
- Upload firmware (`esp32_cam_basic.ino`)  
- Open Serial Monitor  
- Copy the IP address  

---

### 2. Python Environment
- Install Python (recommended: Python 3.8 / 3.9)  
- Create a virtual environment  
- Install required libraries (OpenCV, NumPy)  

---

### 3. YOLO Model Setup
- Download YOLO model files  
- Place them inside the `YOLO/` folder  
- Ensure correct file paths in the Python script  

---

### 4. Run the Project
- Update ESP32-CAM IP in Python script  
- Run `object_detection.py`  
- Ensure both devices are on the same network  

---

## 📸 Results

### Sample Detections

![Person](images/person.png)
![Remote](images/remote.png)
![Books](images/books.png)
![Laptop](images/laptop.png)
![Phone](images/phone.png)

---

## ⚡ Performance Tips

- Ensure proper lighting conditions  
- Keep camera stable  
- Adjust confidence thresholds for better detection  
- Use smaller YOLO models for faster performance  

---

## 🔧 Limitations

- Performance depends on lighting conditions  
- Requires external computer for processing  
- Large model files (weights) cannot be hosted directly on GitHub  
- Detection accuracy depends on dataset (COCO)  

---

## 🧪 Testing

- Power up ESP32-CAM  
- Run Python script  
- Verify detection results on screen  
- Check terminal output for detected objects  

---
<img width="596" height="444" alt="person_detection3" src="https://github.com/user-attachments/assets/723edfd1-0c26-4528-8391-fde07f57fc7f" />



## 🛠️ Troubleshooting

- Ensure stable power supply to ESP32-CAM  
- Verify correct IP address  
- Check Wi-Fi connectivity  
- Use virtual environment to avoid library conflicts  
- Press RST button if upload issues occur  

---

## 📌 Summary

This project demonstrates how to integrate **ESP32-CAM**, **OpenCV**, and **YOLO** for real-time object detection. By offloading heavy computation to a computer, the system remains efficient while delivering powerful AI capabilities.

It serves as a strong foundation for building advanced IoT-based vision systems.

---

## 📚 References

- https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers  
- https://github.com/yoursunny/esp32cam  
- https://ftdichip.com/drivers/  
- https://www.theengineeringprojects.com  
- https://circuitdigest.com  
- https://forum.edgeimpulse.com  
- https://how2electronics.com  

---

## 🤝 Contributing

Contributions are welcome! Feel free to improve performance, add features, or enhance the project.
