# Déterminer la plus longue sous-suite commune entre deux suites X et Y.
#
# Rafael Cartenet
#
# Consignes :
# 1) Coder l'algorithme et l'appliquer à l'exemple (ABCBDAB et BDCABA).
# 2) Coder l'écriture de Z.
# 3) Coder l'écriture de Z sans le tableau B.
# 4) Déterminer la plus longue sous-suite de 1001010 et 010110110.
# 5) Trouver une plus longue sous suite croissante de nombres d'une suite de n nombres.


# ------- METHODE 1 : Utilisation de la matrice B ------- #
def LongestSubSequenceWithB(X, Y):
    n = len(X)
    m = len(Y)

# On rajoute un caractère devant les deux chaînes pour ne pas être embêté avec l'indice 0.
    X, Y = "." + X, "." + Y

# Tableau Zij : longueur d'une plus longue sous site connue pour Xi et Yj.
    Z = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

# Tableau Bij : Chemin pour retrouver la plus longue chaîne trouvée.
#   Flèche vers le haut : 1
#   Flèche vers la gauche : 2
#   Flèche en Diagonale : 3
    B = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

# Remplissage du tableau Z et B en même temps.
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if X[i] == Y[j]:
                Z[i][j] = Z[i - 1][j - 1] + 1
                B[i][j] = 3
            else:
                if Z[i - 1][j] >= Z[i][j - 1]:
                    Z[i][j] = Z[i - 1][j]
                    B[i][j] = 2
                else:
                    Z[i][j] = Z[i][j - 1]
                    B[i][j] = 1

# On détermine la chaîne optimale en remontant le tableau Z grâce au tableau B.
    chaine = ""
    i, j = n, m
    while (i != 0) | (j != 0):
        if B[i][j] == 3:
            chaine = Y[j] + chaine
            i, j = i - 1, j - 1
        elif B[i][j] == 2:
            j -= 1
        else:
            i -= 1

# Résultat
    return chaine


# ------- METHODE 2 : Sans l'utilisation de la matrice B ------- #
def LongestSubSequenceWithoutB(X, Y):
    n = len(X)
    m = len(Y)

    X, Y = "." + X, "." + Y

    Z = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if X[i] == Y[j]: Z[i][j] = Z[i - 1][j - 1] + 1
            else:
                if Z[i - 1][j] >= Z[i][j - 1]: Z[i][j] = Z[i - 1][j]
                else: Z[i][j] = Z[i][j - 1]

# On détermine la chaîne optimale en remontant le tableau Z sans l'utilisation du tableau B.
    i, j = n, m
    chaine = ""
    while (i != 0) | (j != 0):
        if X[i] == Y[j]:
            chaine = Y[j] + chaine
            i, j = i - 1, j - 1
        elif Z[i - 1][j] >= Z[i][j - 1]: j -= 1
        else: i -= 1
# Résultat
    return chaine

# Remarques :
# - En

# Exemples :
X = "ABCBDAB"
Y = "BDCABA"
print(LongestSubSequenceWithoutB(X, Y))
print(LongestSubSequenceWithB(X, Y))

X = "11010101"
Y = "010110110"
print(LongestSubSequenceWithoutB(X, Y))
print(LongestSubSequenceWithB(X, Y))
