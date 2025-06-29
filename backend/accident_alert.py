import cv2
import smtplib
import ssl
import numpy as np
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from tensorflow.keras.models import load_model
import os

# Load crash detection model
model_path = os.path.join("backend", "models", "accident_detection_model.h5")
model = load_model(model_path)

# Function to send email alert with image snapshot
def send_email_alert(receiver_email, image_path):
    sender_email = "sathwikapillalamarri@gmail.com"
    password = "vqcd rxhy bpef pajm"  # App password from Gmail (2-step verification must be enabled)

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = '🚨 Accident Detected - Immediate Attention Required'

    body = "An accident has been detected. Please find the attached snapshot."
    message.attach(MIMEText(body, 'plain'))

    with open(image_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename=incident.jpg")
        message.attach(part)

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print(f"✅ Email sent successfully to {receiver_email}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")