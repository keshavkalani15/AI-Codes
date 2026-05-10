from collections import deque

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
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)  

            
def Main():
    graph = {}
    visited = set()
    
    num = int(input("Enter no. of nodes: "))
    for i in range(num):
        data = input(f"Enter Node {i+1}: ")
        neighbors = input(f"Enter neighbor of {i+1} space seperated: ").split()
        graph[data] = neighbors

    start = input("Enter Start node: ")
    
    bfs(graph, start)
    
def prims():
    n = int(input("Enter no. of nodes: "))
    
    print("Enter Adjacency Matrix: ")
    graph = []
    for i in range(n):
        row = [int(x) for x in input().split()]
        graph.append(row) 
        
    selected = [False]*n
    selected[0] = True
    
    print("\nEdges in MST: ")
    
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
        selected[y] = True
        
def nqueens(board, row, n, cols, diag1, diag2):
    if row == n:
        print("Problem Solved!!")
        printMST(board, n)
        return True
    
    for col in range(n):
        if cols[col] or diag1[row - col + n - 1] or diag2[row + col]:
            continue
    
        print(f"Placing the queen at {row}, {col}")
        board[row] = col
        cols[col] = True
        diag1[row - col + n - 1] = True
        diag2[row + col] = True
        
        if nqueens(board, row + 1, n, cols, diag1, diag2):
            return True
        
        print(f"Backtracking from ({row}, {col})")
        board[row] = -1
        cols[col] = False
        diag1[row - col + n - 1] = False
        diag2[row + col] = False
        
    return False
        
def printMST(board, n):
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
        
def nqueenMain():
    n = int(input("Enter no. of Queens: "))
    board = [-1] * n
    cols = [False] * n
    diag1 = [False] * (2*n - 1)
    diag2 = [False] * (2*n - 1)
    
    if not nqueens(board, 0, n, cols, diag1, diag2):
        print("No Soln")
        
nqueenMain()