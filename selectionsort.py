def selectionSort():
    newArray = []
    num = int(input("Enter no. of elements: "))
    for i in range(num):
        data = int(input(f"Enter Element {i+1}: "))
        newArray.append(data)
    
    for i in range(num):
        min_index = i
        for j in range(i+1, num):
            if newArray[i] > newArray[j]:
                min_index = j
        
        newArray[i], newArray[min_index] = newArray[min_index], newArray[i]
    print("Sorted Array: ", newArray)
    
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
            
def bfs(graph, start):
    visited = set()

            
def Main():
    graph = {}
    visited = set()
    
    num = int(input("Enter no. of nodes: "))
    for i in range(num):
        data = input(f"Enter Node {i+1}: ")
        neighbors = input(f"Enter neighbor of {i+1} space seperated: ").split()
        graph[data] = neighbors

    start = input("Enter Start node: ")
    
    dfs(graph, start, visited)
    
