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


class TestElement(unittest.TestCase):
    def test_element_creation(self):
        nodes = [Point(0, 0), Point(1, 1), Point(2, 2)]
        e = Element(nodes)
        self.assertEqual(len(e.nodes), 3)
        self.assertEqual(e.nodes[0].x, 0)
        self.assertEqual(e.nodes[1].y, 1)
    
    def test_element_creation_error(self):
        with self.assertRaises(ValueError):
            Element([Point(0, 0)])
    
    def test_checkIfLine_two_points(self):
        e = Element([Point(0, 0), Point(1, 1)])
        self.assertTrue(e.checkIfLine())
    
    def test_checkIfLine_three_collinear_points(self):
        e = Element([Point(0, 0), Point(1, 1), Point(2, 2)])
        self.assertTrue(e.checkIfLine())
    
    def test_checkIfLine_three_non_collinear_points(self):
        e = Element([Point(0, 0), Point(1, 1), Point(2, 0)])
        self.assertFalse(e.checkIfLine())
    
    def test_line_horizontal(self):
        e = Element([Point(0, 5), Point(10, 5)])
        A, B, C = e.line()
        self.assertEqual(A, 0)
        self.assertEqual(B, 10)
        self.assertEqual(C, -50)
    
    def test_line_vertical(self):
        e = Element([Point(5, 0), Point(5, 10)])
        A, B, C = e.line()
        self.assertEqual(A, -10)
        self.assertEqual(B, 0)
        self.assertEqual(C, 50)
    
    def test_line_diagonal(self):
        e = Element([Point(0, 0), Point(10, 10)])
        A, B, C = e.line()
        self.assertEqual(A, -10)
        self.assertEqual(B, 10)
        self.assertEqual(C, 0)
    
    def test_line_non_collinear(self):
        e = Element([Point(0, 0), Point(1, 1), Point(2, 0)])
        self.assertIsNone(e.line())
    
    def test_translate_segment(self):
        e = Element([Point(1, 1), Point(3, 3)])

        translated = e.translate_segment((2, 3))

        self.assertEqual(translated.nodes[0].x, 3)
        self.assertEqual(translated.nodes[0].y, 4)
        self.assertEqual(translated.nodes[1].x, 5)
        self.assertEqual(translated.nodes[1].y, 6)

        e2 = Element([Point(0, 0), Point(1, 1), Point(2, 0)])
        translated2 = e2.translate_segment((-1, 5))
        
        self.assertEqual(translated2.nodes[0].x, -1)
        self.assertEqual(translated2.nodes[0].y, 5)
        self.assertEqual(translated2.nodes[1].x, 0)
        self.assertEqual(translated2.nodes[1].y, 6)
        self.assertEqual(translated2.nodes[2].x, 1)
        self.assertEqual(translated2.nodes[2].y, 5)
    
    def test_translate_segment_zero_vector(self):
        e = Element([Point(1, 1), Point(3, 3)])
        translated = e.translate_segment((0, 0))
        
        self.assertEqual(translated.nodes[0].x, 1)
        self.assertEqual(translated.nodes[0].y, 1)
        self.assertEqual(translated.nodes[1].x, 3)
        self.assertEqual(translated.nodes[1].y, 3)


if __name__ == '__main__':
    unittest.main()