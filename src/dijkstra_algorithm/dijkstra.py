def dijkstra_shortest_path(graph, source):
    n = len(graph)
    unvisited = set(range(n))
    paths = [0] * n
    for vertex in range(n):
        if vertex != source:
            paths[vertex] = float('inf')
    while unvisited:
        # select the shortest path vertext
        curr = 0
        temp = float('inf')
        for vertex in unvisited:
            if temp > paths[vertex]:
                curr = vertex
            temp = paths[vertex]
        unvisited.remove(curr)

        # calculate the distance from curr to each neighbour
        for vertex in unvisited:
            if graph[curr][vertex] != 0:
                paths[vertex] = min(paths[curr] + graph[curr][vertex], paths[vertex])
        
    return paths