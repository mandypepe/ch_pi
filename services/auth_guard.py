from flask import request, jsonify
from services.jwt_handler import decode_jwt

def check_jwt():
    token = request.headers.get('Authorization')
    if not token:
        raise Exception('Missing access token')
    jwt = token.split('Bearer ')[1]
    try:
        return decode_jwt(jwt)
    except Exception as e:
        raise Exception(f'Invalid access token: {e}')

def auth_guard(role=None):
    def wrapper(route_function):
        def decorated_function(*args, **kwargs):
            try:
                user_data = check_jwt()
            except Exception as e:
                return jsonify({"message": f'{e}', "status": 401}), 401
            if role and role not in user_data['roles']:
                return jsonify({"message": 'Authorization required.', "status": 403}), 403
            return route_function(*args, **kwargs)
        decorated_function.__name__ = route_function.__name__
        return decorated_function
    return wrapper