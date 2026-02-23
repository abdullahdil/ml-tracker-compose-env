from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
import datetime

class Experiment(Base):
    __tablename__ = "experiments"

    id = Column(Integer, primary_key=True, index=True)
    model_name = Column(String, index=True, nullable=False)
    dataset_name = Column(String, nullable=False)
    accuracy = Column(Float, nullable=False)
    loss = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)