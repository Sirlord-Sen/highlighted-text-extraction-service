from . import request_middlewares as request

def before_request_middleware(app):
    app.before_request_funcs.setdefault(None, [
        request.ensure_content_type,
        request.ensure_public_unavailability,
    ])

def after_request_middleware(app):
    app.after_request_funcs.setdefault(None, [
        request.enable_cors
    ])

