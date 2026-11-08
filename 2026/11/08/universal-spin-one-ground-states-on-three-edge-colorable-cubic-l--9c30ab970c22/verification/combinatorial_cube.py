"""Independent matching, edge-coloring, and even-cycle census for Q_3.

Does not use spin-state enumeration or energy evaluation.
"""
from collections import Counter
from itertools import combinations

vertices = tuple(range(8))
edges = tuple((u, v) for u in vertices for v in vertices
              if u < v and (u ^ v).bit_count() == 1)
assert len(edges) == 12

matching_counts = Counter()
even_cycle_weight = 0
cycle_support_counts = Counter()
for mask in range(1 << len(edges)):
    chosen = [e for i,e in enumerate(edges) if mask & (1 << i)]
    endpoints = [u for e in chosen for u in e]
    if len(set(endpoints)) == len(endpoints):
        matching_counts[len(chosen)] += 1

    degrees = Counter(endpoints)
    if not all(degrees[v] in (0, 2) for v in vertices):
        continue
    neighbors = {v: set() for v in vertices}
    for u,v in chosen:
        neighbors[u].add(v)
        neighbors[v].add(u)
    seen = set()
    components = 0
    valid = True
    for root in vertices:
        if root in seen or not neighbors[root]:
            continue
        stack = [root]
        reached = set()
        while stack:
            u = stack.pop()
            if u in reached: continue
            reached.add(u)
            stack.extend(neighbors[u]-reached)
        seen |= reached
        if len(reached) % 2:
            valid = False
        components += 1
    if valid:
        even_cycle_weight += 2**components
        cycle_support_counts[len(chosen)] += 2**components

by_vertex = {v: [] for v in vertices}
for i,(u,v) in enumerate(edges):
    by_vertex[u].append(i)
    by_vertex[v].append(i)

def colorings(i, assignment):
    if i == len(edges):
        return 1
    u,v = edges[i]
    forbidden = {assignment[j] for j in by_vertex[u]+by_vertex[v]
                 if j in assignment}
    ans = 0
    for col in range(3):
        if col not in forbidden:
            assignment[i] = col
            ans += colorings(i+1, assignment)
            del assignment[i]
    return ans

n_three_colorings = colorings(0,{})
assert matching_counts == Counter({0:1,1:12,2:42,3:44,4:9})
assert sum(matching_counts.values()) == 108
assert even_cycle_weight == 69
assert cycle_support_counts == Counter({0:1,4:12,6:32,8:24})
assert n_three_colorings == 24
print("matching polynomial", dict(sorted(matching_counts.items())))
print("even-cycle weighted enumerator", dict(sorted(cycle_support_counts.items())))
print("proper labeled 3-edge colorings", n_three_colorings)
print("COMBINATORIAL_CUBE_OK")
