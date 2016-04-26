def fill_Z(Z, n):
    for i in range(n):
        Z[i][i] = 0
        Z[i][i+1] = P[i]*P[i+1]*P[i+2]
    for d in range(1,n-2):
        for i in range(1,n-d):
            j=i+d
            print(i,j)


def P_to_tab(P, n):
    temp = [0]
    temp.append(P[0][0])
    temp.append(P[0][1])
    for i in range(1,n):
        temp.append(P[i][1])
    return temp

#n = int(input())
#P = []

n = 6
P = [[30, 35],
     [35, 15],
     [15, 5],
     [5, 10],
     [10, 20],
     [20, 25]]

Z = [[0 for _ in range(n+1)] for _ in range(n+1)]
P = P_to_tab(P, n)
print(*P)
fill_Z(Z, n)
print(*Z, sep='\n')
