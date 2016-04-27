from collections import deque

def dfs_longest(graph, current, visited=set()):
    if current not in visited:
        visited.add(current)
        nexts = get_neighbours(graph, current)
        if nexts:
            return 1 + max([dfs_longest(graph, node, visited) for node in nexts])
    return 0


def bfs_longest(graph, start):
    visited = set()
    next = deque(get_neighbours(graph, start))
    visited.add(start)
    while next:
        current = next.popleft()
        visited.add(current)
        [next.append(node) for node in get_neighbours(graph, current) if node not in visited]
    return current


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
        node1 = edge.pop()
        if node1 not in graph:
            add_node(graph, node1)
        if edge:
            node2 = edge.pop()
            if node2 not in graph:
                add_node(graph, node2)
        else:
            node2 = node1
        graph[node2].append(node1)
        graph[node1].append(node2)
    return graph


def add_node(graph, node):
    if node not in graph:
        graph[node] = []


n = int(input())
E = []
for i in range(n):
    E.append(input().split())

n1 = E[0][0]
G = edges_to_graph(E)

print(dfs_longest(G, bfs_longest(G, n1)) // 2)