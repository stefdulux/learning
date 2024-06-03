import requests
from bs4 import BeautifulSoup
import csv

# récupère les titres ou descriptions comme liste de strings
def extraire_donnees(elements):
    resultat = []
    for element in elements:
        resultat.append(element.get_text(strip=True))
    return resultat

# charger la donnée dans un fichier csv
def charger_donnees(nom_fichier, en_tete, titres, descriptions):
    with open(nom_fichier, 'w', newline='', encoding='utf-8') as fichier_csv:
        writer = csv.writer(fichier_csv, delimiter=',')
        writer.writerow(en_tete)
        # zip permet d'itérer sur deux listes à la fois
        for titre, description in zip(titres, descriptions):
            writer.writerow([titre, description])

def etl():
    # lien de la page à scrapper
    url = "https://www.gov.uk/search/news-and-communications"
    reponse = requests.get(url)
    page = reponse.content

    # transforme (parse) le HTML en objet BeautifulSoup
    soup = BeautifulSoup(page, "html.parser")

    # récupération de tous les titres
    titres = soup.find_all("a", class_="gem-c-document-list__item-title")
    # récupération de toutes les descriptions
    descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")

    # Vérifiez si les éléments sont trouvés
    if not titres or not descriptions:
        print("Aucun titre ou description trouvé")
        return

    # Affichage pour vérification
    print("Titres trouvés:", [titre.get_text(strip=True) for titre in titres])
    print("Descriptions trouvées:", [description.get_text(strip=True) for description in descriptions])

    en_tete = ["title", "description"]
    titres = extraire_donnees(titres)
    descriptions = extraire_donnees(descriptions)
    charger_donnees("data.csv", en_tete, titres, descriptions)

etl()

