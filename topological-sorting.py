# Definition of a directed graph node
# class DirectedGraphNode:
#    def __init__(self, x):
#        self.label = x
#        self.neighbors = []

class Solution:
    def dfs(self, i, countrd, ans):
        ans.append(i)
        countrd -= 1
        for j in i.neighbors:
            countrd[j] = countrd[j] - 1
            if countrd[j] == 0:
                self.dfs(j, countrd, ans)

    '''
    @param graph: a list of directed graph node
    @return: a list of integers
    '''
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
