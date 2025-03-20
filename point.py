class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def checkIfOnLine(self, line):
        if line.checkIfLine():
            point1 = line.nodes[0]
            point2 = line.nodes[1]
            
            slope = (point2.y - point1.y) / (point2.x - point1.x)
            
            b = slope * point1.x - point1.y
            
            y = slope * self.x + b
            if y == self.y:
                return True
            return False
    
    def checkIfOnSection(self, line):
        if self.checkIfOnLine(line):
            point1 = line.nodes[0]
            point2 = line.nodes[1]
            return min(point1.x, point2.X) <= self.x <= max(point1.x, point2.x) and min(point1.y, point2.y) <= self.y <= max(point1.y, point2.y)
    
    def point_position(self, line):
        point1 = line.nodes[0]
        point2 = line.nodes[1]
        det = (point2.x - point1.x) * (self.y - point1.y) - (point2.y - point1.y) * (self.x - point1.x)
        if det > 0:
            return "left"
        elif det < 0:
            return "right"
        else:
            return "on line"
        
    def reflect_point(self, line):
        A, B, C = line.line()
        D = A * A + B * B
        x = (B * (B * self.x - A * self.y) - A * C) / D
        y = (A * (-B * self.x + A * self.y) - B * C) / D
        return (2 * x - self.x, 2 * y - self.y)
