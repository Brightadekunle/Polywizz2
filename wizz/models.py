from itsdangerous import TimedJSONWebSignatureSerializer as serializer
from datetime import datetime
from wizz import db
from flask import current_app



class Document(db.Model):
    __tablename__ = 'documents'
    {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    image_file = db.Column(db.String(300), nullable=False, default='image.jpg')
    saved_image_file = db.Column(db.String(300), nullable=False, default='image1.jpg')
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow)

    def generate_token(self, expiration=3600):
        s = serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id}).decode('utf-8')

class NewDocument(db.Model):
    __tablename__ = 'newdocuments'
    {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))