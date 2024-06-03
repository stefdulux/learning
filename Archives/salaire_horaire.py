def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12

def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel / 4

def salaire_horaire(salaire_hebdomadaire,hor_hbdo):
    return salaire_hebdomadaire / hor_hbdo

Salaire_annuel = float(input("Merci de bien vouloir saisir votre salaire annuel : "))
horaire_Hebdo = float(input("Merci de bien vouloir m'indiquer le nombre d'heure travaillé par semaine : "))

salmens = salaire_mensuel(Salaire_annuel)

salhebdo = salaire_hebdomadaire(salmens)

salhor = salaire_horaire(salhebdo, horaire_Hebdo)

print(f"Votre salaire horaire est de {salhor:.2f} euros")
