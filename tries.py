class Node:
    def __init__(self):
        self.key = None
        self.value = None
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word, value):
        currentWord = word
        currentNode = self.root
        while len(currentWord) > 0:
            if currentWord[0] in currentNode.children:
                currentNode = currentNode.children[currentWord[0]]
                currentWord = currentWord[1:]
            else:
                newNode = Node()
                newNode.key = currentWord[0]
                if len(currentWord) == 1:
                    newNode.value = value
                currentNode.children[currentWord[0]] = newNode
                currentNode = newNode
                currentWord = currentWord[1:]

    def lookup(self, word):
        currentWord = word
        currentNode = self.root
        while len(currentWord) > 0:
            if currentWord[0] in currentNode.children:
                currentNode = currentNode.children[currentWord[0]]
                currentWord = currentWord[1:]
            else:
                return "Not in trie"
        if currentNode.value == None:
            return "None"
        return currentNode.value

    def printAllNodes(self):
        nodes = [self.root]
        while len(nodes) > 0:
            for letter in nodes[0].children:
                nodes.append(nodes[0].children[letter])
            print nodes.pop(0).key

def makeTrie(words):
    trie = Trie()
    for word in words:
        trie.insert(word, words[word])
    return trie


trie = makeTrie({'hello': 5, 'hat': 7, 'her': 1})
print(trie.lookup('nope'))

print(trie.lookup('hello'))
print(trie.lookup('her'))

print(trie.printAllNodes())
