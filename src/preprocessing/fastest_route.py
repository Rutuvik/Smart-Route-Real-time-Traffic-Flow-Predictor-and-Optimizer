import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import os

# Load graph with speed
graph_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data/osm/pune_graph_speed.graphml"))
G = ox.load_graphml(graph_path)

# Example: set origin and destination by latitude/longitude
origin_point = (18.5204, 73.8567)       # Pune city center
destination_point = (18.5360, 73.8750)  # Some nearby point

# Find nearest nodes to these points
orig_node = ox.distance.nearest_nodes(G, X=origin_point[1], Y=origin_point[0])
dest_node = ox.distance.nearest_nodes(G, X=destination_point[1], Y=destination_point[0])

# Compute fastest path using travel_time as edge weight
route = nx.shortest_path(G, orig_node, dest_node, weight="travel_time")

# Plot the route
fig, ax = ox.plot_graph_route(G, route, node_size=10, edge_color='gray', route_color='red', route_linewidth=3)
plt.show()

