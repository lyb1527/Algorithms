'''
A topological sort takes a directed acyclic graph and produces a linear ordering of all its vertices such that tif the graph G contains an edge(v,w) then the vertex v comes before the vertex w in the ordering. DAG are used in many applications to indicate the precedence of events.

The topological sort is a simple but useful adaption of a depth first search. The ALgo for the topological sort is as follows:

1. call dfs(g) for some graph g. The main reason we want to call depth first search is to compute the finish times for each of the vertices.
2. Store the vertices in a list in decreasing order of finish time
3. return the ordered list as the result of the topological sort

'''




# Definition for a Directed graph node
class DirectedGraphNode:#
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def dfs(self, i, countrd, ans):
        ans.append(i)
        countrd[i] -= 1
        for j in i.neighbors:
            countrd[j] = countrd[j] - 1
            if countrd[j] == 0:
                self.dfs(j, countrd, ans)
    """
    @param graph: A list of Directed graph node
    @return: A list of integer
    """
    def topSort(self, graph):
        countrd = {}
        for x in graph:
            countrd[x] = 0

        for i in graph:
            for j in i.neighbors:
                countrd[j] = countrd[j] + 1

        ans = []
        for i in graph:
            if countrd[i] == 0:
                self.dfs(i, countrd, ans)
        return ans

sol=Solution()
A=DirectedGraphNode('0')
B=DirectedGraphNode('1')
C=DirectedGraphNode('2')
D=DirectedGraphNode('3')
E=DirectedGraphNode('4')
F=DirectedGraphNode('5')

A.neighbors=[B,C,D]
B.neighbors=[E]
C.neighbors=[E,F]
D.neighbors=[E,F]
E.neighbors=[]
F.neighbors=[]
graph=[A,B,C,D,E,F]

for i in sol.topSort(graph):
    print i.label
