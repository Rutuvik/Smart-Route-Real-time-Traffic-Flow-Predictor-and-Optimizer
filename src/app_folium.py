import streamlit as st
import osmnx as ox
import networkx as nx
import folium
from streamlit_folium import st_folium

# ------------------ Load Graph ------------------
@st.cache_data
def load_graph():
    graph_path = "../../data/osm/pune_graph_speed.graphml"
    return ox.load_graphml(graph_path)

G = load_graph()

st.title("Smart Route - Interactive Map with Folium")

# ------------------ User Inputs ------------------
origin_place = st.text_input("Origin Place", "Pune City Center")
destination_place = st.text_input("Destination Place", "Kalyani Nagar, Pune")

if origin_place.strip() and destination_place.strip() and st.button("Compute Fastest Route"):
    
    try:
        # Geocode place names
        origin_point = ox.geocoder.geocode(origin_place)
        destination_point = ox.geocoder.geocode(destination_place)
    except Exception as e:
        st.error(f"Could not geocode the place names. Please check your input.\n{e}")
    else:
        # Find nearest nodes
        orig_node = ox.distance.nearest_nodes(G, X=origin_point[1], Y=origin_point[0])
        dest_node = ox.distance.nearest_nodes(G, X=destination_point[1], Y=destination_point[0])

        # Compute fastest route
        route = nx.shortest_path(G, orig_node, dest_node, weight="travel_time")
        route_coords = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in route]

        # Create Folium map centered at origin
        m = folium.Map(location=origin_point, zoom_start=14)

        # Add route polyline
        folium.PolyLine(route_coords, color="red", weight=5, opacity=0.8).add_to(m)

        # Add markers
        folium.Marker(origin_point, tooltip="Origin", icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(destination_point, tooltip="Destination", icon=folium.Icon(color='blue')).add_to(m)

        # Show map in Streamlit
        st_data = st_folium(m, width=700, height=500)

