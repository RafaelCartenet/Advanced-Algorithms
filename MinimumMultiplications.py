def minimum_multiplications(p, n):
    z = [[0 for _ in range(n)] for _ in range(n)]
    dims = [p[0][0], p[0][1]]
    for i in range(1, n):
        dims.append(p[i][1])
    for i in range(n - 1):
        z[i][i] = 0
        z[i][i + 1] = dims[i] * dims[i + 1] * dims[i + 2]
    z[n - 1][n - 1] = 0
    for d in range(2, n):
        for i in range(0, n - d):
            j = i + d
            factor = dims[i] * dims[j + 1]
            z[i][j] = min([z[i][k] + z[k + 1][j] + factor * dims[k + 1] for k in range(i, j)])
    return z[0][n - 1]

N = 6
P = [[30, 35],
     [35, 15],
     [15, 5],
     [5, 10],
     [10, 20],
     [20, 25]]

print(minimum_multiplications(P, N))