class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def checkIfOnLine(self, line):
        if line.checkIfLine():
            point1, point2 = line.nodes[:2]
            if point2.x - point1.x == 0:
                return self.x == point1.x
            else:
                slope = (point2.y - point1.y) / (point2.x - point1.x)
                b = point1.y - slope * point1.x
                expected_y = slope * self.x + b
                return abs(expected_y - self.y) < 1e-10
        return False
    
    def checkIfOnSection(self, line):
        if self.checkIfOnLine(line):
            point1, point2 = line.nodes[:2]
            return (min(point1.x, point2.x) <= self.x <= max(point1.x, point2.x) and 
                    min(point1.y, point2.y) <= self.y <= max(point1.y, point2.y))
        return False
    
    def point_position(self, line):
        point1, point2 = line.nodes[:2]
        det = (point2.x - point1.x) * (self.y - point1.y) - (point2.y - point1.y) * (self.x - point1.x)
        return "left" if det > 0 else "right" if det < 0 else "on line"
        
    def reflect_point(self, line):
        A, B, C = line.line()
        D = A * A + B * B
        x = (B * (B * self.x - A * self.y) - A * C) / D
        y = (A * (-B * self.x + A * self.y) - B * C) / D
        return Point(2 * x - self.x, 2 * y - self.y)
