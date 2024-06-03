import requests
from bs4 import BeautifulSoup
import csv

# lien de la page à scrapper
url = "https://www.gov.uk/search/news-and-communications"
reponse = requests.get(url)

# Vérifier si la requête a réussi
if reponse.status_code != 200:
    print(f"Échec de la requête: {reponse.status_code}")
else:
    page = reponse.content

    # affiche la page HTML
    print(page)

    # transforme (parse) le HTML en objet BeautifulSoup
    soup = BeautifulSoup(page, "html.parser")

    # récupération de tous les titres
    titres = soup.find_all("a", class_="gem-c-document-list__item-title")
    titre_textes = []
    for titre in titres:
        titre_textes.append(titre.get_text(strip=True))

    # récupération de toutes les descriptions
    descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")
    description_textes = []
    for description in descriptions:
        description_textes.append(description.get_text(strip=True))

    # récupération de toutes les dates
    datepubs = soup.find_all("time", class_="gem-c-document-list__attribute")
    datepub_textes = []
    for datepub in datepubs:
        datepub_textes.append(datepub.get_text(strip=True))

    # Vérifiez si les titres, descriptions et dates sont trouvés
    if not titre_textes or not description_textes or not datepub_textes:
        print("Aucun titre, description ou date trouvé.")
    else:
        # création du fichier data2.csv
        en_tete = ['titre', 'description', 'date']
        with open('data2.csv', 'w', newline='', encoding='utf-8') as fichier_csv:
            writer = csv.writer(fichier_csv, delimiter=',')
            writer.writerow(en_tete)
            # zip permet d'itérer sur trois listes à la fois
            for titre, description, date in zip(titre_textes, description_textes, datepub_textes):
                writer.writerow([titre, description, date])
        print("Données enregistrées dans data2.csv")
