import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_root_path(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Bienvenue' in response.data

def test_hello_with_name(client):
    name = "DockerCI"
    response = client.get(f'/hello/{name}')
    assert response.status_code == 200
    assert f'Hello, {name}!'.encode() in response.data
