import pytest
from fastapi.testclient import TestClient
from api import app
from db import SessionLocal, Todo

# Create a TestClient instance for your FastAPI app
client = TestClient(app)

def clear_db():
    """
    Helper function to delete all records from the 'todos' table.
    """
    session = SessionLocal()
    session.query(Todo).delete()
    session.commit()
    session.close()

@pytest.fixture(autouse=True)
def run_around_tests():
    # Before each test, clear the database
    clear_db()
    yield
    # After each test, clear the database again
    clear_db()

def test_create_and_get_todo():
    # --- Create a new todo ---
    response = client.post("/todos", json={"title": "Test Todo"})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["title"] == "Test Todo"
    assert data["is_complete"] is False

    # --- Verify the database now has the new todo ---
    response = client.get("/todos")
    assert response.status_code == 200
    todos = response.json()
    assert len(todos) == 1
    assert todos[0]["title"] == "Test Todo"

def test_clear_database():
    # --- Create a couple of todos ---
    client.post("/todos", json={"title": "Todo 1"})
    client.post("/todos", json={"title": "Todo 2"})

    # Verify that there are two todos
    response = client.get("/todos")
    assert response.status_code == 200
    todos = response.json()
    assert len(todos) == 2

    # --- Clear the database using the helper function ---
    clear_db()

    # Verify that the database is now empty
    response = client.get("/todos")
    assert response.status_code == 200
    todos = response.json()
    assert len(todos) == 0
