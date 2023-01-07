# Union Find Algorithm

The union-find algorithm, also known as the disjoint set data structure, is a method for tracking the connected components of a graph. It can be used to quickly determine whether two vertices are in the same connected component, and to merge two connected components into a single component.

## How it works

The union-find algorithm uses a data structure called a disjoint set, which consists of a set of elements partitioned into a number of disjoint (non-overlapping) subsets. Each element belongs to a single subset, and each subset represents a connected component of the graph.

The algorithm provides the following operations:

- `find(x)`: Returns the representative element (also called the root) of the subset that x belongs to.
- `union(x, y)`: Merges the subsets that x and y belong to into a single subset.

To implement these operations, the algorithm uses a data structure called a rank, which stores the rank (depth) of each element in the set. The rank of an element is the number of levels below it in the tree. The algorithm also uses a data structure called a parent, which stores the parent of each element in the set. The parent of an element is the element that is one level above it in the tree.

The `find` operation works by following the chain of parents from the element x until it reaches the root of the tree. The `union` operation works by attaching the root of one tree to the root of the other tree, using the ranks to determine which root becomes the parent of the other.

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

Initially, each element is in its own subset, and the ranks and parents are as follows:

| Element | Rank | Parent |
| ------- | ---- | ------ |
| 1       | 0    | 1      |
| 2       | 0    | 2      |
| 3       | 0    | 3      |
| 4       | 0    | 4      |
| 5       | 0    | 5      |

After running the `union(1, 2)` and `union(3, 4)` operations, the ranks and parents are as follows:

| Element | Rank | Parent |
| ------- | ---- | ------ |
| 1       | 0    | 1      |
| 2       | 0    | 1      |
| 3       | 0    | 3      |
| 4       | 0    | 3      |
| 5       | 0    | 5      |

At this point, the elements 1 and 2 are in the same subset, and the elements 3 and 4 are in the same subset. The elements 1, 2, 3, and 4 are all connected, but element 5 is not connected to any of them.

## Code

```python
class UnionFind:
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
            return
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

# Example usage
uf = UnionFind(5)
uf.union(1, 2)
uf.union(3, 4)
print(uf.find(1))  # Output: 1
print(uf.find(2))  # Output: 1
print(uf.find(3))  # Output: 3
print(uf.find(4))  # Output: 3
print(uf.find(5))  # Output: 5
```

In this example, the `UnionFind` class has two data structures, `parent` and `rank`, which store the parent and rank of each element in the set, respectively. The `find` method follows the chain of parents from the element x until it reaches the root of the tree. The `union` method attaches the root of one tree to the root of the other tree, using the ranks to determine which root becomes the parent of the other.