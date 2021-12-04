import pytest

from app import app

@pytest.fixture
def client():
    yield app.test_client()

def test_index(client):
    resp = client.get('/', content_type="html/text")
    assert resp.status_code == 200

def test_api(client):
    resp = client.get('/api')
    assert resp.status_code == 200
    assert 'value' in resp.json
    assert resp.json == {'value': 'Asim Sheikh'}
