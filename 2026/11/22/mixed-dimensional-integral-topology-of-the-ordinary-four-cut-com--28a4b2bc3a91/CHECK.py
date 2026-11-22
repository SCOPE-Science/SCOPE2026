"""Exact, self-contained Morse certificate for the ordinary four-cut complex of H(3,3).
Run: python3 CHECK.py. Python standard library only.

A dual simplex is a vertex set all of whose four-subsets induce a connected graph.
The 0-, 1-, and 2-simplices are therefore ALL vertex subsets of these sizes.
A lexicographic vertex-toggle acyclic matching gives a two-term Morse chain complex.
The signed Morse boundary is computed recursively, not only over a finite field.
"""
from itertools import combinations, product
from collections import defaultdict, deque
from functools import lru_cache
from fractions import Fraction

VERTICES = list(product(range(3), repeat=3))
N = len(VERTICES)
ADJ = [frozenset(j for j, y in enumerate(VERTICES)
                if sum(a != b for a, b in zip(x, y)) == 1)
       for x in VERTICES]

def connected_four(s):
    reached = {s[0]}
    while True:
        nxt = reached | {z for a in reached for z in s if z in ADJ[a]}
        if nxt == reached:
            return len(reached) == 4
        reached = nxt

# D is the combinatorial Alexander dual on all 27 vertices.
F = [set() for _ in range(8)]
for k in range(1, 4):
    F[k] = set(combinations(range(N), k))
F[4] = {t for t in combinations(range(N), 4) if connected_four(t)}
# Candidate higher faces arise only by extending an existing face, and each of
# their codimension-one faces must be present (a complete inductive criterion).
for k in (5, 6, 7):
    for old in F[k-1]:
        for j in range(old[-1]+1, N):
            t = old + (j,)
            if all(t[:i] + t[i+1:] in F[k-1] for i in range(k)):
                F[k].add(t)
SIZES = tuple(len(F[k]) for k in range(1, 8))
assert SIZES == (27, 351, 2925, 1593, 324, 54, 0), SIZES
assert all((t[:i] + t[i+1:] in F[len(t)-1] for i in range(len(t)))
           for k in range(2,7) for t in F[k])

# Match faces with opposite occupancy of each vertex, processing 0,...,26.
# Each stage is a matching on still-unmatched faces.
remaining = set().union(*(F[k] for k in range(1,7)))
pairs = []
for v in range(N):
    current = [(s, tuple(sorted(s + (v,)))) for s in remaining if v not in s
               and tuple(sorted(s + (v,))) in remaining]
    for s,t in current:
        assert s in remaining and t in remaining
        remaining.remove(s)
        remaining.remove(t)
    pairs.extend(current)

pair_sizes = tuple(sum(len(s)==k for s,t in pairs) for k in range(1,6))
assert pair_sizes == (26,325,1202,270,54), pair_sizes
crit0 = sorted(s for s in remaining if len(s)==1)
crit2 = sorted(s for s in remaining if len(s)==3)
crit3 = sorted(s for s in remaining if len(s)==4)
assert (len(crit0),len(crit2),len(crit3),len(remaining)) == (1,1398,121,1520)

# Check that reversing the matched downward arcs of the Hasse diagram
# produces an acyclic directed graph, on every face in the dual.
matched = set(pairs)
allfaces = set().union(*(F[k] for k in range(1,7)))
indeg = {s:0 for s in allfaces}
out = defaultdict(list)
num_cover = 0
for k in range(2,7):
    for upper in F[k]:
        for i in range(k):
            lower = upper[:i]+upper[i+1:]
            if (lower,upper) in matched:
                a,b = lower,upper
            else:
                a,b = upper,lower
            out[a].append(b)
            indeg[b] += 1
            num_cover += 1
q = deque(x for x in allfaces if indeg[x]==0)
visited = 0
while q:
    a = q.popleft()
    visited += 1
    for b in out[a]:
        indeg[b]-=1
        if indeg[b]==0:q.append(b)
assert visited==len(allfaces), (visited,len(allfaces))

# This boundary reduction follows integer Morse gradient paths.  For a
# matched 2-simplex f <= g (a 3-simplex), eliminate f from the boundary
# of g, with the signed incidence coefficient ±1.  Boundaries of upper
# 2-simplices paired against 1-simplices contribute nothing to C^M_2.
paired_lower_2 = {s:t for s,t in pairs if len(s)==3}
paired_upper_2 = {t for s,t in pairs if len(s)==2}
critical_2_set = set(crit2)

@lru_cache(None)
def reduce_2(f):
    if f in critical_2_set:
        return {f:1}
    if f in paired_upper_2:
        return {}
    g = paired_lower_2[f]
    pivot = (-1)**next(i for i in range(4) if g[:i]+g[i+1:] == f)
    reduced = defaultdict(int)
    for i in range(4):
        boundary_face = g[:i] + g[i+1:]
        if boundary_face == f:
            continue
        sign = -pivot * ((-1)**i)
        for h, c in reduce_2(boundary_face).items():
            reduced[h] += sign*c
    return {h:c for h,c in reduced.items() if c}

