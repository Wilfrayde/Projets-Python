liste_course = []
choix_user = 0

while choix_user != 5:
    print("Menu :")
    print("1. Ajouter un élément à la liste de courses")
    print("2. Retirer un élément de la liste de courses")
    print("3. Afficher les éléments de la liste de courses")
    print("4. Vider la liste de courses")
    print("5. Quitter le programme")
    choix_user = int(input(""))

    # Ajouter un élément à la liste de course
    if choix_user == 1:
        add_element = input("Noter l'élément à ajouter : ")
        liste_course.append(add_element)
        print(f"L'élément {add_element} a bien été ajouté !")
        choix_user = 0
    
    # Retirer un élément de la liste de course
    if choix_user == 2:
        try:
            remove_element = input("Noter l'élément à supprimer : ")
            liste_course.remove(remove_element)
            print(f"L'élément {remove_element} a bien été supprimé !")
            choix_user = 0
        except ValueError:
            print(f"L'élément {remove_element} n'est pas dans la liste !")

    # Afficher la liste de course
    if choix_user == 3:
        print(f"Ma liste de course contient : {liste_course}")
        choix_user = 0

    # Vider entièrement la liste
    if choix_user == 4:
        liste_course.clear()
        print("La liste de course a entièrement été supprimée !")
        choix_user = 0
    
    # Si l'utilisateur choisit une action supérieur à 5 ou inférieure à 0
    if choix_user >= 6 or choix_user <= -1:
        print("Ce n'est pas une action valide")
        choix_user = 0
