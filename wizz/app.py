import os
from wizz import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')