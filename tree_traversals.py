### Depth First Solutions ###


# 1. pre-order traversal
'''
To move to the right subtree after processing the left subtree,
we must maintian the root information. The choice of ADT for such information
is a stack. Stack is LIFO, it is possible to get the infromation
about the right subtrees back in the reverse order
'''

def preorderRecursive(root, result):
    if not root:
        return
    result.append(root.data)
    preorderRecursive(root.left, result)
    preorderRecursive(root.right, result)

# Time complexity: O(n), Space complexity: O(n)

def preorderIterative(root, result):
    if not root:
        return
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
# Time Complexity: O(n). Space Complexity: O(n)



# 2. InOrder traversal

def inorderRecursive(root, result)
    if not root:
        return
    inorderRecursive(root.left, result)
    result.append(root.data)
    inorderRecursive(root.right, result)

# Time Complexity: O(n). Space Complexity: O(n)

def inorderIterative(root, result):
    if not root:
        return
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
    else:
        node = stack.pop()
        result.append(node.data)
        node = node.right

# Time Complexity: O(n). Space Complexity: O(n)



#3.  post-order Traversal

def postorderRecursive(root, result):
    if not root:
        return
    postorderRecursive(root.left, result)
    postorderRecursive(root.right, result)
    result.append(root.data)

def postorderIterative(root, result):
    if not root:
        return
    visited = set()
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node.node.left
        else:
            node = stack.pop()
            if (node.right and
                not node.right in visited):
                stack.append(node)
                node = node.right
            else:
                visited.add(node)
                result.append(node.data)
                node = None
# Time Complexity: O(n). Space Complexity: O(n)



### Level Order Traversal(inspired of BFS of graph algorithm) ###

"""
* visit the root
* While traversing level l, keep all the elements at level l + 1 in queue
* go the next level and visit all the nodes at that level
* repeat this until all levels are completed
"""

import Queue

def levelOrder(root, result):
    if root is None:
        return
    q = Queue.Queue()
    q.put(root)
    node = None

    while not q.empty():
        node = q.get()   # dequeue FIFO
        result.append(node.getData())
        if node.getLeft() is not None:
            q.put(node.getLeft())
        if node.getRight() is not None:
            q.put(node.getRight())


# Time Complexity: O(n). Space Complexity: O(n)
