def createGrid(height, width):
    grid = []
    tile = 1
    for x in range(0, height):
        row = []
        for y in range(0, width):
            row.append(tile)
            tile += 1
        grid.append(row)
    return grid
