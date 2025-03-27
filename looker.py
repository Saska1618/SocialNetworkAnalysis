import networkx as nx
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from pyvis.network import Network

# load original graph
mtx_file = "./socfb-Caltech36/socfb-Caltech36.mtx"

# read in the original matrix
matrix = scipy.io.mmread(mtx_file)  # Load matrix
G_original = nx.from_scipy_sparse_array(matrix)
# read in the erdos matrix
G_erdos = nx.read_gml('erdos_renyi_random.gml')
# read in the barabasi matrix
G_barabasi = nx.read_gml("barabasi_scale_free.gml")

# Create a Pyvis network
net = Network(notebook=True, height="750px", width="100%", bgcolor="#222222", font_color="white")

# Convert NetworkX graph to Pyvis
net.from_nx(G_original)

# Save and display the interactive graph
net.show("graph.html")