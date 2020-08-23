# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# engine = create_engine('postgresql+psycopg2://postgres:admin@localhost:5432/apiDB')
# Session = sessionmaker(bind=engine)

# Base = declarative_base()

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'admin'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:admin@localhost:5432/apiDB'

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True