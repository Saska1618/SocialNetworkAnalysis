import argparse
import logging
import numpy as np
import networkx as nx
import os
from scipy.io import mmread

def describe_network(G):
    '''
    Describe the network using the following metrics:
    - Min degree
    - Max degree
    - Avg degree
    - Diameter
    - Number of connected components
    - Size of largest connected component
    - Number of shortest paths
    - Average clustering coefficient
    
    Parameters:
    - G: networkx.Graph
    
    Returns:
    - None
    '''
    # Log nodes and links 
    num_nodes = G.number_of_nodes()
    num_links = G.number_of_edges()
    logging.info("Number of nodes: %d", num_nodes)
    logging.info("Number of links: %d", num_links)
    
    degrees = [d for _, d in G.degree()]
    min_degree = np.min(degrees)
    max_degree = np.max(degrees)
    avg_degree = np.mean(degrees)

    # Extract the largest connected component
    connected_components = sorted(nx.connected_components(G), key=len, reverse=True)
    num_components = len(connected_components)
    largest_cc_size = max(len(cc) for cc in connected_components)

    # Shortest paths 
    shortest_paths = [d for _, d in nx.shortest_path_length(G)]

    avg_clustering_coefficient = nx.average_clustering(G)

    logging.info("Min degree: %d", min_degree)
    logging.info("Max degree: %d", max_degree)
    logging.info("Avg degree: %f", avg_degree)

    try: 
        # Try to compute diameter of the network
        diameter = nx.diameter(G)
        logging.info("Diameter of the network: %d", diameter)
    except nx.NetworkXError:   
        logging.warning("AS THE NETWORK IS NOT CONNECTED, THE DIAMETER OF THE NETWORK IS INFINITE")

        for component in connected_components:
            diameter = nx.diameter(G.subgraph(component))
            logging.info("Size of component: %d", len(component))
            logging.info("Diameter of component: %d", diameter)
            logging.info("%s", 30 * "-")

    logging.info("Number of connected components: %d", num_components)
    logging.info("Size of largest connected component: %d", largest_cc_size)
    logging.info("Number of shortest paths: %d", len(shortest_paths))
    logging.info("Average clustering coefficient: %f", avg_clustering_coefficient)
  
if __name__ == "__main__":   
    parser = argparse.ArgumentParser(description="Describe a network from a matrix or GML file.")
    parser.add_argument("path", type=str, help="Path to the matrix or GML file")
    parser.add_argument("--log", type=str, help="Path to the log file", default='./out.log')
    args = parser.parse_args()

    log_file = args.log
 
    logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s",
                        handlers=[
                            logging.FileHandler(log_file, mode='w'),
                            logging.StreamHandler()
                        ])

    file_path = args.path
    file_ext = os.path.splitext(file_path)[-1].lower()

    if file_ext == ".gml":
        G = nx.read_gml(file_path)
    else:
        matrix = mmread(file_path)
        G = nx.Graph(matrix)
    
    describe_network(G)
