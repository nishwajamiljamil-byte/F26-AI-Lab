from collections import deque
graph={
    "A": ["B", "C"],"B": ["D", "E"],"C": ["F"],"D": [],"E": ["G"],"F": [],"G": []
}
def run_dls_trace(current_node, target_node,depth_limit, current_path):
    if current_node== target_node:
        return "FOUND", current_path
    if depth_limit== 0:
        return "CUTOFF", None
    cutoff_occurred= False
    for neighbor in graph[current_node]:
        if neighbor in current_path:
            continue
        status,result= run_dls_trace(neighbor, target_node,depth_limit-1, current_path + [neighbor])
        if status =="FOUND":
          return "FOUND", result
        if status =="CUTOFF":
          cutoff_occured= True
    if cutoff_occurred:
        return "CUTOFF", None
    else:
        return "FAILURE", None
for limit in [1,2,3,4]:
    status, path= run_dls_trace("A","G",limit,["A"])
    print (f"Limit {limit} | Status: {status} | Path: {path}")

