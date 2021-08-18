from werkzeug.exceptions import  NotFound, Unauthorized, InternalServerError


class JSONException(Exception):
    status_code = NotFound.code
    message = ''

    def __init__(self, message,status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        return {
            'status': 'error',
            'message': self.message,
            'code': self.status_code,
            'type': str(self.__class__.__name__)
        }

class InvalidContentType(JSONException):
    """Raised when an invalid Content-Type is provided."""
    pass


class InvalidPermissions(JSONException):
    status_code = Unauthorized.code


class InvalidAPIRequest(JSONException):
    """
    Raised when an invalid request has been made.
    (e.g. accessed unexisting url, the schema validation did
    not pass)
    """
    pass


class InternalServerError(JSONException):
    status_code = InternalServerError.code