import random
secret_number = random.randint(1, 100)
cpt = 0
while True:
    
    user_number =  int(input("Entrer un nombre"))
    cpt += 1
    if user_number > secret_number:
        print("le nombre secret est plus petit que", user_number)
    elif user_number < secret_number:
        print("le nombre secret est plus grand que", user_number)
    else:
        print("Félicitations! Vous avez trouvé le nombre secret.")
        break
    
print("Nombre d'essais:", cpt)