# EX1: B C B D
# EX4:
# a)
# def somme_chiffres(n):
#     if n < 10:        # cas de base
#         return n // 1     # (1)
#     return n % 10 + somme_chiffres(n//10)  # (2) et (3)
# print(somme_chiffres(4050))
# b)
# def contient(L, x):
#     if len(L) == 0:
#         return False    # (4)
#     if L[0] == x:
#         return True    # (5)
#     return contient(L[1:],x)  # (6)
# print(contient([5,8,10,60,50,3,12,14],5))
# c)
# def compter(chaine, c):
#     if chaine == "":
#         return 0    # (7)
#     if chaine[0] == c:
#         return 1 + compter(chaine[1:],c)  # (8) et (9)
#     return compter(chaine[1:],c)            # (10)
# print(compter("caractere","r"))

# EX5
# a)
# def population(n):
#     if n == 0:
#         return 1
#     return 2*population(n-1)
# print(population(3))
# b)
# import os

# def taille_dossier(dossier):
#     taille = 0
#     for element in os.listdir(dossier):
#         chemin = os.path.join(dossier, element)
#         if os.path.isdir(chemin):
#             taille += taille_dossier(chemin)
#         else:
#             taille += os.path.getsize(chemin)
#     return taille

# c)
# import math 

# def longueur_cote(points):
#     if len(points) == 1 :
#         return math.sqrt((points[0][0] ** 2) + (points[0][1] ** 2))
#     return math.sqrt((points[0][0] ** 2) + (points[0][1] ** 2)) + longueur_cote(points[1:])
# print(longueur_cote([(3,4),(5,12),(9,40)]))

# EX6
# a)
# def longueur(L) :
#     if L == []:
#         return 0
#     return 1 + longueur(L[1:])
# print(longueur([1,2,3,4,5,6,7,8,9,10]))

# b)
# def maximum(L):
#     if len(L) == 1 :
#         return L[0]
#     if L[0] > maximum(L[1:]):
#         return L[0]
#     else:
#         return maximum(L[1:])
# print(maximum([1,2,3,15,5,6,7,8,9,10]))

# c)
# def miroir(L):
#     if len(L) == 1:
#         return [L[0]]
#     return miroir(L[1:])+[L[0]]
# print(miroir([1,2,3,15,5,6,7,8,9,10]))

# d)
# def aplatir(L):
#     if L == []:
#         return []
#     if len(L) == 1 :
#         if type(L[0]) == list :
#             return aplatir(L[0])
#         else :
#             return [L[0]]
#     if type(L[0]) == list :
#         return aplatir(L[0]) + aplatir(L[1:])
#     return [L[0]] + aplatir(L[1:])
# print(aplatir([1, [2, 3], [4, [5, 6]]]))