X = "."+"ABCBDAB"
Y = "."+"BDCABA"
n = len(X)-1
m = len(Y)-1

# Flèche vers le haut : 1
# Flèche vers la gauche : 2
# Diagonale : 3

Z = [[0 for _ in range(m+1)] for _ in range(n+1)]
B = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if X[i] == Y[j]:
            Z[i][j] = Z[i-1][j-1] + 1
            B[i][j] = 3
        else:
            if Z[i-1][j] >= Z[i][j-1]:
                Z[i][j] = Z[i-1][j]
                B[i][j] = 2
            else:
                Z[i][j] = Z[i][j-1]
                B[i][j] = 1

print(*Z,sep='\n')
print(Z[n][m])
print(*B,sep='\n')

i, j = n, m

chaine = ""

while (i!=0)|(j!=0):
    if B[i][j] == 3:
        chaine += Y[j]
        i, j = i-1, j-1
    elif B[i][j] == 2:
        j -= 1
    else:
        i -= 1

print(chaine[::-1])
