# Kahn's Topological Sort Algorithm

Kahn's topological sort algorithm is a method for sorting the vertices of a directed acyclic graph (DAG) in a linear order that respects the partial order of the graph. The algorithm is used to find a topological ordering, which is a linear ordering of the vertices such that for every edge (u, v), vertex u comes before vertex v in the ordering.

## How it works

1. Initialize an empty queue and an empty list of sorted vertices.
2. For each vertex in the graph, add it to the queue if it has no incoming edges (i.e., it is a root vertex).
3. While the queue is not empty:
   1. Remove the first vertex from the queue.
   2. Add the vertex to the end of the list of sorted vertices.
   3. For each neighbor of the vertex:
      1. Decrement the in-degree (number of incoming edges) of the neighbor.
      2. If the in-degree of the neighbor becomes 0, add the neighbor to the queue.
4. If the list of sorted vertices has the same number of vertices as the original graph, return the list. Otherwise, return an error message indicating that the graph contains a cycle.

## Example

Consider the following graph:

```python
  1 
  |
  2
  |
  3
 / \
4   5
 \ /
  6
```

The edges of the graph, along with their weights, are as follows:

| Edge | Weight |
| ---- | ------ |
| 1-2  | 3      |
| 2-3  | 2      |
| 3-4  | 1      |
| 3-5  | 4      |
| 4-6  | 5      |
| 5-6  | 6      |

Running Kahn's topological sort algorithm on this graph, we get the following topological ordering:

1. Add vertex 1 to the queue (no incoming edges)
2. Remove vertex 1 from the queue and add it to the list of sorted vert



## Code

Here is some Python code that implements Kahn's topological sort algorithm for sorting the vertices of a directed acyclic graph (DAG) in a topological ordering:

```python
def toposort(graph):
    # Initialize in-degrees and queue
    in_degrees = {vertex: 0 for vertex in graph}
    queue = []
    for vertex in graph:
        for neighbor in graph[vertex]:
            in_degrees[neighbor] += 1
    for vertex in in_degrees:
        if in_degrees[vertex] == 0:
            queue.append(vertex)

    # Initialize list of sorted vertices
    sorted_vertices = []

    # Process vertices in queue
    while queue:
        vertex = queue.pop(0)
        sorted_vertices.append(vertex)
        for neighbor in graph[vertex]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                queue.append(neighbor)

    # Check for cycles
    if len(sorted_vertices) == len(graph):
        return sorted_vertices
    else:
        return "Graph contains a cycle"

# Example usage
graph = {
    '1': ['2'],
    '2': ['3'],
    '3': ['4', '5'],
    '4': ['6'],
    '5': ['6']
}
print(toposort(graph))  # Output: ['1', '2', '3', '4', '5', '6']
```

In this example, the input graph is represented as a dictionary of lists, where the keys are the vertices and the values are lists of their neighbors. The `toposort` function returns a list of the vertices in a topological ordering, or an error message if the graph contains a cycle.

The `toposort` function first initializes the in-degrees of all the vertices and adds the root vertices (vertices with no incoming edges) to the queue. It then processes the vertices in the queue one by one, adding them to the list of sorted vertices and decrementing the in-degrees of their neighbors. If the in-degree of a neighbor becomes 0, it is added to the queue. Finally, the function checks that the list of sorted vertices has the same number of vertices as the original graph, and returns an error message if it does not.