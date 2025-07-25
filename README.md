
# 🚦 AI-Powered Traffic Management System  

### **📌 Overview**  
The **AI-Powered Traffic Management System** is designed to **optimize traffic signal control** using **Reinforcement Learning (RL) and Computer Vision**. It detects traffic density in real-time using **YOLOv5** and adjusts signal timings dynamically to **reduce congestion** and **improve efficiency**.
An intelligent, real-time traffic optimization solution that combines **computer vision**, **reinforcement learning**, and **deep learning** to improve urban traffic flow, reduce wait times, and handle emergencies automatically.

---

## 📌 Features

- 🎯 **Real-time vehicle detection** using YOLOv5
- 🤖 **Q-learning** to dynamically optimize traffic signal timings
- ⚠️ **Accident detection** using a custom CNN model
- 🔍 **License plate recognition** with EasyOCR
- 📊 **Interactive simulation dashboard** using Streamlit

---

## 🧠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core development |
| YOLOv5 | Vehicle detection |
| Q-Learning | Traffic light optimization |
| CNN | Accident detection |
| EasyOCR | License plate recognition |
| Streamlit | UI/Visualization |
| OpenCV | Image processing |
| PyTorch | Deep learning framework |

---

## 🚗 How It Works

1. **Vehicle Detection**  
   Detects number and type of vehicles in real time using YOLOv5.

2. **Signal Timing Control**  
   Applies Q-learning to adjust signal timing based on traffic density, reducing idle time by **30%**.

3. **Accident Detection**  
   A CNN monitors road footage and triggers **real-time alerts** for collisions or stalled vehicles.

4. **License Plate Recognition**  
   OCR is used to extract plate numbers for fast vehicle identification and law enforcement.

5. **Dashboard**  
   Streamlit dashboard for:
   - Monitoring live vehicle feed
   - Simulating traffic conditions
   - Testing accident response
   - Tuning Q-learning parameters

---

## 🚀 Results

| Metric | Result |
|--------|--------|
| 🎯 Vehicle Detection Accuracy | **92%** |
| ⏱️ Wait Time Reduction | **30%** |
| ⚠️ Accident Response | **Instant Alerting** |
| 🔍 License Recognition | **High Accuracy** |
| 🖥️ Dashboard | **Fully Interactive** | 

---

## **📂 Project Structure**
```
AI-Traffic-Management/
│── backend/
│   ├── main.py             # FastAPI Backend
│   ├── traffic_rl.py       # Reinforcement Learning Logic
│   ├── vision.py           # YOLOv5 Traffic Detection
│   ├── models/             # Pre-trained models
│   ├── config.py           # Configuration settings
│── frontend/
│   ├── app.py              # Flask Frontend
│── yolov5/                 # YOLOv5 Model Files
│── Dockerfile              # Docker Configuration
│── requirements.txt        # Python Dependencies
│── README.md               # Project Documentation
```

---

## **🚀 Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/sathwika-sree8/AI-Powered-Traffic-Management-System.git
cd AI-Powered-Traffic-Management-System
```

### **2️⃣ Setup Virtual Environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### **3️⃣ Run Backend**
```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```
- **API Docs**: Open `http://127.0.0.1:8000/docs`

### **4️⃣ Run Frontend**
```bash
cd frontend
python app.py  # Flask frontend
# OR
npm install && npm start  # React frontend
```

### **5️⃣ (Optional) Run with Docker**
```bash
docker build -t ai-traffic .
docker run -p 8000:8000 ai-traffic
```

---

## **🖼 Screenshots**
### 🚦 Traffic Detection 
![Traffic Detection](https://github.com/sathwika-sree8/AI-Powered-Traffic-Management-System/blob/main/vehicles%20detection.png?raw=true)

### 🖥️ Frontend Interface
![Frontend](https://github.com/sathwika-sree8/AI-Powered-Traffic-Management-System/blob/main/AI%20Traffic%20Management.png?raw=true)



# **📜 License**
This project is **open-source** and available under the **MIT License**.


## **💬 Contact & Contributions**
**👩‍💻 Developed by:** [Sathwika Sree](https://github.com/sathwika-sree8)  

