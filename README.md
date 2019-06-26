# MultiCoarse

Graphic and phonetic search for coarse (rude, vulgar) words in multiple languages. Based on the Wiktionnary list of those words in some language, currently English, French, Spanish, Italian (TBC).

## Requirements

- python modules (pip): epitran wiktionaryparser bs
- flite : http://www.speech.cs.cmu.edu/flite/

## Extract coarse words from Wiktionary

``
cd createdb
python base.py
python crawlinsert.py
``

This will create the file `createdb/coarsewords.db`

## Run the web server

``
cd flask
cd multicoarseweb
ln -s ../../createdb/coarsewords.db
python run.py
``

Server should be locally visible : http://127.0.0.1:5000
