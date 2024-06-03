#Dans le fichier principal, on peut importer les fonctions de `operations.py` 
#à l'aide de l'instruction `import` , puis les utiliser pour effectuer des opérations.
import my_operations


def main():
    # Utilisation de la fonction addition
    resultat_addition = my_operations.addition(3, 5)
    print("Résultat de l'addition :", resultat_addition)
    # Utilisation de la fonction multiplication
    resultat_multiplication = my_operations.multiplication(8, 2)
    print("Résultat de la multiplication :", resultat_multiplication)


if __name__ == "__main__":
    main()