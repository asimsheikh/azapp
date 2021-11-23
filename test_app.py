import pytest
from pathlib import Path

from app import app

@pytest.fixture
def client():
    BASE_DIR = Path(__file__).resolve().parent.parent
    app.config["TESTING"] = True
    app.config["DATABASE"] = BASE_DIR.joinpath("test.db")

    init_db()
    yield app.test_client()
    init_db()

def test_index():
    tester = app.test_client()
    resp = tester.get('/', content_type="html/text")

    assert resp.status_code == 200
    assert resp.data == b'Hello, World'

def test_database():
    assert Path("flaskr.db").is_file()
