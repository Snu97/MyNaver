from datetime import datetime

from flask import Blueprint, url_for, request, render_template, g
from werkzeug.utils import redirect
from .auth_views import login_required

from naver import db
from naver.models import Novel, Number, Review, Comment

bp = Blueprint('review', __name__, url_prefix='/review')



@bp.route('/create/<int:novel_id>', methods=('POST',))
@login_required
def create(novel_id):
    novel = Novel.query.get_or_404(novel_id)
    content = request.form['content']
    review = Review(novel=novel, content=content, create_date=datetime.now(), user=g.user)
    db.session.add(review)
    db.session.commit()
    return redirect(url_for('best._list', novel_id=novel_id))

@bp.route('/create/comment/<int:number_id>', methods=('POST',))
@login_required
def create_comment(number_id):
    number = Number.query.get_or_404(number_id)
    content = request.form['content']
    comment = Comment(number=number, content=content, create_date=datetime.now(), user=g.user)
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('best.detail', number_id=number_id))