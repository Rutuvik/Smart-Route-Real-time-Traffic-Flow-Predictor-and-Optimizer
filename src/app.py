import streamlit as st
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import random
import os

# ---------------- Step 5: Cache the graph to speed up the app ----------------
@st.cache_data
def load_graph():
    graph_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/osm/pune_graph_speed.graphml"))
    return ox.load_graphml(graph_path)

# Load the graph (cached)
G = load_graph()

st.title("Smart Route - Real-time Traffic Optimizer")

# Load graph
graph_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/osm/pune_graph_speed.graphml"))
G = ox.load_graphml(graph_path)

# User inputs for origin/destination
# User inputs for origin/destination
origin_place = st.text_input("Origin Place", "Pune City Center")
destination_place = st.text_input("Destination Place", "Kalyani Nagar, Pune")
# Convert place names to coordinates
origin_point = ox.geocoder.geocode(origin_place)  # returns (lat, lon)
destination_point = ox.geocoder.geocode(destination_place)


if st.button("Compute Fastest Route"):
    # Simulate traffic
    for u, v, k, data in G.edges(keys=True, data=True):
        if random.random() < 0.1:
            slowdown_factor = random.uniform(0.3, 0.7)
            data["speed_kph"] *= slowdown_factor
            data["travel_time"] = (data["length"] / 1000) / data["speed_kph"] * 3600

    # Find nearest nodes
    orig_node = ox.distance.nearest_nodes(G, X=origin_point[1], Y=origin_point[0])
    dest_node = ox.distance.nearest_nodes(G, X=destination_point[1], Y=destination_point[0])


    # Compute fastest path
    route = nx.shortest_path(G, orig_node, dest_node, weight="travel_time")

    # Plot
    fig, ax = ox.plot_graph_route(G, route, node_size=10, edge_color='gray', route_color='red', route_linewidth=3, show=False)
    st.pyplot(fig)

