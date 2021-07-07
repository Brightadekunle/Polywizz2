import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOAD_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.doc', '.docx', ".pdf", ".JPG"]
    AGENT_UPLOAD_EXTENSIONS = [".pdf"]
    WORD_EXTENSIONS = ['.doc', '.docx']
    PICTURE_EXTENSIONS = ['.jpg', '.jpeg', '.png', ".JPG"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    INSTAGRAM_MAIL_SUBJECT_PREFIX = 'From polywizz'
    INSTAGRAM_MAIL_SENDER = 'Polywizz Admin'
    CONVERT_API_SECRET_KEY = os.environ.get("CONVERT_API_SECRET_KEY")
    DEBUG = True
    

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:adekunle@localhost:5432/polywizz'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}