import heapq
graph= { 
    'S': [('A', 1), ('B', 4)],'A': [('C', 2)],'B': [('G', 5)],'C': [('G',3)],'G': []
}
h={'S': 5, 'A': 4, 'B':4, 'C': 2, 'G':0}
start= 'S'
goal= 'G'
def search(graph, h, start, goal):
    pq= [(h[start], 0, start, [start])]
    best= {start: 0}
    processed= []
    expanded= 0
    while pq:
        f, g, node, path= heapq.heappop(pq)
        if g != best[node]:
            continue
        processed.append(node)
        expanded +=1
        if node == goal:
            return path, g, processed, expanded
        for nxt, cost in graph[node]:
            new_g= g + cost
            if new_g<best.get(nxt, float("inf")):
                best[nxt]= new_g
                heapq.heappush(
                    pq, (new_g + h[nxt], new_g, nxt, path + [nxt])
                )
    return None, float("inf"), processed, expanded
def path_cost(graph, path):
    total= 0
    for u,v in zip(path, path[1:]):
        for nxt, cost in graph[u]:
            if nxt == v:
                total += cost
                break
    return total
path, cost, processed,count= search(graph, h, start, goal)
print("A* Search")
print("Path:", path)
print("Returned cost:", cost)
print("Independently summed cost:", path_cost(graph, path))
print("Processed nodes:", processed)
print("Expansion count:", count)
zero_h= {node: 0 for node in graph}
path, cost, processed, count= search(
    graph, zero_h, start, goal
)
print("\nUCS Search")
print("Path:", path)
print("Returned cost:", cost)
print("Independently summed cost:", path_cost(graph, path))
print("Processed nodes:", processed)
print("Expansion count:", count)