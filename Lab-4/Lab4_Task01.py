graph= {
    'S': [('A', 1),('B', 4)],'A': [('C', 2)],'B': [('G', 5)],'C': [('G', 3)],'G': []
}
h={'S': 5, 'A': 4, 'B': 4, 'C': 2, 'G': 0}
start= 'S'
goal= 'G'
frontier= [(h[start], 0, start, 0)]
order= 1
expanded= 0
while frontier and expanded <3:
    frontier.sort(key=lambda x: (x[0], x[1]))
    f, _, node, g= frontier.pop(0)
    print(f"\nExpansion {expanded +1}: {node}")
    print(f"g({node})= {g}")
    print(f"h({node}) = {h[node]}")
    print(f"f({node})= {g} + {h[node]}= {f}")
    if node == goal:
        print("Goal found!")
        break
    for child, cost in graph[node]:
        new_g= g + cost
        new_f= new_g + h[child]
        print (f"\n{child}: g= {g} + {cost}= {new_g}")
        print(f"f={new_g} + {h[child]}= {new_f}")
        frontier.append((new_f, order, child, new_g))
        order +=1
    print("\nRemaining frontier:")
    if frontier:
        for f_value, _, n, g_value in sorted(
            frontier, key=lambda x: (x[0], x[1])
        ):
           print(f"{n}: g={g_value}, h={h[n]}, f={f_value}")
    else:
            print("Empty")
    if frontier:
            next_node= min(frontier, key= lambda x: (x[0], x[1]))
            print(f"\nNext selected: {next_node[2]}"
                  f" because it has the lowest f-value."
                  )
    expanded +=1
print("\nFirst 3 expansions completed.")