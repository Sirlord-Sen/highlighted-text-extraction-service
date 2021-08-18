import os
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app
class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('config.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['SECRET_KEY'] is os.getenv("SECRET_KEY"))
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)

class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('config.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['SECRET_KEY'] is os.getenv("SECRET_KEY"))
        self.assertFalse(app.config['DEBUG'] is True)


if __name__ == '__main__':
    unittest.main()