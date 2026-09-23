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