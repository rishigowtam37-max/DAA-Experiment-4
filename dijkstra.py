import heapq

def dijkstra(graph, start):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distance[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight

            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distance


# Graph Representation
graph = {
    0: [(1, 4), (2, 2)],
    1: [(0, 4), (2, 1), (3, 5)],
    2: [(0, 2), (1, 1), (3, 8), (4, 10)],
    3: [(1, 5), (2, 8), (4, 2), (5, 6)],
    4: [(2, 10), (3, 2), (5, 3)],
    5: [(3, 6), (4, 3)]
}

start = 0

distances = dijkstra(graph, start)

print("Shortest distances from source vertex", start)

for vertex in sorted(distances):
    print(f"Vertex {vertex}: {distances[vertex]}")
