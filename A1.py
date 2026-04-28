#  Implement depth first search algorithm and Breadth First Search algorithm, Use an undirected 
#  graph and develop a recursive algorithm for searching all the vertices of a graph or tree data 
#  structure.

from collections import deque

# DFS (Recursive)
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


# BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# -------- USER INPUT --------

graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    node = input(f"Enter vertex {i+1}: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start = input("Enter starting vertex: ")

# -------- OUTPUT --------

print("\nDFS Traversal:")
visited = set()
dfs(graph, start, visited)

print("\nBFS Traversal:")
bfs(graph, start)



# Example

"""
Enter number of vertices: 6

Enter vertex 1: A
Enter neighbors of A: B C

Enter vertex 2: B
Enter neighbors of B: A D E

Enter vertex 3: C
Enter neighbors of C: A F

Enter vertex 4: D
Enter neighbors of D: B

Enter vertex 5: E
Enter neighbors of E: B F

Enter vertex 6: F
Enter neighbors of F: C E

Enter starting vertex: A
"""
