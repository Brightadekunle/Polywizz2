from flask import Flask
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from wizz.config import Config


db = SQLAlchemy()
migrate = Migrate()
mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(Config())
    # config[config_name].init_app(app)

    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    from wizz.main import main

    app.register_blueprint(main)

    return app