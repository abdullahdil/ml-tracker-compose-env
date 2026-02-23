import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import app
from database import get_db, Base

# 1. Setup a temporary SQLite database just for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the tables in the test database
Base.metadata.create_all(bind=engine)

# 2. Override the FastAPI dependency to use the test database instead of Postgres
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# 3. Create the test client
client = TestClient(app)

# --- THE TESTS ---

def test_create_experiment():
    """Test the POST /experiments endpoint"""
    response = client.post(
        "/experiments",
        json={
            "model_name": "pytest_model",
            "dataset_name": "pytest_data",
            "accuracy": 0.95,
            "loss": 0.05
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["model_name"] == "pytest_model"
    assert "id" in data

def test_get_experiments():
    """Test the GET /experiments endpoint"""
    response = client.get("/experiments")
    assert response.status_code == 200
    data = response.json()
    # Ensure it returns a list and contains the experiment we just created
    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["model_name"] == "pytest_model"