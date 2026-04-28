# -------- Selection Sort Function --------
def selection_sort():
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        arr.append(int(input("Enter element: ")))

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    print("Sorted array:", arr)


# -------- Prim's Algorithm Function --------
def prims():
    n = int(input("Enter number of vertices: "))

    print("Enter adjacency matrix:")
    graph = []
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    selected = [False] * n
    selected[0] = True

    print("\nEdges in MST:")

    for _ in range(n - 1):
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

        print(x, "-", y, "=", graph[x][y])
        selected[y] = True


# -------- Main Menu --------
def main():
    print("\n--- Greedy Algorithms Menu ---")
    print("1. Selection Sort")
    print("2. Prim's MST")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        selection_sort()

    elif choice == 2:
        prims()

    elif choice == 3:
        print("Exiting...")

    else:
        print("Invalid choice!")
        
main()


# Example 

# 1. Selection Sort

""" 
Input:
5
64 25 12 22 11
"""

# 2. Prim's Algorithm

"""
Enter number of vertices: 4

0 2 0 6
2 0 3 8
0 3 0 0
6 8 0 0
"""