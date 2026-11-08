#!/usr/bin/env python3
"""Exact combinatorial verification for the independence complex of the truncated tetrahedron."""
from collections import Counter, defaultdict, deque
from itertools import permutations

V = tuple((i, j) for i in range(4) for j in range(4) if i != j)
N = len(V)
INDEX = {v: k for k, v in enumerate(V)}
ADJ = [sum(1 << k for k, (a, b) in enumerate(V)
           if ((i == a and j != b) or (i == b and j == a)))
       for i, j in V]
assert N == 12
assert sum(row.bit_count() for row in ADJ) == 36
assert all(bool(ADJ[i] & (1 << j)) == bool(ADJ[j] & (1 << i))
           for i in range(N) for j in range(N))

faces = [0]
for i in range(N):
    faces += [f | (1 << i) for f in faces if f & ADJ[i] == 0]
face_set = set(faces)
assert len(faces) == len(face_set) == 163
assert Counter(f.bit_count() - 1 for f in faces) == {-1: 1, 0: 12, 1: 48, 2: 72, 3: 30}

# A specified finite discrete Morse matching, entirely generated from the face poset.
# For each pivot, pair currently unmatched faces which differ by this pivot.
order = (1, 9, 8, 5, 10, 2, 3, 7, 4, 0, 11, 6)
unmatched = set(face_set - {0})
pairs = []
for i in order:
    for f in sorted(unmatched):
        g = f | (1 << i)
        if not (f & (1 << i)) and g in unmatched:
            unmatched.remove(f)
            unmatched.remove(g)
            pairs.append((f, g))
assert len(pairs) == 78 and len(unmatched) == 6
assert Counter(f.bit_count() - 1 for f in unmatched) == {0: 1, 2: 5}
assert len(set(x for pair in pairs for x in pair)) == 156
assert not unmatched.intersection(x for pair in pairs for x in pair)

# A finite acyclicity proof: orient each matched cover upward and all other
# covers downward. Kahn elimination must visit every nonempty face.
matched = set(pairs)
heads = {f: [] for f in face_set if f}
indeg = {f: 0 for f in heads}
covers = 0
for f in heads:
    for i in range(N):
        if f & (1 << i):
            lower = f ^ (1 << i)
            if not lower:
                continue
            a, b = (lower, f) if (lower, f) in matched else (f, lower)
            heads[a].append(b)
            indeg[b] += 1
            covers += 1
assert covers == 432
ready = deque(f for f in indeg if indeg[f] == 0)
visited = 0
while ready:
    a = ready.popleft()
    visited += 1
    for b in heads[a]:
        indeg[b] -= 1
        if indeg[b] == 0:
            ready.append(b)
assert visited == 162, "A directed closed gradient path exists"

# Independently calculate all augmented boundary ranks over F_2.
by_dim = defaultdict(list)
for f in faces:
    by_dim[f.bit_count() - 1].append(f)
ranks = {}
for d in range(0, 4):
    low_index = {f: k for k, f in enumerate(by_dim[d - 1])}
    pivots = {}
    for f in by_dim[d]:
        col = 0
        for i in range(N):
            if f & (1 << i):
                col ^= 1 << low_index[f ^ (1 << i)]
        while col:
            v = col.bit_length() - 1
            if v not in pivots:
                pivots[v] = col
                break
            col ^= pivots[v]
    ranks[d] = len(pivots)
assert [len(by_dim[d]) - ranks.get(d, 0) - ranks.get(d + 1, 0)
        for d in range(4)] == [0, 0, 5, 0]

# Exact equivariant Lefschetz character on reduced chains.
def parity(p):
    return (-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))

def cycle_type(p):
    visited = set()
    blocks = []
    for i in range(4):
        if i in visited:
            continue
        j, m = i, 0
        while j not in visited:
            visited.add(j)
            m += 1
            j = p[j]
        blocks.append(m)
    return tuple(sorted(blocks, reverse=True))

class_chars = defaultdict(set)
group = list(permutations(range(4)))
for p in group:
    moved = [INDEX[(p[i], p[j])] for i, j in V]
    total = 0
    for face in faces:
        indices = [i for i in range(N) if face & (1 << i)]
        orbit_image = sum(1 << moved[i] for i in indices)
        if orbit_image != face:
            continue
        images = [moved[i] for i in indices]
        inversions = sum(images[i] > images[j]
                         for i in range(len(images)) for j in range(i + 1, len(images)))
        # Augmented simplex degree = |face|-1 (including empty face).
        sign = -1 if ((len(indices) - 1 + inversions) % 2) else 1
        total += sign
    # The five 2-dimensional critical cells imply homology concentration in degree 2.
    assert total == 1 + parity(p) * sum(p[i] == i for i in range(4)), (p, total)
    class_chars[cycle_type(p)].add(total)
assert {k: tuple(v)[0] for k, v in class_chars.items()} == {
    (1, 1, 1, 1): 5, (2, 1, 1): -1, (2, 2): 1, (3, 1): 2, (4,): 1
}
assert sum(1 + parity(p) * sum(p[i] == i for i in range(4)) for p in group) == 24
# A4-invariant rank is two (even permutations only), and total S4-invariant rank is one.
even = [p for p in group if parity(p) == 1]
assert sum(1 + parity(p) * sum(p[i] == i for i in range(4)) for p in even) == 24

# Every cycle type admits an invariant independent face. Thus each element
# has a fixed point in the geometric realization.
for p in group:
    moved = [INDEX[(p[i], p[j])] for i, j in V]
    assert any(f != 0 and sum(1 << moved[i] for i in range(N) if f & (1 << i)) == f
               for f in faces), p

print("ALL_VERIFY_OK faces=163 nonempty=162 pairs=78 critical=(1,0,5,0) covers=432")
print("BOUNDARY_RANKS", tuple(ranks[d] for d in range(4)))
print("S4_CLASS_CHARS", {str(k): next(iter(v)) for k, v in sorted(class_chars.items())})
print("GROUP_ELEMENTS=24 FIXED_POINT_ELEMENTS=24 QUOTIENT_RANKS_S4=1_A4=2")
