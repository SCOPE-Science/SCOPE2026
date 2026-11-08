#!/usr/bin/env python3
"""Reproduce the Pappus edge-Kempe graph from perfect matchings, stdlib only."""
from collections import Counter, deque

SHIFTS = (5, 7, -7, 7, -7, -5)
N = 18
edges = {tuple(sorted((i, (i + 1) % N))) for i in range(N)}
for i in range(N):
    edges.add(tuple(sorted((i, (i + SHIFTS[i % 6]) % N))))
edges = sorted(edges)
assert len(edges) == 27
edge_index = {e: k for k, e in enumerate(edges)}
inc = [[] for _ in range(N)]
for k, (u, v) in enumerate(edges):
    inc[u].append(k)
    inc[v].append(k)
assert all(len(x) == 3 for x in inc)

matchings = []
def find_matchings(remaining, choice):
    if not remaining:
        matchings.append(frozenset(choice))
        return
    v = min(remaining, key=lambda w: sum((edges[e][0] in remaining and edges[e][1] in remaining) for e in inc[w]))
    for e in inc[v]:
        u, w = edges[e]
        other = w if v == u else u
        if other in remaining:
            find_matchings(remaining - {v, other}, choice + [e])
find_matchings(set(range(N)), [])
assert len(set(matchings)) == len(matchings) == 42

def cycles_on_edges(edge_set):
    remaining = set(edge_set)
    comps = []
    while remaining:
        first = min(remaining)
        component = {first}
        remaining.remove(first)
        queue = [first]
        for e in queue:
            for v in edges[e]:
                for f in inc[v]:
                    if f in remaining:
                        remaining.remove(f)
                        component.add(f)
                        queue.append(f)
        comps.append(component)
    return comps

def canon(cols):
    assigned = {}
    out = []
    for c in cols:
        if c not in assigned:
            assigned[c] = len(assigned)
        out.append(assigned[c])
    return tuple(out)

states = set()
complement_types = Counter()
special = []
for matching in matchings:
    remainder = set(range(len(edges))) - set(matching)
    cyc = cycles_on_edges(remainder)
    lengths = tuple(sorted(map(len, cyc)))
    complement_types[lengths] += 1
    assert lengths in ((18,), (6, 6, 6))
    if lengths == (6, 6, 6):
        special.append(matching)
    # Each cycle has two ways to alternate the two complementary colors.
    for mask in range(1 << len(cyc)):
        colors = [0] * len(edges)
        for ci, comp in enumerate(cyc):
            start = min(comp)
            vertex = edges[start][0]
            current = start
            previous = None
            parity = (mask >> ci) & 1
            while True:
                colors[current] = 1 + parity
                parity ^= 1
                a, b = edges[current]
                vertex = b if vertex == a else a
                choices = [x for x in inc[vertex] if x in comp and x != current]
                assert len(choices) == 1
                nxt = choices[0]
                if nxt == start:
                    break
                current = nxt
        states.add(canon(colors))
assert complement_types == Counter({(18,): 36, (6, 6, 6): 6})
assert len(states) == 20
special = sorted(special, key=lambda m: tuple(sorted(m)))
EXPECTED_SPECIAL = (
    (0,5,9,12,16,19,21,24,26),
    (0,6,7,11,14,18,19,22,24),
    (1,3,7,13,14,17,22,23,25),
    (1,4,5,10,12,17,20,23,26),
    (2,3,8,9,13,15,16,21,25),
    (2,4,6,8,10,11,15,18,20),
)
assert tuple(tuple(sorted(m)) for m in special) == EXPECTED_SPECIAL

states = sorted(states)
lookup = {s: i for i, s in enumerate(states)}
adj = [set() for _ in states]
for i, colors in enumerate(states):
    for a, b in ((0, 1), (0, 2), (1, 2)):
        ab = {e for e, x in enumerate(colors) if x in (a, b)}
        for comp in cycles_on_edges(ab):
            nxt = list(colors)
            for e in comp:
                nxt[e] = b if nxt[e] == a else a
            nxt = canon(nxt)
            if nxt != colors:
                assert nxt in lookup
                adj[i].add(lookup[nxt])
assert all(i in adj[j] for j, row in enumerate(adj) for i in row)
assert Counter(map(len, adj)) == Counter({3: 18, 9: 2})

components = []
unseen = set(range(len(states)))
while unseen:
    start = min(unseen)
    unseen.remove(start)
    component = {start}
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for w in adj[v] & unseen:
            unseen.remove(w)
            component.add(w)
            queue.append(w)
    components.append(component)
assert len(components) == 2 and all(len(c) == 10 for c in components)
assert sum(map(len, adj)) // 2 == 36

for component in components:
    hubs = [v for v in component if len(adj[v]) == 9]
    assert len(hubs) == 1
    hub = hubs[0]
    peripheral = component - {hub}
    triangles = []
    unseen = set(peripheral)
    while unseen:
        a = min(unseen)
        tri = {a} | (adj[a] & peripheral)
        assert len(tri) == 3
        assert all((tri - {v}) == (adj[v] & peripheral) for v in tri)
        triangles.append(tri)
        unseen -= tri
    assert len(triangles) == 3
    # Each component is K_1 joined to three disjoint triangles.
    assert sum(len(adj[v] & component) for v in component) // 2 == 18

hubs = [v for v in range(len(states)) if len(adj[v]) == 9]
exception_counts = []
for s in states:
    classes = [frozenset(i for i, c in enumerate(s) if c == a) for a in range(3)]
    exception_counts.append(sum(m in special for m in classes))
assert Counter(exception_counts) == Counter({1: 18, 3: 2})
for m in special:
    containing = [s for s in states if m in [frozenset(i for i, c in enumerate(s) if c == a) for a in range(3)]]
    assert len(containing) == 4
    assert sorted(exception_counts[lookup[s]] for s in containing) == [1, 1, 1, 3]
for hub in hubs:
    extraordinary = []
    for a in range(3):
        matching = frozenset(i for i, c in enumerate(states[hub]) if c == a)
        extraordinary.append(special.index(matching))
    assert len(extraordinary) == 3

print('PASS: 42 perfect matchings (36 Hamiltonian complements, 6 three-hexagon complements)')
print('PASS: 20 unlabeled 1-factorizations; 36 Kempe adjacencies')
print('PASS: Kempe graph is two disjoint copies of K1 join 3 K3')
print('Exceptional matching edge-index sets:', [sorted(m) for m in special])
assert sorted(tuple(sorted(special.index(frozenset(i for i, c in enumerate(states[h]) if c == a)) for a in range(3))) for h in hubs) == [(0, 2, 5), (1, 3, 4)]
print('Hub exceptional matching indices:', [sorted(special.index(frozenset(i for i, c in enumerate(states[h]) if c == a)) for a in range(3)) for h in hubs])
