from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)

def test_get_games_mocked():
    with patch("main.get_games") as mock_get:
        mock_get.return_value = {"id": 1, "name": "NFS"}
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"id": 1, "name": "NFS"}

def test_add_game_mocked():
    with patch("main.add_game") as mock_save:
        item = {"name": "Call of Duty"}
        mock_save.return_value = {"status": "success", "saved_item": item}
        response = client.post("/item", json=item)
        assert response.status_code == 200
        assert response.json() == {"status": "success", "saved_item": item}
