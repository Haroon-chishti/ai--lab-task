# WITH QUEUEUE AND NODE
from collections import deque

class Node:
    def __init__(self, state):
        self.state = state
        self.children = graph[state]

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

def bfs_with_queue(start):
    visited = []
    queue = deque([Node(start)])
    while queue:
        node = queue.popleft()
        if node.state not in visited:
            visited.append(node.state)
            for c in node.children:
                queue.append(Node(c))
    return visited

start = 'A'
print("BFS with (Queue & Node):", bfs_with_queue(start))