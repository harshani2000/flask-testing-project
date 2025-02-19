import pytest
from src.flask.app import app

@pytest.fixture
def client():
    return app.test_client()

def test_hello_endpoint(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World!"}

def test_sum_endpoint(client):
    response = client.get('/sum/4/5')
    assert response.status_code == 200
    assert response.json == {"sum": 9}

