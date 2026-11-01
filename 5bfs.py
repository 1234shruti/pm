from collections import deque

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = [start]

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(path + [neighbor])

    return None


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

start = 'A'
goal = 'G'

path = bfs(graph, start, goal)

if path:
    print("Robot path:", path)
else:
    print("No path found")