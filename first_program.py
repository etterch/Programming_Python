# Fonction pure
def addition(a, b):
   return a + b
# Fonction d'ordre supérieur
def multiplier(facteur):
   def appliquer(valeur):
       return valeur * facteur
   return appliquer
double = multiplier(2)
triple = multiplier(3)
print(addition(5, 7)) # 12
print(double(4)) # 8
print(triple(4)) # 12

x=1
y=3
x=y
y=x+y
z=_
print(z) 