import matplotlib.pyplot as plt
import matplotlib.cm as cm

def setupAxis(x_vals, y_vals):
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(min(x_vals) - 1, max(x_vals) + 1)
    plt.ylim(min(y_vals) - 1, max(y_vals) + 1)
    plt.xticks(sorted(set(x_vals)))  
    plt.yticks(sorted(set(y_vals)))  
    plt.grid(True, linestyle='--', alpha=0.6)

def plotter(nodes, elements):
    plt.figure(figsize=(8, 6))

    node_positions = {i + 1: (node.x, node.y) for i, node in enumerate(nodes)}

    for node_id, (x, y) in node_positions.items():
        plt.scatter(x, y, color='blue', zorder=2)
        plt.text(x + 0.1, y + 0.1, str(node_id), fontsize=12, color='black')

    cmap = plt.get_cmap('tab10')

    for i, element in enumerate(elements):
        if len(element.nodes) > 1:
            x_vals = [node.x for node in element.nodes]
            y_vals = [node.y for node in element.nodes]
            
            x_vals += (x_vals[0],)
            y_vals += (y_vals[0],)

            plt.plot(x_vals, y_vals, color=cmap(i), linewidth=2, zorder=1)
            
    x_vals, y_vals = zip(*node_positions.values())
    
    setupAxis(x_vals, y_vals)
    
    plt.show()
