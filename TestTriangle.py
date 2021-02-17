# Connor Smith
# Professor Saremi
# SSW 567
# HW 02a
# "I pledge my honor that I have abided by the Stevens Honor System"
import unittest

from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangles1(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangles2(self):
        self.assertEqual(classifyTriangle(6, 10, 8), 'Right', '6,10,8 is a Right triangle')

    def testEquilateralTriangles1(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testEquilateralTriangles2(self):
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral', '10,10,10 should be equilateral')

    def testIsoscelesTriangles1(self):
        self.assertEqual(classifyTriangle(8, 5, 8), 'Isosceles', '8,5,8 should be isosceles')

    def testIsoscelesTriangles2(self):
        self.assertEqual(classifyTriangle(13, 13, 8), 'Isosceles', '13,13,8 should be isosceles')

    def testScaleneTriangles1(self):
        self.assertEqual(classifyTriangle(8, 5, 6), 'Scalene', '8,5,6 should be scalene')

    def testScaleneTriangles2(self):
        self.assertEqual(classifyTriangle(14, 12, 8), 'Scalene', '14,12,8 should be scalene')

    def testNotTriangles(self):
        self.assertEqual(classifyTriangle(14, 2, 8), 'NotATriangle', '14,2,8 should not be a triangle')

    def testInvalidTriangles(self):
        self.assertEqual(classifyTriangle(250, 250, 150), 'Isosceles', '250,250,150 should be isosceles')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
