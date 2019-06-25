from flask_sqlalchemy import SQLAlchemy

from .views import app

import logging as lg

# Create database connection object
db = SQLAlchemy(app)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mot = db.Column(db.String(200), nullable=False)
    phonetique = db.Column(db.String(200), nullable=False)
    definition = db.Column(db.String(200), nullable=False)
    etymologie = db.Column(db.String(200), nullable=False)
    langues = db.Column(db.String(200), nullable=False)

    def __init__(self, mot, phonetique, definition, etymologie, langues):
        self.mot = mot
        self.phonetique = phonetique
        self.definition = definition
        self.etymologie = etymologie
        self.langues = langues
##    def data_entry():
##	# J'ai retiré rowid qui est généré tout seul
##    print('Insert data')
##    cursor.execute('INSERT INTO coarsewords.db(mot, phonetique, definition, etymologie, langues) VALUES ("putain", "bla", "mot grossier", "ancien", "fr")')
        

db.create_all()

def init_db():
    #db.session.data_entry()
    db.create_all()
    db.session.add(Content("THIS IS SPARTAAAAAAA!!!", 1))
    db.session.add(Content("What's your favorite scary movie?", 0))
    db.session.commit()
    lg.warning('Database initialized!')
