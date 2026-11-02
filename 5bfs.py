import collections

grid = [
    [0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)

moves = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1)    # Right
]

queue = collections.deque([start])
visited = {start}
parent = {start: None}

while queue:
    current = queue.popleft()

    if current == goal:
        break

    r, c = current

    for dr, dc in moves:
        nr = r + dr
        nc = c + dc

        if (0 <= nr < len(grid) and
            0 <= nc < len(grid[0]) and
            grid[nr][nc] == 0 and
            (nr, nc) not in visited):

            visited.add((nr, nc))
            parent[(nr, nc)] = current
            queue.append((nr, nc))

if goal in visited:
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    print("Shortest Path:")
    for position in path:
        print(position)

    print("Path Cost:", len(path) - 1)

else:
    print("No path found!")