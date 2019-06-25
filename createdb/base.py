import sqlite3

conn = None
cursor = None

def connect():
    global conn, cursor
    print('Connect to DB')
    conn = sqlite3.connect('coarsewords.db')
    cursor = conn.cursor()

def create_table():
    print('Recreate table')
    cursor.execute('DROP TABLE IF EXISTS coarseword;')
    cursor.execute('CREATE TABLE IF NOT EXISTS coarseword (mot TEXT, catégories TEXT, phonétique TEXT, définition TEXT, étymologie TEXT, langues TEXT )')

def sql_escape(s):
    return '"'+s.replace('"', '""')+'"'

def insert_grossier(mot = '', categorie = '', phonetique = '', definition = '', etymologie = '', langue = ''):
    print('Insert grossier')
    mot = sql_escape(mot)
    categorie = sql_escape(categorie)
    phonetique = sql_escape(phonetique)
    definition = sql_escape(definition)
    etymologie = sql_escape(etymologie)
    langue = sql_escape(langue)
    cursor.execute('INSERT INTO coarseword(mot, catégories, phonétique, définition, étymologie, langues) VALUES ('+mot+','+categorie+','+phonetique+','+definition+','+etymologie+','+langue+')')
    conn.commit()

connect()
create_table()
insert_grossier()
