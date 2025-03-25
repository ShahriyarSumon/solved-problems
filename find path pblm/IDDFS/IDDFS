def iddfs(maze, start, target):
    rows, cols = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dls(x, y, depth, limit, visited, path):
        if (x, y) == target:
            path.append((x, y))
            return True
        if depth >= limit:
            return False

        visited.add((x, y))
        path.append((x, y))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                if dls(nx, ny, depth + 1, limit, visited, path):
                    return True
        path.pop()
        visited.remove((x, y))
        return False

    depth = 0
    while True:
        visited = set()
        path = []
        if dls(start[0], start[1], 0, depth, visited, path):
            print(f"Path found at depth {depth} using IDDFS")
            print("Traversal Order:", path)
            return
        depth += 1
        if depth > 5:
            print(f"Path not found at max depth {depth} using IDDFS")
            return



rows, cols = map(int, input().split())


maze = []
for _ in range(rows):
    maze.append(list(map(int, input().split())))

start = tuple(map(int, input("start: ").split()))
target = tuple(map(int, input("target : ").split()))

iddfs(maze, start, target)
