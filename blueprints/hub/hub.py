from flask import Blueprint, request, render_template, session

blueprint_hub = Blueprint (
    'blueprint_hub',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='assets'
)

@blueprint_hub.route('/', methods=['GET', 'POST'])
def hub():
    return render_template('hub.html')