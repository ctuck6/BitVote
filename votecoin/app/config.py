class Config():
    DEBUG = True
    SECRET_KEY = "you-will-never-guess"
    WTF_CSRF_SECRET_KEY = 'you-will-never-guess'

config = {
    "development": Config
}