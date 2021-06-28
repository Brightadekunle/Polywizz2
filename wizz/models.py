from datetime import datetime
from wizz import db


class Document(db.Model):
    __tablename__ = 'documents'
    {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    image_file = db.Column(db.String(300), nullable=False, default='image.jpg')
    saved_image_file = db.Column(db.String(300), nullable=False, default='image1.jpg')
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow)