from app import app

def test_index():
    tester = app.test_client()
    resp = tester.get('/', content_type="html/text")

    assert resp.status_code == 200
    assert resp.data == b'Hello, World'

