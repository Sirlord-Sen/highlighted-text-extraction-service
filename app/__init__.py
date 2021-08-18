from flask import Flask
from config.config import config_by_name

def create_app(config_name):
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False
    app.config.from_object(config_by_name[config_name])

    from app.highlight.controllers.controllers import api as textdetect_route
    from app.highlight.middlewares import after_request_middleware, before_request_middleware
    from app.highlight.middlewares import response_middlewares as response

    before_request_middleware(app=app)
    after_request_middleware(app=app)
    
    # register custom error handler
    response.json_error_handler(app=app)
    
    app.register_blueprint(textdetect_route)

    return app
