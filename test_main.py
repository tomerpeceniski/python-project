import pytest
from main import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_hello(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello from Flask! ;)"}

def test_sumvalues_success(client):
    response = client.post('/sumvalues', json={"values": [1, 2, 3]})
    assert response.status_code == 200
    assert response.get_json() == {"result": 6}

def test_sumvalues_missing_field(client):
    response = client.post('/sumvalues', json={})
    assert response.status_code == 400
    assert "error" in response.get_json()

def test_sumvalues_invalid_type(client):
    response = client.post('/sumvalues', json={"values": [1, "a", 3]})
    assert response.status_code == 400
    assert "error" in response.get_json()
