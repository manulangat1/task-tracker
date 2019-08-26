from app import db
from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),index=True)
    email = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    last_seen = db.Column(db.DateTime,default=datetime.utcnow)
    def __repr__(self):
        return '<User {}'.format(self.username)
    def save(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def commit():
        db.session.commit()
