import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "欢迎使用FastAPI!"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_create_user():
    user_data = {
        "name": "测试用户",
        "email": "test@example.com",
        "password": "testpassword"
    }
    response = client.post("/api/v1/users/", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "测试用户"
    assert data["email"] == "test@example.com"
    assert data["id"] == 1
    assert data["is_active"] == True

def test_get_users():
    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_user_not_found():
    response = client.get("/api/v1/users/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "用户未找到"}