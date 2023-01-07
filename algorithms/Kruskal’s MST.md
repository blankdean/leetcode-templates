# Kruskal's Minimum Spanning Tree Algorithm

Kruskal's algorithm is a method for finding the minimum spanning tree in a weighted, connected graph. A minimum spanning tree is a subgraph of the original graph that includes all of the vertices and is a tree, meaning it has no cycles. The weight of a minimum spanning tree is the sum of the weights of all the edges in the tree.

## How it works

1. Sort the edges of the graph in non-decreasing order of weight.
2. Initialize a tree with all the vertices, but no edges.
3. For each edge, in order of increasing weight:
   1. If adding the edge would not create a cycle, add it to the tree.
4. When all the edges have been considered, the tree is the minimum spanning tree.

## Example

Consider the following graph:

```
  1-----2
  |\   /|
  | \ / |
  |  5  |
  | / \ |
  |/   \|
  3-----4
```

The edges of the graph, along with their weights, are as follows:

| Edge | Weight |
| ---- | ------ |
| 1-2  | 3      |
| 1-3  | 5      |
| 1-5  | 4      |
| 2-4  | 2      |
| 3-4  | 6      |
| 3-5  | 1      |
| 4-5  | 3      |

Sorting the edges by weight, we get the following list:

| Edge | Weight |
| ---- | ------ |
| 3-5  | 1      |
| 2-4  | 2      |
| 1-2  | 3      |
| 4-5  | 3      |
| 1-5  | 4      |
| 1-3  | 5      |
| 3-4  | 6      |

Starting with an empty tree, we add the edges in order, as long as they do not create a cycle:

| Tree    | Edge Added |
| ------- | ---------- |
| (empty) |            |
| 5       | 3-5        |
| 2       | 2-4        |
| 1       | 1-2        |
| 4       | 4-5        |
| 3       | 1-5        |

At this point, adding any more edges would create a cycle, so we stop. The final tree is:

```
  1-----2
  |     |
  |     |
  |  5  |
  |     |
  |     |
  3-----4
```

The weight of this tree is 1 + 2 + 3 + 3 = 9, which is the minimum possible weight for any tree that includes all of the vertices.



## Code

To detect a cycle in Python when using Kruskal's minimum spanning tree algorithm, you can use a disjoint set data structure, also known as a union-find data structure. This data structure is used to track the connected components of a graph and can quickly determine whether adding an edge to the tree would create a cycle.

Here is some example Python code that uses a disjoint set to detect a cycle in Kruskal's algorithm:

``` python
# Implementation of a disjoint set data structure
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False  # Adding this edge would create a cycle
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1
        return True

# Kruskal's algorithm using a disjoint set to detect cycles
def kruskal(edges, n):
    # Sort the edges by weight
    edges.sort(key=lambda x: x[2])

    disjoint_set = DisjointSet(n)
    minimum_spanning_tree = []
    for edge in edges:
        u, v, w = edge
        if disjoint_set.union(u, v):
            minimum_spanning_tree.append((u, v, w))
    return minimum_spanning_tree

# Example usage
edges = [(0, 1, 3), (1, 2, 2), (2, 3, 5), (3, 4, 4), (4, 0, 1)]
n = 5
print(kruskal(edges, n))  # Output: [(0, 4, 1), (1, 2, 2), (3, 4, 4)]
```

In this example, the disjoint set data structure is used to track the connected components of the graph as the edges are added to the minimum spanning tree. When the `union` method is called, it returns `False` if adding the edge would create a cycle, and `True` otherwise. The algorithm only adds an edge to the minimum spanning tree if `union` returns `True`.



## Time complexity

Kruskal's algorithm has a time complexity of O(E log E), where E is the number of edges in the graph. This is because the algorithm sorts the edges by weight, which takes O(E log E) time.

