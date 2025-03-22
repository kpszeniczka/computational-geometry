from point import Point

class Element:
    def __init__(self, nodes):
        if len(nodes) < 2:
            raise ValueError("An element must have at least two points.")
        self.nodes = nodes
        
    def checkIfLine(self):
        if len(self.nodes) <= 2:
            return True
        point1, point2 = self.nodes[:2]
        A = point1.y - point2.y
        B = point2.x - point1.x
        C = point1.x * point2.y - point2.x * point1.y
        for node in self.nodes[2:]:
            if abs(A * node.x + B * node.y + C) > 1e-10:
                print("Points are not on the same line, this element is a polygon")
                return False
        return True

    def line(self):
        point1, point2 = self.nodes[:2]
        A = point1.y - point2.y
        B = point2.x - point1.x
        C = point1.x * point2.y - point2.x * point1.y
        return (A, B, C) if self.checkIfLine() else None
                
    def translate_segment(self, vector):
        new_nodes = [Point(node.x + vector[0], node.y + vector[1]) for node in self.nodes]
        return Element(new_nodes)