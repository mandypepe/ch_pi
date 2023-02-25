from services.jwt_handler import generate_jwt, decode_jwt
from services  import auth_guard
from services.auth_guard  import auth_guard
from services.auth_provider import authenticate
import os
from app import create_app
import mock
#coverage run -m pytest conftest.py
#coverage report -m  --omit */lib/*,*/Library/*


def test_create_app():
        assert isinstance(create_app(),object)

@mock.patch.dict(os.environ, {"SECRET_KEY": "gh"})
def test_generate_jwt():
        payload= {'username': 'admin', 'email': 'a@a.cu', 'roles': ['admin', 'user']}
        toke= generate_jwt(payload)
        assert isinstance(toke,str)

@mock.patch.dict(os.environ, {"SECRET_KEY": "yXzB0lEGphwTYfKenExHmNqMmpFJJRjI"})
def test_decode_jwt():
        token= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZW1haWwiOiJhQGEuY3UiLCJyb2xlcyI6WyJhZG1pbiIsInVzZXIiXX0.zupvTDSDGWge8-e8chB84ZDl0794wtXoDYAhG-GlN-I"
        decode= decode_jwt(token)
        assert isinstance(decode,dict)

def test_auth_guard():
        assert isinstance(auth_guard,object)


def test_authenticate():
        with mock.patch.dict(os.environ, {"SECRET_EMAIL": "yXzB0@lEGphwTYfKenExHmNqM.mpFJJRjI"}):
                with mock.patch.dict(os.environ, {"SECRET_PASSW": "yXzB0lEGphwTYfKenExHmNqMmpFJJRjI"}):
                        email=""
                        passs=""
                        assert isinstance(authenticate(email,passs),bool)



