from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def home():
   return render_template('home.html') 

@app.route('/searchword', methods=['GET'])
def result():    
    db=sqlite3.connect('coarsewords.db')
    # print(request)
    # print(request.method)
    # for key in request.form.keys():
    #     print(key)
    # wordsearched = request.form['word']
    res = db.execute(" select * from coarseword") # WHERE phonetics='wordsearched'
    words = res.fetchall()
    return render_template('result.html', words=words) 
