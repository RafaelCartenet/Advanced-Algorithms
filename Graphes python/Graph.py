from collections import deque

def dfs(graph, current, target, visited=set()):
    if current not in visited:
        visited.add(current)
        if current == target:
            return True
        else:
            nexts = get_neighbours(graph, current)
            return True in [dfs(graph, node, target, visited) for node in nexts]
    return False

def bfs(graph, start, target):
    visited = set()
    next = deque(get_neighbours(graph, start))
    visited.add(start)
    while next:
        current = next.popleft()
        if current == target:
            return True
        else:
            visited.add(current)
            [next.append(node)for node in get_neighbours(graph, current)if node not in visited]
    return False

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


def find_path(graph, start, end, path=[]):
    path += [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


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
    return graph


def add_edge(graph, edge):
    edge = set(edge)
    node1 = edge.pop()
    if edge:
        node2 = edge.pop()
    else:
        node2 = node1
    if node1 in graph:
        graph[node1].append(node2)
    else:
        graph[node1] = [node2]


def add_node(graph, node):
    if node not in graph:
        graph[node] = []


def get_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            if {neighbour, node} not in edges:
                edges.append({node, neighbour})
    return edges


def get_neighbours(graph, node):
    nodes = []
    if node in graph:
        for neighbour in graph[node]:
            if neighbour not in nodes:
                nodes.append(neighbour)
    return nodes


def to_string(graph):
    res = "Graph :\n"
    for k in graph:
        res += str(k) + " : " + str(get_neighbours(graph, k)) + "\n"
    return res


G = {'A': ['B', 'C'],
     'B': ['C', 'D'],
     'C': ['D'],
     'D': ['C'],
     'E': ['F'],
     'F': ['C']}

V = ['A', 'B', 'C', 'D', 'E', 'F']
E = [['A', 'B'],
     ['A', 'C'],
     ['B', 'C'],
     ['B', 'D'],
     ['C', 'D'],
     ['D', 'C'],
     ['E', 'F'],
     ['F', 'C']]

# n = int(input())
# E = []
# for i in range(n):
#     E.append(input().split())

G = edges_to_graph(E)
print(to_string(G))

print(dfs(G, 'A', 'E', set()))
print(bfs(G, 'A', 'E'))