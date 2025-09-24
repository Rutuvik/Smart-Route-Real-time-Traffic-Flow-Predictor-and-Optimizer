import osmnx as ox
import os

# Load graph
graph_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data/osm/pune_graph.graphml"))
G = ox.load_graphml(graph_path)

# Define default speeds by road type (in km/h)
speed_map = {
    "motorway": 80,
    "trunk": 70,
    "primary": 60,
    "secondary": 50,
    "tertiary": 40,
    "residential": 30,
    "unclassified": 30,
    "service": 20,
}

# Add speed attribute to edges
for u, v, k, data in G.edges(keys=True, data=True):
    highway_type = data.get("highway")
    if isinstance(highway_type, list):
        highway_type = highway_type[0]  # pick first if multiple types
    speed = speed_map.get(highway_type, 30)
    data["speed_kph"] = speed
    # calculate travel time in seconds
    data["travel_time"] = (data["length"] / 1000) / speed * 3600

# Save updated graph
save_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data/osm/pune_graph_speed.graphml"))
ox.save_graphml(G, save_path)
print(f"Graph with speed attributes saved to: {save_path}")

