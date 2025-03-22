import cv2
import torch
import numpy as np

# Load YOLOv5 model (uses cache, avoids re-downloading)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Define vehicle classes
VEHICLE_CLASSES = ["car", "bus", "truck", "motorcycle"]

def detect_vehicles(video_path: str):
    """
    Detects vehicles in a given video file using YOLOv5.
    :param video_path: Path to the video file
    """
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"❌ Error: Could not open video at {video_path}")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Perform YOLO object detection
        results = model(frame)
        detections = results.xyxy[0].cpu().numpy()  # Convert to NumPy

        for det in detections:
            x1, y1, x2, y2, conf, cls = det[:6]
            cls = int(float(cls))  # ✅ Ensure class index is an integer
            class_name = model.names[cls]  # Get class label

            if class_name in VEHICLE_CLASSES:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(frame, class_name, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow("🚗 Traffic Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # ✅ Your exact video path
    video_path = r"C:\Users\SATHWIKA\PycharmProjects\AI-Traffic-Management\istockphoto-1136760244-640_adpp_is.mp4"
    detect_vehicles(video_path)
