from flask import Flask
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from wizz.config import Config
import os
basedir = os.path.abspath(os.path.dirname(__file__))


db = SQLAlchemy()
migrate = Migrate()
mail = Mail()


def create_app():
    app = Flask(__name__)
    # app.config.from_object(Config())
    # config[config_name].init_app(app)
    POSTGRES = {
    'user': 'postgres',
    'pw': 'adekunle',
    'db': 'polywizz',
    'host': 'localhost',
    'port': '5432',
}
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:adekunle@localhost:5432/polywizz'
    app.config["CSRF_ENABLED"] = True
    app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
    app.config["UPLOAD_EXTENSIONS"] = ['.jpg', '.jpeg', '.png', '.doc', '.docx', ".pdf", ".JPG"]
    app.config["AGENT_UPLOAD_EXTENSIONS"] = [".pdf"]
    app.config["WORD_EXTENSIONS"] = ['.doc', '.docx']
    app.config["PICTURE_EXTENSIONS"] = ['.jpg', '.jpeg', '.png', ".JPG"]
    # app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///polywizz'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
    app.config["MAIL_SERVER"] = 'smtp.googlemail.com'
    app.config["MAIL_PORT"] = 587
    app.config["MAIL_USE_TLS"] = True
    app.config["MAIL_USERNAME"] = os.environ.get('MAIL_USERNAME')
    app.config["MAIL_PASSWORD"] = os.environ.get('MAIL_PASSWORD')
    app.config["INSTAGRAM_MAIL_SUBJECT_PREFIX"] = 'From polywizz'
    app.config["INSTAGRAM_MAIL_SENDER"] = 'Polywizz Admin'
    app.config["DEBUG"] = True

    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    from wizz.main import main

    app.register_blueprint(main)

    return app