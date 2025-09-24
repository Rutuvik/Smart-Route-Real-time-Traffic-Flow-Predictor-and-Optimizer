import osmnx as ox
import matplotlib.pyplot as plt
import os

# Path to the saved graph
graph_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data/osm/pune_graph.graphml"))

# Load the graph
G = ox.load_graphml(graph_path)

# Plot the graph
fig, ax = ox.plot_graph(G, figsize=(10, 10), node_size=10, edge_color='blue', edge_linewidth=0.5)
plt.show()

