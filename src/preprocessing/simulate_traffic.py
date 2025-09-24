import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import random
import os

# Load speed-enhanced graph
graph_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data/osm/pune_graph_speed.graphml"))
G = ox.load_graphml(graph_path)

# Simulate traffic: randomly reduce speeds on some edges
for u, v, k, data in G.edges(keys=True, data=True):
    # Randomly choose edges to slow down
    if random.random() < 0.1:  # 10% of edges are congested
        slowdown_factor = random.uniform(0.3, 0.7)  # reduce speed by 30-70%
        data["speed_kph"] *= slowdown_factor
        data["travel_time"] = (data["length"] / 1000) / data["speed_kph"] * 3600

# Choose origin/destination
origin_point = (18.5204, 73.8567)
destination_point = (18.5360, 73.8750)
orig_node = ox.distance.nearest_nodes(G, X=origin_point[1], Y=origin_point[0])
dest_node = ox.distance.nearest_nodes(G, X=destination_point[1], Y=destination_point[0])

# Compute fastest route under simulated traffic
route = nx.shortest_path(G, orig_node, dest_node, weight="travel_time")

# Plot the route
fig, ax = ox.plot_graph_route(G, route, node_size=10, edge_color='gray', route_color='red', route_linewidth=3)
plt.show()

