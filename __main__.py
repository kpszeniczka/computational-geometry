import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import util, visualization, unittest
from point import Point
from element import Element


def main():
    filename = "test.txt"

    nodes, elements = util.load_file(filename)

    visualization.plotter(nodes, elements)

if __name__ == "__main__":
    main()