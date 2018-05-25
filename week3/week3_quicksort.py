import math
import time
from random import shuffle

with open("quicksort.txt") as f:
    data = f.read().splitlines()

def quick_sort_first(array,start,end):
    global calcs

    if end <= start:
        return

    p = array[start]
    j = start

    for i in range(start+1, end):
        calcs += 1
        current = array[i]
        if current < p:
            j += 1
            array[i] = array[j]
            array[j] = current

    array[start] = array[j]
    array[j] = p

    quick_sort_first(array,start,j)
    quick_sort_first(array,j+1,end)

nums = [int(x) for x in data]

calcs = 0
quick_sort_first(nums,0,len(nums))
calcs


# In[5]:


# def quick_sort_last(array,start,end):
#     global calcs

#     if end <= start:
#         return

#     p = array[end]
#     j = start

#     for i in range(start, end):
#         calcs += 1
#         current = array[i]
#         if current < p:
#             array[i] = array[j]
#             array[j] = current
#             j += 1


#     array[end] = array[j]
#     array[j] = p

#     quick_sort_last(array,start,j-1)
#     quick_sort_last(array,j+1,end)


# In[6]:


def quick_sort_last(array,start,end):
    global calcs

    if end <= start:
        return

    p = array[end]
    array[end] = array[start]
    array[start] = p
    j = start

    for i in range(start+1, end+1):
        calcs += 1
        current = array[i]
        if current < p:
            j += 1
            array[i] = array[j]
            array[j] = current

    array[start] = array[j]
    array[j] = p

    quick_sort_last(array,start,j-1)
    quick_sort_last(array,j+1,end)


# In[7]:


nums = [int(x) for x in data]

calcs = 0
quick_sort_last(nums,0,len(nums)-1)
calcs


# In[24]:


def quick_sort_med(array,start,end):
    global calcs

    if end <= start:
        return

    options = [array[start],array[end],array[end // 2]]

    options.sort()
    p = options[1]
    array[array.index(p)] = array[start]
    array[start] = p
    j = start

    for i in range(start+1, end+1):
        calcs += 1
        current = array[i]
        if current < p:
            j += 1
            array[i] = array[j]
            array[j] = current

    array[start] = array[j]
    array[j] = p


    quick_sort_med(array,start,j-1)
    quick_sort_med(array,j+1,end)


nums = [int(x) for x in data]

calcs = 0
quick_sort_med(nums,0,len(nums)-1)
calcs


# In[ ]:


# def brute_force(array):
#     new = []
#     lowest = array[0]
#     i = 0

#     while len(array) > 0:
#         lowest = array[0]
#         for j in range(len(array)):
#             if array[j] < lowest:
#                 lowest = array[j]
#         new.append(lowest)
#         array.pop(array.index(lowest))
#     return new


# shuffle(test)

# start = time.time()
# test = brute_force(test)
# end = time.time()

# print(end - start)
