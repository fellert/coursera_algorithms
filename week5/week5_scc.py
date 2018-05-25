import collections
import sys
import threading

sys.setrecursionlimit(1000000)
threading.stack_size(67108864)

# data = test4.splitlines()
# data = [list(map(int, line.split())) for line in data if line != ""]

with open("scc.txt") as f:
    data = f.read().splitlines()
    data = [list(map(int, line.split())) for line in data]

# G = collections.defaultdict(list)
# GREV = collections.defaultdict(list)

largest = max([x[0] for x in data])

G = {}
GREV = {}

for i in range(1,largest+1):
    G[i] = []
    GREV[i] = []

for line in data:
    G[line[0]].append(line[1])
    GREV[line[1]].append(line[0])

def main():

    def dfs_loop(graph):

        global t, s, visited, leader

        i = max(graph.keys())

        t = 0
        s = 0
        visited = {}
        leader = {}

        while i > 0:
            if i not in visited:
                s = i
                dfs(graph,i)
            i -= 1

    def dfs(graph,i):

        global t, s

        visited[i] = 1
        leader[i] = s

        for j in graph[i]:
            if j not in visited:
                dfs(graph,j)
        t += 1
        f[i] = t

    f = {}
    dfs_loop(GREV)

    reassigned = {}
    for i in range(1,largest+1):
        reassigned[i] = []

    for x in G:
        reassigned[f[x]] = [f[i] for i in G[x]]

    dfs_loop(reassigned)

    print(sorted(list(collections.Counter(leader.values()).values()), reverse=True)[:5])


thread = threading.Thread(target=main)
thread.start()
