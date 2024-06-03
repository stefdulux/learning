import requests
from bs4 import BeautifulSoup
import csv

# lien de la page à scrapper
url = "https://gouvernement.lu/fr.html"
reponse = requests.get(url)

# Vérifier si la requête a réussi
if reponse.status_code != 200:
    print(f"Échec de la requête: {reponse.status_code}")
else:
    page = reponse.content

    # transforme (parse) le HTML en objet BeautifulSoup
    soup = BeautifulSoup(page, "html.parser")

    # récupération de tous les titres et liens
    articles = soup.find_all("a", class_="teaser__link")
    titres_liens = []
    for article in articles:
        titre = article.get_text(strip=True)
        lien = article.get('href')
        if lien and not lien.startswith('http'):
            lien = "https://gouvernement.lu" + lien
        titres_liens.append((titre, lien))

    # Vérifiez si les titres et liens sont trouvés
    if not titres_liens:
        print("Aucun titre ou lien trouvé.")
    else:
        # création du fichier data_gouvernement.csv
        en_tete = ['titre', 'lien']
        with open('data_gouvernement.csv', 'w', newline='', encoding='utf-8') as fichier_csv:
            writer = csv.writer(fichier_csv, delimiter=',')
            writer.writerow(en_tete)
            # écrire les titres et liens
            for titre, lien in titres_liens:
                writer.writerow([titre, lien])
        print("Données enregistrées dans data_gouvernement.csv")
