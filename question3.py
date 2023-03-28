# Count the number of nodes at given level in a tree using BFS

from collections import deque

class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
    
def node_count(root,level):
    if not root:
        return 0
    
    queue = deque([(root,0)])
    count = 0

    while queue:
        node,cur_lev = queue.popleft()
        if cur_lev == level:
            count += 1
        elif cur_lev > level:
            break

        if node.left:
            queue.append((node.left,cur_lev+1))
        if node.right:
            queue.append((node.right,cur_lev+1))

    return count

root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
print(node_count(0,1))
