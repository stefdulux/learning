import requests
import csv

# lien de la page à scrapper
url = "https://www.gov.uk/search/news-and-communications"
reponse = requests.get(url)

# Vérifier si la requête a réussi
if reponse.status_code != 200:
    print(f"Échec de la requête: {reponse.status_code}")
else:
    page = reponse.content.decode('utf-8')  # Assurez-vous que le contenu est encodé en UTF-8

    # création du fichier data_html.csv
    with open('data_html.csv', 'w', newline='', encoding='utf-8') as fichier_csv:
        writer = csv.writer(fichier_csv)
        writer.writerow(['html_content'])  # En-tête du fichier CSV
        writer.writerow([page])  # Écrire le contenu HTML dans une seule cellule

    print("Contenu HTML enregistré dans data_html.csv")
