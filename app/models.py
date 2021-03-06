#-*- coding:utf-8 -*-

from .apps import db

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    user_count = db.Column(db.String(100), unique=True)
    user_name = db.Column(db.String(100), unique=True)
    user_sex = db.Column(db.String(100))
    user_pwd = db.Column(db.String(100))
    user_mail = db.Column(db.String(100))
    user_phone = db.Column(db.String(100))
    user_addtime = db.Column(db.DateTime, index=True)
    user_photo = db.Column(db.String(100))
    user_ispass = db.Column(db.Integer)

    def check_pwd(self,pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.user_pwd,pwd)


