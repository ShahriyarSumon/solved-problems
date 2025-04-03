
def is_safe(graph, colors, vertex, color):

    for neighbor in graph[vertex]:
        if colors[neighbor] == color:
            return False
    return True

def graph_coloring_util(graph, colors, vertex, K):
       if vertex == len(graph):
        return True

    for color in range(1, K + 1):
        if is_safe(graph, colors, vertex, color):
            colors[vertex] = color
            if graph_coloring_util(graph, colors, vertex + 1, K):
                return True
          
            colors[vertex] = 0

    return False

def graph_coloring(graph, N, M, K):
       colors = [0] * N

     if graph_coloring_util(graph, colors, 0, K):
        print(f"Coloring Possible with {K} Colors")
        print("Color Assignment:", colors)
    else:
        print(f"Coloring Not Possible with {K} Colors")

def main():
 
    N, M, K = map(int, input("Enter number of vertices, edges, and colors (N M K): ").split())
    
    graph = {i: [] for i in range(N)}
    
    print(f"Enter {M} edges (u v) pairs:")
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
       graph_coloring(graph, N, M, K)

if __name__ == "__main__":
    main()

