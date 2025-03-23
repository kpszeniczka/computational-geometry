import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import util, unittest
from visualization import Visualization
from point import Point
from element import Element


def main():
    filename = "test.txt"

    nodes, elements = util.load_file(filename)

    vis = Visualization(figsize = (12, 10),
                        node_color = 'blue',
                        text_offset=(0.2, 0.2),
                        linewidth=2)
    
    fig, ax = vis.plot(
        nodes = nodes,
        elements = elements,
        title = "Choroszcz is my lover",
        show = False
    )

    point_to_check = nodes[2]
    line_segment = elements[0]
    
    is_on_segment = point_to_check.checkIfOnSection(line_segment)
    is_on_line = point_to_check.checkIfOnLine(line_segment)
    
    print(f"Point 3 ({point_to_check.x}, {point_to_check.y}):")
    print(f"  Is on line: {is_on_line}")
    print(f"  Is on segment: {is_on_segment}")
    
    if is_on_segment:
        vis.highlight_nodes([2], color='green', size=150)
    else:
        vis.highlight_nodes([2], color='orange' if is_on_line else 'red', size=150)
    
    vis.highlight_elements([0], color='blue', linewidth=3)
    
    line_to_check = elements[1]
    point_position = nodes[5]
    
    position = point_position.point_position(line_to_check)
    
    print(f"Point 6 ({point_position.x}, {point_position.y}) is {position} of line 4-5")
    
    position_color = 'green' if position == "on line" else 'blue' if position == "left" else 'red'
    vis.highlight_nodes([5], color=position_color, size=150)
    vis.highlight_elements([1], color='purple', linewidth=3)
    
    section_to_translate = elements[2]
    translation_vector = (2, -1.5)
    
    translated_section = section_to_translate.translate_segment(translation_vector)
    translated_x = [node.x for node in translated_section.nodes]
    translated_y = [node.y for node in translated_section.nodes]
    
    ax.plot(translated_x, translated_y, 'r--', linewidth=2)
    print(f"Translated section 3 by vector {translation_vector}")
    vis.highlight_elements([2], color='orange', linewidth=3)
    
    mirror_line = elements[3]
    point_to_mirror = nodes[9]
    
    mirrored_point = point_to_mirror.reflect_point(mirror_line)
    
    ax.scatter(mirrored_point.x, mirrored_point.y, color='magenta', s=150, zorder=3)
    ax.text(mirrored_point.x + 0.2, mirrored_point.y + 0.2, 'M', fontsize=12)
    print(f"Mirrored point 10: Original({point_to_mirror.x}, {point_to_mirror.y}) → Mirrored({mirrored_point.x:.2f}, {mirrored_point.y:.2f})")
    vis.highlight_nodes([9], color='cyan', size=150)
    vis.highlight_elements([3], color='green', linewidth=3)
    
    legend_elements = [
        plt.Line2D([0], [0], color='blue', marker='o', markersize=10, label='Nodes'),
        plt.Line2D([0], [0], color='green', marker='o', markersize=10, label='Point on segment'),
        plt.Line2D([0], [0], color='orange', marker='o', markersize=10, label='Point on line (not segment)'),
        plt.Line2D([0], [0], color='red', marker='o', markersize=10, label='Point not on line'),
        plt.Line2D([0], [0], color='blue', marker='o', markersize=10, label='Point left of line'),
        plt.Line2D([0], [0], color='red', marker='o', markersize=10, label='Point right of line'),
        plt.Line2D([0], [0], color='cyan', marker='o', markersize=10, label='Point to mirror'),
        plt.Line2D([0], [0], color='magenta', marker='o', markersize=10, label='Mirrored point'),
        plt.Line2D([0], [0], color='blue', linestyle='-', label='Line segment to check'),
        plt.Line2D([0], [0], color='purple', linestyle='-', label='Line for position check'),
        plt.Line2D([0], [0], color='orange', linestyle='-', label='Section to translate'),
        plt.Line2D([0], [0], color='red', linestyle='--', label='Translated section'),
        plt.Line2D([0], [0], color='green', linestyle='-', label='Mirror line')
    ]
    ax.legend(handles=legend_elements, loc='upper right')

    all_x = [node.x for node in nodes]
    all_y = [node.y for node in nodes]
    
    all_x.extend(translated_x)
    all_y.extend(translated_y)
    
    all_x.append(mirrored_point.x)
    all_y.append(mirrored_point.y)
    
    padding = 2
    x_min, x_max = min(all_x) - padding, max(all_x) + padding
    y_min, y_max = min(all_y) - padding, max(all_y) + padding
    
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

    ax.grid(True, linestyle=vis.gridstyle, alpha=vis.gridalpha)
    
    plt.tight_layout()
    vis.save("geometry_operations.png")
    plt.show()

if __name__ == "__main__":
    main()