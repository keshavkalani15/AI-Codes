from collections import deque

def selectionSort():
    newArray = []
    n = int(input("Enter no. of elements in array: "))
    
    for i in range(n):
        num = int(input(f"Enter num {i+1}: "))
        newArray.append(num)
        
    print("\nYour given array is: ", newArray)
    print("\nSorting using selection sort algorithm!!")
    
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if newArray[min_index] > newArray[j]:
                min_index = j
        
        newArray[min_index], newArray[i] = newArray[i], newArray[min_index]
    
    print("\nSelection Sorting Process Completed!!")
    print("\nYour sorted array is: ", newArray)
    print("\nThankyou!!")


def dfsAlgo(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        
        for neighbor in graph[node]:
            dfsAlgo(graph, neighbor, visited)
            
def rundfs():
    graph = {}
    n = int(input("Enter No. of nodes: "))
    
    for i in range(n):
        node = input(f"Enter Vertex {i+1}: ")
        neighbor = input(f"Enter neighbor of Vertex {i+1} (space-seperated): ").split()
        print(neighbor)
        graph[node] = neighbor
        
    start = input("Enter start node: ")
    visited = set()
    
    dfsAlgo(graph, start, visited)
    print("\n")
    bfsAlgo(graph, start)
    
def bfsAlgo(graph, start):
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
    
rundfs()