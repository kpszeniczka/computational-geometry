class Element:
    def __init__(self, nodes):
        self.nodes = nodes
        
    def checkIfLine(self, A, B, C):
        nodes = self.nodes
        for i in range(len(nodes) - 1):
            if abs(A * nodes[i].x + B * nodes[i].y + C) > 1e-10:
                print("Points are not on the same line, this element is polygon")
                return "Line doesn't exist"
        return True

    def line(self):
        nodes = self.nodes
        point1 = nodes[0]
        point2 = nodes[1]
        A = point1.y - point2.y
        B = point2.x - point1.x
        C = point1.x * point2.y - point2.x * point1.y
        if self.checkIfLine(A, B, C):
            return A, B, C
            
    def translate_segment(segment, vector):
        point1 = segment.nodes[0]
        point2 = segment.nodes[1]
        return (point1.x + vector[0], point1.y + vector[1]), (point2.x + vector[0], point2.y + vector[1])   
            