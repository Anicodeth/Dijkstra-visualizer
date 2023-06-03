import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    # Create a dictionary to store the shortest distances from the start node
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0

    # Create a set to keep track of visited nodes
    visited = set()

    while len(visited) < len(graph.nodes):
        # Find the node with the minimum distance
        min_distance = float('inf')
        min_node = None
        for node in graph.nodes:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node

        # Mark the node as visited
        visited.add(min_node)

        # Update the distances of the neighboring nodes
        for neighbor in graph.neighbors(min_node):
            new_distance = distances[min_node] + graph[min_node][neighbor]['weight']
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances

# Create an example graph
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'C', weight=1)
G.add_edge('B', 'D', weight=10)
G.add_edge('C', 'D', weight=8)
G.add_edge('C', 'E', weight=10)
G.add_edge('D', 'E', weight=2)

# Compute the shortest distances using Dijkstra's algorithm
distances = dijkstra(G, 'A')

# Print the shortest distances
for node, distance in distances.items():
    print(f'Shortest distance from A to {node}: {distance}')

# Visualize the graph
pos = nx.spring_layout(G)  # Compute node positions
nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
