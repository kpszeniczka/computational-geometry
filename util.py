import point, element

def load_file(filename):
    nodes = []
    elements = []
    
    with open(filename, 'r') as file:
        node_section = False
        element_section = False
        for line in file:
            if line.startswith('*'):
                if line.strip() == '*NODES':
                    node_section = True
                    element_section = False
                    continue
                elif line.strip() == '*ELEMENTS':
                    node_section = False
                    element_section = True
            elif node_section:
                words = line.split()
                if len(words) == 3:
                    x = float(words[1].strip())
                    y = float(words[2].strip())
                    nodes.append(point.Point(x,y))
            elif element_section:
                words = line.split()
                node_ids = [int(word) for word in words[1:]]
                node_list = [nodes[i-1] for i in node_ids]
                elements.append(element.Element(node_list))
    return nodes, elements
