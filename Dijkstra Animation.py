import pygame
import networkx as nx
import time

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dijkstra Visualization")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create an example graph
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'C', weight=1)
G.add_edge('B', 'D', weight=5)
G.add_edge('C', 'D', weight=8)
G.add_edge('C', 'E', weight=10)
G.add_edge('D', 'E', weight=2)

# Define node positions for visualization
node_positions = {'A': (100, 100), 'B': (300, 200), 'C': (300, 400), 'D': (500, 300), 'E': (700, 200)}

# Initialize animation variables
animation_delay = 1  # Delay between each step (in seconds)
visited_nodes = set()
distances = {node: float('inf') for node in G.nodes}
distances['A'] = 0
previous = {node: None for node in G.nodes}
path = []

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the edges
    for edge in G.edges:
        start_pos = node_positions[edge[0]]
        end_pos = node_positions[edge[1]]
        pygame.draw.line(screen, WHITE, start_pos, end_pos, 2)
        weight = G[edge[0]][edge[1]]['weight']
        text_pos = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
        font = pygame.font.Font(None, 20)
        text = font.render(f"{weight}", True, WHITE)
        screen.blit(text, (text_pos[0] - 10, text_pos[1] - 10))

    # Draw the nodes
    for node, position in node_positions.items():
        color = YELLOW if node in visited_nodes else BLUE
        pygame.draw.circle(screen, color, position, 20)
        font = pygame.font.Font(None, 20)
        text = font.render(f"{distances[node]}", True, WHITE)
        screen.blit(text, (position[0] - 10, position[1] - 30))

    # Highlight the shortest path
    for i in range(len(path) - 1):
        pygame.draw.line(screen, RED, node_positions[path[i]], node_positions[path[i + 1]], 2)

    # Update the screen
    pygame.display.flip()

    # Find the node with the minimum distance
    min_distance = float('inf')
    current_node = None
    for node in G.nodes:
        if node not in visited_nodes and distances[node] < min_distance:
            min_distance = distances[node]
            current_node = node

    if current_node is None:
        break

    visited_nodes.add(current_node)

    # Update distances and previous nodes
    for neighbor in G.neighbors(current_node):
        new_distance = distances[current_node] + G[current_node][neighbor]['weight']
        if new_distance < distances[neighbor]:
            distances[neighbor] = new_distance
            previous[neighbor] = current_node

    # Add the current node to the shortest path
    path.append(current_node)

    # Delay before next step
    time.sleep(animation_delay)

# Quit Pygame


time.sleep(5)
pygame.quit()
