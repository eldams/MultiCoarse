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
    
    db=sqlite3.connect('grossiers.db')
    print(db)
    res=db.execute(" select * from motsgrossiers ")
    mots= res.fetchall()
    lstmots = ''
    for mot in mots:
        lstmots += "<table>" +"<td style='background-color:rgb(238, 130, 238);'>"+ "Mot : " + mot[0]+"</td>"+ '<td style="background-color:DodgerBlue;">' + "Phonetique : " + mot[1]+ '</td>'   + '<td style="background-color:Tomato;">' + "Definition : "+  mot[2]+ '</td>' +  '<td style="background-color:hsla(9, 100%, 64%, 0.5);">' + "Etymologie : " +  mot[3]+ '</td>' + '<td style="background-color:rgb(255, 165, 0);">' + "Langue : " +  mot[4]+ '</td>' + "</table>"
        
    return lstmots 
##if __name__ == "__main__":
##    app.run()
