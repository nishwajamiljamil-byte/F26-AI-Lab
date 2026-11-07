from collections import deque
graph={"A":["B","C"],"B":["D","E"],"C":["F"],"D":[],"E":["G"],"F":[],"G":[]}
def run_bfs_trace(start_node, goal_node):
    queue=deque([(start_node,[start_node])]); 
    visited_set={start_node}
    while queue:
       node,path=queue.popleft()
       if node==goal_node: 
         return path
       for neighbor in graph[node]:
         if neighbor not in visited_set:
            visited_set.add(neighbor); 
            queue.append((neighbor,path+[neighbor]))
def run_dfs_trace(start_node, goal_node):
    stack=[(start_node,[start_node])]; 
    visited_set=set()
    while stack:
       current_node,path=stack.pop()
       if current_node==goal_node: 
          return path
       if current_node in visited_set: 
          continue
       visited_set.add(current_node)
       for neighbor in reversed(graph[current_node]): 
          stack.append((neighbor,path+[neighbor]))
print(run_bfs_trace("A","G")); 
print(run_dfs_trace("A","G"))