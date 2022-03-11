class Location:
    def __init__(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = dist

def find_min_distance(tiles):
    loc = Location(0, 0, 0)
    explored = [[False for _ in range(len(tiles[0]))] for _ in range(len(tiles))]

    for row in range(len(tiles)):
        for col in range(len(tiles[row])):
            if tiles[row][col] == "S":
                loc.row = row
                loc.col = col
                explored[row][col] = True
                break
    
    queue = [loc]
    while len(queue) != 0:
        loc = queue.pop(0)
        row, col, dist = loc.row, loc.col, loc.dist

        if tiles[row][col] == "G":
            return dist

        if is_valid(row - 1, col, tiles, explored):
            queue.append(Location(row - 1, col, dist + 1))
            explored[row - 1][col] = True

        if is_valid(row + 1, col, tiles, explored):
            queue.append(Location(row + 1, col, dist + 1))
            explored[row + 1][col] = True

        if is_valid(row, col - 1, tiles, explored):
            queue.append(Location(row, col - 1, dist + 1))
            explored[row][col - 1] = True

        if is_valid(row, col + 1, tiles, explored):
            queue.append(Location(row, col + 1, dist + 1))
            explored[row][col + 1] = True

    return -1

def is_valid(row, col, tiles, explored):
    if ((row >= 0 and col >= 0) and
        (row < len(tiles) and col < len(tiles[0])) and
        tiles[row][col] != "#" and
        not explored[row][col]):
        return True
    return False

if __name__ == '__main__':
    tiles = [
        ["#", "S", ".", "#", "G", ".", "."],
        [".", "#", ".", "#", ".", ".", "#"],
        ["#", ".", ".", "#", "#", ".", "."],
        [".", ".", "#", "#", ".", ".", "."],
        [".", ".", ".", ".", ".", "#", "."],
        ["#", ".", "#", ".", ".", ".", "."]
    ]

    print(find_min_distance(tiles))
