#   Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and 
#   Backtracking for n-queens problem or a graph coloring problem. 

def is_safe(board, row, col, n):
    # check column
    for i in range(row):
        if board[i] == col:
            return False

    # check left diagonal
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(board, row, n):
    if row == n:
        print("\nSolution Found:")
        print_board(board, n)
        return True

    for col in range(n):
        print(f"Trying Queen at row {row}, col {col}")

        if is_safe(board, row, col, n):
            print(f"Placed at ({row}, {col})")
            board[row] = col

            if solve(board, row + 1, n):
                return True

            # backtrack
            print(f"Backtracking from ({row}, {col})")
            board[row] = -1

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

# -------- OUTPUT --------

if not solve(board, 0, n):
    print("No solution exists")
    
    
# Example

"Enter number of queens: 4"