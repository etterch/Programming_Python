gestionnaire_taches={1: "Ajouter une tâche", 2: "Afficher les tâches", 3: "Marquer une tâche comme terminée",4: "Supprimer une tâche", 5: "Quitter"}

list_taches=[]
while True:
 for num, operation in gestionnaire_taches.items():
    print(num, "-", operation)
 user_choice = int(input("Choisissez une opération: "))
 if user_choice == 5:
        break
 elif user_choice == 1:
        tache = input("Entrer la tache à ajouter: ")
        list_taches.append({"tache": tache, "terminee": False})
 elif user_choice == 2:
        if not list_taches:
            print("Aucune tâche à afficher.")
        else:
            for index, task in enumerate(list_taches, start=1):
                    if task["terminee"]:
                         status = "X"
                    else:
                         status = " "
                    print(index, ".[", status, "]", task["tache"])

 elif user_choice == 3:
       if not list_taches:
            print("Aucune tâche à marquer comme terminée.")
       else:
            for index, tache in enumerate(list_taches, start=1):
               print(index, "-", tache["tache"])
            task_number = int(input("Entrez le numero de la tache à marquer comme terminée: "))
            if task_number < 1 or task_number > len(list_taches):
                print("Numéro de tâche invalide.")
            else:
                 list_taches[task_number-1]["terminee"] = True
 elif user_choice == 4:
      if not list_taches:
                  print("Aucune tâche à marquer comme terminée.")
      else:
                  for index, tache in enumerate(list_taches, start=1):
                     print(index, "-", tache["tache"])
                  task_number = int(input("Entrez le numero de la tache à marquer comme terminée: "))
                  if task_number < 1 or task_number > len(list_taches):
                      print("Numéro de tâche invalide.")
                  else:
                      del list_taches[task_number-1]