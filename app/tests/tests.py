
from app.repositories import database
from fastapi import status
import secrets


def test_get_post_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(database, "get_post_by_id", mock_get)
    test_id =secrets.token_hex(12)
    response = test_app.get(f"/posts/{test_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND



    
