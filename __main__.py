import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import point, element, util, visualization


def main():
    filename = "test.txt"

    nodes, elements = util.load_file(filename)

    print(elements[0].line())

    visualization.plotter(nodes, elements)
    

if __name__ == "__main__":
    main()