students = {"Med" : [10, 12, 20],
            "Sama" : [9, 14, 8],
            "Maha" : [7, 6, 11]
            }

def calculer_moyenne(notes):
    total = sum(notes)
    average = total / len(notes)
    return average

for name, note in students.items():
    moy = calculer_moyenne(note)
    if moy >= 10:
        print("the average ", moy ,"of", name,"Good")
    else:
          print("the average ", moy ,"of", name,"Bad")