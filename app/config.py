import os

class Config:

    ENV = 'DEV'
    if ENV == 'DEV':
        SECRET_KEY='2d2986a33c9cb2300e9a73a412ef9d29'
        SQLALCHEMY_DATABASE_URI='sqlite:///blog.db'
    else:
        SECRET_KEY = os.getenv('SECRET_KEY')
        SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('EMIL_ADDRESS')
    MAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
