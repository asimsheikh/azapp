import pytest
from pathlib import Path

from app import app, init_db

@pytest.fixture
def client():
    BASE_DIR = Path(__file__).resolve().parent.parent
    app.config["TESTING"] = True
    app.config["DATABASE"] = str(BASE_DIR.joinpath("test.db"))

    init_db()
    yield app.test_client()
    init_db()

def login(client, username, password):
    return client.post(
            "/login", 
            data=dict(username=username, password=password),
            follow_redirects=True,
    )

def logout(client):
    return client.get('/logout', follow_redirects=True) 

def test_index(client):
    resp = client.get('/', content_type="html/text")

    assert resp.status_code == 200
    assert resp.data == b'Hello, World'

def test_database():
    assert Path("flaskr.db").is_file()
