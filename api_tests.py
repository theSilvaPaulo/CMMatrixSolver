import unittest
from flask import Flask
from flask_testing import TestCase

from run import app_views

class TestAppViews(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.register_blueprint(app_views)
        app.config['TESTING'] = True
        return app

    def test_inverte_diagonais(self):
        data = {'matriz': [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}
        response = self.client.post('/inverte-diagonais', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['matriz_invertida'], [[3, 2, 1], [4, 5, 6], [9, 8, 7]])

    def test_conta_submatriz(self):
        data = {
            'matriz': [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]],
            'submatriz': [[3, 4], [4, 5]]
        }
        response = self.client.post('/conta-submatriz', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['contagem'], 3)

if __name__ == '__main__':
    unittest.main()