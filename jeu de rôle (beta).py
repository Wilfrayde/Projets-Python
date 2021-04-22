import random

player_life = 50
ennemy_life = 50
player_pot = 3
player_choice = ""

while player_life > 0 and ennemy_life > 0:
    print(f"Il vous reste {player_pot} potions. \n")
    print("Votre choix :")
    print("1. Attaquer")
    print("2. Utiliser une potion")
    player_choice = int(input(""))

    # L'utilisateur attaque
    if player_choice == 1:
        ennemy_life -= random.randint(5, 10)
        player_life -= random.randint(5, 15)
        print(f"Vous attaquez l'ennemi, il lui reste {ennemy_life} PV")
        print(f"L'ennemi vous attaque, il vous reste {player_life} PV.")
        print("-------------------------------------------------")
        player_choice = ""

    # L'utilisateur utilise une potion
    if player_choice == 2 and player_pot > 0:
        print("Vous passez votre tour...")
        player_pot -= 1
        player_life += random.randint(15, 50)
        print(f"Vous buvez une potion et avez maintenant {player_life} PV.")
        player_life -= random.randint(5, 15)
        print(f"L'ennemi vous attaque, il vous reste {player_life} PV.")
        print("-------------------------------------------------")
        player_choice = ""
    elif player_pot == 0:
        print("Vous n'avez plus aucune potion !")
        print("-------------------------------------------------")
        player_choice = ""   
else:
    if player_life <= 0:
        print("Vous avez perdu la partie ! \nFin du jeu.")
    elif ennemy_life <= 0:
        print("Vous avez gagnez la partie ! \nFin du jeu.")



# Modif à apporter :
# Ne plus avoir de nb négatif en affichant le nb de PV du joueur et de l'ennemi
# Afficher le nb de dégât du tour
