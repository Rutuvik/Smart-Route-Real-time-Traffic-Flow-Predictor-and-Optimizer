# Smart Route – Real-time Traffic Flow Predictor and Optimizer

## Description
Smart Route is an interactive Python app built with Streamlit and OSMnx that predicts and visualizes the fastest driving route between two locations in a city. Users input origin and destination, and the app computes the shortest path based on travel time.

It demonstrates real-world applications of graph analysis, routing algorithms, and geographic data processing.

## Features
- Build city road network graphs using OpenStreetMap.
- Compute fastest driving routes using travel time.
- Display routes with basic statistics (distance, nodes).
- Static route visualization using Matplotlib.

## Tech Stack
- Python, Streamlit
- OSMnx, NetworkX
- Matplotlib

## Future Enhancements
- Integrate real-time traffic for dynamic route optimization.
- Add step-by-step directions for better navigation.
- Interactive maps with Folium or Google Maps API.
- Speed simulation to predict traffic flow and delays.
- Optimize graph processing for larger cities.

## Getting Started
1. Clone the repo.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the app: `streamlit run src/app.py`.
