import random


def generate_grid(N):
    grid = [[random.choice(['.', '#']) for _ in range(N)] for _ in range(N)]

    while True:
        src = (random.randint(0, N - 1), random.randint(0, N - 1))
        goal = (random.randint(0, N - 1), random.randint(0, N - 1))
        if src != goal and grid[src[0]][src[1]] == '.' and grid[goal[0]][goal[1]] == '.':
            break

    return grid, src, goal


def print_grid(grid):
    for row in grid:
        print(' '.join(row))


def dfs(grid, src, goal):
    N = len(grid)
    stack = [src]
    parent = {src: None}
    visited = set()
    topo_order = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        topo_order.append(node)

        if node == goal:
            break

        x, y = node
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == '.' and (nx, ny) not in visited:
                stack.append((nx, ny))
                parent[(nx, ny)] = node

    path = []
    if goal in parent:
        cur = goal
        while cur:
            path.append(cur)
            cur = parent[cur]
        path.reverse()

    return path, topo_order


def main():
    N = random.randint(4, 7)
    grid, src, goal = generate_grid(N)

    print("Generated Grid:")
    print_grid(grid)
    print(f"\nSource: {src}")
    print(f"Goal: {goal}")

    path, topo_order = dfs(grid, src, goal)

    print("\nDFS Path:")
    print(path if path else "No path found")

    print("\nTopological Order of Node Traversal:")
    print(topo_order)


if __name__ == "__main__":
    main()
