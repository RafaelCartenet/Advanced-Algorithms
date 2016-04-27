"""
Etant donné la multiplication de n matrices, on veut trouver le nombre mini-
mum de multiplications à réaliser pour calculer le produit de ces n matrices.

Rappel :
z(i,j) = nombre de multiplications minimal pour faire le produit Ai*...*Aj

Rafael Cartenet
"""

def minimum_multiplications(p, n):
    # On stocke les dimensions des matrices dans une liste dims, p[0] p[1] étant
    # les dimensions de la matrice 0, et p[i] (i de 1 à n-1) la deuxième dimen-
    # sion de la matrice i.
    dims = [p[0][0], p[0][1]]
    for i in range(1, n):
        dims.append(p[i][1])

    # On initialise le tableau z (n*n).
    z = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n - 1):
        z[i][i] = 0 # diagonale nulle
        z[i][i + 1] = dims[i] * dims[i + 1] * dims[i + 2] # diagonale supérieure
    z[n - 1][n - 1] = 0

    # On parcourt les diagonales 2 à n-1
    for d in range(2, n):
        for i in range(0, n - d):
            j = i + d
            factor = dims[i] * dims[j + 1]
            z[i][j] = min([z[i][k] + z[k + 1][j] + factor * dims[k + 1] for k in range(i, j)])

    # Affichage du tableau z:
    #print(*z,sep='\n')

    # Le résultat est donc le nombre minimal de multiplications pour faire le
    # produit A0*...*An-1 : z(0,n-1)
    return z[0][n - 1]

N = 6 # nombre de matrices.
P = [[30, 35], # dimensions des matrices.
     [35, 15],
     [15, 5],
     [5, 10],
     [10, 20],
     [20, 25]]

print(minimum_multiplications(P, N))
