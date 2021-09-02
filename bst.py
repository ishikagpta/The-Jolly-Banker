from node import Node

# This class represents a Binary Search Tree and its functions.
class BinarySearchTree:

    # Constructor initializes the size of the binary search tree and its root
    def __init__(self):
        self.__size = 0
        self.__root = None

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0

    # A function that takes in a key and returns the node value from the BinarySearchTree.
    def get(self, key):
        if self.__root == None:
            return None
        if self.__root.getKey() == key:
            return self.__root.getValue()
        currentNode = Node(8)
        currentNode = self.__root
        # traversing the tree to get the node based on the key
        while currentNode != None and currentNode.getKey() != key:
            if currentNode.getKey() > key:
                currentNode = currentNode.getLeftChild()
            else:
                currentNode = currentNode.getRightChild()
        if currentNode == None:
            return None
        else:
            return currentNode.getValue()

    def __getitem__(self, key):
        return self.get(key)

    # A function that takes in a key and a value and inserts it as a node into the BinarySearchTree.
    def insert(self, key, value):
        if self.__root == None:
            self.__root = Node(key, value)
            self.__size = 1
            return
        currentNode = self.__root

        # Traversing the tree and putting the node where it should be.
        # If it's already there it changes the value to be the new one.
        # Otherwise it would compare it to the keys and put it in the right place.
        while currentNode != None:
            if currentNode.getKey() == key:
                currentNode.setValue(value)
                return
            elif currentNode.getKey() > key:
                if currentNode.getLeftChild() == None:
                    newNode = Node(key, value)
                    currentNode.setLeftChild(newNode)
                    self.__size += 1
                    return
                else:
                    currentNode = currentNode.getLeftChild()
            else:
                if currentNode.getRightChild() == None:
                    newNode = Node(key, value)
                    currentNode.setRightChild(newNode)
                    self.__size += 1
                    return
                else:
                    currentNode = currentNode.getRightChild()

    def __setitem__(self, key, value):
        self.insert(key, value)

    def inOrderTraversal(self, func):
        theNode = self.__root
        self.inOrderTraversalRec(self.__root, func)

    def inOrderTraversalRec(self, theNode, func):
        if theNode != None:
            self.inOrderTraversalRec(theNode.getLeftChild(), func)
            func(theNode.getKey(), theNode.getValue())
            self.inOrderTraversalRec(theNode.getRightChild(), func)

    # A function that takes in a key and removes the node associated with that key from the BinarySearchTree.
    def remove(self, key):
        self.__root = self.__remove(self.__root, key)

    # This helper function takes in a node and key. It searchs for the key in the BST and removes it if available.
    def __remove(self, node, key):
        if node is not None:
            # Traversing the tree to get the appropriate node.
            if key < node.getKey():
                node.setLeftChild(self.__remove(node.getLeftChild(), key))
            elif key > node.getKey():
                node.setRightChild(self.__remove(node.getRightChild(), key))
            else:
                # Replacing the deleted node with the appropriate node.
                if node.getLeftChild() is None:
                    return node.getRightChild()
                if node.getRightChild() is None:
                    return node.getLeftChild()
                # node to be deleted and replaced
                delete_node = node
                node = self.__min(node.getRightChild())
                node.setRightChild(self.__helper_delete_min(delete_node.getRightChild()))
                node.setLeftChild(delete_node.getLeftChild())
            return node

    # Gets the min for the current node - meaning the left child
    def __min(self, node):
        if node.getLeftChild() is None:
            return node
        return self.__min(node.getLeftChild())

    # Delete the minimum value node
    def __delete_min(self):
        self.__root = self.__helper_delete_min(self.__root)

    # Helper function to delete the minimum value node
    def __helper_delete_min(self, node):
        # get the right child of the lowest left child
        if node.getLeftChild() is None:
            return node.getRightChild()
        # setting the left child to be the returned right child
        node.setLeftChild(self.__helper_delete_min(node.getLeftChild()))
        return node

    # A function that takes in a key and checks if it is stored in the BinarySearchTree as a Node. It returns a
    # boolean value if it exists or not.
    def contains(self, key):
        if self.__root == None:
            return False
        elif self.__root.getKey() == key:
            return True
        currentNode = self.__root
        # Traversing the BST to reach the wanted node
        while currentNode != None and currentNode.getKey() != key:
            if currentNode.getKey() > key:
                currentNode = currentNode.getLeftChild()
            else:
                currentNode = currentNode.getRightChild()
        return currentNode != None

    # A function that searches if a node is in the BinarySearchTree.
    def searchTree(self, key):
        return self.contains(self.__root, key)
