# WITHOUT QUEUEUE AND NODE
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G', 'H'],
    'E': [],
    'F': ['I', 'K'],
    'G': [],
    'H': ['L'],
    'I': [],
    'K': ['M'],
    'L': [],
    'M': []
}

def bfs(graph, start):
    visited = []
    frontier = [start]
    while frontier:
        new_frontier = []
        for node in frontier:
            if node not in visited:
                visited.append(node)
                new_frontier.extend(graph[node])
        frontier = new_frontier
    return visited

start = 'A'
print("BFS Traversal:", bfs(graph, start))
