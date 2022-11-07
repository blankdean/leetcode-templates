# DFS of adjacency matrix (graph)
def dfs(graph: Dict[int, List[int]], cur: int, visited: Set[int]):
    if cur in visited: return
    
    visited.add(cur)
    print(cur, end = " ")
    
    for next in graph[cur]:
        dfs(graph, next, visited)


# BFS of adjacency matrix (graph)
def bfs(graph: Dict[int, List[int]], node: int):
    q = deque([node])
    visited = set([node])

    while q:
        cur = q.popleft()
        
        print(cur, end = " ")
        
        for next in graph[cur]:
            if next in visited: 
                continue
                
            q.append(next)
            visited.add(next)


# DFS Iterative
def DFS(self,s):            
    visited = [False for i in range(self.V)]

    stack = []
    stack.append(s)

    while (len(stack)):
       
        s = stack[-1]
        stack.pop()

        # Stack may contain same vertex twice. So
        # we need to print the popped item only
        # if it is not visited.
        if (not visited[s]):
            print(s,end=' ')
            visited[s] = True

        # Get all adjacent vertices of the popped vertex s
        # If a adjacent has not been visited, then push it
        # to the stack.
        for node in self.adj[s]:
            if (not visited[node]):
                stack.append(node)
