# Exercice "Micros"
x = int(20)

x = ["pomme", "banana", "cerise"]
print(x)
print(type(x))

x = tuple(("pomme", "banana", "cerise"))

#conversion

x=float(1)
y=int(2.8)
z=complex(1)

print(x)
print(y)
print(z)

a=float(x)
b=int(y)
c=complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#afficher un nombre aléatoire entre 1 et 10
import random
x = random.randrange(1,10)
print(x)


#type string
a = """blabla
test
tarata
"""
print(a)

a="Salut"
print(a[1])

for x in "Banana":
    print(x)

#Afficher la longueur de la chaine "Lait"
a = "Lait"
print(len(a))

#J'ai une phrase, je souhaite "détecter" un mot dans cette phrase
#a = "Voila la phrase"
#print("la" in a)

# j'aimerais afficher quelque chose de plus sympa que True ou False...

a = "Voila la phrase"
if "la" in a:
    print("Trouvé")

if "la" not in a:
    print("Pas Trouvé")

# Le "slicing"

a = "Exemple"
print(a[2:4])

#Comment afficher la position du départ jusqu'au caractère 4 ?
# Affichher que le m par exemple

a = "Exemple"
print(a[:4])

# Si je peux afficher pl, au moins 2 solutions... J'aimerais partir "à l'envers" de la chaine
a = "Exemple"
print(a[-3:-1])

#Tester
print(bool("Hello"))
print(bool(15))

#Retourne False :
print(bool(None))
print(bool(0))
print(bool(False))
print(bool(""))
print(bool(()))
print(bool([]))

def maFonction() :
    return True
print(maFonction())

# PROBLEME
#J'aimerais tester si un nombre est entier...

x=100
print(isinstance(x,int))

x=float(1)
y=float(3.4)
z=float("6")
s=float("4.5")

print(type(x))
print(type(y))
print(type(z))
print(type(s))

#b,c = test()
 #rappel notre tuple était 5,6
# for i in a:
 #    print(i)

# récupèrérer l'élément unique présent dans le tuple
# tuple
#  approche 1
# c = b[0]
# c
# 3
# approche 2
# d, = b
# d
# 3
#
# autre syntaxe nom_variable, =
# u = [5]
# v, = u
# v
# 5

# Exercice 1

#prenom = "Pierre"
#age = 20
#majeur = True
#compte_en_banque = float(20135.384)
#amis = ["Marie", "Julien", "Adrien"]
#parents = tuple("Marc", "Caroline")

# Exercice 2
#Corriger l'erreur

site_web = "google"
print(site_web)

# Exercice 3
# Variable d'un type vers un autre
# Après avoir déclarer une variable afficher "le nombre est 17"
nombre = 17
print("Le nombre est"+str(nombre))

# Exercice 4
#Trouver la valeur de la variabe
# On veut "printer" la valeur que contient la variable a

a=3
b=6
a=b
b=7

print(6)

# Exercie 5
a=2
b=6
c=3
print(a,b,c, sep=" + ")
# comment printer les valeurs ? et leur somme d'un coup ? On veut afficher "2 + 6 + 3"
# Contrainte : utiliser une nouvelle fonctionnalité python 3

# Exercice 6 : Corriger le code suivant :
#list = range(3)
#list2 = range(5)
#print(list(list2))

list1 = range(3)
list2 = range(5)
print(list(list2))
# list est une fontcion

# Exercice 7
# Vérifier qu'une variable est bien d'un certain type
prenom = "Vincent"
if type(prenom) == str:
    print("la varaible est une chaine")
#condition et printer "la varaible est une chaine"

prenom = 0
if isinstance(prenom, str):
    print("la variable est un entier")
#condition et printer " la variable est un entier" ou rien si vous poursuivez le test pour la chaîne de caractère

# Exercice 8
# Remplacer un mot par un autre dans la chaîne "Salut les dev". Rempalcer Salut par Bonsoir

phrase = "Salut les dev"
nouvelle_phrase = phrase.replace("Salut", "Bonsoir")
print(nouvelle_phrase)

#extraction
print(nom[:5])
print(nom[5:])
print(nom[2:5])

#exemple
mon_nom_fois_4 = mon_nom * 4
print(mon_nom_fois_4)

