import os


SECRET_KEY = os.environ.get('SECRET_KEY')
UPLOAD_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.doc', ".pdf"]
SQLALCHEMY_DATABASE_URI = 'sqlite:///polywizz.db'
