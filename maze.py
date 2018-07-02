import random
import sys

# Using bits to represent each direction.
# eg. NORTH: 0001, SOUTH:0010, EAST:0100, WEST:1000
NORTH, SOUTH, EAST, WEST = 1, 2, 4, 8

# Bit used to check if already visited in solver.
SOLVER_VISITED = 16

# DY and DX represent the change in the maze coordinates(x, y) on moving to each direction.
DY = {NORTH: -1, SOUTH: 1, WEST: 0, EAST: 0}
DX = {NORTH: 0, SOUTH: 0, WEST: -1, EAST: 1}
# OPPOSITE just maps a direction to it's opposite dierction.
OPPOSITE = {NORTH: SOUTH, SOUTH: NORTH, EAST: WEST, WEST: EAST}

def get_empty_maze(width, height):
    '''
    Returns maze of required width and height filled with 0's(0000)
    '''
    return [[0 for _ in range(width)] for _ in range(height)]

def get_carved_maze(maze, current_y, current_x):
    '''
    Takes an empty maze and carves passages in it using recursive backtracking.
    '''
    directions = [NORTH, SOUTH, EAST, WEST]
    # Shuffle the order of direction to randomize the path directions.
    random.shuffle(directions)
    for direction in directions:
        # New cell coordinates = current cell coordinates + DY/DX
        new_y = current_y + DY[direction]
        new_x = current_x + DX[direction]
        # If new cell within maze boundaries and is unvisited.
        if 0 <= new_y < len(maze) and 0 <= new_x < len(maze[new_y]) and maze[new_y][new_x] == 0:
            # We add the direction to the cell by OR'ing with the direction value.
            maze[current_y][current_x] |= direction
            # We add the opposite direction to the new cell by OR'ing with the opposite direction value.
            maze[new_y][new_x] |= OPPOSITE[direction]
            # Call the function recursively with new cell coordinates.
            get_carved_maze(maze, new_y, new_x)
    return maze
 
def get_maze_solution_path(maze, current_y, current_x, end_y, end_x, points=[]):
    '''
    Takes a carved maze and tries to find a path from start coordinates to end coordinates.
    Uses recursive backtracking.
    '''
    if current_y == end_y and current_x == end_x:
        points.append((current_y, current_x))
        return points
    directions = [NORTH, SOUTH, EAST, WEST]
    # Find which directions have an open path in a cell.
    valid_directions = list(filter(lambda direction: direction & maze[current_y][current_x] != 0, directions))
    random.shuffle(valid_directions)
    for direction in valid_directions:
        new_y = current_y + DY[direction]
        new_x = current_x + DX[direction]
        # If new cell within maze boundaries and is unvisited by solver.
        if 0 <= new_y < len(maze) and 0 <= new_x < len(maze[new_y]) and (maze[new_y][new_x] & SOLVER_VISITED == 0):
            maze[current_y][current_x] |= SOLVER_VISITED
            points.append((current_y, current_x))
            get_maze_solution_path(maze, new_y, new_x, end_y, end_x, points)
            if points[-1] == (end_y, end_x):
                return points
            points.pop()
    return []

def print_maze(maze):
    '''
    Given a maze, display it using ascii characters.
    '''
    width = len(maze[0])
    height = len(maze)
    print(width, height)
    # Print the top boundary.
    print(' ' + '_' * ((width * 2) - 1))
    for y in range(height):
        # Print the left boundary.
        sys.stdout.write('|')
        for x in range(width):
            # Print bottom wall in a cell depending on if there is a south path.
            if maze[y][x] & SOUTH != 0:
                sys.stdout.write(' ')
            else:
                sys.stdout.write('_')
            # Print right wall in a cell depending on if there is a east path.
            if maze[y][x] & EAST != 0:
                if (maze[y][x] | maze[y][x+1]) & SOUTH != 0:
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('_')
            else:
                sys.stdout.write('|')
        print()
