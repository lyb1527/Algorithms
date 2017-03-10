# implement a graph DS
'''
Using dictionaries, easy to implement the adjacency list in python.
Create two classes, Graph, which hold the master list of vertices, and
Vertex, which represents each vertex in the Graph
Each vertex uses a dictionary to keep track of the the vertices to which it is
connected to and the weight of each edge.
'''

class Vertex:
    def __init__(self, key):
        #initialized the id, will typically be a string and connected to dictionary
        self.id = key
        self.connectedTo = {}

    # used to add a connection from this vertex to another
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + 'connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getID(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

# Graph class contains a dict that maps vertex names to vertex objects
# Graph also provides methods for adding vertices to a Graph#
# and connect one vertex to another.

# __iter__ method to make it easy to iterate over all the vertex objects in ta particular graph.


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def geVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


# create an instance of graph to test
g = Graph()
for i in range(6):
    g.addVertex(i)
print(g.vertList)

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

for v in g:
    for w in v.getConnections():
        print("(%s, %s)" % (v.getID(), w.getID()))