morse_columns = []
for sigma in crit3:
    coeffs = defaultdict(int)
    for i in range(4):
        for f,c in reduce_2(sigma[:i]+sigma[i+1:]).items():
            coeffs[f] += (-1)**i*c
    morse_columns.append({f:c for f,c in coeffs.items() if c})

assert len(morse_columns)==121
assert sum(len(col) for col in morse_columns)==264
assert all(abs(v)==1 for col in morse_columns for v in col.values())
assert sum(bool(col) for col in morse_columns)==84
active_rows = sorted({f for col in morse_columns for f in col})
assert len(active_rows)==24

# Rational row reduction yields an UPPER bound on the integral rank (and
# its exact rational rank).  All coefficients are represented as Fractions.
row_index = {f:i for i,f in enumerate(active_rows)}
row_basis = {}
for col in morse_columns:
    vec = {row_index[f]:Fraction(c) for f,c in col.items()}
    while vec:
        p = min(vec)
        if p not in row_basis:
            pivot = vec[p]
            row_basis[p] = {r:x/pivot for r,x in vec.items()}
            break
        factor = vec[p]
        for r,x in row_basis[p].items():
            val = vec.get(r,Fraction(0)) - factor*x
            if val:vec[r]=val
            else:vec.pop(r,None)
assert len(row_basis)==12, len(row_basis)

# Exact integer primitive-minor certificate: these particular 12 columns
# and 12 rows have determinant -1, so all Smith nonzero factors are 1.
SELECTED_COLUMNS = [0,1,2,3,4,5,19,20,21,22,23,24]
SELECTED_ROWS = [
    (1,2,13),(1,2,16),(1,2,22),(1,2,25),
    (1,12,13),(1,15,16),(1,21,22),(1,24,25),
    (2,12,14),(2,15,17),(2,21,23),(2,24,26)
]

def determinant_bareiss(M):
    a = [row[:] for row in M]
    n = len(a)
    sign = 1
    previous = 1
    for k in range(n-1):
        if a[k][k]==0:
            i = next((i for i in range(k+1,n) if a[i][k]!=0),None)
            if i is None:return 0
            a[k],a[i]=a[i],a[k]
            sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator = a[i][j]*p - a[i][k]*a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator//previous
            a[i][k]=0
        previous=p
    return sign*a[n-1][n-1]
minor = [[morse_columns[j].get(f,0) for j in SELECTED_COLUMNS] for f in SELECTED_ROWS]
assert determinant_bareiss(minor)==-1
# Smith rank 12 with determinant-one rank-12 minor implies that torsion
# invariants (whose product is gcd of all maximal minors) are all 1.
rank = len(row_basis)
beta2 = len(crit2)-rank
beta3 = len(crit3)-rank
assert (beta2,beta3)==(1386,109)
# reduced Euler characteristic of dual computed independently from all faces
reduced_euler = sum((-1)**(k-1)*len(F[k]) for k in range(1,7))-1
assert reduced_euler == beta2-beta3 == 1277
assert N-4-1 == 22       # original ordinary four-cut facet dimension
assert N-3-2 == 22 and N-3-3 == 21  # combinatorial duality degrees
# Independent mod-two simplicial chain computation on the uncollapsed dual.
# This is only a corroborating check: integral torsion-freeness uses the unit minor.
def rank_mod2(columns):
    basis = {}
    for vector in columns:
        while vector:
            pivot = vector.bit_length()-1
            if pivot in basis:
                vector ^= basis[pivot]
            else:
                basis[pivot] = vector
                break
    return len(basis)
raw_ranks = []
for k in range(2,7):
    lower_idx = {face:i for i,face in enumerate(sorted(F[k-1]))}
    columns = (sum(1 << lower_idx[t[:i]+t[i+1:]] for i in range(k))
               for t in sorted(F[k]))
    raw_ranks.append(rank_mod2(columns))
assert tuple(raw_ranks) == (26, 325, 1214, 270, 54), raw_ranks
# Here k=2 (edges -> vertices) has rank 26; k=3 (triangles -> edges) 325.
print('raw_mod2_boundary_ranks',tuple(raw_ranks))
print('dual_face_counts',SIZES)
print('paired_lower_dimensions',pair_sizes)
print('acyclic_hasse',visited,'faces',num_cover,'cover_relations')
print('critical_faces',len(crit0),len(crit2),len(crit3))
print('morse_boundary_nonzeros',sum(map(len,morse_columns)),'rational_rank',rank,'unit_minor_det',-1)
print('dual_integral_betti_H2_H3',beta2,beta3)
print('four_cut_integral_betti_H21_H22',beta3,beta2)
print('ALL CHECKS PASSED')
