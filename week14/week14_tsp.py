
# coding: utf-8

# In[206]:


import math
from itertools import combinations
import numpy as np
import time

start = time.time()

with open("tsp.txt") as f:
    data = f.read().splitlines()
    cities = []
    for line in data:
        cities.append([float(x) for x in line.split(" ")])


# In[223]:


def distances(cities):
    
    d = {}
    
    for x in range(len(cities)):
        for y in range(len(cities)):
            d[(x+1,y+1)] = get_distance(cities[x],cities[y])
    
    return d
  
def get_distance(c1,c2):
    
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)


# In[307]:


def tour(cities,dist):
    
    # Node number for use in creating combinations below
    indexes = list(range(1,len(cities)))

    # Create hash table A - set with "1" is set to zero and everything else is "+infinity"
    A = {}

    for x in indexes:
        A[(x,)] = {1: math.inf} 
    
    A[(1,)] = {1: 0} 

    for m in range(2,len(cities)):  

        prev = A
        A = {}
        
        # Create all possible sets
        for S in combinations(indexes,m):
            # If set contains 1 (starting vertex) then continue
            if 1 in S:
                A[S] = {1: math.inf}
                for j in S[1:]:
                    A[S][j] = min([prev[tuple(i for i in S if i != j)][k] + dist[(k,j)] for k in S if k != j])

    return min(A[i][2] + dist[2,1] for i in A.keys())


# In[314]:


# Split up the dataset into two smaller tours
left_cities = [13] + cities[1:14]
right_cities = [13] + cities[12:]
left_dist = distances(cities[1:14])
right_dist = distances(cities[12:])

left_tour = tour(left_cities,left_dist)
right_tour = tour(right_cities,right_dist)


# In[315]:


# Add the min result from the two tour and subtract the common edge length
common_edge = get_distance(cities[12],cities[13])

min_dist = left_tour + right_tour - 2*(common_edge)
print(min_dist)

end = time.time()
print(end-start)

