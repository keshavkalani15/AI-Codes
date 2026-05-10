#  Implement A star Algorithm for any game search problem. 

# Goal State
goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

# Heuristic: Misplaced tiles
def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count


def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_neighbors(state):
    neighbors = []
    x, y = find_zero(state)

    moves = [(0,1),(0,-1),(1,0),(-1,0)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new = [row[:] for row in state]
            new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
            neighbors.append(new)

    return neighbors


def a_star(start):
    open_list = [start]
    g = {str(start): 0}
    parent = {str(start): None}

    while open_list:
        current = min(open_list, key=lambda x: g[str(x)] + heuristic(x))

        print("\nCurrent State:")
        for row in current:
            print(row)

        print("\ng(n) =", g[str(current)])
        print("h(n) =", heuristic(current))
        print("f(n) =", g[str(current)] + heuristic(current))

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[str(current)]
            return path[::-1]

        open_list.remove(current)

        for neighbor in get_neighbors(current):
            cost = g[str(current)] + 1

            if str(neighbor) not in g or cost < g[str(neighbor)]:
                g[str(neighbor)] = cost
                parent[str(neighbor)] = current

                if neighbor not in open_list:
                    open_list.append(neighbor)

    return None


# -------- USER INPUT --------

print("Enter initial state (use 0 for blank):")
start = []

for i in range(3):
    row = [int(x) for x in input().split()]
    start.append(row)

# -------- OUTPUT --------

path = a_star(start)

if path:
    print("\nSolution Found")
else:
    print("\nNo solution found")
    
    
# Example

"""
1 2 3
4 0 6
7 5 8
"""