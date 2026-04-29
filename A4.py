#   Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and 
#   Backtracking for n-queens problem or a graph coloring problem. 

def solve(board, row, n, cols, diag1, diag2):
    if row == n:
        print("\nSolution Found:")
        print_board(board, n)
        return True

    for col in range(n):
        print(f"Trying Queen at row {row}, col {col}")

        # Branch and Bound check (O(1))
        if cols[col] or diag1[row - col + n - 1] or diag2[row + col]:
            continue

        # Place queen
        print(f"Placed at ({row}, {col})")
        board[row] = col
        cols[col] = True
        diag1[row - col + n - 1] = True
        diag2[row + col] = True

        if solve(board, row + 1, n, cols, diag1, diag2):
            return True

        # Backtracking
        print(f"Backtracking from ({row}, {col})")
        board[row] = -1
        cols[col] = False
        diag1[row - col + n - 1] = False
        diag2[row + col] = False

    return False


def print_board(board, n):
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# -------- USER INPUT --------
n = int(input("Enter number of queens: "))

board = [-1] * n
cols = [False] * n
diag1 = [False] * (2 * n - 1)
diag2 = [False] * (2 * n - 1)

# -------- OUTPUT --------
if not solve(board, 0, n, cols, diag1, diag2):
    print("No solution exists")
    
    
# Example

"Enter number of queens: 4"