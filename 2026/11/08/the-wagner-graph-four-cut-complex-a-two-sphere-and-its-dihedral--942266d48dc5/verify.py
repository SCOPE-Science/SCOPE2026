#!/usr/bin/env python3
"""Exact finite verification of the Wagner graph's ordinary four-cut complex.

Run with Python 3; no third-party dependencies. Vertex sets are encoded as 8-bit masks.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, product
from math import gcd

N = 8
EDGES = {frozenset((i, (i + 1) % N)) for i in range(N)}
EDGES |= {frozenset((i, (i + 4) % N)) for i in range(4)}
assert len(EDGES) == 12


def connected(subset):
    selected = set(subset)
    seen = {min(selected)}
    queue = list(seen)
    for u in queue:
        for v in selected - seen:
            if frozenset((u, v)) in EDGES:
                seen.add(v)
                queue.append(v)
    return len(seen) == len(selected)


def mask(vertices):
    return sum(1 << x for x in vertices)


FACETS = {mask(set(range(N)) - set(c)) for c in combinations(range(N), 4)
          if not connected(c)}
FACES = {sub for facet in FACETS for sub in range(1 << N)
         if (sub & facet) == sub}
NONEMPTY = FACES - {0}
COUNTS = Counter(x.bit_count() - 1 for x in NONEMPTY)
assert len(FACETS) == 26
assert [COUNTS[k] for k in range(4)] == [8, 28, 48, 26]
assert len(FACES) == 111


def incidence(coface):
    vertices = [i for i in range(N) if coface & (1 << i)]
    return [(coface ^ (1 << vertex), -1 if rank % 2 else 1)
            for rank, vertex in enumerate(vertices)]


def matching(order):
    unmatched = set(NONEMPTY)
    pairs = []
    for i in order:
        for a in sorted(unmatched):
            b = a | (1 << i)
            if b != a and a in unmatched and b in unmatched:
                pairs.append((a, b))
                unmatched.remove(a)
                unmatched.remove(b)
    return pairs, unmatched


def directed_acyclicity(pairs):
    reversed_edges = set(pairs)
    indegree = {x: 0 for x in NONEMPTY}
    adjacency = {x: [] for x in NONEMPTY}
    hasse = 0
    for b in NONEMPTY:
        for a, _ in incidence(b):
            if a not in NONEMPTY:
                continue
            hasse += 1
            source, target = (a, b) if (a, b) in reversed_edges else (b, a)
            adjacency[source].append(target)
            indegree[target] += 1
    q = deque(x for x in NONEMPTY if not indegree[x])
    visited = 0
    while q:
        x = q.popleft()
        visited += 1
        for y in adjacency[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                q.append(y)
    assert visited == len(NONEMPTY), "Morse matching contains a closed gradient path"
    return hasse


def project_2_chains(pairs, critical):
    lower = {a: (b, next(coef for face, coef in incidence(b) if face == a))
             for a, b in pairs}
    upper = {b for a, b in pairs}

    @lru_cache(None)
    def project(a):
        if a in critical:
            return {a: 1}
        if a in upper:
            return {}
        b, pivot = lower[a]
        result = defaultdict(int)
        for face, coef in incidence(b):
            if face == a:
                continue
            for c, amount in project(face).items():
                result[c] -= coef * pivot * amount
        return dict(result)

    def chain_projection(chain):
        result = defaultdict(int)
        for a, coefficient in chain.items():
            for c, amount in project(a).items():
                result[c] += amount * coefficient
        return {c: v for c, v in result.items() if v}

    return chain_projection


def boundary_column(b):
    return dict(incidence(b))


# Two distinct pivot orders; both full matchings must be acyclic.
for order in (list(range(N)), list(range(N - 1, -1, -1))):
    pairs, crit = matching(order)
    assert len(pairs) == 53
    assert Counter(a.bit_count() - 1 for a in crit) == {0: 1, 2: 2, 3: 1}
    hasse = directed_acyclicity(pairs)
    assert hasse == 304
    crit2 = sorted(a for a in crit if a.bit_count() == 3)
    crit3 = [a for a in crit if a.bit_count() == 4]
    proj = project_2_chains(pairs, crit)
    vector = [proj(boundary_column(crit3[0])).get(x, 0) for x in crit2]
    assert gcd(*vector) == 1
    if order[0] == 0:
        assert (crit2, crit3, vector) == ([38, 50], [180], [-1, 1])
        selected_projection = proj
        selected_critical = crit2
    print("Morse", "ascending" if order[0] == 0 else "descending",
          "pairs", len(pairs), "critical", Counter(a.bit_count() - 1 for a in crit),
          "boundary", vector, "hasse", hasse)


# Integer primitive octahedral 2-cycle supported on vertices 0,...,5.
PAIRS = ((0, 1), (2, 3), (4, 5))
oct_sphere = defaultdict(int)
for choices in product((0, 1), repeat=3):
    ordered = [PAIRS[i][choices[i]] for i in range(3)]
    inversions = sum(ordered[i] > ordered[j] for i in range(3) for j in range(i + 1, 3))
    sign = -1 if (sum(choices) + inversions) % 2 else 1
    oct_sphere[mask(ordered)] += sign
assert len(oct_sphere) == 8
assert set(oct_sphere) <= NONEMPTY
boundary = defaultdict(int)
for f, coefficient in oct_sphere.items():
    for a, sgn in incidence(f):
        boundary[a] += coefficient * sgn
assert all(v == 0 for v in boundary.values())
projection = selected_projection(oct_sphere)
assert [projection.get(x, 0) for x in selected_critical] == [1, 0]
# The critical 3-cell boundary [-1,1] yields quotient Z^2/<(-1,1)>;
# the induced generator map is the sum of the two critical coordinates.
assert sum(projection.values()) == 1
print("Octahedral generator", "pairs", PAIRS, "projection", projection, "degree", 1)


# Independent integer boundary certificate: a square minor with determinant +1.
# The listed indices are triangular 3-vertex masks, not order-dependent row numbers.
UNIT_MINOR_TRIANGLES = (11, 13, 19, 21, 22, 25, 26, 35, 37, 38,
                        41, 42, 44, 49, 50, 52, 69, 70, 73, 74,
                        76, 81, 82, 84, 88, 98)
assert len(UNIT_MINOR_TRIANGLES) == 26
assert all(t in NONEMPTY and t.bit_count() == 3 for t in UNIT_MINOR_TRIANGLES)
columns = sorted(f for f in FACETS)
matrix = [[dict(incidence(c)).get(r, 0) for c in columns]
          for r in UNIT_MINOR_TRIANGLES]

def bareiss_det(A):
    A = [list(row) for row in A]
    n = len(A)
    previous = 1
    sign = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            j = next(j for j in range(k + 1, n) if A[j][k] != 0)
            A[k], A[j] = A[j], A[k]
            sign *= -1
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                value = A[i][j] * pivot - A[i][k] * A[k][j]
                assert value % previous == 0
                A[i][j] = value // previous
            A[i][k] = 0
        previous = pivot
    return sign * A[-1][-1]

assert bareiss_det(matrix) == 1
print("Integral boundary", "26x26 minor", "determinant", 1)


# The opposite-edge orbit is intrinsic: such edges belong to two squares,
# whereas each rim edge belongs to one. Hence Aut(W) is exactly dihedral.
fourcycles = [set(s) for s in combinations(range(N), 4)
              if len([e for e in EDGES if e <= set(s)]) == 4
              and all(sum(v in e for e in EDGES if e <= set(s)) == 2 for v in s)]
assert len(fourcycles) == 4
for e in EDGES:
    number = sum(e <= f for f in fourcycles)
    chord = set(e) == {min(e), (min(e) + 4) % N}
    # chord detection independent of endpoint orientation
    chord = (max(e) - min(e) == 4)
    assert number == (2 if chord else 1)
print("Intrinsic edge orbits", "eight rim edges", "four chords", "four squares")


# Independent mod-2 simplicial chain ranks.
def rank_gf2(dimension):
    rows = sorted(x for x in NONEMPTY if x.bit_count() == dimension)
    columns = sorted(x for x in NONEMPTY if x.bit_count() == dimension + 1)
    index = {x: i for i, x in enumerate(rows)}
    pivots = {}
    for col in columns:
        v = 0
        for a, _ in incidence(col):
            v ^= (1 << index[a])
        while v:
            top = v.bit_length() - 1
            if top in pivots:
                v ^= pivots[top]
            else:
                pivots[top] = v
                break
    return len(pivots)

ranks = [rank_gf2(k) for k in (1, 2, 3)]
assert ranks == [7, 21, 26]
assert COUNTS[2] - ranks[1] - ranks[2] == 1
print("Boundary GF2 ranks", ranks)


# Dihedral automorphism action via signed simplicial Hopf traces.
def trace_h2(permutation):
    trace = -1  # subtract H_0
    for face in NONEMPTY:
        vertices = [i for i in range(N) if face >> i & 1]
        images = [permutation[i] for i in vertices]
        if set(images) == set(vertices):
            inversions = sum(images[i] > images[j]
                             for i in range(len(images)) for j in range(i + 1, len(images)))
            trace += (-1 if (len(vertices) - 1 + inversions) % 2 else 1)
    return trace

for k in range(8):
    rotation = [(i + k) % N for i in range(N)]
    reflection = [(k - i) % N for i in range(N)]
    for name, p, expected in (("rotation", rotation, (-1) ** k),
                              ("reflection", reflection, (-1) ** (k + 1))):
        assert {frozenset((p[u], p[v])) for u, v in (tuple(e) for e in EDGES)} == EDGES
        value = trace_h2(p)
        assert value == expected, (k, name, value, expected)
print("Dihedral character", "16 exact signed traces verified", "r=-1", "s=-1")
print("WAGNER_FOURCUT_SPHERE_CHARACTER_VERIFIED")
