from flask import Blueprint, url_for, render_template
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/webnovel/')
def webnovel():
    return render_template('novel/webnovel.html')


@bp.route('/')
def _Home():
    return render_template('Home.html')

