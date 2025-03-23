from point import Point
from element import Element
import numpy as np
import math

def generate_circle_polygon(center, radius, n):
    if n < 3:
        raise ValueError("Number of sides must be at least 3")
    
    points = []
    for i in range(n):
        angle = 2 * math.pi * i / n
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        points.append(Point(x, y))
    
    return Element(points)

def generate_split_polygons(center, radius, line_points, n_points = 12, offset_factor=0.5):
    x1, y1 = line_points[0]
    x2, y2 = line_points[1]
    
    A = y1 - y2
    B = x2 - x1
    C = x1 * y2 - x2 * y1
    
    norm = math.sqrt(A**2 + B**2)
    if norm == 0:
        raise ValueError("Line points must be distinct")
    
    A, B = A/norm, B/norm
    C = C/norm
    
    D = A * center[0] + B * center[1] + C
    if D < 0:
        A, B, C = -A, -B, -C
    circle_points = []
    
    for i in range(n_points):
        angle = 2 * math.pi * i / n_points
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        point = Point(x, y)
        position = A * x + B * y + C
        circle_points.append((point, position))
    
    polygon1_points = []
    polygon2_points = []
    
    for point, position in circle_points:
        if position >= 0:
            offset_x = point.x + offset_factor * radius * A
            offset_y = point.y + offset_factor * radius * B
            polygon1_points.append(Point(offset_x, offset_y))
        else:
            offset_x = point.x - offset_factor * radius * A
            offset_y = point.y - offset_factor * radius * B
            polygon2_points.append(Point(offset_x, offset_y))
    
    if not polygon1_points or not polygon2_points:
        raise ValueError("Line does not intersect with the circle properly")

    polygon1 = Element(polygon1_points)
    polygon2 = Element(polygon2_points)
    
    return polygon1, polygon2