import unittest
from point import Point
from element import Element
import math

class TestPoint(unittest.TestCase):
    def test_point_creation(self):
        p = Point(3, 4)
        self.assertEqual(p.x, 3)
        self.assertEqual(p.y, 4)
    
    def test_checkIfOnLine_horizontal(self):
        e = Element([Point(0, 5), Point(10, 5)])
        
        p1 = Point(5, 5)
        self.assertTrue(p1.checkIfOnLine(e))
        
        p2 = Point(5, 6)
        self.assertFalse(p2.checkIfOnLine(e))
    
    def test_checkIfOnLine_vertical(self):
        e = Element([Point(5, 0), Point(5, 10)])
        
        p1 = Point(5, 5)
        self.assertTrue(p1.checkIfOnLine(e))
        
        p2 = Point(6, 5)
        self.assertFalse(p2.checkIfOnLine(e))
    
    def test_checkIfOnLine_diagonal(self):
        
        e = Element([Point(0, 0), Point(10, 10)])
        
        p1 = Point(5, 5)
        self.assertTrue(p1.checkIfOnLine(e))
        
        p2 = Point(5, 6)
        self.assertFalse(p2.checkIfOnLine(e))

        e2 = Element([Point(0, 10), Point(10, 0)])

        p3 = Point(5, 5)
        self.assertTrue(p3.checkIfOnLine(e2))

        p4 = Point(5, 6)
        self.assertFalse(p4.checkIfOnLine(e2))
    
    def test_checkIfOnSection_horizontal(self):
        e = Element([Point(0, 5), Point(10, 5)])
        
        p1 = Point(5, 5)
        self.assertTrue(p1.checkIfOnSection(e))
        
        p2 = Point(15, 5)
        self.assertFalse(p2.checkIfOnSection(e))
        
        p3 = Point(5, 6)
        self.assertFalse(p3.checkIfOnSection(e))
    
    def test_checkIfOnSection_vertical(self):
        e = Element([Point(5, 0), Point(5, 10)])
        
        p1 = Point(5, 5)
        self.assertTrue(p1.checkIfOnSection(e))
        
        p2 = Point(5, 15)
        self.assertFalse(p2.checkIfOnSection(e))
        
        p3 = Point(6, 5)
        self.assertFalse(p3.checkIfOnSection(e))
    
    def test_point_position(self):
        e = Element([Point(0, 0), Point(10, 10)])
        
        p1 = Point(5, 5)
        self.assertEqual(p1.point_position(e), "on line")
        
        p2 = Point(5, 6)
        self.assertEqual(p2.point_position(e), "left")
        
        p3 = Point(5, 4)
        self.assertEqual(p3.point_position(e), "right")
    
    def test_reflect_point(self):
        e1 = Element([Point(0, 5), Point(10, 5)])
        p1 = Point(3, 8)
        reflected1 = p1.reflect_point(e1)
        self.assertAlmostEqual(reflected1.x, 3)
        self.assertAlmostEqual(reflected1.y, 2)
        
        e2 = Element([Point(5, 0), Point(5, 10)])
        p2 = Point(8, 3)
        reflected2 = p2.reflect_point(e2)
        self.assertAlmostEqual(reflected2.x, 2)
        self.assertAlmostEqual(reflected2.y, 3)
        
        e3 = Element([Point(0, 0), Point(10, 10)])
        p3 = Point(3, 7)
        reflected3 = p3.reflect_point(e3)
        self.assertAlmostEqual(reflected3.x, 7)
        self.assertAlmostEqual(reflected3.y, 3)

if __name__ == '__main__':
    unittest.main()