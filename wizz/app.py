import os
from flask_migrate import Migrate
from wizz import create_app, db


# app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app = create_app("production")
migrate = Migrate(app, db)
