# -*- coding: utf-8 -*-

import bs4
import epitran
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from wiktionaryparser import WiktionaryParser


# Récupération de la page avec BS
my_url = ['https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Termes_vulgaires_en_anglais','https://fr.wiktionary.org/w/index.php?title=Cat%C3%A9gorie:Termes_vulgaires_en_anglais&pagefrom=rim#mw-pages']

# Préparation du parser
parser = WiktionaryParser()
parser.set_default_language('english')
parser.include_relation('alternative forms')

epi = epitran.Epitran('eng-Latn')

# Préparation de la base de données
import base

for url in my_url:

    uClient = uReq(url)
    page_html = uClient.read()

    page_soup = soup(page_html, "html.parser")

    parser = WiktionaryParser()

    for div in page_soup.findAll("div", {"class":"mw-category-group"}):
        for ul in div.findAll("a"): # parcourir tous les paragraphes
            # Se débarrasser des lignes vides (sauf la première, je ne sais pas pourquoi)
            text = ul.text
            if text == "": # permet de se débarrasser de la première ligne vide
                continue
            print('Extraction du mot: ', text)

            wikiparsedlst = parser.fetch(text)
            for wikiparsed in wikiparsedlst:
                print(wikiparsed)
                # for prop in wikiparsed:
                #     print(prop, wikiparsed[prop])
                #parser.exclude_part_of_speech('noun')
                # print(exprgrossiere)
                etymology = wikiparsed['etymology']
                definitions = []
                categorie = []

                for definitionlst in wikiparsed['definitions']:
                    for definition in definitionlst['text']:
                        definitions.append(definition.strip())
                    if isinstance(definitionlst, list):
                        for partofspeech in definitionlst['partOfSpeech']:
                            print(partofspeech + "\n")
                    else:
                        print(definitionlst['partOfSpeech'] + "\n")
                        categorie.append(definitionlst['partOfSpeech'])
                        print(categorie)

                pronunciations = []
                for pronunciation in wikiparsed['pronunciations']['text']:
                    import re
                    ipa_match = re.findall(r'IPA *: */([^/]*)/', pronunciation)
                    new_list = []
                    for ipa in ipa_match:
                        new_list.append(ipa)
                    print(new_list)
                    script = ''
                    try:
                        script = epi.transliterate(text)
                    except KeyError:
                        continue
                pronunciations.append(script.strip())

                base.insert_grossier(text, '|'.join(categorie), '|'.join(pronunciations), '|'.join(definitions), etymology, 'en')


uClient.close()

#['https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Termes_vulgaires_en_anglais','https://fr.wiktionary.org/w/index.php?title=Cat%C3%A9gorie:Termes_vulgaires_en_anglais&pagefrom=rim#mw-pages','https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Termes_vulgaires_en_espagnol','https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Termes_vulgaires_en_fran%C3%A7ais','https://fr.wiktionary.org/w/index.php?title=Cat%C3%A9gorie:Termes_vulgaires_en_fran%C3%A7ais&pagefrom=connasse#mw-pages','https://fr.wiktionary.org/w/index.php?title=Cat%C3%A9gorie:Termes_vulgaires_en_fran%C3%A7ais&pagefrom=foutre#mw-pages','https://fr.wiktionary.org/w/index.php?title=Cat%C3%A9gorie:Termes_vulgaires_en_fran%C3%A7ais&pagefrom=ratisser+le+bunker#mw-pages']
#['https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Termes_vulgaires_en_italien']
#epi = epitran.Epitran('ita-Latn')