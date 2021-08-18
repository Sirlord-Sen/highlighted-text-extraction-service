from flask import jsonify, request
from werkzeug.exceptions import NotFound

from ..handlers.exceptions import JSONException, InvalidAPIRequest


def json_error_handler(app):
    @app.errorhandler(JSONException)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response


    @app.errorhandler(NotFound.code)
    def resource_not_found(error):
        msg = 'The requested URL `%s` was not found on the server.' % request.path
        response = jsonify(InvalidAPIRequest(message=msg).to_dict())
        response.status_code = NotFound.code
        return response 