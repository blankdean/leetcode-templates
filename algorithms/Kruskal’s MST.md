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

## Time complexity

Kruskal's algorithm has a time complexity of O(E log E), where E is the number of edges in the graph. This is because the algorithm sorts the edges by weight, which takes O(E log E) time.

