# coding:utf-8
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash,check_password_hash

from app import db
class User(db.Model):
    id = db.Column(db.INTEGER,primary_key=True)
    email = db.Column(db.String(250),unique=True,nullable=False)
    username = db.Column(db.String(250),unique=True,nullable=False)
    password = db.Column(db.String(250),nullable=False)
    login_time = db.Column(db.INTEGER)

    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email
    def __str__(self):
        return 'Users(id={})'.format(self.id)

    @staticmethod
    def set_password(password):
        return generate_password_hash(password)

    @staticmethod
    def check_password(hash,password):
        return check_password_hash(hash,password)

    def get(self,id):
        return self.query.filter_by(id=id).first()

    def add(self,user):
        db.session.add(user)
        return session_commit()

    def update(self):
        return session_commit()

    def delete(self,id):
        self.query.filter_by(id=id).delete()
        return session_commit()

def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return reason

