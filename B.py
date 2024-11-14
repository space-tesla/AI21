# Q.2 Write a Python program to implement the Heuristic Search algorithm.

def heuristic_search(graph, heuristic, start, goal):
    open_list = [(start, heuristic[start])] 
    parents = {start: None}  
    while open_list:
        open_list.sort(key=lambda x: x[1])
        current, _ = open_list.pop(0)  

        print(f"Visiting node: {current}, Heuristic: {heuristic[current]}")

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]  

        for neighbor in graph.get(current, []):
            if neighbor not in parents:  
                parents[neighbor] = current
                open_list.append((neighbor, heuristic[neighbor]))

    return None  
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F']
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 1,
    'E': 2,
    'F': 0
}

path = heuristic_search(graph, heuristic, 'A', 'F')

if path:
    print("Path to goal:", " -> ".join(path))
else:
    print("No path found")



"""Output:
Visiting node: A, Heuristic: 6
Visiting node: C, Heuristic: 3
Visiting node: E, Heuristic: 2
Visiting node: D, Heuristic: 1
Visiting node: F, Heuristic: 0
Path to goal: A -> C -> E -> F"""