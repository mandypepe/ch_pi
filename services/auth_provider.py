import os
def authenticate(email, password):
    emailos=os.environ.get('SECRET_EMAIL')
    passwordos=os.environ.get('SECRET_PASSW')
    if email == emailos and password == passwordos:
        return {
            'username': 'admin',
            'email': f'{emailos}',
            'roles': ['admin', 'user']
        }
    else:
        return False