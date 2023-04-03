# Các đồ thị có hướng

graph1 = {
    '0': ['2', '4', '5'],
    '1': ['4', '5'],
    '2': ['3', '4'],
    '3': [],
    '4': ['5'],
    '5': []
}

graph2 = {
    '1': ['2', '4', '5'],
    '2': ['1', '3', '4', '6'],
    '3': ['2'],
    '4': ['1', '2', '5', '6'],
    '5': ['1', '4', '6', '7'],
    '6': ['2', '4', '5'],
    '7': ['5']
}

graphAlphabet = {
    'A': ['B', 'C', 'D'],
    'B': ['G', 'I'],
    'G': [],
    'I': [],
    'C': ['E', 'F'],
    'E': ['K'],
    'F': [],
    'D': [],
    'K': []
}
visited = [] # List of visited nodes

def dfs(visited, graph, node) :
    if node not in visited :
        print(node, end=" ")
        visited.append(node)
        for neighbour in graph[node] :
            dfs(visited, graph, neighbour)


dfs(visited, graph2, '2')