#1 Imput des nombres entre virgules
Nombres = input("Merci de me donner une liste de nombre séparés par des virgulkes (1,2,3,4) : ")
print("Les nombres saisis sont : " + Nombres)

#2 la somme des nombres est calculée
somme = 0
list_Nombres = Nombres.split(",")
for unite in list_Nombres:
    somme = somme + int(unite)

print("La somme de ces nombres est : " + str(somme))

#3 Calcul de la moyenne
quantite = len(list_Nombres)
moyenne = somme / quantite
print("La moyenne de ces nombres est : " + str(moyenne))

#4 calcul de la quantité supérieur à la moyenne
quantite_sup_moyenne = 0
for unite in list_Nombres:
    if int(unite) > moyenne:
        quantite_sup_moyenne = quantite_sup_moyenne + 1
print("Il y a " + str(quantite_sup_moyenne) + " nombres au dessus de la moyenne")

#5 calcul du nombre de nombre pairs
quantite_paires = 0
for unite in list_Nombres:
    if int(unite) % 2 == 0:
        quantite_paires = quantite_paires + 1
print("Il y a " + str(quantite_paires) + " nombres pairs dans la liste")


