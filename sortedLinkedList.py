from math import sqrt
class Node:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self._next = None
    def getDist(self):
        return sqrt(self.x*self.x + self.y*self.y)


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def add(self, name, x, y):
        pass

    def remove(self, post = -1):
        pass

    def length(self):
        return self.size
    
    def printAll(self):
        currNode = self.head
        while currNode is not None:
            print(currNode.x, currNode.y, currNode.name)
            currNode = currNode._next
        print("-"*40)
