import unittest
from sortedLinkedList_sol import LinkedList

class MyCase(unittest.TestCase):

    def test_add1(self):
        ll = LinkedList()
        ll.add("A",0,0)
        currNode = ll.head
        
        self.assertEqual(currNode.x, 0)
        self.assertEqual(currNode.y, 0)
        self.assertEqual(currNode.name, "A")


    def test_add2(self):
        ll = LinkedList()
        ll.add("B",1,1)
        ll.add("A",0,0)
        
        ls = [
            (0,0,"A"),
            (1,1,"B"),
        ]
        currNode = ll.head
        i = 0 
        while currNode is not None:
            self.assertEqual(currNode.x, ls[i][0])
            self.assertEqual(currNode.y, ls[i][1])
            self.assertEqual(currNode.name, ls[i][2])
            i += 1
            currNode = currNode._next
    
    def test_add3(self):
        ll = LinkedList()
        ll.add("A",0,0)
        ll.add("B",3,3)
        ll.add("C",1,1)
        ll.add("D",2,2)
        ll.add("E",5,5)
        
        ls = [
            (0,0,"A"),
            (1,1,"C"),
            (2,2,"D"),
            (3,3,"B"),
            (5,5,"E"),
        ]
        currNode = ll.head
        i = 0 
        while currNode is not None:
            self.assertEqual(currNode.x, ls[i][0])
            self.assertEqual(currNode.y, ls[i][1])
            self.assertEqual(currNode.name, ls[i][2])
            i += 1
            currNode = currNode._next
    
    def test_remove1(self):
        ll = LinkedList()
        ll.add("A",0,0)
        ll.add("B",3,3)
        ll.add("C",1,1)
        ll.add("D",2,2)
        ll.add("E",5,5)
        ll.remove()
        
        ls = [
            (0,0,"A"),
            (1,1,"C"),
            (2,2,"D"),
            (3,3,"B"),
        ]
        currNode = ll.head
        i = 0 
        while currNode is not None:
            self.assertEqual(currNode.x, ls[i][0])
            self.assertEqual(currNode.y, ls[i][1])
            self.assertEqual(currNode.name, ls[i][2])
            i += 1
            currNode = currNode._next
    
    def test_remove2(self):
        ll = LinkedList()
        ll.add("A",0,0)
        ll.add("B",3,3)
        ll.add("C",1,1)
        ll.add("D",2,2)
        ll.add("E",5,5)
        ll.remove(0)
        
        ls = [
            (1,1,"C"),
            (2,2,"D"),
            (3,3,"B"),
            (5,5,"E"),
        ]
        currNode = ll.head
        i = 0 
        while currNode is not None:
            self.assertEqual(currNode.x, ls[i][0])
            self.assertEqual(currNode.y, ls[i][1])
            self.assertEqual(currNode.name, ls[i][2])
            i += 1
            currNode = currNode._next
    
    def test_remove3(self):
        ll = LinkedList()
        ll.add("A",0,0)
        ll.add("B",3,3)
        ll.add("C",1,1)
        ll.add("D",2,2)
        ll.add("E",5,5)
        ll.remove(2)
        
        ls = [
            (0,0,"A"),
            (1,1,"C"),
            (3,3,"B"),
            (5,5,"E"),
        ]
        currNode = ll.head
        i = 0 
        while currNode is not None:
            self.assertEqual(currNode.x, ls[i][0])
            self.assertEqual(currNode.y, ls[i][1])
            self.assertEqual(currNode.name, ls[i][2])
            i += 1
            currNode = currNode._next
    



if __name__ == '__main__':
    unittest.main()