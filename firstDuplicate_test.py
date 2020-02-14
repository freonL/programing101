import unittest
# from sol.firstDuplicate_sol_ok import firstDuplicate as fn
# from sol.firstDuplicate_sol_better import firstDuplicate as fn
# from sol.firstDuplicate_sol_best import firstDuplicate as fn
from firstDuplicate import firstDuplicate as fn

class MyCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(fn([]), -1)

    def test_2(self):
        self.assertEqual(fn([1]), -1)
    
    def test_3(self):
        self.assertEqual(fn([2,3]), -1)
    
    def test_4(self):
        self.assertEqual(fn([1,2,3,4,5]), -1)
    
    def test_5(self):
        self.assertEqual(fn([1,2,2,4,5]), 2)

    def test_6(self):
        self.assertEqual(fn([1,3,2,3,5]), 3)
    
    def test_7(self):
        self.assertEqual(fn([1,3,2,3,2]), 3)

    def test_8(self):
        self.assertEqual(fn([1,3,3,2,2]), 3)
    
    def test_9(self):
        self.assertEqual(fn([1,3,2,2,3]), 2)

    def test_10(self):
        self.assertEqual(fn([1,2,6,4,5]), -1)
    

    def test_worst1(self):
        ls = list()
        ls.append(1)
        for i in range(3,1000):
            ls.append(i)
        ls.append(2)
        ls.append(2)

        self.assertEqual(fn(ls), 2)
    
    def test_worst2(self):
        ls = list()
        ls.append(1)
        for i in range(3,10000):
            ls.append(i)
        ls.append(2)
        ls.append(2)

        self.assertEqual(fn(ls), 2)


if __name__ == '__main__':
    unittest.main()