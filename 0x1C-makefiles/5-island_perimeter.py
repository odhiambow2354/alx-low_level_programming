#!/usr/bin/python3

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
    - grid (list of list of integers): The grid representing the island.
    
    Returns:
    - int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    
    perimeter = 0
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4
                
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2
    
    return perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
