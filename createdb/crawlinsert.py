# -*- coding: utf-8 -*-

import bs4
import epitran
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from wiktionaryparser import WiktionaryParser

# Récupération de la page avec BS
my_urls = {
    'en' : ['https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Termes_vulgaires_en_anglais', 'https://fr.wiktionary.org/w/index.php?title=Cat%C3%A9gorie:Termes_vulgaires_en_anglais&pagefrom=rim#mw-pages'],
    'fr': ['https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Termes_vulgaires_en_fran%C3%A7ais','https://fr.wiktionary.org/w/index.php?title=Cat%C3%A9gorie:Termes_vulgaires_en_fran%C3%A7ais&pagefrom=connasse#mw-pages','https://fr.wiktionary.org/w/index.php?title=Cat%C3%A9gorie:Termes_vulgaires_en_fran%C3%A7ais&pagefrom=foutre#mw-pages','https://fr.wiktionary.org/w/index.php?title=Cat%C3%A9gorie:Termes_vulgaires_en_fran%C3%A7ais&pagefrom=ratisser+le+bunker#mw-pages'],
    'es': ['https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Termes_vulgaires_en_espagnol'],
# (pas d'epitran pour l'Italien)   'it': ['https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Termes_vulgaires_en_italien'], 
}

epitran_langs = {
    'en': 'eng-Latn',
    'fr': 'fra-Latn',
    'es': 'spa-Latn',
}

for lang in my_urls:

    parser = WiktionaryParser()
    parser.set_default_language(lang)
    parser.include_relation('alternative forms')
    epi = epitran.Epitran(epitran_langs[lang])

    # Préparation de la base de données
    import base

    urllst = my_urls[lang]
    for url in urllst:

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
                print('Query Wikitionnary for word: ', text)

                wikiparsedlst = parser.fetch(text)
                for wikiparsed in wikiparsedlst:
                    # print(wikiparsed)
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
                        # if isinstance(definitionlst, list):
                        #     for partofspeech in definitionlst['partOfSpeech']:
                        #         print(partofspeech + "\n")
                        if len(definitionlst):
                            # print(definitionlst['partOfSpeech'] + "\n")
                            categorie.append(definitionlst['partOfSpeech'])
                            # print(categorie)

                    pronunciations = []
                    for pronunciation in wikiparsed['pronunciations']['text']:
                        import re
                        ipa_match = re.findall(r'IPA *: */([^/]*)/', pronunciation)
                        new_list = []
                        for ipa in ipa_match:
                            pronunciations.append(ipa)
                    if not len(pronunciations):
                        try:
                            pronunciations.append(epi.transliterate(text))
                        except KeyError:
                            continue
                    base.insert_coarseword(text, '|'.join(categorie), '|'.join(pronunciations), '|'.join(definitions), etymology, lang)

        uClient.close()
