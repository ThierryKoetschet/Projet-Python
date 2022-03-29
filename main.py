# Auteur :         Thierry Koetschet
# Projet :         Suite de Fibonacci en Python
# Version :        1.0
# Date :           28.03.2022
# Description :    Programme permettant d'afficher la suite de Fibonacci en demandant la longueur de la suite
#                  à l'utilisateur et en utilisant les tableaux

# variables utiles à l'affichage de la suite de fibonacci
nombrePrecedent, nombreActuel = 0, 1

# demande à l'utilisateur de donner une valeur pour la suite de fibonacci
longueurFibonacci = int(input("Donnez une longueur pour la suite de fibonacci : "))

# vérifie que le nombre donné est un entier
if longueurFibonacci <= 0:
   print("Veuillez entrer un nombre positif")
# si la longueur de la suite est de 1, retourne le nombreActuel
elif longueurFibonacci == 1:
   print("Fibonacci sequence upto",longueurFibonacci,":")
   print(nombrePrecedent)
# génère la suite de fibonacci
else:
   print(nombrePrecedent, end=' ')
   for x in range(1, longueurFibonacci):
       print(nombreActuel, end=' ')
       nombreActuel += nombrePrecedent
       nombrePrecedent = nombreActuel - nombrePrecedent