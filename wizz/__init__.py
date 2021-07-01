from flask import Flask
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()
mail = Mail()


def create_app(config_file='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    from wizz.main import main

    app.register_blueprint(main)

    return app