from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import config
import os
basedir = os.path.abspath(os.path.dirname(__file__))


db = SQLAlchemy()
mail = Mail()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    mail.init_app(app)

    from wizz.main import main

    app.register_blueprint(main)

    
    return app