graph={
    'p':['q','r','s'],
    'q':['p','r'],
    'r':['p','q','t'],
    't':['r'],
    's':['p']
    }
visited=[]
queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        s=queue.pop()
        print(s,end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
bfs(visited,graph,'p')
