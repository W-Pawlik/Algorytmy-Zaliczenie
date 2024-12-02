from collections import deque

class Graph:
    def __init__(self):
        self.graph = {} 

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  

    def bfs(self, start):
        visited = set() 
        queue = deque([start]) 
        visited.add(start)

        print("BFS order:", end=" ")
        while queue:
            current = queue.popleft()
            print(current, end=" ")

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()


g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
g.add_edge(3, 7)

g.bfs(1)  
