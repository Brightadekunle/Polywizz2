import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    

    @staticmethod
    def init_app(app):
        pass


config = {
    # 'development': DevelopmentConfig,
    'default': Config
}