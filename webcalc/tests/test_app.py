import unittest
from webcalc.app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_add(self):
        response = self.client.get('/add?a=10&b=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['result'], 15)

    def test_sub(self):
        response = self.client.get('/sub?a=10&b=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['result'], 5)

    def test_mut(self):
        response = self.client.get('/mut?a=10&b=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['result'], 50)

    def test_div(self):
        response = self.client.get('/div?a=10&b=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['result'], 2)

    def test_div_by_zero(self):
        response = self.client.get('/div?a=10&b=0')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

if __name__ == '__main__':
    unittest.main()