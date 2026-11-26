#!/usr/bin/env python3
"""Exhaustive independent certificates for Petersen acyclic-orientation clicks.

Uses only Python 3 standard library. No external files are required.
The graph is KG(5,2) with vertices lexicographic 2-subsets and edges
between disjoint 2-subsets; an orientation is a 15-bit vector.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations

V = tuple(combinations(range(5), 2))
N = len(V)
E = tuple((a, b) for a in range(N) for b in range(a + 1, N)
          if not (set(V[a]) & set(V[b])))
M = len(E)
assert (N, M) == (10, 15)
edge_index = {e: i for i, e in enumerate(E)}
inc = [[] for _ in range(N)]
for k, (u, v) in enumerate(E):
    inc[u].append((k, 0))
    inc[v].append((k, 1))
vertex_flip = [sum(1 << k for k, _ in inc[u]) for u in range(N)]


def arcs(s):
    return [(v, u) if s >> k & 1 else (u, v)
            for k, (u, v) in enumerate(E)]


def is_acyclic_kahn(s):
    out = [[] for _ in range(N)]
    indeg = [0] * N
    for u, v in arcs(s):
        out[u].append(v)
        indeg[v] += 1
    q = deque(u for u in range(N) if not indeg[u])
    seen = 0
    while q:
        u = q.popleft()
        seen += 1
        for v in out[u]:
            indeg[v] -= 1
            if not indeg[v]:
                q.append(v)
    return seen == N


def is_acyclic_dfs(s):
    out = [[] for _ in range(N)]
    for u, v in arcs(s):
        out[u].append(v)
    color = [0] * N

    def visit(u):
        color[u] = 1
        for v in out[u]:
            if color[v] == 1 or (color[v] == 0 and not visit(v)):
                return False
        color[u] = 2
        return True

    return all(color[u] != 0 or visit(u) for u in range(N))


# Independent DAG tests cover every possible directed edge assignment.
acyclic = []
for s in range(1 << M):
    a = is_acyclic_kahn(s)
    assert a == is_acyclic_dfs(s), ('acyclicity disagreement', s)
    if a:
        acyclic.append(s)
states = set(acyclic)
assert len(acyclic) == 16680

# The independent chromatic(-1) expansion also checks the state count.
# The coefficient at q is +/-T_G(1,0) for a connected graph.
chi = [0] * (N + 1)
for subset in range(1 << M):
    parent = list(range(N))
    parts = N

    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for k, (u, v) in enumerate(E):
        if subset >> k & 1:
            a, b = root(u), root(v)
            if a != b:
                parent[a] = b
                parts -= 1
    chi[parts] += -1 if subset.bit_count() & 1 else 1
assert sum(c * (-1 if k & 1 else 1) for k, c in enumerate(chi)) == 16680
assert chi[1] == -704

# A click at a source (or its undirected inverse, a sink) changes every
# incident edge. Reject a vertex unless all incident arcs point consistently.
adj = {}
for s in acyclic:
    neighbors = set()
    for u in range(N):
        if (all((s >> k & 1) == end for k, end in inc[u]) or
            all((s >> k & 1) != end for k, end in inc[u])):
            t = s ^ vertex_flip[u]
            assert t in states
            neighbors.add(t)
    adj[s] = neighbors
for s in acyclic:
    assert all(s in adj[t] for t in adj[s]), ('asymmetric click', s)
assert sum(map(len, adj.values())) // 2 == 28140

# Components and exact radii/diameters.
components = []
component_id = {}
for s in acyclic:
    if s in component_id:
        continue
    index = len(components)
    q = deque([s]); component_id[s] = index; members = []
    while q:
        u = q.popleft(); members.append(u)
        for w in adj[u]:
            if w not in component_id:
                component_id[w] = index; q.append(w)
    components.append(tuple(sorted(members)))
assert len(component_id) == 16680
assert len(components) == 704
expected_sizes = {12: 120, 16: 120, 21: 120, 22: 120,
                  28: 120, 38: 60, 50: 24, 66: 20}
assert dict(Counter(map(len, components))) == expected_sizes

# A second, independent partition test uses the published cycle-circulation
# invariant: evaluate orientation signs along six fundamental cycles.
parent = list(range(N))
def root(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

tree = [[] for _ in range(N)]
chords = []
for k, (u, v) in enumerate(E):
    a, b = root(u), root(v)
    if a == b:
        chords.append((k, u, v))
    else:
        parent[a] = b
        tree[u].append((v, k));tree[v].append((u, k))
assert len(chords) == 6
cycles = []
for chord, u, v in chords:
    # Oriented fundamental cycle traverses the chord u->v then tree v->u.
    q = deque([v]); pred = {v: None}
    while q and u not in pred:
        a = q.popleft()
        for b, k in tree[a]:
            if b not in pred:
                pred[b] = (a, k);q.append(b)
    path = [(chord, 1)]
    x = u
    backwards = []
    while x != v:
        a, k = pred[x]
        e0, e1 = E[k]
        backwards.append((k, 1 if a == e0 else -1))
        x = a
    path += list(reversed(backwards))
    cycles.append(tuple(path))

def signature(s):
    return tuple(sum(sign * (-1 if s >> k & 1 else 1) for k, sign in cyc)
                 for cyc in cycles)

signature_groups = defaultdict(list)
for s in acyclic:
    signature_groups[signature(s)].append(s)
assert len(signature_groups) == len(components)
for members in signature_groups.values():
    assert len({component_id[s] for s in members}) == 1

# The natural full S5 relabeling action of KG(5,2).
vertex_index = {v: i for i, v in enumerate(V)}
actions = []
for p in permutations(range(5)):
    vm = [vertex_index[tuple(sorted(p[z] for z in v))] for v in V]
    bits = []
    inverted = 0
    for k, (u, v) in enumerate(E):
        a, b = vm[u], vm[v]
        pair = (min(a, b), max(a, b))
        assert pair in edge_index
        k2 = edge_index[pair]
        bits.append(k2)
        if a > b:
            inverted ^= (1 << k2)
    assert len(set(bits)) == M
    actions.append((tuple(bits), inverted))
assert len(actions) == 120

def action(s, a):
    bits, inverted = a
    t = inverted
    for k, k2 in enumerate(bits):
        if s >> k & 1:
            t ^= (1 << k2)
    return t

# Every component is a click-equivalence class; relabeling transports it.
orbits = []
remaining = set(range(len(components)))
while remaining:
    k = min(remaining)
    rep = components[k][0]
    orbit = frozenset(component_id[action(rep, a)] for a in actions)
    assert orbit <= remaining
    assert all(len(components[j]) == len(components[k]) for j in orbit)
    remaining -= orbit
    orbits.append((k, orbit))
assert len(orbits) == 9

# Compute exact eccentricity at every acyclic orientation, not representatives.
component_metrics = {}
for k, members in enumerate(components):
    edge_count = sum(len(adj[s]) for s in members) // 2
    ecc = []
    for s in members:
        dist = {s: 0}
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    q.append(v)
        assert len(dist) == len(members)
        ecc.append(max(dist.values()))
    component_metrics[k] = (len(members), edge_count, min(ecc), max(ecc))

# A reverse-orientation involution commutes with the relabeling action.
all_bits = (1 << M) - 1
print('size copies vertices_per_component_edges radius diameter symmetry_orbits')
rows = []
for size in sorted(expected_sizes, reverse=True):
    ids = [k for k, members in enumerate(components) if len(members) == size]
    descriptors = {component_metrics[k] for k in ids}
    assert len(descriptors) == 1
    descriptor = next(iter(descriptors))
    orbit_ids = [i for i, (_, orbit) in enumerate(orbits) if orbit & set(ids)]
    row = (size, len(ids), *descriptor[1:], len(orbit_ids))
    rows.append(row)
    print(*row)
assert rows == [
    (66, 20, 150, 5, 6, 1),
    (50, 24, 105, 5, 6, 1),
    (38, 60, 73, 5, 6, 1),
    (28, 120, 49, 5, 6, 1),
    (22, 120, 34, 5, 5, 1),
    (21, 120, 33, 5, 5, 2),
    (16, 120, 22, 5, 5, 1),
    (12, 120, 14, 5, 5, 1),
]
assert sum(row[0] * row[1] for row in rows) == 16680
assert sum(row[2] * row[1] for row in rows) == 28140
orbit_of = {j: i for i, (_, orb) in enumerate(orbits) for j in orb}
reversal = []
for i, (k, orb) in enumerate(orbits):
    j = component_id[components[k][0] ^ all_bits]
    reversal.append(orbit_of[j])
assert sorted(len(orbit) for _, orbit in orbits) == sorted([20, 24, 60, 120, 120, 60, 60, 120, 120])
assert sum(i != j for i, j in enumerate(reversal)) == 2
assert all(len(components[orbits[i][0]]) == 21 for i, j in enumerate(reversal) if i != j)
print('summary orientations=16680 edges=28140 components=704')
print('symmetry_orbit_sizes', sorted([len(x) for _, x in orbits]))
print('reversal_interchanges_21_vertex_orbits', True)
print('cycle_signatures', len(signature_groups))
print('VERIFY_OK')
