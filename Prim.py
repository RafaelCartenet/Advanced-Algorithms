"""
Algorithme de Prim :
Etant donné un graph non orienté pondéré, trouver l'arbre couvrant de poids mi-
nimal.

Je représente mes graphes en python dans un dictionnaire (map):
exemple :

G = {'a': {'b': 4, 'c': 2},
     'b': {'a':5, 'c': 1},
     'c': {'a': 2}}

Il y a un arc entre a et b de poid 4, un entre a et c de poid 2, un entre b et
a de poid 5 etc.
J'ai ainsi créé plusieurs méthodes permettant de manipuler les graphes, décrites
ci-dessous.
Il faut préciser à l'algorithme de Prim le sommet de départ, on peut le choisir
aléatoirement.
La sortie de l'algorithme est un autre dictionnaire (map) ayant pour clé un
sommet et en valeur son prédécesseur. Le premier sommet n'a pas de prédecesseur
c'est donc -1.

Remarque :
- On stocke les points restants (et leur distance) sous forme de tas pour
  augmenter la complexité, accès ajout et tri très rapide.


Rafael Cartenet
"""

import heapq
import operator


def prim(graph, start):
    # Dictionnaire des prédecesseurs.
    prev = {}
    # Dictionnaire des distances des sommets par rapport à l'arbre construit.
    dist = {}
    # Set permettant de stocker les sommets déjà visités.
    visited = set()

    # On initialise les dictionnaires.
    for node in graph:
        prev[node] = -1             # -1 pour tous les sommets
        dist[node] = float('inf')   # +Inf pour tous les sommets ..
    dist[start] = 0                 # .. sauf le premier

    # On stocke les sommets restants avec leur distance dans une liste de tuple
    # ce qui va nous permettre de trier les sommets restants par rapport à leur
    # distance. Passage par des tas (heaps).
    remaining_nodes = [(dist[node], node) for node in graph]

    while remaining_nodes: # Tant qu'il y a des sommets non reliés à l'arbre.
        # Passage en heap (+tri à chaque fois).
        heapq.heapify(remaining_nodes)

        # Extraction du sommet le plus prêt.
        closest_node = heapq.heappop(remaining_nodes)[1]
        visited.add(closest_node)

        # On met à jour les distances des voisins si besoin, ainsi que les
        # sommets précédents.
        for node in get_neighbours(graph, closest_node):
            if node not in visited:
                if graph[closest_node][node] < dist[node]:
                    dist[node] = graph[closest_node][node]
                    prev[node] = closest_node
                    # On supprime le sommet des sommets restants.
                    ind = list(map(operator.itemgetter(1), remaining_nodes)).index(node)
                    remaining_nodes[ind] = (dist[node], node)

    # on renvoit le dictionnaire de prédecesseurs.
    return prev


"""
Méthode permettant d'ajouter un arc entre les sommets edge d'un poid weight.
Nous sommes dans le cas des graphes non orientés donc on ajoute cette arrête aux
deux sommets.
"""
def add_edge(graph, edge, weight):
    edge = set(edge)
    node1 = edge.pop()
    if edge:
        node2 = edge.pop()
    else:
        node2 = node1
    graph[node1][node2] = weight
    graph[node2][node1] = weight


"""
Méthode permettant d'ajouter un nouveau sommet à mon graphe.
"""
def add_node(graph, node):
    if node not in graph:
        graph[node] = {}


"""
Méthode permettant de renvoyer tous les sommets voisins d'un noeud.
Sortie : une liste de sommets
"""
def get_neighbours(graph, node):
    nodes = []
    if node in graph:
        for neighbour in graph[node]:
            if neighbour not in nodes:
                nodes.append(neighbour)
    return nodes


"""
Méthode permettant de créer un graphe à partir d'arrêtes. On suppose que notre
graphe ne peux alors pas contenir de points non connectés (pas important).
Les arrêtes sont en entrée sous forme d'une liste d'arrêtes :
[sommet1, sommet2, poid]
Sortie : un graphe
"""
def edges_to_graph(edges):
    graph = dict()
    for edge in edges:
        weight = edge.pop()
        node1 = edge.pop()
        if node1 not in graph:
            add_node(graph, node1)
        if edge:
            node2 = edge.pop()
            if node2 not in graph:
                add_node(graph, node2)
        else:
            node2 = node1
        graph[node2][node1] = weight
        graph[node1][node2] = weight
    return graph


"""
Méthode d'affichage d'un graphe
"""
def to_string(graph):
    res = "Graph :\n"
    for k in graph:
        res += str(k) + " : " + str(graph[k]) + "\n"
    return res


E = [['A', 'B', 3],
     ['A', 'C', 5],
     ['B', 'C', 6],
     ['B', 'D', 7],
     ['C', 'D', 1],
     ['D', 'C', 2],
     ['E', 'F', 3],
     ['F', 'C', 5]]


H = edges_to_graph(E) # Création d'un graphe à partir d'arrêtes.

print(to_string(H)) # Affichage du graphe.
print(prim(H,'A')) # Affichage des prédecesseurs de l'arbre obtenu.
