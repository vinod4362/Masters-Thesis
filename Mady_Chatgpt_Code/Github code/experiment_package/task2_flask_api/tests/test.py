# test_api.py
import json
import pytest

import app as todo_app


@pytest.fixture(autouse=True)
def client():
    # Reset in-memory DB before each test
    todo_app.DB.clear()
    todo_app.NEXT_ID = 1

    todo_app.app.config["TESTING"] = True
    with todo_app.app.test_client() as c:
        yield c


def _json(resp):
    return json.loads(resp.data.decode("utf-8")) if resp.data else None


def test_create_minimal(client):
    resp = client.post("/todos", json={"title": "Buy milk"})
    assert resp.status_code == 201
    body = _json(resp)
    assert body["id"] == 1
    assert body["title"] == "Buy milk"
    assert body["done"] is False


def test_create_with_done_true(client):
    resp = client.post("/todos", json={"title": "Call mom", "done": True})
    assert resp.status_code == 201
    body = _json(resp)
    assert body["done"] is True


def test_create_requires_title(client):
    # Missing title
    resp = client.post("/todos", json={"done": False})
    assert resp.status_code == 400

    # Title must be string
    resp = client.post("/todos", json={"title": 123})
    assert resp.status_code == 400


def test_list_empty_then_populated(client):
    resp = client.get("/todos")
    assert resp.status_code == 200
    assert _json(resp) == []

    client.post("/todos", json={"title": "A"})
    client.post("/todos", json={"title": "B"})
    resp = client.get("/todos")
    data = _json(resp)
    assert len(data) == 2
    assert {t["title"] for t in data} == {"A", "B"}


def test_get_and_404(client):
    client.post("/todos", json={"title": "Only one"})
    resp = client.get("/todos/1")
    assert resp.status_code == 200
    assert _json(resp)["title"] == "Only one"

    resp = client.get("/todos/999")
    assert resp.status_code == 404


def test_patch_update_title_and_done(client):
    client.post("/todos", json={"title": "Task", "done": False})
    resp = client.patch("/todos/1", json={"title": "Task v2"})
    assert resp.status_code == 200
    assert _json(resp)["title"] == "Task v2"

    resp = client.patch("/todos/1", json={"done": True})
    assert resp.status_code == 200
    assert _json(resp)["done"] is True


def test_patch_validation_and_404(client):
    client.post("/todos", json={"title": "X"})
    # Invalid types
    resp = client.patch("/todos/1", json={"title": 42})
    assert resp.status_code == 400
    resp = client.patch("/todos/1", json={"done": "yes"})
    assert resp.status_code == 400

    # Empty/None payload
    resp = client.patch("/todos/1", data="")  # no JSON
    assert resp.status_code == 400

    # Nonexistent id
    resp = client.patch("/todos/999", json={"title": "nope"})
    assert resp.status_code == 404


def test_delete_and_404(client):
    client.post("/todos", json={"title": "Temp"})
    resp = client.delete("/todos/1")
    assert resp.status_code == 204
    assert resp.data == b""

    # Already gone
    resp = client.delete("/todos/1")
    assert resp.status_code == 404


def test_content_type_is_json(client):
    client.post("/todos", json={"title": "ct"})
    resp = client.get("/todos/1")
    assert resp.status_code == 200
    assert resp.headers.get("Content-Type").startswith("application/json")
