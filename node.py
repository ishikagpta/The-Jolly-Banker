# A class to represent a Node in the Binary Search Tree
class Node:

    def __init__(self, key, value=None):
        self.__key = key
        self.__value = value
        self.__leftChild = None
        self.__rightChild = None

    def getLeftChild(self):
        return self.__leftChild

    def getRightChild(self):
        return self.__rightChild

    def setLeftChild(self, theNode):
        self.__leftChild = theNode

    def setRightChild(self, theNode):
        self.__rightChild = theNode

    def getKey(self):
        return self.__key

    def getValue(self):
        return self.__value

    def setValue(self, value):
        self.__value = value

    def isLeaf(self):
        return self.getLeftChild() == None and self.getRightChild == None

    def __str__(self):
        return str(self.__key) + " " + str(self.__value)

    def __repr__(self):
        return str(self.__key) + " " + str(self.__value)
