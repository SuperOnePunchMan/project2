import os
from decouple import config

class Config():
    SECRET_KEY = config('SECRET_KEY', default='supersecretkey')
    DEBUG = config('DEBUG', default=False, cast=bool)

class productionConfig(Config):
    pass


class TestingConfig(Config):
    pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL', default='sqlite:///default.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

config_dict = {
    'development': DevelopmentConfig,
    'production': productionConfig,
    'testing': TestingConfig
}


