from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_invalid_request_returns_422():
    response = client.get("/notes/abc?p=123")
    assert response.status_code == 422

def test_missing_note_returns_404():
    response = client.get("/notes/99")
    assert response.status_code == 404

def test_note_returns_200():
    response = client.get("/notes/1")
    assert response.status_code == 200

def test_note_delete_returns_200():
    response = client.delete("/notes/1")
    assert response.status_code == 200
    response = client.delete("/notes/1")
    assert response.status_code == 404

