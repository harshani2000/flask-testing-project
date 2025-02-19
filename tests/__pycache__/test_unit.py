import pytest
from flask import Flask

# Sample Flask application for testing
@pytest.fixture
def app():
    app = Flask(__name__)
    app.config["TESTING"] = True
    return app

def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, Flask!"

def test_sample():
    assert 1 + 1 == 2  # Simple test

@app.route('/user/<int:user_id>')
    def get_user(user_id):
        return jsonify({"id": user_id, "name": "John Doe"})

    return app

def test_user_api(client):
    response = client.get("/user/1")
    assert response.status_code == 200
    assert response.json["name"] == "John Doe"    
