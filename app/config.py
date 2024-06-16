import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///geographic.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STRIPE_API_KEY = os.environ.get('STRIPE_API_KEY')
