# Dijkstra's Algorithm

Dijkstra's algorithm is a method for finding the shortest path between two vertices in a weighted, directed graph. It can be used to solve the single-source shortest path problem, where the shortest path from a source vertex to all other vertices in the graph is calculated.

## How it works

1. Initialize a distance array, where the distance from the source vertex to each vertex is stored. Set the distance to all vertices as infinity, except for the source vertex, which is set to 0.
2. Initialize a priority queue and add all the vertices to it, with their distances as the priority.
3. While the priority queue is not empty:
   1. Extract the vertex with the minimum distance from the queue.
   2. For each neighbor of the vertex:
      1. Calculate the distance to the neighbor through the current vertex.
      2. If the calculated distance is less than the current distance to the neighbor, update the distance and set the current vertex as the predecessor of the neighbor.
4. The distances and predecessors form a shortest path tree.

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

Running Dijkstra's algorithm from the source vertex 1, we get the following distances and predecessors:

| Vertex | Distance | Predecessor |
| ------ | -------- | ----------- |
| 1      | 0        | -           |
| 2      | 3        | 1           |
| 3      | 5        | 1           |
| 4      | 7        | 2           |
| 5      | 4        | 1           |

Using these distances and predecessors, we can reconstruct the shortest paths from the source vertex 1 to all other vertices:

| Vertex | Shortest Path |
| ------ | ------------- |
| 1      | 1             |
| 2      | 1-2           |
| 3      | 1-3           |
| 4      | 1-2-4         |
| 5      | 1-5           |

## Code

Here is some Python code that implements Dijkstra's algorithm for finding the shortest path between two vertices in a weighted, directed graph:

```python
# Dijkstra's algorithm
def dijkstra(graph, source):
    # Initialize distances and predecessors
    distances = {vertex: float('inf') for vertex in graph}
    predecessors = {vertex: None for vertex in graph}
    distances[source] = 0

    # Initialize priority queue
    queue = []
    for vertex in graph:
        heapq.heappush(queue, (distances[vertex], vertex))

    # Process vertices in the queue
    while queue:
        distance, vertex = heapq.heappop(queue)
        if distance == distances[vertex]:  # Only process vertex if it is not already processed
            for neighbor, weight in graph[vertex].items():
                new_distance = distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = vertex
                    heapq.heappush(queue, (new_distance, neighbor))

    return distances, predecessors

# Example usage
graph = {
    '1': {'2': 3, '3': 5, '5': 4},
    '2': {'4': 2},
    '3': {'4': 6, '5': 1},
    '4': {'5': 3}
}
source = '1'
distances, predecessors = dijkstra(graph, source)
print(distances)  # Output: {'1': 0, '2': 3, '3': 5, '4': 7, '5': 4}
print(predecessors)  # Output: {'1': None, '2': '1', '3': '1', '4': '2', '5': '1'}
```

In this example, the input graph is represented as a dictionary of dictionaries, where the keys are the vertices and the values are dictionaries of their neighbors and the weights of the edges to those neighbors. The `dijkstra` function returns a tuple of two dictionaries, one containing the distances from the source vertex to all other vertices and the other containing the predecessors of each vertex in the shortest path tree.

The `dijkstra` function uses a priority queue, implemented using Python's `heapq` module, to process the vertices in order of increasing distance. It updates the distances and predecessors of each vertex as it processes them, and adds them back to the queue if their distance is updated. This ensures that the algorithm always processes the vertex with the minimum distance first.

## Time complexity

Dijkstra's algorithm has a time complexity of O((V + E) log V), where V is the number of vertices and E is the number of edges in the graph. This is because the algorithm uses a priority queue, which takes O(log V) time to insert and extract elements, and it processes each vertex and each edge at least once.

