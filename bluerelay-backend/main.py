from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

alerts_db = {}

class Alert(BaseModel):
    id: str
    headline: str
    severity: str
    area: str
    url: str
    transfers: int = 0

@app.post("/alerts", response_model=Alert)
def create_alert(alert: Alert):
    if alert.id in alerts_db:
        raise HTTPException(status_code=400, detail="Alert already exists")
    alerts_db[alert.id] = alert
    return alert

@app.get("/alerts", response_model=List[Alert])
def get_alerts():
    return list(alerts_db.values())

@app.get("/alerts/{alert_id}", response_model=Alert)
def get_alert(alert_id: str):
    if alert_id not in alerts_db:
        raise HTTPException(status_code=404, detail="Not found")
    return alerts_db[alert_id]

@app.put("/alerts/{alert_id}/transfer", response_model=Alert)
def transfer_alert(alert_id: str):
    if alert_id not in alerts_db:
        raise HTTPException(status_code=404, detail="Not found")
    alerts_db[alert_id].transfers += 1
    return alerts_db[alert_id]

@app.delete("/alerts/{alert_id}")
def delete_alert(alert_id: str):
    if alert_id not in alerts_db:
        raise HTTPException(status_code=404, detail="Not found")
    del alerts_db[alert_id]
    return {"detail": "Alert deleted"}
