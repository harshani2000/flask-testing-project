import unittest
from src.app import app
from flask import json

class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True  # Enables testing mode

    def test_user_login(self):
        response = self.app.post('/login', data=json.dumps({
            "username": "testuser",
            "password": "testpassword"
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)  # Check login success
        self.assertIn('token', response.get_json())  # Ensure token is returned

if __name__ == '__main__':
    unittest.main()
