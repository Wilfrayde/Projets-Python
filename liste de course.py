liste_course = []
choix_user = 0

while choix_user != 5:
    print("Menu :")
    print("1. Ajouter un élément à la liste de courses")
    print("2. Retirer un élément de la liste de courses")
    print("3. Afficher les éléments de la liste de courses")
    print("4. Vider la liste de courses")
    print("5. Quitter le programme")

    try:
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
            print("Ma liste de course contient : ")
            for elmt in liste_course:
                print(elmt)
                
        # Vider entièrement la liste
        if choix_user == 4:
            liste_course.clear()
            print("La liste de course a entièrement été supprimée !")
            choix_user = 0
    
    # Si l'utilisateur choisit une autre action que celles indiquées
    except ValueError:
        print("Ce n'est pas une action valide")
        choix_user = 0
