from flask import Flask
from config.config import config_by_name

def create_app(config_name):
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False
    app.config.from_object(config_by_name[config_name])

    from app.highlight.controllers import api as textdetect_route

    app.register_blueprint(textdetect_route)

    return app
