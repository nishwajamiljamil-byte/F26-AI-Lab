import heapq
graph= { 
    'S': [('A', 1), ('B', 4)],'A': [('C', 2)],'B': [('G', 5)],'C': [('G',3)],'G': []
}
h={'S': 5, 'A': 4, 'B':4, 'C': 2, 'G':0}
h['C']= 10
def astar(start, goal):
    pq= [(h[start], 0, start, [start])]
    best= {start: 0}
    processed= []
    while pq:
        f, g, node, path= heapq.heappop(pq)
        if g != best[node]:
            continue
        processed.append(node)
        if node == goal:
            return path, g, processed, len(processed)
        for nxt, cost in graph[node]:
            new_g= g + cost
            if new_g<best.get(nxt, float('inf')):
                best[nxt]=new_g
                heapq.heappush(
                    pq, (new_g + h[nxt], new_g, nxt, path + [nxt])
                )
    return None, float('inf'), processed, len(processed)
path, cost, processed, count = astar('S', 'G')
print("Modified h(C):", h['C'])
print("Path:", path)
print("Cost:", cost)
print("Processed nodes:", processed)
print("Expansion count:", count)
