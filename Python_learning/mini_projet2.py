def calculer_moyenne(notes):
    total = sum(notes)
    average = total / len(notes)
    return average
numbers_students =int(input("Enter the number of students:"))
    
students = {}
while True:
    try:
            number_notes = int(input("Enter the number of notes: "))
            break
    except ValueError:
                print("Erreur: just number")
for i in range(numbers_students):
    #name = input("Enter the name:")
    name = input("Enter the name: ")
    notes = []   # liste vide pour stocker les notes de CET étudiant

    for j in range(number_notes):
        note = float(input("Enter a note: "))
        notes.append(note)   # ajoute la note à la liste

#print(name, "has notes:", notes)

    students[name] = notes

#print(students)
for name, note in students.items():
    moy = calculer_moyenne(note)
    if moy >= 10:
        print("the average ", moy ,"of", name,"Successed")
    else:
          print("the average ", moy ,"of", name,"Failed")

