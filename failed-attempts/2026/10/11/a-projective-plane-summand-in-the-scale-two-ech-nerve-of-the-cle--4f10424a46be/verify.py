#!/usr/bin/env python3
"""Finite exact verification of the Clebsch graph scale-two Cech nerve.
All computations use integer and finite-field arithmetic and explicit bitsets.
Python 3 standard library only; no file inputs are required.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from math import gcd

N = 16
GENERATORS = (1, 2, 4, 8, 15)
NEIGHBORS = {v: {v ^ g for g in GENERATORS} for v in range(N)}
assert all(len(NEIGHBORS[v]) == 5 for v in range(N))
assert all(u in NEIGHBORS[v] for v in range(N) for u in NEIGHBORS[v])
for u in range(N):
    for v in range(u + 1, N):
        assert len(NEIGHBORS[u] & NEIGHBORS[v]) == (0 if v in NEIGHBORS[u] else 2)

FACETS = [sum(1 << v for v in ({c} | NEIGHBORS[c])) for c in range(N)]
assert len(set(FACETS)) == N
assert all(f.bit_count() == 6 for f in FACETS)
FACES = {0}
for facet in FACETS:
    sigma = facet
    while sigma:
        FACES.add(sigma)
        sigma = (sigma - 1) & facet
assert len(FACES) == 809
assert Counter(s.bit_count()-1 for s in FACES if s) == {0:16, 1:120, 2:320, 3:240, 4:96, 5:16}

def boundary(simplex):
    vertices = [v for v in range(N) if (simplex >> v) & 1]
    return {simplex ^ (1 << v): (1 if i % 2 == 0 else -1)
            for i, v in enumerate(vertices)}

# Sequential vertex toggles are a completely determined matching.
UNMATCHED = set(FACES)
PAIRS = []
STAGE_SIZES = []
for v in range(N):
    count = 0
    for a in sorted(UNMATCHED):
        b = a | (1 << v)
        if not ((a >> v) & 1) and b in UNMATCHED:
            PAIRS.append((a,b))
            UNMATCHED.remove(a)
            UNMATCHED.remove(b)
            count += 1
    STAGE_SIZES.append(count)
assert sum(STAGE_SIZES) == len(PAIRS) == 376
assert (0, 1) in PAIRS
assert Counter(f.bit_count()-1 for f in UNMATCHED) == {1:1, 2:56}
CRITICAL_EDGE = next(f for f in UNMATCHED if f.bit_count() == 2)
assert CRITICAL_EDGE == 0x42
CRITICAL_TRIANGLES = sorted(f for f in UNMATCHED if f.bit_count() == 3)

# Kahn's algorithm exhaustively verifies Forman acyclicity on the full
# augmented face poset, not just the number of matched pairs.
MATCHING = set(PAIRS)
H = {f: [] for f in FACES}
DEGREE_IN = {f: 0 for f in FACES}
incidences = 0
for high in FACES:
    for low in boundary(high):
        assert low in FACES
        if (low, high) in MATCHING:
            source,target = low,high
        else:
            source,target = high,low
        H[source].append(target)
        DEGREE_IN[target] += 1
        incidences += 1
assert incidences == 2752
q = deque(f for f in FACES if DEGREE_IN[f] == 0)
visited = 0
while q:
    f = q.popleft()
    visited += 1
    for neighbor in H[f]:
        DEGREE_IN[neighbor] -= 1
        if DEGREE_IN[neighbor] == 0:
            q.append(neighbor)
assert visited == len(FACES), "The matching must be acyclic"

# Gradient-path method for the reduced integer Morse d_2. A 1-simplex
# matched down to a vertex disappears. A 1-simplex matched up to a
# triangle is replaced by the signed sum of the other triangle edges.
LOW_TO_HIGH = {a:b for a,b in PAIRS}
HIGH_TO_LOW = {b:a for a,b in PAIRS}
@lru_cache(None)
def edge_projection(edge):
    assert edge.bit_count() == 2
    if edge == CRITICAL_EDGE:
        return 1
    if edge in HIGH_TO_LOW:      # edge is the upper member of (vertex, edge)
        assert HIGH_TO_LOW[edge].bit_count() == 1
        return 0
    triangle = LOW_TO_HIGH[edge]
    assert triangle.bit_count() == 3
    bd = boundary(triangle)
    return -sum(coef * edge_projection(e) for e,coef in bd.items() if e != edge) * bd[edge]
COEFFICIENTS = [sum(sign * edge_projection(e) for e,sign in boundary(t).items())
                for t in CRITICAL_TRIANGLES]
assert Counter(COEFFICIENTS) == {0:44, -2:6, 2:6}, Counter(COEFFICIENTS)
assert gcd(*COEFFICIENTS) == 2

# Separate algebraic chain-cancellation route, independent of the
# recursion used above. Cancels 376 unit boundary pivots in the integral
# reduced simplicial chain complex, respecting exact signed faces.
ACTIVE = set(FACES)
DIFFERENTIAL = {f: boundary(f) for f in FACES}
for low,high in PAIRS:
    pivot = DIFFERENTIAL[high].get(low,0)
    assert abs(pivot)==1, (low,high,pivot)
    for f in list(ACTIVE):
        if f == low or f == high or f.bit_count()!=high.bit_count():
            continue
        c = DIFFERENTIAL[f].get(low,0)
        if c:
            for target,value in DIFFERENTIAL[high].items():
                DIFFERENTIAL[f][target] = DIFFERENTIAL[f].get(target,0) - c*pivot*value
                if not DIFFERENTIAL[f][target]:
                    del DIFFERENTIAL[f][target]
    for f in ACTIVE:
        if f != low and f != high:
            DIFFERENTIAL[f].pop(low,None)
            DIFFERENTIAL[f].pop(high,None)
    ACTIVE.remove(low)
    ACTIVE.remove(high)
assert ACTIVE == UNMATCHED
assert [DIFFERENTIAL[t].get(CRITICAL_EDGE,0) for t in CRITICAL_TRIANGLES] == COEFFICIENTS
assert all(set(DIFFERENTIAL[f]).issubset(ACTIVE) for f in ACTIVE)

# Independent finite-field simplicial ranks, in dimensions 1..5.
def rank_mod_prime(dim,p):
    # Columns are the simplicial boundaries in dimension dim.
    pivots = {}
    for face in sorted(f for f in FACES if f.bit_count() == dim+1):
        col = {key: (val%p) for key,val in boundary(face).items()}
        col = {k:v for k,v in col.items() if v}
        while col:
            lead = min(col)
            if lead not in pivots:
                inv = pow(col[lead], -1, p)
                pivots[lead] = {k: (inv*v)%p for k,v in col.items()}
                break
            factor = col[lead]
            for key,value in pivots[lead].items():
                col[key] = (col.get(key,0) - factor*value)%p
            col = {k:v for k,v in col.items() if v}
    return len(pivots)
RANKS_2 = [rank_mod_prime(i,2) for i in range(1,6)]
RANKS_3 = [rank_mod_prime(i,3) for i in range(1,6)]
assert RANKS_2 == [15,104,160,80,16], RANKS_2
assert RANKS_3 == [15,105,160,80,16], RANKS_3
assert all(i==0 or i==2 or i==-2 for i in COEFFICIENTS)

print('VERIFY_OK')
print('degree=5; graph_parameters=(16,5,0,2); facets=16')
print('f_vector=(16,120,320,240,96,16); faces_with_empty=809')
print('matching_pairs=376; stage_sizes='+str(STAGE_SIZES))
print('hasse_incidences=2752; directed_acyclic=yes')
print('reduced_critical_faces=(1 edge,56 triangles); edge=0x42')
print('morse_boundary_coefficients='+str(COEFFICIENTS))
print('morse_d2_coefficient_counts='+str(dict(Counter(COEFFICIENTS))))
print('gcd_morse_d2=2; homotopy_type=RP2_vee_55_S2')
print('boundary_ranks_mod2='+str(RANKS_2))
print('boundary_ranks_mod3='+str(RANKS_3))
