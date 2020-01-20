import sys, ast
from itertools import permutations

def etape(permutation):
    size = len(permutation)
    for i in range(size):
        for j in range(i + 1, size):
            if haut(permutation[i] - permutation[j]) == haut(i - j):
                return False
    return True

def resultat(la_list):
    list_permututation = []
    solutions = []

    for bas in list(range(len(la_list))):
        if bas not in la_list:
            list_permututation.append(bas)

    la_list=list(filter((-1).__ne__, la_list))

    for permutation in permutations(list_permutution):
        permutation=list(permutation)
        permutation=la_list+permutation
        if etape (permutation):
            solutions.append(permutation)
    return len(solutions)
