#!/usr/bin/python3


def island_perimeter(grid):
    count = 0

    column = len(grid[0])

    for i in range(len(grid) * column):
        r = i // column
        c = i % column
        if grid[r][c] == 1:
            if r != 0 and c != 0:
                if grid[r - 1][c] == 1 and grid[r][c - 1]:
                    pass
                elif grid[r - 1][c] == 1 or grid[r][c - 1]:
                    count += 2
                else:
                    count += 4
    return count
