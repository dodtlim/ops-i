import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Authentication Endpoints
def test_register():
    response = client.post("/auth/register", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 201
    assert response.json() == {"message": "User registered"}

def test_login():
    response = client.post("/auth/login", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert "token" in response.json()

def test_logout():
    response = client.post("/auth/logout", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code == 204

# Metrics Endpoints
def test_get_metrics():
    response = client.get("/api/metrics", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_metric():
    response = client.post("/api/metrics", json={"cpu_usage": 50, "memory_usage": 1024, "instance_id": "i-123456"}, headers={"Authorization": "Bearer testtoken"})
    assert response.status_code == 201
    assert response.json() == {"message": "Metric added"}

def test_get_metric():
    response = client.get("/api/metrics/i-123456", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code == 200
    assert "cpu_usage" in response.json()

def test_update_metric():
    response = client.put("/api/metrics/i-123456", json={"cpu_usage": 60, "memory_usage": 2048, "instance_id": "i-123456"}, headers={"Authorization": "Bearer testtoken"})
    assert response.status_code == 200
    assert response.json() == {"message": "Metric updated"}

def test_delete_metric():
    response = client.delete("/api/metrics/i-123456", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code == 204

# AI Predictions Endpoints
def test_get_predictions():
    response = client.get("/api/predictions", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_prediction():
    response = client.post("/api/predictions", json={"predicted_issue": "Issue A", "confidence": 0.95, "predicted_actions": ["Action 1", "Action 2"]}, headers={"Authorization": "Bearer testtoken"})
    assert response.status_code == 201
    assert response.json() == {"message": "AI Prediction added"}

# Scaling Logs Endpoints
def test_get_scaling_logs():
    response = client.get("/api/scaling_logs", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_scaling_log():
    response = client.post("/api/scaling_logs", json={"action_taken": "Scale up", "reason": "High CPU usage", "instance_ids": ["i-123456", "i-789012"]}, headers={"Authorization": "Bearer testtoken"})
    assert response.status_code == 201
    assert response.json() == {"message": "Scaling log added"}

# Frontend Endpoints
def test_get_dashboard_summary():
    response = client.get("/api/dashboard/summary", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code == 200
    assert response.json() == {"summary": "Dashboard summary"}

def test_get_metrics_trend():
    response = client.get("/api/dashboard/metrics/trend", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code == 200
    assert response.json() == {"trend": "Metrics trend"}

def test_get_recent_ai_predictions():
    response = client.get("/api/dashboard/ai_predictions/recent", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code == 200
    assert response.json() == {"predictions": "Recent AI predictions"}

def test_get_recent_scaling_logs():
    response = client.get("/api/dashboard/scaling_logs/recent", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code == 200
    assert response.json() == {"logs": "Recent scaling logs"}

def test_get_recent_alerts():
    response = client.get("/api/dashboard/alerts/recent", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code == 200
    assert response.json() == {"alerts": "Recent alerts"}