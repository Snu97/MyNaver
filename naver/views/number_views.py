from datetime import datetime

from flask import Blueprint, url_for, request, render_template, g, flash
from werkzeug.utils import redirect
from .auth_views import login_required
from ..forms import NumberForm
from naver import db
from naver.models import Novel, Number, Review, Comment

bp = Blueprint('number', __name__, url_prefix='/number')


@bp.route('/create/<int:novel_id>', methods=('POST',))
@login_required
def create(novel_id):
    novel = Novel.query.get_or_404(novel_id)
    content = request.form['content']
    review = Review(novel=novel, content=content, create_date=datetime.now(), user=g.user)
    db.session.add(review)
    db.session.commit()
    return redirect(url_for('best.detail', novel_id=novel_id))

@bp.route('/delete/<int:number_id>')
@login_required
def delete(number_id):
    number = Number.query.get_or_404(number_id)
    if g.user != number.user:
        flash('삭제권한이 없습니다')
        return redirect(url_for('best.detail', number_id=number_id))
    db.session.delete(number)
    db.session.commit()
    return redirect(url_for('best.best'))

@bp.route('/modify/<int:number_id>', methods=('GET', 'POST'))
@login_required
def modify(number_id):
    number = Number.query.get_or_404(number_id)
    if g.user != number.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('best.detail', number_id=number_id))
    if request.method == 'POST':  # POST 요청
        form = NumberForm()
        if form.validate_on_submit():
            form.populate_obj(number)
            number.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect(url_for('main.webnovel', number_id=number_id))
    else:  # GET 요청
        form = NumberForm(obj=number)
    return render_template('Number_form.html', form=form)

