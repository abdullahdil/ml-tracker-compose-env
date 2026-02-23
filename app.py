from datetime import datetime

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional

import models
from database import engine, get_db

# Automatically create the database tables when the app starts
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="ML Experiment Tracker")

# --- Pydantic Schemas for Data Validation ---
class ExperimentCreate(BaseModel):
    model_name: str
    dataset_name: str
    accuracy: float
    loss: float

class ExperimentResponse(ExperimentCreate):
    id: int
    timestamp: datetime  # <--- Changed from str to datetime

    class Config:
        from_attributes = True

# --- API Endpoints ---

# 1. Health Check
@app.get("/health")
def health_check():
    return {"status": "Service is running"}

# 2. Create Experiment
@app.post("/experiments", response_model=ExperimentResponse)
def create_experiment(experiment: ExperimentCreate, db: Session = Depends(get_db)):
    db_experiment = models.Experiment(
        model_name=experiment.model_name,
        dataset_name=experiment.dataset_name,
        accuracy=experiment.accuracy,
        loss=experiment.loss
    )
    db.add(db_experiment)
    db.commit()
    db.refresh(db_experiment)
    return db_experiment

# 3 & 4. Get All Experiments (with optional filtering)
@app.get("/experiments", response_model=List[ExperimentResponse])
def get_experiments(model_name: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(models.Experiment)
    if model_name:
        query = query.filter(models.Experiment.model_name == model_name)
    return query.all()