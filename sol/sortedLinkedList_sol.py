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
        newNode = Node(name, x, y)

        if self.head is None or self.head.getDist() > newNode.getDist():
            newNode._next = self.head
            self.head = newNode
        else:
            currNode = self.head
            while currNode._next is not None and currNode._next.getDist() <= newNode.getDist():
                currNode = currNode._next

            newNode._next = currNode._next
            currNode._next = newNode
        self.size += 1
        pass

    def remove(self, post = -1):
        if post >= self.size:
            return

        if self.head is None:
            return
        
        currNode = self.head

        if post < 0 :
            post = self.size + post

        if post == 0:
            self.head = self.head._next
        else:
            i = 0
            while currNode._next is not None and i < post:
                prev = currNode
                currNode = currNode._next
                i +=1
            
            prev._next = currNode._next
        self.size -= 1

    def length(self):
        return self.size
    
    def printAll(self):
        currNode = self.head
        while currNode is not None:
            print(currNode.x, currNode.y, currNode.name)
            currNode = currNode._next
        print("-"*40)


ll = LinkedList()
ll.add("Central",0,0)
ll.printAll()
ll.add("Newtown",3,2)
ll.printAll()
ll.add("Redfren",1,1)
ll.printAll()
ll.add("Redfren",2,2)
ll.printAll()
ll.add("Bankstown",5,5)
ll.printAll()



