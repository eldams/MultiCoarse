from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
@app.route('/home')
def home():
   return render_template('home.html') 

@app.route('/result')
def result():
    
    db=sqlite3.connect('coarsewords.db')
    print(db)
    res=db.execute(" select * from coarseword")
    mots= res.fetchall()
    lstmots = ''
    lstmots += '<table>'
    lstmots += '<tr>'
    lstmots += '<th style="background-color:rgb(238, 130, 238);">Mot </th>'
    lstmots += '<th style="background-color:DodgerBlue;">Phonetique </td>'
    lstmots += '<th style="background-color:Tomato;">Definition </td>'
    lstmots += '<th style="background-color:hsla(9, 100%, 64%, 0.5);">Etymologie </td>'
    lstmots += '<th style="background-color:rgb(255, 165, 0);">Langue </td>'
    lstmots += '</tr>'
    for mot in mots:
        lstmots += '<tr>'
        lstmots += '<td style="background-color:rgb(238, 130, 238);">' + mot[0]+'</td>'
        lstmots += '<td style="background-color:DodgerBlue;">'+ mot[1]+ '</td>'
        lstmots += '<td style="background-color:Tomato;">'+  mot[2]+ '</td>'
        lstmots += '<td style="background-color:hsla(9, 100%, 64%, 0.5);">' +  mot[3]+ '</td>'
        lstmots += '<td style="background-color:rgb(255, 165, 0);">'+  mot[4]+ '</td>'
        lstmots += '</tr>'
    lstmots += '</table>'
    return lstmots 
##if __name__ == "__main__":
##    app.run()
