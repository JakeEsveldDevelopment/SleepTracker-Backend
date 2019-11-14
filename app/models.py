from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password = db.Column(db.String(64))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tired_rating = db.Column(db.Integer)
    wake_rating = db.Column(db.Integer)
    time_slept = db.Column(db.Integer)
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Entry {} {}>'.format(self.user_id, self.date)
