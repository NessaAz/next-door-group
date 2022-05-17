from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())


class Config:
    SECRET_KEY=os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    

class ProdConfig(Config):
    """"""


config_options={
    'dev': DevConfig,
    'prod': ProdConfig
}