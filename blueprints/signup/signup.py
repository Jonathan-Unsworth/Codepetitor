from flask import Blueprint, render_template, request, redirect, url_for
from pony.orm import commit
from codepetitor.models import db

blueprint_signup = Blueprint (
    'blueprint_signup',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='assets'
)

@blueprint_signup.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('signup/signup.html')
    else:
        username = request.form['username']
        password = request.form['password']
        ps = db.Player_Stats(level=0, elo_rating=1200, wins=0, loses=0, win_lost_ratio=0)
        commit()
        db.Player(username=username, password=password, player_stats_id=ps.player_stats_id)
        commit()
        return redirect(url_for('blueprint_login.login'))
