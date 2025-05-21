# SocialNetworkAnalysis

University project for social network analysis

TODO:

ATTILA

- create 2 networks - one random, one scale-free

FOR EACH GRAPH

    HUNOR
    - [x] provide a detailed description of the network: number of nodes, links, significance and meaning

    HUNOR
    - [x] compute network properties: min/max/average degree, dimaeter, connected componenets and the size of the largest one, shortest paths,average clustering coefficient

    ATTILA
    - provide a visualization for the network

    MOZES
    - compute and plot: degree distribution, clustering coefficient distribution, betweenness centrality distribution, connected components size distribution

    MOZES
    - identify most important nodes according to different measures

HUNOR, MOZES, ATTILA

- what type of network is the selected real network

## Facebook Social Network Dataset

### Overview

This dataset represents a social friendship network extracted from Facebook. It consists of people (nodes) and their friendship ties (edges). The network is undirected and unweighted, meaning that friendships are mutual and there is no numerical weight assigned to the relationships.

### Network Characteristics

- **Number of Nodes (People):** 769
- **Number of Links (Friendship Ties):** 16,656
- **Vertex Type:** Person
- **Edge Type:** Friendship, social relationship
- **Graph Format:** Undirected
- **Edge Weights:** Unweighted

### Significance

This dataset can be used to study social network structures, community detection, and information spread within a social environment. By analyzing the network, researchers can:

- Identify influential individuals within the network.
- Detect community structures and clusters of closely connected users.
- Analyze the small-world properties and connectivity of social graphs.
- Investigate the degree distribution and centrality measures to understand user influence.

### We decided that our graph seems to be a scale-free network

## RoyalRoad Book Networks

### Overview

These networks have as nodes books from the RoyalRoad website and links are created between similar books. Similarity is defined based on one or more of the following: a number of similar tags, similar overall rating, follower count and number of pages.

### Networks Generated

The following networks were generated based on the following criteria:

- **t3_r007p_p007p_f007p**: To have a connection, two books have to share at least 3 tags and the number of pages, rating and follower count has to be within 7% of each other.
- **t3_r007p_p007p**: To have a connection, two books have to share at least 3 tags and the number of pages and rating has to be within 7% of each other.
- **t3_r007_f007p**: To have a connection, two books have to share at least 3 tags and rating and follower count has to be within 7% of each other.
- **t3_p007p_f007p**: To have a connection, two books have to share at least 3 tags and the number of pages and follower count has to be within 7% of each other.
