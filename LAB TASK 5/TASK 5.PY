from collections import defaultdict, deque

class Node:
    def __init__(self, key):
        self.key = key
        self.neighbors = []

def build_graph(adj):
    nodes = {k: Node(k) for k in adj}
    for u, vs in adj.items():
        for v in vs:
            if v not in nodes:
                nodes[v] = Node(v)
            nodes[u].neighbors.append(nodes[v])
    return nodes

def dfs_stack(nodes, start_key):
    visited = set()
    order = []
    stack = [nodes[start_key]]
    while stack:
        node = stack.pop()
        if node.key in visited:
            continue
        visited.add(node.key)
        order.append(node.key)
        for nb in reversed(node.neighbors):
            if nb.key not in visited:
                stack.append(nb)
    return order

class TNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_iter(root):
    if not root:
        return []
    out = []
    stack = [root]
    while stack:
        node = stack.pop()
        out.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return out

def inorder_iter(root):
    out = []
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        out.append(cur.val)
        cur = cur.right
    return out

def postorder_iter(root):
    out = []
    stack = []
    last = None
    cur = root
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            peek = stack[-1]
            if peek.right and last is not peek.right:
                cur = peek.right
            else:
                out.append(peek.val)
                last = stack.pop()
    return out

if __name__ == "__main__":
    adj = {0:[1,2],1:[2,3],2:[3],3:[1,4],4:[]}
    nodes = build_graph(adj)
    order = dfs_stack(nodes, 0)
    print("DFS (stack) order:", order)
    root = TNode(1,TNode(2,TNode(4),TNode(5)),TNode(3,TNode(6),TNode(7)))
    print("Preorder:", preorder_iter(root))
    print("Inorder:", inorder_iter(root))
    print("Postorder:", postorder_iter(root))