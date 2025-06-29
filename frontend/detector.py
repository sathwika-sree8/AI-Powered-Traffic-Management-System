
import cv2
import easyocr
import sqlite3
from datetime import datetime
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
import os

# Load models
model = YOLO("backend/models/yolov8n.pt")  # Make sure the path is correct
ocr = easyocr.Reader(['en'])
tracker = DeepSort()
# Create database directory if it doesn't exist
if not os.path.exists("database"):
    os.makedirs("database")
# Connect to SQLite database
conn = sqlite3.connect("database/violations.db", check_same_thread=False)
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS violations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        license_plate TEXT,
        violation TEXT,
        time TEXT
    )
''')

def detect_violations(video_path):
    cap = cv2.VideoCapture(video_path)
    logs = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(frame, conf=0.5)
        detections = results[0].boxes.data.cpu().numpy()
        names = results[0].names

        objects = []
        for det in detections:
            x1, y1, x2, y2 = map(int, det[:4])
            conf = float(det[4])
            cls = int(det[5])
            label = names[cls]
            if label in ["person", "motorcycle", "helmet"]:
                objects.append(([x1, y1, x2 - x1, y2 - y1], conf, label))

        tracks = tracker.update_tracks(objects, frame=frame)

        for track in tracks:
            if not track.is_confirmed():
                continue

            l, t, r, b = map(int, track.to_ltrb())
            crop = frame[t:b, l:r]

            # Logic for violation: person + bike, but no helmet
            person = any(obj[2] == "person" for obj in objects)
            helmet = any(obj[2] == "helmet" for obj in objects)
            bike = any(obj[2] == "motorcycle" for obj in objects)

            if person and bike and not helmet:
                try:
                    plate_text = ocr.readtext(crop)
                    plate = plate_text[0][1] if plate_text else "UNKNOWN"
                except:
                    plate = "UNKNOWN"

                time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Save to DB
                c.execute(
                    "INSERT INTO violations (license_plate, violation, time) VALUES (?, ?, ?)",
                    (plate, "No Helmet", time_now)
                )
                conn.commit()

                logs.append({
                    "license_plate": plate,
                    "violation": "No Helmet",
                    "time": time_now
                })

    cap.release()
    return logs
