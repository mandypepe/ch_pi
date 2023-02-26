import os
import jwt

def generate_jwt(payload):
    token=jwt.encode(payload, os.environ.get('SECRET_KEY'), algorithm="HS256")
    return token

def decode_jwt(token):
    token=jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=["HS256"])
    return token