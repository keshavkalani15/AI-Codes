#goal state

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

def find_zero(state):
    for i in state:
        for j in i:
            if state[i][j] == 0:
                return i,j
            
def heuristic(state):
    count = 0
    for i in range(3):    
        for j in range(3):
            if state[i][j] != goal[i][j]:
                count += 1
                
    return count

def get_neighbor(state):
    neighbors = []
    x, y = find_zero(state)
    
    moves = [(0,1), (0,-1), (1,0), (-1,0)]
    
    for dx, dy in moves:
        nx, ny = dx + x, dy + y
        
        if 0 <= x < 3 and 0 <= y < 3:
            new = [row[:] for row in state]
            new[x][y], new[nx][ny] = new[nx][ny], new[x][y] 
            neighbors.append(new)
            
    return neighbors