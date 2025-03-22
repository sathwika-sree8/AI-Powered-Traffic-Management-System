import torch
from ultralytics import YOLO

model = YOLO("yolov5s.pt")  # Load YOLO model
print("Model Loaded Successfully")
