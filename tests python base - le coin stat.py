# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 15:29:06 2024

@author: Nono
"""

def square(x):
    """square a number"""
    return x ** 2

for N in range(1, 4):
    print(f"{N} squared is {square(N)}")
    
liste_nombre = [12, 35, 12, 9, 56, 24, 35, 12, 89, 24, 35, 12]
nombre_cherche = 12
nombre_remplace = 100
l =[]

print("Liste avant remplacement ", liste_nombre)

def remplacer (liste_nombre, nombre_cherche, nombre_remplace):
    for i in liste_nombre:
        if i ==  nombre_cherche:
            i = nombre_remplace
        l.append(i)

remplacer (liste_nombre, nombre_cherche, nombre_remplace)

# Définition en compréhension
liste_carre_com = [x ** 2 for x in range(99)]
print(liste_carre_com)

mots = ["Bonjour", "le", "monde", "Python", "est", "génial"]
mots_long = [len(x) for x in mots if len(x) > 3]

# dictionnaire avec les nombres au carré de 0 à 99
dict_carre = {k:k**2 for k in range(0,99)}
print(dict_carre)

#filtrer sur produits dont le prix est <= prix_max
produits = {'pommes': 30, 'bananes': 15, 'cerises': 20}

def filtrer_produits(produits,prix_max):
    produits2 =   {k:v for k,v in produits.items() if v<=prix_max}
    return produits2
    
filtrer_produits(produits,16)

#dc3 - exo 3

a = [12, 35, 9, 56, 24, 89, 24]
 
def remplace(liste,seuil):
    b = [i for i in liste if i>seuil]
    return b

remplace(a, 13)

a = [("Marie", 85), ("Pierre", 92), ("Julie", 78)]

def aff(a):
    for prenom,note in a:
        print("L'élève {} a obtenu la note de {}/100.".format(prenom,note))
        
#DC4 6 - librairie Numpy
import numpy as np

array1 = np.random.random([5,3])
array_sum = np.sum(array1)
array_mean = np.mean(array1)
array_std = np.std(array1)
array_min = np.min(array1)
array_max = np.max(array1)
array_sqrt = np.sqrt(array1)
array_abs = np.abs(array1)
array_power = np.power(array1, 2)
array_exp = np.exp(array1)
array_log = np.log(np.abs(array1))
array_sin = np.sin(array1)
array_median = np.median(array1)

matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array_with_matrice = np.array(matrice)
np.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

inverse = np.linalg.inv(matrice)
np.linalg.det(matrice)

#maj numpy_array - indexation
elements_respectant_condition = np.array(matrice)[np.array(matrice)> 2]
indices = np.where(np.array(matrice) > 3)

#  Slicing et indexation avancée
array6 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Slicing
premiere_ligne = array6[0, :]
preliere_colonne = array6[:,0]
premiere_ligne

# Indexation avancée
lignes = [0, 1]
colonnes = [1, 2]
elements_selectionnes = array6[lignes, colonnes]
elements_selectionnes

# Diffusion (broadcasting) - etendue des valeurs pour faire +
array9 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array10 = np.array([1, 2, 3])
array9+array10

#r redimensionné le numpy array
array3 = np.arange(9) 
array3.shape #((9,))
array3_redimensionne = array3.reshape((3, 3))
print(array3_redimensionne)

array1_allonge = np.append(array9, [6, 7, 8])
print(array1_allonge)
#attention ajout en colonne => (12,)


#Quelques modules utiles en data science

#math: Pour les fonctions mathématiques de base.
#statistics Pour faire des statistiques
#os: Pour interagir avec le système d'exploitation, comme la gestion des chemins de fichiers et les commandes du système d'exploitation.
#sys: Fournit un accès à certaines variables et fonctions qui interagissent fortement avec l'interpréteur Python.
#json: Pour la lecture et l'écriture de données au format JSON.
#csv: Pour lire et écrire des fichiers CSV.
#datetime: Pour manipuler les dates et les heures.
#random: Pour la génération de nombres aléatoires.
#re: Pour les expressions régulières, utiles dans le traitement de texte et le nettoyage des données.
#sqlite3: Pour la gestion de bases de données SQL légères.
#pickle: Pour la sérialisation et la désérialisation de structures de données Python.

# Importer et renommer tout le module 
%run description.py
import description as desc 
# Création de la liste
chiffre_affaires = [3000, 5000, 4000, 8000, 10000]
# Application de la fonction 
statdescca = desc.statdescriptive(chiffre_affaires)
print(statdescca)

# Exemple d'utilisation de random (choice, seed,sample,randint,shuffle)
import random

# Lecture et ecriture fichiers txt
with open("resultatbisv2.txt", "w") as f:
    for i in range(0,10):
        f.write(f"La valeur est {i}\n")
# Lecture deuxième approche (readlines et read().splitlines())
with open("resultatbisv2.txt", "r") as f:
    resultat = f.readlines()
resultat

#Lecture et ecriture fichiers csv
import csv
with open("test.csv","w") as f:
    reader = csv.reader(f,delimiter=',')







