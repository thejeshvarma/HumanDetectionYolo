# 🚀 AI-Powered Real-Time Human Detection & Telegram Alerts  

This project uses **YOLO (You Only Look Once)** and **OpenCV** to detect humans in real-time from a webcam feed. Upon detection, an alert message and image are sent to a specified **Telegram chat** via a bot.  

## 🔥 Features  
✅ **Live Video Monitoring** – Captures frames using OpenCV  
✅ **AI-Powered Detection** – Uses YOLO for real-time human detection  
✅ **Instant Telegram Alerts** – Sends messages & images upon detection  
✅ **Automatic Retry** – Ensures successful message delivery  
✅ **Annotated Display** – Shows detected objects in real-time  

---

## 🛠 Tech Stack  
- **Python** – Main programming language  
- **YOLO** – Deep learning object detection model  
- **OpenCV** – Image and video processing  
- **Matplotlib** – Visualization of detected frames  
- **Telegram Bot API** – Sending alerts  

---

## 🚀 Installation & Setup  

### 1️⃣ Clone this Repository  
```bash
git clone https://github.com/yourusername/surveillance-bot.git
cd surveillance-bot
```

### 2️⃣ Install Dependencies  
Make sure you have Python installed, then install the required packages:  
```bash
pip install ultralytics opencv-python matplotlib python-telegram-bot asyncio
```

### 3️⃣ Set Up Telegram Bot  
- Create a Telegram bot via [BotFather](https://t.me/BotFather) and get the **BOT_TOKEN**.  
- Get your **CHAT_ID** using [this guide](https://t.me/getmyid_bot).  

### 4️⃣ Run the Project  
Replace `BOT_TOKEN` and `CHAT_ID` in `sendimg.py`, then execute:  
```bash
python surveillance.py
```

---

## 📌 File Structure  
```
/surveillance-bot
│── surveillance.py   # Main script for human detection
│── sendimg.py        # Handles sending images/messages via Telegram
│── yolo11n.pt        # YOLO model weights
│── requirements.txt  # Dependencies list
│── README.md         # Project documentation
```

---

## 🎯 How It Works  
1️⃣ **Starts the webcam** and continuously captures frames.  
2️⃣ **Uses YOLO to detect humans** in real time.  
3️⃣ **If a human is detected**, saves the frame as an image.  
4️⃣ **Sends an alert** (message + image) via Telegram.  
5️⃣ **Automatically retries** if the message fails.  

---

## 🔮 Future Enhancements  
🔹 **ESP32-CAM Integration** – Bring IoT to CCTV surveillance  
🔹 **Cloud Storage** – Store detected images securely  
🔹 **Face Recognition** – Differentiate between known & unknown persons  
🔹 **Mobile App Notifications** – Enhance real-time security alerts  

---

Feel free to **fork, modify, and contribute**! 🚀  

#AI #ComputerVision #YOLO #MachineLearning #OpenCV #TelegramBot #SmartSecurity #IoT #ESP32CAM #Innovation
