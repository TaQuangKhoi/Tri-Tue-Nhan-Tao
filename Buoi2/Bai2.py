graph1 = {
    '5' : ['3', '7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

graph2 = {
    '1' : ['8', '5', '2'],
    '8' : ['6', '4', '3'],
    '1' : ['10', '7'],
    '2' : ['9']
}

graph3 = {
    '60' : ['30', '70'],
    '30' : ['25', '38'],
    '25' : ['10', '28'],
    '38' : ['32'],
    '70' : ['61', '85']
}

visited = [] # List of visited nodes
queue   = [] # Initialize a queue


def bfs(visited, graph, node) :
    visited.append(node)
    queue.append(node)

    while queue: # Create a loop to visit each node
        m = queue.pop(0)
        print(m, end = " ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph1, '5')