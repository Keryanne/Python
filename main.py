# # Exercice "Micros"
# x = int(20)
#
# x = ["pomme", "banana", "cerise"]
# print(x)
# print(type(x))
#
# x = tuple(("pomme", "banana", "cerise"))
#
# #conversion
#
# x=float(1)
# y=int(2.8)
# z=complex(1)
#
# print(x)
# print(y)
# print(z)
#
# a=float(x)
# b=int(y)
# c=complex(x)
#
# print(a)
# print(b)
# print(c)
#
# print(type(a))
# print(type(b))
# print(type(c))
#
# #afficher un nombre aléatoire entre 1 et 10
# import random
# x = random.randrange(1,10)
# print(x)
#
#
# #type string
# a = """blabla
# test
# tarata
# """
# print(a)
#
# a="Salut"
# print(a[1])
#
# for x in "Banana":
#     print(x)
#
# #Afficher la longueur de la chaine "Lait"
# a = "Lait"
# print(len(a))
#
# #J'ai une phrase, je souhaite "détecter" un mot dans cette phrase
# #a = "Voila la phrase"
# #print("la" in a)
#
# # j'aimerais afficher quelque chose de plus sympa que True ou False...
#
# a = "Voila la phrase"
# if "la" in a:
#     print("Trouvé")
#
# if "la" not in a:
#     print("Pas Trouvé")
#
# # Le "slicing"
#
# a = "Exemple"
# print(a[2:4])
#
# #Comment afficher la position du départ jusqu'au caractère 4 ?
# # Affichher que le m par exemple
#
# a = "Exemple"
# print(a[:4])
#
# # Si je peux afficher pl, au moins 2 solutions... J'aimerais partir "à l'envers" de la chaine
# a = "Exemple"
# print(a[-3:-1])
#
# #Tester
# print(bool("Hello"))
# print(bool(15))
#
# #Retourne False :
# print(bool(None))
# print(bool(0))
# print(bool(False))
# print(bool(""))
# print(bool(()))
# print(bool([]))
#
# def maFonction() :
#     return True
# print(maFonction())
#
# # PROBLEME
# #J'aimerais tester si un nombre est entier...
#
# x=100
# print(isinstance(x,int))
#
# x=float(1)
# y=float(3.4)
# z=float("6")
# s=float("4.5")
#
# print(type(x))
# print(type(y))
# print(type(z))
# print(type(s))
#
# #b,c = test()
#  #rappel notre tuple était 5,6
# # for i in a:
#  #    print(i)
#
# # récupèrérer l'élément unique présent dans le tuple
# # tuple
# #  approche 1
# # c = b[0]
# # c
# # 3
# # approche 2
# # d, = b
# # d
# # 3
# #
# # autre syntaxe nom_variable, =
# # u = [5]
# # v, = u
# # v
# # 5
#
# # Exercice 1
#
# #prenom = "Pierre"
# #age = 20
# #majeur = True
# #compte_en_banque = float(20135.384)
# #amis = ["Marie", "Julien", "Adrien"]
# #parents = tuple("Marc", "Caroline")
#
# # Exercice 2
# #Corriger l'erreur
#
# site_web = "google"
# print(site_web)
#
# # Exercice 3
# # Variable d'un type vers un autre
# # Après avoir déclarer une variable afficher "le nombre est 17"
# nombre = 17
# print("Le nombre est"+str(nombre))
#
# # Exercice 4
# #Trouver la valeur de la variabe
# # On veut "printer" la valeur que contient la variable a
#
# a=3
# b=6
# a=b
# b=7
#
# print(6)
#
# # Exercie 5
# a=2
# b=6
# c=3
# print(a,b,c, sep=" + ")
# # comment printer les valeurs ? et leur somme d'un coup ? On veut afficher "2 + 6 + 3"
# # Contrainte : utiliser une nouvelle fonctionnalité python 3
#
# # Exercice 6 : Corriger le code suivant :
# #list = range(3)
# #list2 = range(5)
# #print(list(list2))
#
# list1 = range(3)
# list2 = range(5)
# print(list(list2))
# # list est une fontcion
#
# # Exercice 7
# # Vérifier qu'une variable est bien d'un certain type
# prenom = "Vincent"
# if type(prenom) == str:
#     print("la varaible est une chaine")
# #condition et printer "la varaible est une chaine"
#
# prenom = 0
# if isinstance(prenom, str):
#     print("la variable est un entier")
# #condition et printer " la variable est un entier" ou rien si vous poursuivez le test pour la chaîne de caractère
#
# # Exercice 8
# # Remplacer un mot par un autre dans la chaîne "Salut les dev". Rempalcer Salut par Bonsoir
#
# phrase = "Salut les dev"
# nouvelle_phrase = phrase.replace("Salut", "Bonsoir")
# print(nouvelle_phrase)
#
# #extraction
# print(nom[:5])
# print(nom[5:])
# print(nom[2:5])
#
# #exemple
# mon_nom_fois_4 = mon_nom * 4
# print(mon_nom_fois_4)

## Cours du 02/11/2022 ##

## GESTION DES EXCEPTIONS ##

