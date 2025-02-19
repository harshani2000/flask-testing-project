import unittest
from src.app import app  # Import the Flask app
from src.helpers import some_function  # Example function to test

class TestUnitCases(unittest.TestCase):

    def test_some_function(self):
        result = some_function(5, 10)
        self.assertEqual(result, 15)  # Expected output

    def test_home_route(self):
        tester = app.test_client()
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)  # Ensure home page loads

if __name__ == '__main__':
    unittest.main()
