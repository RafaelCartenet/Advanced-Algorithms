# Prim algorithm
# Find the minimum spanning tree of a connected undirect graph.
# Complexity O(n²)

import heapq
import operator

def prim(graph, start):
    prev = {}
    dist = {}
    visited = set()

    for node in graph:
        prev[node] = -1
        dist[node] = float('inf')
    dist[start] = 0
    remaining_nodes = [(dist[node], node) for node in graph]

    while remaining_nodes:
        heapq.heapify(remaining_nodes)
        closest_node = heapq.heappop(remaining_nodes)[1]
        visited.add(closest_node)
        for node in get_neighbours(graph, closest_node):
            if node not in visited:
                if graph[closest_node][node] < dist[node]:
                    dist[node] = graph[closest_node][node]
                    prev[node] = closest_node
                    ind = list(map(operator.itemgetter(1), remaining_nodes)).index(node)
                    remaining_nodes[ind] = (dist[node], node)
    return prev


def add_edge(graph, edge, weight):
    edge = set(edge)
    node1 = edge.pop()
    if edge:
        node2 = edge.pop()
    else:
        node2 = node1
    graph[node1][node2] = weight
    graph[node2][node1] = weight


def add_node(graph, node):
    if node not in graph:
        graph[node] = {}


def get_neighbours(graph, node):
    nodes = []
    if node in graph:
        for neighbour in graph[node]:
            if neighbour not in nodes:
                nodes.append(neighbour)
    return nodes


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


def to_string(graph):
    res = "Graph :\n"
    for k in graph:
        res += str(k) + " : " + str(graph[k]) + "\n"
    return res


V = ['A', 'B', 'C', 'D', 'E', 'F']
E = [['A', 'B', 3],
     ['A', 'C', 5],
     ['B', 'C', 6],
     ['B', 'D', 7],
     ['C', 'D', 1],
     ['D', 'C', 2],
     ['E', 'F', 3],
     ['F', 'C', 5]]

H = edges_to_graph(E)
print(to_string(H))

print(prim(H,'A'))
