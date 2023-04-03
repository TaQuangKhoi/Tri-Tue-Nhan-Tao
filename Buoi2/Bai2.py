graph = {
    '5' : ['3', '7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

graph1 = {
    '1' : ['2', '3', '4'],

    '2' : ['5', '6'],
    '3' : [],
    '4' : ['7', '8'],

    '5' : ['9', '10'],
    '6' : [],
    '7' : ['11', '12'],
    '8' : [],

    '9' : [],
    '10' : [],
    '11' : [],
    '12' : []
}

graph2 = {
    '1' : ['8', '5', '2'],

    '8' : ['6', '4', '3'],
    '5' : [],
    '2' : ['9'],

    '6' : ['10', '7'],
    '4' : [],
    '3' : [],
    '9' : [],

    '10' : [],
    '7' : []
}

graph3 = {
    '60' : ['30', '70'],

    '30' : ['25', '38'],
    '70' : ['61', '85'],

    '25' : ['10', '28'],
    '38' : ['32'],
    '61' : [],
    '85' : [],

    '10' : [],
    '28' : [],
    '32' : []
}

visited = [] # List of visited nodes
queue   = [] # Initialize a queue

# biến node là nút bắt đầu
def bfs(visited, graph, node) :
    visited.append(node)
    queue.append(node)

    while queue: # Create a loop to visit each node
        print("Queue: ", queue, end = "\n")
        m = queue.pop(0)
        print(m, end = " ")

        for neighbour in graph[m]:
            print( "Graph[m] %s" % (graph[m]) , end = "\n")
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph1, '5')