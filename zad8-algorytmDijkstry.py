import heapq  

class Graph:
    def __init__(self):
        self.graph = {}  

    def add_edge(self, u, v, weight):
        """Dodaj krawędź do grafu"""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight)) 

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.graph}  
        previous_nodes = {node: None for node in self.graph} 
        distances[start] = 0
        pq = [(0, start)]  

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        return distances, previous_nodes

    def print_shortest_path(self, start, end):
        """Wyświetl najkrótszą odległość i ścieżkę od start do end"""
        distances, previous_nodes = self.dijkstra(start)
        if distances[end] == float('inf'):
            print(f"Nie ma ścieżki od {start} do {end}.")
            return

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous_nodes[current]
        path = path[::-1]  

        print(f"Najkrótsza odległość od {start} do {end}: {distances[end]}")
        print(f"Ścieżka: {' -> '.join(map(str, path))}")


g = Graph()
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 4)
g.add_edge(2, 3, 2)
g.add_edge(2, 4, 6)
g.add_edge(3, 4, 3)

g.print_shortest_path(1, 4) 
