import streamlit as st
import requests
import pandas as pd
from datetime import datetime
from detector import detect_violations
from tensorflow.keras.models import load_model
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.accident_alert import send_email_alert,model
import cv2
import numpy as np
# -------------------- Page Config --------------------
st.set_page_config(page_title="🚦 AI Traffic Management System", layout="wide")

# -------------------- Title --------------------
st.title("🚦 AI Traffic Management")

# -------------------- Functions --------------------
def start_vehicle_detection():
    try:
        response = requests.get("http://127.0.0.1:8000/detect/")
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def optimize_traffic_lights():
    try:
        response = requests.get("http://127.0.0.1:8000/control/")
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def handle_video_upload(video_file):
    if video_file:
        with open("video/uploaded_video.mp4", "wb") as f:
            f.write(video_file.read())

        logs = detect_violations("video/uploaded_video.mp4")
        return logs
    return None

def display_violation_data(logs):
    if logs:
        df = pd.DataFrame(logs)
        st.dataframe(df)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📄 Download Violation Report", csv, "violation_log.csv", "text/csv")
    else:
        st.info("✅ No violations detected.")

def run_accident_detection(video_file, receiver_email):
    st.success("🛠️ Processing video... please wait")
    os.makedirs("video", exist_ok=True)
    temp_path = os.path.join("video", "temp_input.mp4")

    with open(temp_path, "wb") as f:
        f.write(video_file.read())

    cap = cv2.VideoCapture(temp_path)
    detected = False

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        resized = cv2.resize(frame, (299, 299))
        processed = resized.astype('float32') / 255.0
        processed = np.expand_dims(processed, axis=0)

        prediction = model.predict(processed)

        if prediction[0][0] > 0.7:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            os.makedirs("accidents", exist_ok=True)
            image_path = os.path.join("accidents", f"accident_{timestamp}.jpg")
            cv2.imwrite(image_path, frame)

            send_email_alert(receiver_email, image_path)
            st.error("🚑 Accident Detected! Email alert sent.")
            st.image(image_path, caption="Snapshot of Accident", use_column_width=True)
            detected = True
            break

    cap.release()
    os.remove(temp_path)

    if not detected:
        st.success("✅ No accident detected.")

# -------------------- Vehicle Detection Section --------------------
st.header("🚗 Vehicle Detection & Traffic Light Optimization")

col1, col2 = st.columns(2)

with col1:
    if st.button("Start Vehicle Detection"):
        detection_result = start_vehicle_detection()
        st.write(detection_result)

with col2:
    if st.button("Optimize Traffic Lights"):
        control_result = optimize_traffic_lights()
        st.write(control_result)

# -------------------- Traffic Violation Detection Section --------------------
st.header("🚨 Traffic Violation Detection")

video_file = st.file_uploader("📤 Upload a traffic video", type=["mp4", "mov", "avi"])
frame_placeholder = st.empty()

if video_file:
    violation_logs = handle_video_upload(video_file)
    display_violation_data(violation_logs)

st.header("🚑 Accident Detection & Emergency Alert")

accident_video = st.file_uploader("📹 Upload a video for accident detection", type=["mp4", "avi", "mov"], key="accident_video")
receiver_email = st.text_input("📧 Enter responder's email", placeholder="example@email.com")

if st.button("Run Accident Detection"):
    if not accident_video:
        st.warning("⚠️ Please upload a video file.")
    elif not receiver_email:
        st.warning("⚠️ Please enter a valid responder email.")
    else:
        run_accident_detection(accident_video, receiver_email)

