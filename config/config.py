from os import environ, path
from typing import List, Type
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv()

class BaseConfig:
    CSRF_ENABLED = True
    SECRET_KEY = environ.get('SECRET_KEY')
    STATIC_FOLDER = 'static'


class DevelopmentConfig(BaseConfig):
    FLASK_ENV = 'developement'
    DEVELOPMENT = True
    DEBUG = True
    CONFIG_NAME = "dev"
    TESTING = False


class TestingConfig(BaseConfig):
    FLASK_ENV = 'testing'
    CONFIG_NAME = "test"
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'
    CONFIG_NAME = "prod"
    DEBUG = False
    TESTING = False

class StagingConfig(BaseConfig):
    FLASK_ENV = 'staging'
    CONFIG_NAME = "stage"
    DEVELOPMENT = True
    DEBUG = True

EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig,
    TestingConfig,
    ProductionConfig,
    StagingConfig
]
config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}

