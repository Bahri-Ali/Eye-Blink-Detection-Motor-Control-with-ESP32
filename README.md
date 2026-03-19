# Eye Blink Detection & Servo Control with ESP32

## Description
This project uses **MediaPipe Face Mesh** and **OpenCV** to detect the user's eye status (open or closed) in real-time via webcam. When eyes are closed, the system sends a signal to an **ESP32** board to control a **servo motor** and LEDs.  
It is designed for educational purposes and demonstrates **real-time human-computer interaction** using computer vision and microcontroller control.

## Features
- Real-time eye blink detection  
- Servo motor moves based on eye status  
- LEDs indicate eye state (red = closed, green = open)  
- Efficient serial communication to ESP32  
- Visual feedback with eye contour drawn on webcam feed  

## Requirements
- Python 3.10+  
- OpenCV  
- MediaPipe  
- PySerial  
- ESP32 board with Servo motor and LEDs  
- USB data cable  

## Installation

```bash
# Clone the repository
git clone git@github.com:Bahri-Ali/Eye-Blink-Detection-Motor-Control-with-ESP32.git
cd Eye-Blink-Detection-Motor-Control-with-ESP32

# Create virtual environment
python -m venv cv_env
source cv_env/bin/activate  # Linux/macOS
cv_env\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run the project
python aa.py
