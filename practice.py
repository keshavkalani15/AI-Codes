from collections import deque

def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
            
def bfs(graph, node):
    visited = set()
    queue = deque([node])
    visited.add(node)
    
    while queue:
        data = queue.popleft()
        print(data, end=" ")
        
        for neighbor in graph[data]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
            
def dfsMain():
    graph = {}
    visited = set()
    n = int(input("enter total no. of nodes: "))
    for i in range(n):
        node = input(f"Enter Node {i+1}: ")
        neighbor = input("Enter neighbors (space seperated): ").split()
        graph[node] = neighbor
        
    print("\n\n",graph)
    
    start = input("\n\nEnter start node: ")
    print("DFS: ")
    dfs(graph, start, visited)
    print("BFS: ")
    bfs(graph, start)
            
def selectionSort():
    n = int(input("Enter total no of elements: "))
    newArray = []
    for i in range(n):
        num = int(input(f"Enter Num {i+1}: "))
        newArray.append(num)
        
    print("Final Array is: ", newArray)
    print()
    
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if(newArray[min_index] > newArray[j]):
                min_index = j
        newArray[min_index], newArray[i] = newArray[i], newArray[min_index]
        
    print("\nSorted Array: ", newArray)
    
def prims():
    n = int(input("Enter no. of Nodes: "))
    graph = []
    print("Enter Adjacency Matrix: ")
    for i in range(n):
        row = [int(x) for x in input().split()]
        graph.append(row)
        
    selected = [False]*n
    selected[0] = True
    total_cost = 0
     
    for _ in range(n-1):
        min_edge = 999
        x = 0
        y = 0
        
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j] != 0:
                        if graph[i][j] < min_edge:
                            min_edge = graph[i][j]
                            x = i
                            y = j
                            
        print(x, " - ", y, " = ", graph[x][y])
        total_cost += graph[x][y]
        selected[y] = True
    print("Total cost = ", total_cost)
    
def solve(board, row, n, cols, diag1, diag2):
    if row == n:
        print("\nSolution Found: ")
        printBoard(board, n)
        return True
    
    for col in range(n):
        print(f"Trying Queen at row {row}, col {col}")
        
        if cols[col] or diag1[row - col + n -1] or diag2[row + col]:
            continue
        
        board[row] = col
        cols[col] = True
        diag1[row - col + n - 1] = True
        diag2[row + col] = True
        
        if solve(board, row+1, n, cols,diag1, diag2):
            return True
        
        board[row] = -1
        cols[col] = False
        diag1[row - col + n - 1] = False
        diag2[row + col] = False
        
    return False

def printBoard(board, n): 
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

def nQueenMain():
    n = int(input("Enter no. of Queens: "))
    
    board = [-1]*n
    cols = [False]*n
    diag1 = [False]*(2*n - 1)
    diag2 = [False]*(2*n - 1)
    
    if not solve(board, 0, n, cols, diag1, diag2):
        print("No Solution Found")
        
nQueenMain()