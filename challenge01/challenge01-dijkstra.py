
# coding: utf-8

# Dundee University Computing Society 2016 - Created by Stuart Huddy, s.w.m.huddy@dundee.ac.uk
# Note: Some examples have been from Universität of Osnabrück

# ## Setup your environment
# 
# ### a) Install Python
# 
# To be able to run Jupyter Notebooks you will need Python. Follow this exercise to get everything up and running.
# 
# #### UNIX (e.g. Ubuntu)
# 
# The following commands will install Python and the components required to build some of the packages we will use.
# 
# ```sh
# sudo apt-get install build-essential python3-dev python3
# pip3 install --upgrade pip
# pip3 install jupyter numpy matplotlib
# ```
# 
# #### MacOS
# 
# We recommend using homebrew to install Python.
# 
# ```sh
# ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
# brew install python3
# pip3 install --upgrade pip
# pip3 install jupyter numpy matplotlib
# ```
# 
# #### Windows
# 
# Go to [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/) and download the _Latest Python 3 Release_. Install it and make sure that _Add to PATH_ is checked during the installation.
# 
# Open your command line (`START` → `cmd.exe`). Type the following commands:
# 
# ```sh
# pip install --upgrade pip
# pip install jupyter numpy matplotlib
# ```
# 
# If some of those installations fail, check if `pip` produces output. Otherwise `'pip' is not recognized as an internal or external command, operable program or batch file.`. If that is the case, rerun the installation and check "Add to PATH" or try restarting your computer. In the other cases it might be you have problems with compiling the packages. Try to find them on [http://www.lfd.uci.edu/~gohlke/pythonlibs/](http://www.lfd.uci.edu/~gohlke/pythonlibs/), download them and install them with: 
# 
# ```sh
# pip install *.whl
# ```
# 

# # Programming Challenge 01:Dijkstra's algorithm
# 
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm Find the shortest paths from a given source node to all other nodes by developing the paths in order of increasing paths lengths. By the kth stage of the agorithm, there is a known set M consisting of k nodes which are the k nodes closest to (i.e. least cost away from) the source node. The (k+1)st stage of the algorithm will add to M the node which was not previously in M, and has the shortest (least cost) path from the source node. It will also establish the path to that node from the source.

# Peusdo Code for Algorithm:
# 1. Initalise as follows:
# The set M contains only s, the source node. The path costs from s to neighbouring nodes are known. (In fact, the costs of all individual links within the network are known - this information is essential for the algorithm to function.)
#     
# 2. Find the neighbouring node w not in set M that has the least-cost path from the source node and add node w to set M.
# 
# 3. Update the known least-cost paths for all the nodes not in set M by comparing the current known cost of the path from the source node to a node n with (the cost of the path from the source to the node w (just added to set M) + The cost fo the path from node w to node n). Do this for all nodes n outside the set M.

# In[1]:

import math
#Dataset of lengths. If paths between points are 0, it either means
#it is itself or a node it does not have direct access to.
inf = math.inf

D=     ([0  ,2  ,5  ,1  ,inf,inf],#n0
        [3  ,0  ,3  ,2  ,inf,inf],#n1
        [8  ,6  ,0  ,3  ,1  ,5  ],#n2
        [7  ,2  ,3  ,0  ,1  ,inf],#n3
        [inf,inf,1  ,1  ,0  ,2  ],#n4
        [inf,inf,8  ,inf,4  ,0  ])#n5


#i is the node we wish to work out it's sink tree.
#Remember path to itself will always be zero.
#Return array of integers with least cost to get to that node from i
def dijkstra(D, i):
    n=[0,1,2,3,4,5] #nodes in network
    #algorithm goes here

    
    
    
#Below are asserts which tests if the outcome 
#of the dijkstra's algorithm works. DO NOT DELETE
assert dijkstra(D, 0) == [0, 2, 3, 1, 2, 4], "Node 0 sink tree not correct"
assert dijkstra(D, 1) == [3, 0, 3, 2, 3, 5], "Node 1 sink tree not correct"
assert dijkstra(D, 2) == [7, 4, 0, 2, 1, 3], "Node 2 sink tree not correct"
assert dijkstra(D, 3) == [5, 2, 2, 0, 1, 3], "Node 3 sink tree not correct"
assert dijkstra(D, 4) == [6, 3, 1, 1, 0, 2], "Node 4 sink tree not correct"
assert dijkstra(D, 5) == [10, 7, 5, 5, 4, 0], "Node 5 sink tree not correct"


# In[ ]:




# In[ ]:



