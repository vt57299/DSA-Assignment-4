# Breadth First Traversal for a graph

from collections import defaultdict
class graph:
    def __init__(self):
        self.data = defaultdict(list)

    def addedge(self,u,v):
        self.data[u].append(v)
    
    def bfs(self,start):
        visited = [False] * (max(self.data)+1)
        queue = []

        queue.append(start)
        visited[start] = True

        while queue:
            start= queue.pop(0)
            print(start,end=" ")
        
            for i in self.data[start]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i]  = True


obj = graph()
obj.addedge(0,1)
obj.addedge(0,2)
obj.addedge(1,2)
obj.addedge(2,0)
obj.addedge(2,3)
obj.addedge(3,3)

obj.bfs(2)
