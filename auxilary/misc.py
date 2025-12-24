def display_graph(graph):
    for key in graph:
        print(f"Cell {key}: State = {graph[key][0]}, Neighbors = {graph[key][1]}")