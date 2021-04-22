import random

nb_myst = random.randint(0, 100)
choix_user = ""
nb_essais = 5

while choix_user != nb_myst:
    try:
        print("Devinez le nombre mystère compris entre 0 et 100")
        print(f"Il vous reste {nb_essais} essais")
        choix_user = int(input("Votre choix : "))

        # Si le nb rentré par l'utilisateur est plus petit ou plus grand que le nombre mystère
        if choix_user < nb_myst:
            print("Le nombre mystère est plus grand \n")
            nb_essais -= 1
            choix_user = ""
        elif choix_user > nb_myst:
            print("Le nombre mystère est plus petit \n")
            nb_essais -= 1
            choix_user = ""

        # Si le nb rentré par l'utilisateur est égal au nb mystère
        if choix_user == nb_myst:
            print("Vous avez trouvé le nombre mystère ! \n")
            print(f"Il vous aura fallu {6 - nb_essais} essais pour trouver le nombre mystère \n")
            break

        # Si le joueur utilise tout les essais
        if nb_essais == 0:
            print("Vous avez utilisé tous vos essais, recommencez ! \n")
            nb_myst = random.randint(0, 100)
            nb_essais = 5
            choix_user = ""
    
    except ValueError:
        print("Veuillez entrer un nombre valide")
        continue
