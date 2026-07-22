operations ={1 : "Addition", 2: "Soustraction", 3: "Multiplication", 4: "Division", 5: "Quitter"}
#operator_symbol = {1: "+", 2: "-", 3: "*", 4: "/"}


def addition (a, b):
    return a + b

def soustraction (a, b):
    return a-b

def multiplication (a, b):
    return a * b

def divion (a, b):
    if b == 0:
        print("Erreur: Division par zéro n'est pas autorisée.")
        return None
    return a / b

result =0
while True:
 user_choice = int(input("Choose an operation:\n1. Addition\n2. Soustraction\n3. Multiplication\n4. Division\n5. Quitter\n"))   
 if user_choice == 1:
        a= float(input("Entrer le premier nombre"))
        b= float(input("Entrer le deuxieme nombre"))
        result = addition(a, b)
 elif user_choice == 2:
        a= float(input("Entrer le premier nombre"))
        b= float(input("Entrer le deuxieme nombre"))
        result = soustraction(a, b) 
 elif user_choice == 3:
         a= float(input("Entrer le premier nombre"))
         b= float(input("Entrer le deuxieme nombre"))
         result = multiplication(a, b)
 elif user_choice == 4:
        a= float(input("Entrer le premier nombre"))
        b= float(input("Entrer le deuxieme nombre"))
        result = divion(a, b)
        if result is None:
         continue 
 elif user_choice == 5:
        print("Exiting the calculator.")
        break
 print("Result:", result)