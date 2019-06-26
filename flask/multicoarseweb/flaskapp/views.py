from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
app.config.from_object('config')

epitran_langs = {
    'en': 'eng-Latn',
    'fr': 'fra-Latn',
    'es': 'spa-Latn',
}

@app.route('/')
def home():
   return render_template('home.html') 

@app.route('/searchword', methods=['GET'])
def result():    
    db=sqlite3.connect('coarsewords.db')
    wordsearch = request.args.get('word')
    langsearch = request.args.get('lang')
    import epitran
    epi = epitran.Epitran(epitran_langs[langsearch])
    wordipa = ''
    try:
        wordipa = epi.transliterate(wordsearch)
    except KeyError:
        pass
    res = db.execute(" select word, categories, phonetics, definition, etymology, langs from coarseword WHERE word='"+wordsearch+"' or phonetics='"+wordipa+"'")
    words = res.fetchall()
    return render_template('result.html', words=words) 
