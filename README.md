
# 🚦 AI-Powered Traffic Management System  

### **📌 Overview**  
The **AI-Powered Traffic Management System** is designed to **optimize traffic signal control** using **Reinforcement Learning (RL) and Computer Vision**. It detects traffic density in real-time using **YOLOv5** and adjusts signal timings dynamically to **reduce congestion** and **improve efficiency**.

---

## **🌟 Features**
✅ **Real-time Traffic Detection** using YOLOv5  
✅ **Reinforcement Learning-based Traffic Signal Optimization**  
✅ **Smart Decision-Making** for dynamic signal control  
✅ **FastAPI Backend** for API services  
✅ **Interactive Frontend (Flask) for Visualization**  
✅ **Docker Support** for easy deployment  

---

## **🛠 Tech Stack**
- **Backend**: FastAPI, Python  
- **Frontend**: Flask / React  
- **Machine Learning**: YOLOv5, OpenCV, NumPy  
- **Database**: Firebase  
- **Deployment**: Docker, Google Cloud  

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
## Traffic Detection
![Traffic Detection]("C:\Users\SATHWIKA\OneDrive\Pictures\Screenshots\Screenshot 2025-03-21 232630.png")

## Frontend
![Frontend]("C:\Users\SATHWIKA\OneDrive\Pictures\Screenshots\Screenshot 2025-03-22 003954.png")






# **📜 License**
This project is **open-source** and available under the **MIT License**.


## **💬 Contact & Contributions**
**👩‍💻 Developed by:** [Sathwika Sree](https://github.com/sathwika-sree8)  

