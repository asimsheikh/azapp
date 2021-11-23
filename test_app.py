import pytest
from pathlib import Path

from app import app

@pytest.fixture
def client():
    yield app.test_client()

def test_index(client):
    resp = client.get('/', content_type="html/text")
    assert resp.status_code == 200

