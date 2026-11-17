#!/usr/bin/env python3
"""Exact finite verification of the dodecahedral independence-homology character.

Python standard library only. The graph is GP(10,2). Bitmasks encode subsets.
No external source files, packages, or saved computational data are used.
"""
from collections import Counter, defaultdict

N = 20
ADJ = [0] * N
for i in range(10):
    for u, v in ((i, (i + 1) % 10),
                 (i, 10 + i),
                 (10 + i, 10 + (i + 2) % 10)):
        ADJ[u] |= 1 << v
        ADJ[v] |= 1 << u
assert all(a.bit_count() == 3 for a in ADJ)

FACES = defaultdict(list)
def enumerate_faces(S, remaining):
    if not remaining:
        FACES[S.bit_count()].append(S)
        return
    b = remaining & -remaining
    i = b.bit_length() - 1
    enumerate_faces(S, remaining ^ b)
    enumerate_faces(S | b, remaining & ~(b | ADJ[i]))
enumerate_faces(0, (1 << N) - 1)
for layer in FACES.values():
    layer.sort()
face_counts = [len(FACES[k]) for k in range(9)]
assert face_counts == [1, 20, 160, 660, 1510, 1912, 1240, 320, 5]

# Reduced integral simplicial chain complex, reduced modulo 2.
# The map from vertices to the empty face is included in the ranks.
ranks = [0] * 9
for k in range(1, 9):
    row_index = {f: j for j, f in enumerate(FACES[k - 1])}
    pivots = {}
    for f in FACES[k]:
        boundary = 0
        t = f
        while t:
            b = t & -t
            t ^= b
            boundary ^= 1 << row_index[f ^ b]
        while boundary:
            leading = boundary.bit_length() - 1
            if leading not in pivots:
                pivots[leading] = boundary
                break
            boundary ^= pivots[leading]
    ranks[k] = len(pivots)
assert ranks[1:] == [1, 19, 141, 519, 991, 921, 315, 5]
mod2_reduced_betti = [len(FACES[k]) - ranks[k] - (ranks[k + 1] if k < 8 else 0)
                      for k in range(1, 9)]
assert mod2_reduced_betti == [0, 0, 0, 0, 0, 4, 0, 0]
assert sum((-1)**k * face_counts[k] for k in range(9)) == 4

# Exhaustive automorphism enumeration, checking all previously assigned
# adjacencies and non-adjacencies at every extension.
AUTOS = []
partial = [-1] * N
def automorphism_search(depth, used):
    if depth == N:
        AUTOS.append(tuple(partial))
        return
    assigned = [j for j in range(N) if partial[j] != -1]
    v = max((j for j in range(N) if partial[j] == -1),
            key=lambda j: (sum((ADJ[j] >> t) & 1 for t in assigned), -j))
    for w in range(N):
        if used >> w & 1:
            continue
        if all(bool(ADJ[v] >> t & 1) == bool(ADJ[w] >> partial[t] & 1)
               for t in assigned):
            partial[v] = w
            automorphism_search(depth + 1, used | (1 << w))
            partial[v] = -1
automorphism_search(0, 0)
assert len(AUTOS) == len(set(AUTOS)) == 120
ID = tuple(range(N))
AUTO_SET = set(AUTOS)
assert ID in AUTO_SET

def multiply(g, h):
    return tuple(g[h[i]] for i in range(N))
def inverse(g):
    ans = [0] * N
    for i, j in enumerate(g):
        ans[j] = i
    return tuple(ans)

# The five eight-point independent sets are the five inscribed cube vertices.
CUBES = sorted(FACES[8])
assert len(CUBES) == 5
assert all(sum(1 << i for i in range(N) if c >> i & 1) == c for c in CUBES)

def cube_action(g):
    return tuple(CUBES.index(sum(1 << g[i] for i in range(N) if c >> i & 1))
                 for c in CUBES)

def cyclic_orbits(g):
    unseen = set(range(N))
    result = []
    while unseen:
        i = min(unseen)
        cyc = []
        j = i
        while j in unseen:
            unseen.remove(j)
            cyc.append(j)
            j = g[j]
        assert j == i
        result.append(tuple(cyc))
    return result

def trace_by_orbit_graph(g):
    """Independence polynomial at -1 of admissible orbit graph."""
    cycles = cyclic_orbits(g)
    allowed = []
    for cyc in cycles:
        B = sum(1 << i for i in cyc)
        if all(not (ADJ[i] & (B ^ (1 << i))) for i in cyc):
            allowed.append(B)
    q = len(allowed)
    qa = [0] * q
    for j in range(q):
        for k in range(j + 1, q):
            if any(ADJ[i] & allowed[k] for i in range(N) if allowed[j] >> i & 1):
                qa[j] |= 1 << k
                qa[k] |= 1 << j
    def independence_at_minus_one(active):
        if not active:
            return 1
        b = active & -active
        i = b.bit_length() - 1
        return (independence_at_minus_one(active ^ b)
                - independence_at_minus_one(active & ~(b | qa[i])))
    return independence_at_minus_one((1 << q) - 1)

