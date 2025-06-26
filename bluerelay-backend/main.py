import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()
ALERTS_FILE = "alerts.json"

class Alert(BaseModel):
    id: str
    headline: str
    severity: str
    area: str
    url: str
    transfers: int = 0

def read_alerts():
    try:
        with open(ALERTS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def write_alerts(alerts):
    with open(ALERTS_FILE, "w") as f:
        json.dump(alerts, f, indent=2)

@app.get("/")
def home():
    return {"message": "welcome to BlueRelay backend API! head over to /alerts for alerts."}

@app.get("/alerts", response_model=List[Alert])
def get_alerts():
    alerts = read_alerts()
    return alerts

@app.post("/alerts", response_model=Alert)
def create_alert(alert: Alert):
    alerts = read_alerts()
    if any(a["id"] == alert.id for a in alerts):
        raise HTTPException(status_code=400, detail="Alert already exists")
    alerts.append(alert.dict())
    write_alerts(alerts)
    return alert

@app.put("/alerts/{alert_id}/transfer", response_model=Alert)
def transfer_alert(alert_id: str):
    alerts = read_alerts()
    for a in alerts:
        if a["id"] == alert_id:
            a["transfers"] += 1
            write_alerts(alerts)
            return a
    raise HTTPException(status_code=404, detail="Not found")

@app.delete("/alerts/{alert_id}")
def delete_alert(alert_id: str):
    alerts = read_alerts()
    new_alerts = [a for a in alerts if a["id"] != alert_id]
    if len(new_alerts) == len(alerts):
        raise HTTPException(status_code=404, detail="Not found")
    write_alerts(new_alerts)
    return {"detail": "Alert deleted"}
