'''
Implement a graph using adjacency list using either a hashtable with an array as values or hashtable with linked lists as a valuesince
python combines the idea of arrays and linked lists we can easily implemtn
this representation using a dictionary with nodes as keys and alist as vlalues


'''

class Node(object):
    def __init__(self, value):
        self.value = value


class Graph(object):
    def __init__(self):
        # node to list of neighbors hashtable
        self.nodes = {}

    def nodes(self):
        # return all nodes of graph
        return self.nodes.keys()

    def edges(self):
        # return all the edges for a graph
        edges = []
        for node in self.nodes:
            for incident in self.nodes[node]:
                edge = (node, incident)
                if edge not in edges:
                    edges.append(edge)
        return edges

    def insert_node(self, value, x):
        # insert a node with value which is a neighbor of x
        node = Node(value)
        self.nodes[node] = [x]
        self.nodes[x].append(node)

    def remove_node(self, node):
        # remove a given node of the graph
        for node in self.nodes:
            if node in self.nodes[node]:
                self.nodes[node].remove(node)
        del self.nodes[node]


'''
Two classes, graph holding the master list of vertices, Vertex representing
each vertex in the graph

Each vertex uses a dictionary to keep track of the vertices to  which it is connected and the weight of each edge.
dictionary is called connectedTo.


'''
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + 'connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return connectedTo.keys()

    def getID(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]



class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
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

    def addEdge(self, f, t, cost):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.key()

    def __iter__(self):
        return iter(self.vertList.values())

g = Graph()
for i in range(6):
    g.addVertex(i)
print(g.vertList)
