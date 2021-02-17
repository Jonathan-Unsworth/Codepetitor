from flask import Blueprint, render_template

blueprint_signup = Blueprint (
    'blueprint_signup',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='assets'
)

@blueprint_signup.route('/')
def signup():
    return render_template('signup/signup.html')
