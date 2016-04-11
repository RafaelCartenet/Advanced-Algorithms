# Etant donné n cubes élémentaires,
# quel est le nombre minimal de tas de forme cube ou pyramide ?
#
# Rafael Cartenet

# Calcul des z(i) pour i allant de 1 à n
def pre(k):
    Z.append(0)
    for n in range(1,k+1):
        Z.append(min([Z[n-i] for i in T if i <=n])+1)

# Input : entier
n=int(input())

# Calcul des valeurs
# Cubes : liste des i au cube pour i allant de 1 à n^(1/3)
cube=[i**3 for i in range(1,int(n**(1/3)+1))]

# Pyramides : liste des sommes des carrés de i pour i allant de 1 à 3n^(1/3)
pyra=[int(i*(i+1)*(2*i+1)/6)for i in range(1,int((3*n)**(1/3)))]

# Création du tableau T : fusion de listes triées en une liste triée.
c,p=0,0
T=[]
while (c<len(cube))&(p<len(pyra)):
    if cube[c] == pyra[p]:
        T.append(pyra[p])
        p, c = p+1, c+1
    elif cube[c]<pyra[p]:
        T.append(cube[c])
        c += 1
    else:
        T.append(pyra[p])
        p += 1
# concaténation de la liste non vide restante
if cube[c:] == []:
    T += pyra[p:]
else:
    T += cube[c:]

# Initialisation du tableau Z
Z=[]

# Calcul des éléments du tableau Z jusqu'à l'indice n
pre(n)

# Output : dernier élément du tableau (indice n)
print(Z[-1])
