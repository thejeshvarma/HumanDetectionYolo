import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO
from sendimg import send_message, send_photo
import time
import asyncio
import os
from asyncio import TimeoutError

# Load the model
model = YOLO("yolo11n.pt")

async def send_with_retry(message, image_path=None, max_retries=3):
    for attempt in range(max_retries):
        try:
            await send_message(message)
            if image_path:
                await send_photo(image_path)
            return True
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {str(e)}")
            if attempt < max_retries - 1:
                await asyncio.sleep(1)  # Wait before retry
    return False

cap = cv2.VideoCapture(0)
plt.ion()
fig, ax = plt.subplots()

last_sent_time = 0
temp_image_path = "temp_detection.jpg"

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    
    current_time = time.time()
    for detection in results[0].boxes:
        cls_id = int(detection.cls[0].item())
        class_name = results[0].names[cls_id]
        if class_name == "person":
            if current_time - last_sent_time >= 3:
                cv2.imwrite(temp_image_path, frame)
                success = asyncio.run(send_with_retry(
                    "Alert!! : Human Movement Detected",
                    temp_image_path
                ))
                if success:
                    last_sent_time = current_time
            break
    
    annotated_frame = results[0].plot()
    ax.clear()
    ax.imshow(cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB))
    plt.pause(0.001)

cap.release()
cv2.destroyAllWindows()

if os.path.exists(temp_image_path):
    os.remove(temp_image_path)
