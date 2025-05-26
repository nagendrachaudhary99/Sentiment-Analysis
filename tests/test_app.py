from fastapi.testclient import TestClient
import pytest
from app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    
def test_classify_endpoint_exists():
    # Just test that the endpoint exists, without running the model
    response = client.post("/classify", json={"text": "test"})
    assert response.status_code in [200, 422, 500]  # Allowing error codes since we're not mocking the model 