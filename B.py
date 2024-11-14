# Q.2 Write a Python program to implement the Heuristic Search algorithm.

# Heuristic Search Algorithm Implementation (Greedy Best-First Search)

# Define a Node class to represent each state in the search
class Node:
    def _init_(self, name, heuristic):
        self.name = name        # Name of the node
        self.heuristic = heuristic  # Heuristic value (estimated cost to goal)
        self.parent = None      # Parent node to trace the path
        self.children = []      # List of children nodes

# Function to add children nodes to a parent node
def add_child(node, child_node):
    node.children.append(child_node)
    child_node.parent = node

# Heuristic Search Function (Greedy Best-First Search)
def heuristic_search(start_node, goal_node):
    open_list = [start_node]  # List of nodes to be evaluated
    closed_list = []          # List of nodes that have already been evaluated
    
    while open_list:
        # Sort open list based on heuristic value (greedy approach)
        open_list.sort(key=lambda x: x.heuristic)
        current_node = open_list.pop(0)  # Select the node with the lowest heuristic value
        
        print(f"Visiting node: {current_node.name}, Heuristic: {current_node.heuristic}")
        
        # If we have reached the goal, trace back the path
        if current_node.name == goal_node.name:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            path.reverse()
            return path
        
        closed_list.append(current_node)  # Move the node to closed list
        
        # Add children of the current node to the open list
        for child in current_node.children:
            if child not in open_list and child not in closed_list:
                open_list.append(child)
    
    return None  # No path found

# Example problem: Search from 'A' to 'F'
start = Node('A', 6)
goal = Node('F', 0)

B = Node('B', 4)
C = Node('C', 3)
D = Node('D', 1)
E = Node('E', 2)

# Adding children to each node
add_child(start, B)
add_child(start, C)
add_child(B, D)
add_child(C, E)
add_child(D, goal)
add_child(E, goal)

# Perform Heuristic Search
path = heuristic_search(start, goal)

# Output the path if found
if path:
    print("Path to goal:", " -> ".join(path))
else:
    print("No path found")


Output:
Visiting node: A, Heuristic: 6
Visiting node: C, Heuristic: 3
Visiting node: E, Heuristic: 2
Visiting node: D, Heuristic: 1
Visiting node: F, Heuristic: 0
Path to goal: A -> C -> E -> F