from flask import Flask, session, redirect, url_for, request
from pony.flask import Pony
from flask_socketio import SocketIO
from engineio.payload import Payload

Payload.max_decode_packets = 2


def auth():
    if 'username' not in session and request.endpoint != 'blueprint_login.login' and request.endpoint != 'blueprint_signup.signup':
        return redirect(url_for('blueprint_login.login'))
    

socketio = SocketIO()

def create_app():
    codepetitor = Flask(__name__)
    codepetitor.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    codepetitor.before_request(auth)
    
    Pony(codepetitor)
    from codepetitor.models import db


    from codepetitor.blueprints.login.login import blueprint_login
    from codepetitor.blueprints.signup.signup import blueprint_signup
    from codepetitor.blueprints.hub.hub import blueprint_hub
    from codepetitor.blueprints.collaborator.collaborator import blueprint_collaborator

    codepetitor.register_blueprint(blueprint_login, url_prefix='/login')
    codepetitor.register_blueprint(blueprint_signup, url_prefix='/signup')
    codepetitor.register_blueprint(blueprint_hub, url_prefix='/hub')
    codepetitor.register_blueprint(blueprint_collaborator, url_prefix='/collaborator', app=socketio)

    socketio.init_app(codepetitor)

    return codepetitor


create_app()
#if __name__ == '__main__':
    # app = create_app()
    # socketio = SocketIO(app)
    # socketio.run(app)

