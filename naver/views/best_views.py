from datetime import datetime

from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect

from .. import db
from naver.models import Novel, Number, Review
from ..forms    import NumberForm, NovelForm
from naver.views.auth_views import login_required

bp = Blueprint('best', __name__, url_prefix='/best')

@bp.route('/')
def best_home():
    return redirect(url_for('best.best'))

@bp.route('/popular/')
def best():
    novel_rank = Novel.query.order_by(Novel.create_date.desc())
    return render_template('novel/novel_popular.html', novel_rank=novel_rank)

@bp.route('/list/<int:novel_id>/')
def _list(novel_id):
    page = request.args.get('page', type=int, default=1)
    novel = Novel.query.get_or_404(novel_id)
    number_list = Number.query.order_by(Number.create_date.desc())
    number_list = number_list.paginate(page, per_page=10)
    return render_template('novel/novel_list.html', novel=novel, number_list=number_list)

@bp.route('/detail/<int:number_id>/')
def detail(number_id):
    number = Number.query.get_or_404(number_id)
    return render_template('novel/novel_detail.html', number=number)

@bp.route('/my/volumeWrite/<int:novel_id>/', methods=('GET', 'POST'))
@login_required
def create(novel_id):
    novel = Novel.query.get_or_404(novel_id)
    form = NumberForm()
    if request.method == 'POST' and form.validate_on_submit():
        number = Number(novel=novel ,subject=form.subject.data, content=form.content.data, create_date=datetime.now(), user=g.user)
        db.session.add(number)
        db.session.commit()
        return redirect(url_for('main.webnovel'))
    return render_template('Number_form.html', form=form)

@bp.route('/my/')
@login_required
def my_list():
    return render_template('novel/novel_my.html')


@bp.route('/my/novelWrite', methods=('GET', 'POST'))
@login_required
def novel_create():
    form = NovelForm()
    if request.method == 'POST' and form.validate_on_submit():
        novel = Novel(subject=form.subject.data, content=form.content.data, create_date=datetime.now(), user=g.user)
        db.session.add(novel)
        db.session.commit()
        return redirect(url_for('main.webnovel'))
    return render_template('novel/novel_create.html', form=form)

@bp.route('/modify/<int:novel_id>', methods=('GET', 'POST'))
@login_required
def modify(novel_id):
    novel = Novel.query.get_or_404(novel_id)
    if g.user != novel.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('question.detail', novel_id=novel_id))
    if request.method == 'POST':  # POST 요청
        form = NovelForm()
        if form.validate_on_submit():
            form.populate_obj(novel)
            novel.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect(url_for('main.webnovel', novel_id=novel_id))
    else:  # GET 요청
        form = NovelForm(obj=novel)
    return render_template('novel/novel_create.html', form=form)

@bp.route('/delete/<int:novel_id>')
@login_required
def delete(novel_id):
    novel = Novel.query.get_or_404(novel_id)
    if g.user != novel.user:
        flash('삭제권한이 없습니다')
        return redirect(url_for('best.detail', novel_id=novel_id))
    db.session.delete(novel)
    db.session.commit()
    return redirect(url_for('best.best'))

