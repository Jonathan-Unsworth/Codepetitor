from flask import Blueprint, request, render_template, redirect, url_for, session
from codepetitor.models import db


blueprint_login = Blueprint (
    'blueprint_login',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='assets'
)

@blueprint_login.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login/login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        player = db.Player.get(username=username, password=password)
        if player:
            session['username'] = player.username
            return redirect(url_for('blueprint_hub.hub'))
        else:
            return redirect(url_for('blueprint_login.login'))
    
