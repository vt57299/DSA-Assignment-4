# Depth First Traversal for a Graph

def add_node(v):
    if v in graph:
        print(v,"is already present in graph")
    else:
        graph[v] = []
                                        
def add_edge(v1,v2):                     
    if v1 not in graph:               
        print(v1,"is not present in graph")
    elif v2 not in graph:                 
        print(v2,"is not present in graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)


def dfs(node,visited,graph):
    if node not in graph:
        print("Node is not present in graph")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            dfs(i,visited,graph)

visited = set()
graph = {}

add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")

add_edge("A","B")
add_edge("B","E")
add_edge("A","C")
add_edge("A","D")
add_edge("B","D")
add_edge("C","D")
add_edge("E","D")
print(graph)
dfs("K",visited,graph)
