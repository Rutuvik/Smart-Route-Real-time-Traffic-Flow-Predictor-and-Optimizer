import osmnx as ox
import os

def build_and_save_graph(place_name: str, save_path: str):
    """
    Download road network for a given place from OpenStreetMap
    and save it as GraphML.
    """
    print(f"Downloading road network for: {place_name}")
    G = ox.graph_from_place(place_name, network_type="drive")

    print(f"Saving graph to {save_path}")
    ox.save_graphml(G, filepath=save_path)
    print("Done!")

if __name__ == "__main__":
    place = "Pune, India"

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data/osm"))
    os.makedirs(base_dir, exist_ok=True)
    save_file = os.path.join(base_dir, "pune_graph.graphml")

    build_and_save_graph(place, save_file)
