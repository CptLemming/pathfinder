def draw_grid(grid, start=None, goal=None, width=2, cost={}):
    for y in range(0, grid.height):
        row = ''
        for x in range(0, grid.width):
            if (x, y) == start:
                row += 'S'.ljust(width)
            elif (x, y) == goal:
                row += 'G'.ljust(width)
            elif (x, y) in grid.walls:
                row += ''.ljust(width, '#')
            elif (x, y) in cost:
                row += '{0}'.format(cost[(x, y)]).ljust(width)
            else:
                row += '.'.ljust(width)
        print(row)


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)
