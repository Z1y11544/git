# def selection(lst):
#     for i in range(len(lst)):
#         min_index = i
#         for j in range(i + 1, len(lst)):
#             if lst[j] < lst[min_index]:
#                 min_index = j
#         lst[i], lst[min_index] = lst[min_index], lst[i]
#     return lst
# def fonct_inser(lst):
#     for i in range(1,len(lst)):
#         en_cours = lst[i]
#         j = i
#         while j > 0 and lst[j-1] > en_cours:
#             lst[j] = lst[j-1]
#             j -= 1
#         lst[j] = en_cours
#     return lst

# lst = [17,9,20,14,5,3,0,7]
# lst_tri = selection(lst)
# print(selection(lst))
# print(fonct_inser(lst))

# def cherche_dichotomie(lst,x):
#     debut = 0
#     fin = len(lst)-1
#     mid = (debut + fin) // 2
#     while debut <= fin:
#         if lst[mid] == x:
#             return True
#         elif lst[mid] < x:
#             debut = mid + 1
#         else:
#             fin = mid - 1
#         mid = (debut + fin) // 2
#     return False
# print(cherche_dichotomie(lst_tri, 7))

# def somme(liste):
#     if len(liste) == 1:
#         return liste[0]
#     return liste[0] + somme(liste[1:])
# print(somme([3,10,7,4]))

# def inverser_recu(chaine):
#     if len(chaine) == 1:
#         return chaine[0]
#     # return chaine[-1] + inverser(chaine[:-1])
#     return inverser_recu(chaine[1:]) + chaine[0]
# print(inverser_recu('bonjour'))

# def inverser_norm(chaine):
#     result = ""
#     for c in chaine:
#         result = c + result
#     return result
# print(inverser_norm('bonjour'))