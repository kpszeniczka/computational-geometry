import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

class Visualization:
    def __init__(self, figsize=(8, 6), gridstyle='--', gridalpha=0.6, node_color='blue', 
                 text_color='black', text_offset=(0.1, 0.1), linewidth=2):
        
        self.figsize = figsize
        self.gridstyle = gridstyle
        self.gridalpha = gridalpha
        self.node_color = node_color
        self.text_color = text_color
        self.text_offset = text_offset
        self.linewidth = linewidth
        self.cmap = plt.get_cmap('tab10')
        self.fig = None
        self.ax = None
        self.nodes = None
        self.elements = None
        
    def _setup_axis(self, x_vals, y_vals, padding=1):
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        
        if len(set(x_vals)) == 1:
            x_min, x_max = x_vals[0] - padding, x_vals[0] + padding
        else:
            x_min, x_max = min(x_vals) - padding, max(x_vals) + padding
            
        if len(set(y_vals)) == 1:
            y_min, y_max = y_vals[0] - padding, y_vals[0] + padding
        else:
            y_min, y_max = min(y_vals) - padding, max(y_vals) + padding
        
        self.ax.set_xlim(x_min, x_max)
        self.ax.set_ylim(y_min, y_max)
        self.ax.set_xticks(sorted(set(x_vals)))
        self.ax.set_yticks(sorted(set(y_vals)))
        self.ax.grid(True, linestyle=self.gridstyle, alpha=self.gridalpha)
        
    def plot(self, nodes, elements, show=True, title=None):
        self.nodes = nodes
        self.elements = elements
        
        self.fig, self.ax = plt.subplots(figsize=self.figsize)
        
        if title:
            self.ax.set_title(title)
        
        node_positions = {i + 1: (node.x, node.y) for i, node in enumerate(nodes)}
        
        for node_id, (x, y) in node_positions.items():
            self.ax.scatter(x, y, color=self.node_color, zorder=2)
            self.ax.text(x + self.text_offset[0], y + self.text_offset[1], 
                        str(node_id), fontsize=12, color=self.text_color)
        
        for i, element in enumerate(elements):
            if len(element.nodes) > 1:
                x_vals = [node.x for node in element.nodes]
                y_vals = [node.y for node in element.nodes]
                
                if len(element.nodes) > 2:
                    x_vals.append(x_vals[0])
                    y_vals.append(y_vals[0])
                
                self.ax.plot(x_vals, y_vals, color=self.cmap(i % 10), 
                            linewidth=self.linewidth, zorder=1)
                
        x_vals, y_vals = zip(*node_positions.values())
        self._setup_axis(x_vals, y_vals)
        
        if show:
            plt.show()
            
        return self.fig, self.ax
    
    def save(self, filename, dpi=300):
        if self.fig is not None:
            self.fig.savefig("./pictures/" + filename, dpi=dpi, bbox_inches='tight')
            print(f"Figure saved to {filename}")
        else:
            print("No figure to save. Call plot() first.")
    
    def highlight_nodes(self, nodes_to_highlight, color='red', size=100):
        if self.ax is None:
            print("No plot available. Call plot() first.")
            return
            
        if self.nodes is None:
            print("No nodes available. Call plot() first.")
            return
            
        for idx in nodes_to_highlight:
            if idx < 0 or idx >= len(self.nodes):
                print(f"Warning: Node index {idx} out of range")
                continue
                
            node = self.nodes[idx]
            self.ax.scatter(node.x, node.y, color=color, s=size, zorder=3)
    
    def highlight_elements(self, elements_to_highlight, color='pink', linewidth=3):
        if self.ax is None:
            print("No plot available. Call plot() first.")
            return
            
        if self.elements is None:
            print("No elements available. Call plot() first.")
            return
            
        for idx in elements_to_highlight:
            if idx < 0 or idx >= len(self.elements):
                print(f"Warning: Element index {idx} out of range")
                continue
                
            element = self.elements[idx]
            if len(element.nodes) > 1:
                x_vals = [node.x for node in element.nodes]
                y_vals = [node.y for node in element.nodes]
                
                if len(element.nodes) > 2:
                    x_vals.append(x_vals[0])
                    y_vals.append(y_vals[0])
                
                self.ax.plot(x_vals, y_vals, color=color, 
                            linewidth=linewidth, zorder=3)
    def adjust_plot_for_points(self, extra_points=None, padding=1):
        if self.ax is None:
            print("No plot available. Call plot() first.")
            return
            
        x_vals = [node.x for node in self.nodes]
        y_vals = [node.y for node in self.nodes]
        
        if extra_points:
            for point in extra_points:
                if hasattr(point, 'x') and hasattr(point, 'y'):
                    x_vals.append(point.x)
                    y_vals.append(point.y)
                elif isinstance(point, (list, tuple)) and len(point) >= 2:
                    x_vals.append(point[0])
                    y_vals.append(point[1])
        
        x_min, x_max = min(x_vals) - padding, max(x_vals) + padding
        y_min, y_max = min(y_vals) - padding, max(y_vals) + padding
        
        self.ax.set_xlim(x_min, x_max)
        self.ax.set_ylim(y_min, y_max)

        self.ax.grid(True, linestyle=self.gridstyle, alpha=self.gridalpha)
        
        return self.ax