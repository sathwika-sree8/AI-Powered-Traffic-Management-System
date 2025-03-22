from fastapi import FastAPI
from vision import detect_vehicles
from traffic_rl import TrafficLightRL

app = FastAPI()
traffic_rl = TrafficLightRL()

@app.get("/")
def home():
    return {"message": "AI Traffic Management API"}

@app.get("/detect/")
def detect():
    detect_vehicles("data/traffic.mp4")
    return {"status": "Detection started"}

@app.get("/control/")
def control_traffic():
    action = traffic_rl.choose_action()
    return {"traffic_light_action": "Switch to Green" if action else "Stay Red"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
