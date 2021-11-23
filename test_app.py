from pathlib import Path

from app import app

def test_index():
    tester = app.test_client()
    resp = tester.get('/', content_type="html/text")

    assert resp.status_code == 200
    assert resp.data == b'Hello, World'

def test_test():
    tester = app.test_client()
    resp = tester.get('/test', content_type="html/text")

    assert resp.status_code == 200
    assert resp.data == b'Test working'

def test_database():
    assert Path("flaskr.db").is_file()
