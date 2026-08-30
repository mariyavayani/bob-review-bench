import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.app import app
from app import repository


@pytest.fixture
def client(tmp_path, monkeypatch):
    db_path = tmp_path / "test_taskflow.db"
    monkeypatch.setattr(repository, "DB_PATH", str(db_path))
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def test_create_and_list_task(client):
    response = client.post("/tasks", json={"title": "Write tests"})
    assert response.status_code == 201
    task = response.get_json()
    assert task["title"] == "Write tests"

    listed = client.get("/tasks").get_json()
    assert len(listed) == 1
    assert listed[0]["title"] == "Write tests"


def test_create_task_requires_title(client):
    response = client.post("/tasks", json={})
    assert response.status_code == 400


def test_get_missing_task_returns_404(client):
    response = client.get("/tasks/999")
    assert response.status_code == 404


def test_update_task(client):
    created = client.post("/tasks", json={"title": "Draft"}).get_json()
    response = client.put(f"/tasks/{created['id']}", json={"done": 1})
    assert response.status_code == 200
    assert response.get_json()["done"] == 1


def test_delete_task(client):
    created = client.post("/tasks", json={"title": "Temp"}).get_json()
    response = client.delete(f"/tasks/{created['id']}")
    assert response.status_code == 204
    assert client.get(f"/tasks/{created['id']}").status_code == 404
