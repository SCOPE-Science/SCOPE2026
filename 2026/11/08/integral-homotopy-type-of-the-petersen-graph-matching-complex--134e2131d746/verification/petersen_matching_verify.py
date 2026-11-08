#!/usr/bin/env python3
"""Exact finite certificate for the ordinary matching complex of KG(5,2).

Only the Python standard library is required. Vertices of the Petersen graph
are 2-subsets of {0,...,4}, graph adjacency is disjointness. Simplicial
vertices are graph edges, ordered lexicographically. The empty simplex is
included in the augmented chain complex.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

points = list(combinations(range(5), 2))
edges = [(i, j) for i in range(10) for j in range(i + 1, 10)
         if set(points[i]).isdisjoint(points[j])]
assert len(edges) == 15

# Exhaustive simplex test by pairwise endpoints, independently by used masks.
faces = set()
for mask in range(1 << len(edges)):
    chosen = [edges[i] for i in range(len(edges)) if mask & (1 << i)]
    test1 = all(set(e).isdisjoint(f) for e, f in combinations(chosen, 2))
    used = 0
    test2 = True
    for a, b in chosen:
        two = (1 << a) | (1 << b)
        if two & used:
            test2 = False
            break
        used |= two
    assert test1 == test2
    if test1:
        faces.add(mask)

fv = Counter(m.bit_count() - 1 for m in faces if m)
assert dict(fv) == {0: 15, 1: 75, 2: 145, 3: 90, 4: 6}
assert len(faces) == 332

# Greedy complete-interval matching by toggling successive simplex vertices.
unpaired = set(faces)
pairs = []
for j in range(15):
    for lo in sorted(unpaired):
        hi = lo | (1 << j)
        if hi != lo and hi in unpaired:
            pairs.append((lo, hi))
            unpaired.remove(lo)
            unpaired.remove(hi)
assert len(pairs) == 159
assert len(unpaired) == 14
assert 0 not in unpaired
assert Counter(m.bit_count() - 1 for m in unpaired) == {2: 7, 3: 7}

# Verify all covering incidences in the augmented face poset, orientation
# reversed on matched pairs. Kahn's algorithm is an exhaustive DAG test.
matched = set(pairs)
adj = {m: [] for m in faces}
indegree = {m: 0 for m in faces}
incidences = 0
for hi in faces:
    for j in range(15):
        if hi & (1 << j):
            lo = hi ^ (1 << j)
            assert lo in faces
            src, dst = (lo, hi) if (lo, hi) in matched else (hi, lo)
            adj[src].append(dst)
            indegree[dst] += 1
            incidences += 1
assert incidences == 990
q = deque(x for x in faces if indegree[x] == 0)
visited = 0
while q:
    u = q.popleft()
    visited += 1
    for v in adj[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)
assert visited == len(faces), 'matching is cyclic'

# Construct the exact augmented signed simplicial boundary.
original = {}
for mask in faces:
    bits = [j for j in range(15) if mask & (1 << j)]
    original[mask] = {mask ^ (1 << j): (-1) ** pos
                      for pos, j in enumerate(bits)}
assert all(r in faces for col in original.values() for r in col)

# Independently test d^2=0 before reducing, including augmentation.
for m in faces:
    double = defaultdict(int)
    for s, c in original[m].items():
        for t, d in original[s].items():
            double[t] += c * d
    assert all(c == 0 for c in double.values())

# Algebraic elementary cancellation is the chain-level implementation of
# discrete Morse paths. Each pivot must remain an exact integer unit.
cols = {m: dict(v) for m, v in original.items()}
survivors = set(faces)
pending = set(pairs)
pivot_count = 0
while pending:
    admissible = [(lo, hi, cols[hi].get(lo, 0)) for lo, hi in pending
                  if abs(cols[hi].get(lo, 0)) == 1]
    assert admissible, 'no available unit pivot'
    lo, hi, pivot = min(admissible, key=lambda t: (t[1].bit_count(), t[1]))
    boundary_hi = dict(cols[hi])
    for m in list(survivors):
        if m == lo or m == hi or m.bit_count() != hi.bit_count():
            continue
        b = cols[m].get(lo, 0)
        if b:
            for row, c in boundary_hi.items():
                new = cols[m].get(row, 0) - b * pivot * c
                if new:
                    cols[m][row] = new
                else:
                    cols[m].pop(row, None)
    for m in survivors:
        cols[m].pop(hi, None)
    cols.pop(hi)
    cols.pop(lo)
    survivors.remove(hi)
    survivors.remove(lo)
    pending.remove((lo, hi))
    pivot_count += 1
assert pivot_count == 159
assert survivors == unpaired
assert Counter(m.bit_count() - 1 for m in survivors) == {2: 7, 3: 7}
assert all(all(row in survivors for row in col) for col in cols.values())

crit2 = sorted(m for m in survivors if m.bit_count() == 3)
crit3 = sorted(m for m in survivors if m.bit_count() == 4)
assert crit2 == [162, 276, 530, 1156, 2336, 4114, 28672]
assert crit3 == [5250, 6416, 10400, 14464, 17696, 21760, 25120]
M = [[cols[hi].get(lo, 0) for hi in crit3] for lo in crit2]
expected = [
    [ 1, 0,-1, 0, 1, 0, 1],
    [ 0,-1, 1, 1,-1,-1,-1],
    [ 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0],
    [-1, 1, 0,-1, 0, 1, 0],
    [ 0, 0, 0, 0, 0, 0, 0],
]
assert M == expected
assert M[5] == [-M[0][i] - M[1][i] for i in range(7)]
assert M[0][0] * M[1][1] - M[0][1] * M[1][0] == -1
# Hence rank 2 and Smith invariant factors 1,1 (all other zeros).

# Separate, original simplicial-chain calculations over several prime fields.
bydim = defaultdict(list)
for m in faces:
    bydim[m.bit_count() - 1].append(m)
for rows in bydim.values():
    rows.sort()

def rank_mod_prime(k, p):
    """Rank of the unreduced signed d_k over a field, sparse elimination."""
    lookup = {m: i for i, m in enumerate(bydim[k - 1])}
    basis = {}
    for m in bydim[k]:
        column = {lookup[row]: val % p for row, val in original[m].items()}
        while column:
            row = max(column)
            if row not in basis:
                inv = pow(column[row], -1, p)
                basis[row] = {j: (inv * v) % p for j, v in column.items()}
                break
            factor = column[row]
            for j, val in basis[row].items():
                now = (column.get(j, 0) - factor * val) % p
                if now:
                    column[j] = now
                else:
                    column.pop(j, None)
    return len(basis)

for prime in (2, 3, 5, 7):
    ranks = [rank_mod_prime(k, prime) for k in range(5)]
    assert ranks == [1, 14, 61, 79, 6], (prime, ranks)
    assert len(bydim[2]) - ranks[2] - ranks[3] == 5
    assert len(bydim[3]) - ranks[3] - ranks[4] == 5

print('PETERSEN_MATCHING_CERTIFICATE_PASS')
print('graph_vertices=10 graph_edges=15 nonempty_simplices=331')
print('f_vector=(15,75,145,90,6) cover_relations=990')
print('matched_pairs=159 critical_2=7 critical_3=7')
print('integral_Morse_boundary_3_to_2=')
for row in M:
    print(' '.join(map(str, row)))
print('Smith_nonzero=(1,1) reduced_Betti_2=5 reduced_Betti_3=5')
print('independent_field_checks=2,3,5,7')
