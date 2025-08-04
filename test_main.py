from fastapi.testclient import TestClient
from main import app, GameCreate
from unittest.mock import MagicMock
from sqlalchemy.orm import Session

client = TestClient(app)

def test_get_games_mocked():
    mock_db = MagicMock(spec=Session)
    mock_db.query.return_value.all.return_value = [{"id": 1, "name": "NFS"}]

    app.dependency_overrides = {
        app.dependency_overrides: lambda: mock_db
    }

    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "name": "NFS"}]

    app.dependency_overrides = {}

def test_add_game_mocked():
    mock_db = MagicMock(spec=Session)
    mock_db.add.return_value = None
    mock_db.commit.return_value = None
    mock_db.refresh.return_value = None

    app.dependency_overrides = {
        app.dependency_overrides: lambda: mock_db
    }

    item = {"name": "Call of Duty"}
    response = client.post("/", json=item)
    assert response.status_code == 200
    assert response.json()["name"] == "Call of Duty"

    app.dependency_overrides = {}

