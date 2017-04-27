import networkx as nx
import pandas as pd
from matplotlib import pyplot as plt

# Specify file location
file_name = "Email-Enron.txt"

# Read an edge list into a networkx graph
g = nx.read_edgelist(file_name, # file location
                     comments="#", # the character used to indicate the start of a comment
                     delimiter="\t", # the character that separates values in a line
                     create_using=nx.Graph() # create as undirected graph
                    )

# Q1
# Your code to print # of nodes, edges, etc.
# Your code to print the density of network
print "# of nodes and edges:"
print nx.info(g)
print "Density:"
print nx.density(g)

#Q3
# Your code to draw degree histogram
degree = nx.degree(g)
df_degree = pd.DataFrame(degree.items(), columns=["node", "degree"])
df_degree.sort_values("degree", ascending=False)
plt.hist(degree.values(), bins=100);
plt.show() # here you will see a pop up diagram. Copy the diagram and close it.

#Q4
# Your code to get a list of components (please call this list components) and put them in a pandas dataframe called df_comp
components = list(nx.connected_component_subgraphs(g))
print len(components)
df_comp = pd.DataFrame()
df_comp["n_nodes"] = [c.number_of_nodes() for c in components]
df_comp.sort_values(by="n_nodes", inplace=True, ascending=False) # since you need to look at the largest component, you need to first sort the dataframe by "n_nodes"
print "q4"
print df_comp
# it turns out component 0 is the largest component
largest_component = components[0] # here I use "largest_component" to refers to component 0. largest_component is a graph
print largest_component
# Your code to get # of nodes and # of edges contained in the graph largest_component
print "number of nodes and edges (largest_component):"
print largest_component.number_of_nodes()
print largest_component.number_of_edges()

#Q5 When you print df_comp in Q4, you should see that component 243 has 16 nodes and component 155 has 14 nodes.
compA = components[243]
# Your code for visualising the graph compA
nx.draw(compA,with_labels=True)
plt.show()

compB= components[155]
# Your code for visualising the graph compB.
nx.draw(compB,with_labels=True)
plt.show()

# Your code here:  Now you have two diagrams compA and comB. In order to compare them, you can look at diagrams, but you also need to look at measures such as average degree and density.
# please write code to get these measures. You can try to get more measures by looking at the documentation of networkx
print "compA measures:"
print nx.info(compA)
print "density: " 
print nx.density(compA)
print "compB measures:"
print nx.info(compB)
print "density: " 
print nx.density(compB)

print ("Isomorphic?", nx.is_isomorphic(compA,compB))

#Q7 - Find cliques for Component A
# Your code to print the cliques
for cliq in nx.find_cliques(compA):
    print cliq

#Q9.
# Your code to print at least 3 centrality measures.
between = nx.betweenness_centrality(compA)
df_between = pd.DataFrame(between.items(), columns=["node", "betweenness"])
df_between.sort_values("betweenness", ascending=False)
print "Betweenness:"
print df_between

closeness = nx.closeness_centrality(compA)
df_closeness = pd.DataFrame(closeness.items(), columns=["node", "closeness"])
df_closeness.sort_values("closeness", ascending=False)
print "Closeness:"
print df_closeness

eigen = nx.eigenvector_centrality(compA)
df_eigen = pd.DataFrame(eigen.items(), columns=["node", "eigenvector centrality"])
df_eigen.sort_values("eigenvector centrality", ascending=False)
print "Eigenvector:"
print df_eigen