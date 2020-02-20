import unittest

from sol.rotateMatrix_sol import rotateMatrix as fn
# from rotateMatrix import rotateMatrix as fn


class MyCase(unittest.TestCase):

    def test_1(self):
        inArr = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        outArr = [
            [7,4,1],
            [8,5,2],
            [9,6,3]
        ]
        self.assertEqual(fn(inArr), outArr)
    def test_2(self):
        inArr = [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]
        ]
        outArr = [
            [13,9,5,1],
            [14,10,6,2],
            [15,11,7,3],
            [16,12,8,4]
        ]
        self.assertEqual(fn(inArr), outArr)
    
    def test_3(self):
        inArr = [
            [1,0],
            [0,1]
        ]
        outArr = [
            [0,1],
            [1,0]
        ]
        self.assertEqual(fn(inArr), outArr)
    def test_4(self):
        inArr = [
            [0,1,1,1,1,1,1,1,1,0],
            [2,0,0,0,0,0,0,0,0,3],
            [2,0,0,0,0,0,0,0,0,3],
            [2,0,0,0,0,0,0,0,0,3],
            [2,0,0,0,0,0,0,0,0,3],
            [2,0,0,0,0,0,0,0,0,3],
            [2,0,0,0,0,0,0,0,0,3],
            [2,0,0,0,0,0,0,0,0,3],
            [2,0,0,0,0,0,0,0,0,3],
            [0,4,4,4,4,4,4,4,4,0]
        ]
        outArr = [
            [0,2,2,2,2,2,2,2,2,0],
            [4,0,0,0,0,0,0,0,0,1],
            [4,0,0,0,0,0,0,0,0,1],
            [4,0,0,0,0,0,0,0,0,1],
            [4,0,0,0,0,0,0,0,0,1],
            [4,0,0,0,0,0,0,0,0,1],
            [4,0,0,0,0,0,0,0,0,1],
            [4,0,0,0,0,0,0,0,0,1],
            [4,0,0,0,0,0,0,0,0,1],
            [0,3,3,3,3,3,3,3,3,0]

        ]
        self.assertEqual(fn(inArr), outArr)


if __name__ == '__main__':
    unittest.main()