from flask import Flask, session, redirect, url_for, request
from pony.flask import Pony


def auth():
    if 'username' not in session and request.endpoint != 'blueprint_login.login' and request.endpoint != 'blueprint_signup.signup':
        return redirect(url_for('blueprint_login.login'))
    

def create_app():
    codepetitor = Flask(__name__)
    codepetitor.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    codepetitor.before_request(auth)
    
    Pony(codepetitor)
    from codepetitor.models import db

    from codepetitor.blueprints.login.login import blueprint_login
    from codepetitor.blueprints.signup.signup import blueprint_signup
    from codepetitor.blueprints.hub.hub import blueprint_hub
    codepetitor.register_blueprint(blueprint_login, url_prefix='/login')
    codepetitor.register_blueprint(blueprint_signup, url_prefix='/signup')
    codepetitor.register_blueprint(blueprint_hub, url_prefix='/hub')

    return codepetitor


create_app()