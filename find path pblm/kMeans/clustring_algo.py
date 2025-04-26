import random

def generate_data():
    points = []
    centers = []
    for _ in range(100):
        x = random.randint(0, 20)
        y = random.randint(0, 20)
        points.append((x, y))
    for _ in range(10):
        x = random.randint(0, 20)
        y = random.randint(0, 20)
        centers.append((x, y))
    return points, centers

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def assign_clusters(points, centers):
    clusters = {}
    for i in range(len(centers)):
        clusters[i] = []

    for p in points:
        min_dist = float('inf')
        cluster_idx = -1
        for idx, center in enumerate(centers):
            dist = manhattan_distance(p, center)
            if dist < min_dist:
                min_dist = dist
                cluster_idx = idx
        clusters[cluster_idx].append(p)

    return clusters


def update_centers(clusters):
    new_centers = []
    for points in clusters.values():
        if points:
            avg_x = sum(p[0] for p in points) // len(points)
            avg_y = sum(p[1] for p in points) // len(points)
            new_centers.append((avg_x, avg_y))
        else:

            new_centers.append((random.randint(0, 20), random.randint(0, 20)))
    return new_centers


def visualize(points, centers):
    matrix = [["." for _ in range(21)] for _ in range(21)]

    for x, y in points:
        matrix[y][x] = "*"

    for idx, (x, y) in enumerate(centers):
        matrix[y][x] = str(idx % 10)

    print("\nVisualization:")
    for row in reversed(matrix):
        print(" ".join(row))

def kmeans_manhattan():
    points, centers = generate_data()

    for iteration in range(5):
        clusters = assign_clusters(points, centers)
        centers = update_centers(clusters)

    visualize(points, centers)


kmeans_manhattan()
