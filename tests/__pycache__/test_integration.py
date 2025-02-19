from flask import Flask, jsonify
import pytest

# Sample Flask app with multiple components
@pytest.fixture
def app():
    app = Flask(__name__)

    @app.route('/user/<int:user_id>')
    def get_user(user_id):
        return jsonify({"id": user_id, "name": "John Doe"})

    return app

def test_user_api(client):
    response = client.get("/user/1")
    assert response.status_code == 200
    assert response.json["name"] == "John Doe"
