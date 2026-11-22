#!/usr/bin/env python3
"""Independent forest/feedback-vertex-set certificate for Q4 threshold 3.
No infection simulation: complement is an induced forest iff it percolates.
Requires Python 3.9+ only."""
from collections import Counter

vertices = range(16)
adj = [set(v ^ (1 << i) for i in range(4)) for v in vertices]


def forest_data(healthy):
    """Return connected components of induced forest or None on a cycle."""
    H = {v for v in vertices if healthy & (1 << v)}
    seen = set()
    components = []
    for root in H:
        if root in seen:
            continue
        component = set()
        stack = [(root, -1)]
        while stack:
            u, parent = stack.pop()
            if u in seen:
                return None
            seen.add(u)
            component.add(u)
            for w in adj[u].intersection(H):
                if w != parent:
                    stack.append((w, u))
        components.append(component)
    return components


def forest_diameter(comps):
    """Maximum component diameter, computed by BFS from every vertex."""
    def farthest(start, C):
        depth = {start: 0}
        todo = [start]
        for u in todo:
            for w in adj[u].intersection(C):
                if w not in depth:
                    depth[w] = depth[u] + 1
                    todo.append(w)
        return max(depth.values())
    return max((farthest(u, C) for C in comps for u in C), default=-1)


minimal = {}
for infected in range(1 << 16):
    healthy = ((1 << 16) - 1) ^ infected
    comps = forest_data(healthy)
    if comps is None:
        continue
    # Adding any currently infected vertex to the forest must create a cycle.
    # Equivalently it has two healthy neighbors in the same tree component.
    maximal = True
    for v in vertices:
        if not infected & (1 << v):
            continue
        if not any(len(adj[v].intersection(C)) >= 2 for C in comps):
            maximal = False
            break
    if maximal:
        minimal[infected] = forest_diameter(comps) // 2 + 1

hist = Counter((infected.bit_count(), t) for infected, t in minimal.items())
assert hist == {(6, 2): 8, (7, 3): 160, (7, 4): 768}
assert len(minimal) == 936
for rep, sizes, diameter in [
    (5736, [5, 5], 2),
    (5782, [7, 2], 4),
    (5801, [7, 1, 1], 4),
    (5785, [8, 1], 6),
    (5804, [9], 6),
    (5786, [9], 7),
]:
    healthy = 65535 ^ rep
    comps = forest_data(healthy)
    assert sorted([len(c) for c in comps],reverse=True) == sizes
    assert forest_diameter(comps) == diameter
print('PASS: induced-forest and maximality census, 936 minimal seeds, tree-diameter strata')
print('minimal:', sorted(hist.items()))
