import os


# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"

FLASKAPP_ID = 1200420960103822

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'grossiers.db')


