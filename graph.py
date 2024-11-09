import json
import networkx as nx
import matplotlib.pyplot as plt

def load_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def visualize_graph(data):
    G = nx.Graph()

    # Add edges to the graph from JSON data
    for node, neighbors in data.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Draw the graph
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_weight='bold', edge_color='gray')
    plt.show()

if __name__ == "__main__":
    filename = "graph.json"  # Replace with your JSON file name
    data = load_json(filename)
    visualize_graph(data)
