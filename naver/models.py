from naver import db

class Novel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    modify_date = db.Column(db.DateTime(), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('novel_set'))



class Number(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    novel_id = db.Column(db.Integer, db.ForeignKey('novel.id', ondelete='CASCADE'))
    novel = db.relationship('Novel', backref=db.backref('number_set'))
    subject = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('number_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)


"""작품 리뷰"""

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    novel_id = db.Column(db.Integer, db.ForeignKey('novel.id', ondelete='CASCADE'))
    novel = db.relationship('Novel', backref=db.backref('review_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    modify_date = db.Column(db.DateTime(), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('review_set'))

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_id = db.Column(db.Integer, db.ForeignKey('number.id', ondelete='CASCADE'))
    number = db.relationship('Number', backref=db.backref('comment_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    modify_date = db.Column(db.DateTime(), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('comment_set'))
    novel_id = db.Column(db.Integer, db.ForeignKey('novel.id', ondelete='CASCADE'), nullable=True)
    novel = db.relationship('Novel', backref=db.backref('comment_set'))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    nick = db.Column(db.String(20), unique=True, nullable=False)
