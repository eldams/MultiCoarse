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
    cursor.execute('DROP TABLE IF EXISTS coarseword')
    cursor.execute('CREATE TABLE IF NOT EXISTS coarseword (word TEXT, categories TEXT, phonetics TEXT, definition TEXT, etymology TEXT, langs TEXT)')

def sql_escape(s):
    return '"'+s.replace('"', '""')+'"'

def insert_coarseword(word = '', categories = '', phonetic = '', definition = '', etymology = '', lang = ''):
    print('=> Insert coarse word:'+word+','+categories+','+phonetic)
    word = sql_escape(word)
    categories = sql_escape(categories)
    phonetic = sql_escape(phonetic)
    definition = sql_escape(definition)
    etymology = sql_escape(etymology)
    lang = sql_escape(lang)
    cursor.execute('INSERT INTO coarseword(word, categories, phonetics, definition, etymology, langs) VALUES ('+word+','+categories+','+phonetic+','+definition+','+etymology+','+lang+')')
    conn.commit()

connect()
create_table()
# insert_grossier()