# while True :
#     try:
#         x=(input("Identifiant: "))
#         break
#     except ValueError:
#         print("Entrée invalide")
#     finally:
#         print("Gardons le cap")
#
#
# try:
#     2/0
# except ZeroDivisionError:
#     pass
#
# div = input()
# try:
#     div = int(div)
#     if div==1:
#         raise ValueError()
# except ValueError:
#     print("Valeur saisie inutile")
# else:
#     print("Le résultat est ", 7/div)

liste = range(20)
liste_1=[]
for x in liste:
    if x % 2 == 0:
        liste_1.append(x)

print(liste_1)

liste_2 = [x for x in liste if x % 2 == 0]
print(liste_2)

liste_3 = [str(x) for x in liste_2]
print(liste_3)

liste_4 = map(lambda num: num**2, liste_2)
print(liste_4)

for item in liste_4:
    print(item)

liste_5 = [num**2 for num in liste_2]
print(liste_5)

filtre_1 = [item for item in liste_2 if item]
print(filtre_1)

nombres = range(20)
dict_for = {}
for n in nombres :
    if n % 2 == 0:
        dict_for[n] = n**2
    print(dict_for)

#Utiliser les comprehension pour la même chose ?

dict_sans_for = {i: i**2 for i in range(20) if i % 2 == 0}
print(dict_sans_for)

equipe = {'Cristiano':'Juve', 'Hakimi':'Dortmund', 'Kante':'Chelsea'}
equipe_joueur = {equipe[key] for key in equipe}
print(equipe_joueur)
print(equipe)

distance_m = {'v_1':100000, 'v_2':153000, 'v_3':70000}
distance_km = {i:j/1000 for (i,j) in distance_m.items()} #j'aimerai ici  récupérer les v n km dictionnaire distance
print(distance_km)

distance2_m = {'v_1':100, 'v_2':153000, 'v_3':7000}
distance2_km = {i:j/1000 for (i,j) in distance2_m.items() if(j/1000>1)}
print(distance2_km)

#j'aimerai filtrer pou obtenir uniquement les v en en km dans distance2_km

#fonctions Natives / Built-in
import logging
logging.basicConfig(level=logging.INFO)
logging.debug()

d_1 = [[0], [2], [3], [10], [5]]
#Obtenr la valeur maximale à partir des données de la liste ci-dessus max_val
#contrainte : utiliser une fonction lambda dans votre solution

def max_val(d):
    """Trouver la valeur maximale"""
    return max(d, key=lambda x:x)
max_val(d_1)

class felins:
    famille = "mammifères placentaires"
    ordre = "carnivores"
    sous_ordre = "féliformes"

    def man_plac(self):
        """Constructeur"""
        print(self.famille)

    def main():
        tigre = felins()
        tigre.mam.palc()
if __name__ == '__main__':main()

class tigres(felins):
    """classe qui représente un tigre et qui hérite de félin"""
    def __init__(self, type_felin, vitesse):
        self.type_felin = type_felin
        self.vitesse = vitesse

T_1 = tigres("tigre", "100m/h")
T_1.vitesse

issubclass(felins,tigres)
isinstance(T_1, felins)

class Félins:
    def __init__(self, type_félin="tigre", couleur="orange"):
        self.type_félin = "tigre"
        self.couleur = "orange"

class Félins2:
    def __init__(self, type_félin="tigre", couleur="orange"):
        self.type_félin = type_félin
        self.couleur = couleur
    def __str__(self):
        return ("Le félin est de type {} et de couleur {}"
                .format(self.couleur, self.type_félin))

f_1 = Félins()
print(f_1)

f_2 = Félins2()
print(f_2)

class félins:
    def __init__(self, type_félin="tigre", couleur="orange"):
        self.type_félin
        self.couleur = couleur
    def def_couleur(self):
        return self.couleur
    def ch_couleur(self, valeur):
        self.couleur = valeur
    def def_type_félin(self):
        return self.type_félin
    def def_type_félin(self, valeur):
        if valeur == "serpent":
            raise ValueError("Ca va la tête ?")
        self.type_félin = valeur

T_1=félins()
print(T_1.def_couleur(), T_1.def_type_félins())

T_1=ch_couleur("jaune")
print(T_1.def_couleur())


def Afficher_decorateur(function):
    def nouvelle_fonction(a,b):
        print('le résultat de cette opération avec {} et {}'.format(a,b))
        res = function(a,b)
        print('résultat:{}'.format(res))
        return res
    return nouvelle_fonction()

@Afficher_decorateur
def soustraction(a,b):
    return a - b

soustraction(1,2)

@Afficher_decorateur
def addition(a,b):
    return a + b

addition(1,2)

def minuscule(fonc):
    texte = fonc()
    if not isinstance(texte, str):
        raise TypeError("type non adapté")
    return texte.lower()

def salut():
    return "Hello les amis"

minuscule(salut())

@minuscule
def salut():
    return "Hello les amis"

def minuscule(fonc):
    def wrapper():
        texte = fonc()
        if not isinstance(texte, str):
            raise TypeError("type non adapté")
        return texte.lower()
    return wrapper()

@minuscule
def salut():
    return "HELLO les AMIS"
salut()

def adresse_pro(fonc):
    def wrapper():
        texte = fonc()
        res = "".join([texte, "@entreprise.com"])
        return res
    return wrapper()

@adresse_pro
@minuscule

def utilisateur():
    return "Tasnime"


