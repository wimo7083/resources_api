from decouple import config

DEBUG = True

SECRET_KEY = config('DEV_SECRET_KEY', default='secret yo')

TOKEN = config('DEV_BOT_TOKEN', default='token')
APP_TOKEN = config('DEV_APP_TOKEN', default='token')
VERIFICATION_TOKEN = config('DEV_AUTH_TOKEN', default='token')


SQLALCHEMY_TRACK_MODIFICATIONS = False
