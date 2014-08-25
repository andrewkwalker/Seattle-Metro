import networkx as nx
import scipy as sp 
import numpy as np 
import matplotlib.pyplot as mpl 

s = ['10th Ave W & W Fulton St', 'Queen Anne Ave N & Mercer St', 
		'3rd Ave & Cedar St', '3rd Ave & Union St', '5th Ave S & S Jackson St']

x = set(s)
G = nx.MultiGraph()
for y in x:
	G.add_node(y)
G.add_edge(s[0],s[1])
G.add_edge(s[1],s[2])
G.add_edge(s[2],s[3])
G.add_edge(s[3],s[4])

nx.draw_spring(G)
mpl.show()