def sign_on_ordered_set(g, f):
    vertices = [i for i in range(N) if f >> i & 1]
    images = [g[i] for i in vertices]
    if sorted(images) != vertices:
        return 0
    inv = sum(images[i] > images[j] for i in range(len(images))
              for j in range(i + 1, len(images)))
    return (-1) ** inv

def trace_by_signed_simplices(g):
    # Due to the reduced degree -1, this equals the H_5 character,
    # provided reduced rational homology is concentrated in degree five.
    return sum((-1) ** k * sign_on_ordered_set(g, f)
               for k in range(9) for f in FACES[k])

CHI = {}
for g in AUTOS:
    x = trace_by_orbit_graph(g)
    assert x == trace_by_signed_simplices(g)
    CHI[g] = x
assert CHI[ID] == 4
assert sum(x*x for x in CHI.values()) == 120

# Derive the A_5 subgroup as the group of commutators, and verify closure.
COMM = {multiply(multiply(multiply(g, h), inverse(g)), inverse(h))
        for g in AUTOS for h in AUTOS}
assert len(COMM) == 60
assert all(multiply(g, h) in COMM for g in COMM for h in COMM)
assert all(inverse(g) in COMM for g in COMM)
assert len({cube_action(g) for g in AUTOS}) == 60
assert len({cube_action(g) for g in COMM}) == 60
antipodal = tuple((i + 5) % 10 if i < 10 else 10 + (i - 10 + 5) % 10
                  for i in range(N))
assert antipodal in AUTO_SET and antipodal not in COMM
assert cube_action(antipodal) == tuple(range(5))
assert all(multiply(antipodal, g) == multiply(g, antipodal) for g in AUTOS)
assert CHI[antipodal] == -4

# Character equals the antipodal-sign twist of the augmentation
# representation of the permutation action on the five cubes.
for g in AUTOS:
    eps = 1 if g in COMM else -1
    fixed = sum(j == cube_action(g)[j] for j in range(5))
    assert CHI[g] == eps * (fixed - 1)
assert sum(CHI[g] for g in COMM) == 0
assert sum(CHI.values()) == 0
assert sum(CHI[g] ** 2 for g in COMM) == 60

# Whole group, A_5 subgroup, and central antipode quotient invariant ranks.
cube_stabilizer_rot = [g for g in COMM if cube_action(g)[0] == 0]
cube_stabilizer_full = [g for g in AUTOS if cube_action(g)[0] == 0]
assert len(cube_stabilizer_rot) == 12 and len(cube_stabilizer_full) == 24
assert (sum(CHI.values()) // 120,
        sum(CHI[g] for g in COMM) // 60,
        (CHI[ID] + CHI[antipodal]) // 2,
        sum(CHI[g] for g in cube_stabilizer_rot) // 12,
        sum(CHI[g] for g in cube_stabilizer_full) // 24) == (0, 0, 0, 1, 0)

conjugacy_classes = []
remaining = set(AUTOS)
while remaining:
    g = min(remaining)
    cl = {multiply(multiply(h, g), inverse(h)) for h in AUTOS}
    assert cl <= remaining
    remaining -= cl
    conjugacy_classes.append((len(cl), CHI[g],
                              1 if g in COMM else -1,
                              sum(j == cube_action(g)[j] for j in range(5))))
assert Counter(conjugacy_classes) == Counter({
    (1, 4, 1, 5):1, (15, 0, 1, 1):1, (20, 1, 1, 2):1,
    (12, -1, 1, 0):2, (1, -4, -1, 5):1, (15, 0, -1, 1):1,
    (20, -1, -1, 2):1, (12, 1, -1, 0):2})
print('GRAPH_VERTICES=20 EDGES=30 AUTOMORPHISMS=120')
print('FACES_BY_CARDINALITY=' + str(face_counts))
print('REDUCED_F2_BOUNDARY_RANKS=' + str(ranks[1:]))
print('REDUCED_F2_BETTI_DEGREES_0_TO_7=' + str(mod2_reduced_betti))
print('MAXIMAL_INDEPENDENT_CUBE_SETS=' + str([[i for i in range(N) if c>>i & 1] for c in CUBES]))
print('COMMUTATOR_SUBGROUP=60 CUBE_PERMUTATION_IMAGE=60 ANTIPODAL_TRACE=-4')
print('CONJUGACY_CLASSES_(size,trace,antipodal_sign,fixed_cubes)=' + str(sorted(conjugacy_classes)))
print('IRREDUCIBLE_CHARACTER_NORM=1; RESTRICTED_ROTATION_NORM=1')
print('RATIONAL_INVARIANT_RANKS_(full,rotations,antipodal,cube_A4,cube_full)=(0,0,0,1,0)')
print('DODECAHEDRAL_CUBE_AUGMENTATION_CHARACTER_PASS')
