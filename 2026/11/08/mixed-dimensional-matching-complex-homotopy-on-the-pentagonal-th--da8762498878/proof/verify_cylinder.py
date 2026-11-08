#!/usr/bin/env python3
"""Finite exact certificate for the matching complex of P_3 square C_5.

Requires Python 3 and SymPy.  Run: python3 proof/verify_cylinder.py
All simplex orientations are induced by the deterministic edge order below.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

N = 5
VERTICES = tuple((row, col) for row in range(3) for col in range(N))
VERTEX_INDEX = {v: i for i, v in enumerate(VERTICES)}
EDGES = []
for row in range(3):
    for col in range(N):
        if row < 2:
            EDGES.append(((row, col), (row + 1, col)))
        EDGES.append(((row, col), (row, (col + 1) % N)))
assert len(EDGES) == 25 and len(set(frozenset(e) for e in EDGES)) == 25
EDGE_OCC = [sum(1 << VERTEX_INDEX[v] for v in edge) for edge in EDGES]

# Explicit exhaustive branching on whether each edge is selected.
FACES = []
def enumerate_faces(i, occupied, simplex):
    if i == len(EDGES):
        FACES.append(simplex)
        return
    enumerate_faces(i + 1, occupied, simplex)
    if (occupied & EDGE_OCC[i]) == 0:
        enumerate_faces(i + 1, occupied | EDGE_OCC[i], simplex | (1 << i))
enumerate_faces(0, 0, 0)
assert len(FACES) == len(set(FACES))
FACE_SET = set(FACES)
F_VECTOR_AUGMENTED = Counter(s.bit_count() for s in FACES)
assert [F_VECTOR_AUGMENTED[i] for i in range(8)] == [1,25,240,1125,2710,3227,1645,240]

# Staged elementary toggle matching.  Each face is matched at most once.
REMAINING = FACE_SET.copy()
PAIRS = []
for pivot in range(len(EDGES)):
    local_pairs = [(s, s | (1 << pivot)) for s in sorted(REMAINING)
                   if not ((s >> pivot) & 1) and (s | (1 << pivot)) in REMAINING]
    for low, high in local_pairs:
        assert low in REMAINING and high in REMAINING
        REMAINING.remove(low)
        REMAINING.remove(high)
    PAIRS.extend(local_pairs)
UP = dict(PAIRS)
DOWN = {high: low for low, high in PAIRS}
assert len(UP) == len(DOWN) == len(PAIRS) == 4586
assert len(REMAINING) == 41
assert Counter(x.bit_count() - 1 for x in REMAINING) == {4:31, 5:10}
assert 0 in UP and 0 not in DOWN  # augmented empty face is matched upward

# Check the ENTIRE oriented augmented Hasse graph is acyclic.  Ordinary
# discrete Morse matching replaces the empty--vertex pair by one critical vertex.
INDEGREE = {u:0 for u in FACES}
ADJ = {u:[] for u in FACES}
INCIDENCES = 0
for high in FACES:
    for bit in range(len(EDGES)):
        if not (high >> bit) & 1:
            continue
        low = high ^ (1 << bit)
        assert low in FACE_SET
        if UP.get(low) == high:
            source, target = high, low
        else:
            source, target = low, high
        ADJ[source].append(target)
        INDEGREE[target] += 1
        INCIDENCES += 1
q = deque([u for u in FACES if INDEGREE[u] == 0])
processed = 0
while q:
    s = q.popleft(); processed += 1
    for w in ADJ[s]:
        INDEGREE[w] -= 1
        if INDEGREE[w] == 0:
            q.append(w)
assert processed == len(FACES), (processed, len(FACES))

# Signed simplicial boundary of an oriented simplex, in the fixed edge order.
def facets_with_sign(s):
    original=s
    j=0
    while s:
        b=s & -s
        yield original ^ b, (-1 if j%2 else 1)
        s ^= b
        j += 1

# Algebraic Morse reduction of a cell in each degree.  The recursion is
# well-founded by the preceding acyclicity certificate; all signs are integral.
@lru_cache(maxsize=None)
def morse_projection(s):
    if s in REMAINING:
        return {s:1}
    if s in DOWN:
        return {}
    high = UP[s]
    faces = dict(facets_with_sign(high))
    incidence = faces[s]  # precisely +1 or -1
    output = defaultdict(int)
    for t, a in faces.items():
        if t == s:
            continue
        for z,b in morse_projection(t).items():
            output[z] -= incidence*a*b
    return {z:c for z,c in output.items() if c}

CRITICAL_FIVE = sorted(s for s in REMAINING if s.bit_count() == 6)
CRITICAL_FOUR = sorted(s for s in REMAINING if s.bit_count() == 5)
BOUNDARY_MATRIX = []
for s in CRITICAL_FIVE:
    ans = defaultdict(int)
    for t,a in facets_with_sign(s):
        for z,b in morse_projection(t).items():
            ans[z] += a*b
    BOUNDARY_MATRIX.append({z:c for z,c in ans.items() if c})
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
MORSE_BOUNDARY = Matrix([[col.get(s,0) for col in BOUNDARY_MATRIX] for s in CRITICAL_FOUR])
SMITH = smith_normal_form(MORSE_BOUNDARY, domain=ZZ)
SMITH_DIAGONAL = [int(SMITH[i,i]) for i in range(min(SMITH.rows,SMITH.cols)) if SMITH[i,i]]
print("SMITH_DIAGONAL",SMITH_DIAGONAL)
assert [abs(x) for x in SMITH_DIAGONAL] == [1]*7

# Independent mod-two elimination on ORIGINAL simplicial boundary matrices.
FACETS_BY_CARD = [[s for s in FACES if s.bit_count() == k] for k in range(8)]
def rank_mod_two(k):
    # Boundary C_k --> C_{k-1}, where C_k has k+1 selected graph edges.
    if k <= 0:
        return 0
    target = {s:j for j,s in enumerate(FACETS_BY_CARD[k])}
    basis = {}
    for cell in FACETS_BY_CARD[k+1]:
        col = 0
        for face,sgn in facets_with_sign(cell):
            col ^= 1 << target[face]
        while col:
            b=col.bit_length()-1
            if b in basis:
                col ^= basis[b]
            else:
                basis[b]=col
                break
    return len(basis)
RANKS = [rank_mod_two(k) for k in range(7)]
REDUCED_BETTI = {}
for dim in range(1,7):
    b = F_VECTOR_AUGMENTED[dim+1] - RANKS[dim] - (RANKS[dim+1] if dim+1<7 else 0)
    REDUCED_BETTI[dim] = b
assert [REDUCED_BETTI[k] for k in range(1,7)] == [0,0,0,24,3,0], REDUCED_BETTI
assert sum(((-1)**(k-1))*F_VECTOR_AUGMENTED[k] for k in range(8)) == 21
print('GRAPH_VERTICES',len(VERTICES))
print('GRAPH_EDGES',len(EDGES))
print('FACES_INCLUDING_EMPTY',len(FACES))
print('AUGMENTED_F_VECTOR', [F_VECTOR_AUGMENTED[i] for i in range(8)])
print('MATCHED_PAIRS',len(PAIRS))
print('HASSE_INCIDENCES',INCIDENCES)
print('ACYCLIC_ORIENTED_HASSE',processed)
print('CRITICAL_4_5',len(CRITICAL_FOUR),len(CRITICAL_FIVE))
print('SIGNED_INTEGRAL_MORSE_BOUNDARY_5_TO_4',SMITH_DIAGONAL)
print('MOD2_BOUNDARY_RANKS_DIM_0_TO_6',RANKS)
print('MOD2_REDUCED_BETTI_DIM_1_TO_6',[REDUCED_BETTI[k] for k in range(1,7)])
print('ALL_VERIFY_OK')
