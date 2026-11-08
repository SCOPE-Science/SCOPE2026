#!/usr/bin/env python3
"""Independent order-five Latin-square intercalate-switch certificate.
No third-party Python packages are required. All labels are 0,...,4.
"""
import itertools
from collections import deque, Counter

N = 5
perms = list(itertools.permutations(range(N)))

# Enumerate reduced Latin squares independently of full-row enumeration.
reduced = []
rows = [tuple(range(N))]
used = [1 << j for j in range(N)]
by_first = [[p for p in perms if p[0] == r] for r in range(N)]

def rec(r):
    if r == N:
        reduced.append(tuple(x for row in rows for x in row))
        return
    for row in by_first[r]:
        if all(not used[c] & (1 << row[c]) for c in range(N)):
            rows.append(row)
            for c in range(N):
                used[c] |= 1 << row[c]
            rec(r + 1)
            for c in range(N):
                used[c] ^= 1 << row[c]
            rows.pop()
rec(1)
assert len(reduced) == 56

# Each reduced square becomes 24 squares with fixed first row by
# permuting its remaining four rows, then 120 by relabelling symbols.
squares = set()
for red in reduced:
    for tail in itertools.permutations(range(1, N)):
        row_order = (0,) + tail
        base = tuple(red[N * r + c] for r in row_order for c in range(N))
        for sigma in perms:
            squares.add(bytes(sigma[x] for x in base))
assert len(squares) == 161280
sq = sorted(squares)
lookup = {s: i for i, s in enumerate(sq)}

# Different transition predicate from the first implementation: for a
# pair of rows, inspect the cycle decomposition of the symbol map.
def neighbors(s):
    out = []
    for r in range(N):
        for t in range(r + 1, N):
            pos = [0] * N
            for c in range(N):
                pos[s[N * r + c]] = c
            for a in range(N):
                for b in range(a + 1, N):
                    c, d = pos[a], pos[b]
                    if s[N * t + c] == b and s[N * t + d] == a:
                        z = bytearray(s)
                        # Swap the two specified rows in columns c,d.
                        z[N * r + c], z[N * t + c] = z[N * t + c], z[N * r + c]
                        z[N * r + d], z[N * t + d] = z[N * t + d], z[N * r + d]
                        out.append(lookup[bytes(z)])
    assert len(out) == len(set(out))
    return out

adj = [neighbors(s) for s in sq]
assert all(i in adj[j] for i, ns in enumerate(adj) for j in ns)
assert Counter(map(len, adj)) == {0: 17280, 4: 144000}
assert sum(map(len, adj)) // 2 == 288000

comp_id = [-1] * len(sq)
components = []
for i in range(len(sq)):
    if comp_id[i] != -1:
        continue
    mark = len(components)
    comp_id[i] = mark
    todo = [i]
    for u in todo:
        for w in adj[u]:
            if comp_id[w] == -1:
                comp_id[w] = mark
                todo.append(w)
    components.append(todo)
assert Counter(map(len, components)) == {1: 17280, 18000: 8}

# A single 18,000-vertex distance certificate, extended to every
# component and vertex by the independent parity-group orbit check.
seed = next(k[0] for k in components if len(k) == 18000)
dist = [-1] * len(sq)
dist[seed] = 0
todo = [seed]
for u in todo:
    for w in adj[u]:
        if dist[w] == -1:
            dist[w] = dist[u] + 1
            todo.append(w)
distance_profile = tuple(Counter(dist[z] for z in todo)[k] for k in range(14))
assert len(todo) == 18000
assert distance_profile == (1, 4, 12, 36, 108, 252, 612, 1284, 2256, 3624, 4812, 3828, 1112, 59)

# The alternating-group generators are 3-cycles. They generate A5
# because adjacent triple cycles generate a transitive primitive subgroup
# of A5; alternatively enumerate the closure on five letters.
triples = ((0, 1, 2), (1, 2, 3), (2, 3, 4))
gens = []
for axis in range(3):
    for a, b, c in triples:
        p = list(range(N)); p[a], p[b], p[c] = b, c, a
        gens.append((axis, p))

def transform(s, axis, p):
    if axis == 0:  # Permute row labels.
        dest = bytearray(25)
        for r in range(N):
            dest[N * p[r]:N * p[r] + N] = s[N * r:N * r + N]
        return bytes(dest)
    if axis == 1:  # Permute column labels.
        dest = bytearray(25)
        for r in range(N):
            for c in range(N):
                dest[N * r + p[c]] = s[N * r + c]
        return bytes(dest)
    return bytes(p[x] for x in s)  # Relabel symbols.

# Verify that the alternating isotopy subgroup acts transitively on the
# computed component, and that all its generators preserve that component.
seen = {seed}
q = deque([seed])
while q:
    u = q.popleft()
    for axis, p in gens:
        v = lookup[transform(sq[u], axis, p)]
        assert comp_id[v] == comp_id[seed]
        if v not in seen:
            seen.add(v)
            q.append(v)
assert len(seen) == 18000

# Odd transpositions of the three coordinates provide the eight cosets.
p = (1, 0, 2, 3, 4)
orbit_ids = set()
for mask in range(8):
    s = sq[seed]
    for axis in range(3):
        if mask & (1 << axis):
            s = transform(s, axis, p)
    orbit_ids.add(comp_id[lookup[s]])
assert len(orbit_ids) == 8
assert all(len(components[x]) == 18000 for x in orbit_ids)

print('LATIN5_INDEPENDENT_CERTIFICATE_PASS')
print('reduced=56 labeled=161280 isolated=17280 mobile_components=8 mobile_component_size=18000')
print('mobile_degree=4 switch_edges=288000 diameter=radius=13')
print('profile=' + ','.join(map(str, distance_profile)))
print('even_isotopy_orbit=18000 odd_coset_components=8')
