

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            print(f"  Key {key} not found in tree.")
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Case 1: Leaf node (no children)
            if node.left is None and node.right is None:
                return None
            # Case 2: One child
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
       
            else:
                successor = self._min_node(node.right)
                node.key = successor.key
                node.right = self._delete(node.right, successor.key)

        return node

    def _min_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)



class Graph:
    def __init__(self):
 
        self.adj = {}

    def add_node(self, node):
        if node not in self.adj:
            self.adj[node] = []

    def add_edge(self, u, v, weight):
        self.add_node(u)
        self.add_node(v)
        self.adj[u].append((v, weight))

    def print_adjacency_list(self):
        print("  Adjacency List:")
        for node in self.adj:
            edges = ", ".join(f"{v}(w={w})" for v, w in self.adj[node])
            print(f"    {node} -> {edges if edges else 'None'}")

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        order = []

        while queue:
            node = queue.pop(0)
            order.append(node)
            for neighbour, _ in self.adj.get(node, []):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        return order

    def dfs(self, start):
        visited = set()
        order = []
        self._dfs(start, visited, order)
        return order

    def _dfs(self, node, visited, order):
        visited.add(node)
        order.append(node)
        for neighbour, _ in self.adj.get(node, []):
            if neighbour not in visited:
                self._dfs(neighbour, visited, order)




class HashTable:
    def __init__(self, size=5):
        self.size = size
      
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
        # update if key already exists
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                return True
        return False

    def print_table(self):
        print(f"  Hash Table (size={self.size}):")
        for i, bucket in enumerate(self.table):
            content = " -> ".join(f"({k}, {v})" for k, v in bucket)
            print(f"    Bucket[{i}]: {content if content else 'empty'}")



def run_bst():
    print("\n--- Task 1: Binary Search Tree ---\n")

    bst = BST()
    values = [50, 30, 70, 20, 40, 60, 80]
    print(f"Inserting: {values}")
    for v in values:
        bst.insert(v)

    print(f"Inorder after insertions: {bst.inorder()}")

    print("\nSearch 20:", bst.search(20))
    print("Search 90:", bst.search(90))

    # Also insert 65 so 60 has one child before deleting
    bst.insert(65)
    print(f"\nInserted 65. Inorder now: {bst.inorder()}")

    print("\nDeleting 20 (leaf node):")
    bst.delete(20)
    print(f"  Inorder: {bst.inorder()}")

    print("\nDeleting 60 (one child - has child 65):")
    bst.delete(60)
    print(f"  Inorder: {bst.inorder()}")

    print("\nDeleting 30 (two children - has left 40, right subtree):")
    bst.delete(30)
    print(f"  Inorder: {bst.inorder()}")

    print("\nDeleting 50 (root node, two children):")
    bst.delete(50)
    print(f"  Inorder: {bst.inorder()}")


def run_graph():
    print("\n--- Task 2: Graph BFS and DFS ---\n")

    g = Graph()
    edges = [
        ('A', 'B', 2), ('A', 'C', 4),
        ('B', 'D', 7), ('B', 'E', 3),
        ('C', 'E', 1), ('C', 'F', 8),
        ('D', 'F', 5),
        ('E', 'D', 2), ('E', 'F', 6),
    ]
    for u, v, w in edges:
        g.add_edge(u, v, w)

    g.print_adjacency_list()

    bfs_result = g.bfs('A')
    print(f"\n  BFS from A: {' -> '.join(bfs_result)}")

    dfs_result = g.dfs('A')
    print(f"  DFS from A: {' -> '.join(dfs_result)}")


def run_hash_table():
    print("\n--- Task 3: Hash Table (Separate Chaining, size=5) ---\n")

    ht = HashTable(size=5)
    keys = [10, 15, 20, 7, 12]
    values = ['ten', 'fifteen', 'twenty', 'seven', 'twelve']

    print("Inserting keys:", keys)
    for k, v in zip(keys, values):
        ht.insert(k, v)
        print(f"  insert({k}, '{v}') -> bucket[{k % 5}]")

    print()
    ht.print_table()

    print("\nRetrieving keys:")
    for k in [10, 7, 12]:
        print(f"  get({k}) = {ht.get(k)}")

    print("\nDeleting key 15 (bucket[0], collides with 10 and 20):")
    ht.delete(15)
    ht.print_table()

    print("\nGet 15 after deletion:", ht.get(15))


if __name__ == "__main__":
    run_bst()
    run_graph()
    run_hash_table()

    print("\nAll tasks done.")
