#!/usr/bin/env python3
"""Exact finite certificate for the six-point triangular-graph general-position complex.

Pure Python 3, no external dependencies. Every check regenerates data from definitions.
Run: python3 verify.py
"""
from collections import Counter, defaultdict
from itertools import combinations
import heapq

N = 6
PAIRS = tuple(combinations(range(N), 2))
V = len(PAIRS)
assert V == 15

def all_bits(mask):
    while mask:
        b = mask & -mask
        yield b
        mask ^= b

def vertices(mask):
    return tuple(b.bit_length()-1 for b in all_bits(mask))

# Adjacent graph vertices correspond to intersecting source edges.
adj = tuple(tuple(i != j and bool(set(PAIRS[i]) & set(PAIRS[j]))
                  for j in range(V)) for i in range(V))
# This graph has diameter two. Compare a shortest-path definition with
# the forbidden induced-P3 definition on every unordered triple.
dist = [[99] * V for _ in range(V)]
for i in range(V):
    dist[i][i] = 0
    for j in range(V):
        if adj[i][j]:
            dist[i][j] = 1
for k in range(V):
    for i in range(V):
        for j in range(V):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
assert max(map(max, dist)) == 2
bad_triples = []
for i,j,k in combinations(range(V), 3):
    bad_geo = (dist[i][j] == dist[i][k]+dist[k][j] or
               dist[i][k] == dist[i][j]+dist[j][k] or
               dist[j][k] == dist[j][i]+dist[i][k])
    bad_p3 = (int(adj[i][j]) + int(adj[i][k]) + int(adj[j][k]) == 2)
    assert bad_geo == bad_p3
    if bad_geo:
        bad_triples.append((1<<i)|(1<<j)|(1<<k))
assert len(bad_triples) == 180

# Independent face predicate: induced connected components must be cliques.
def cluster_pred(mask):
    nodes = set(vertices(mask))
    while nodes:
        u = min(nodes)
        stack = [u]
        component = {u}
        nodes.remove(u)
        while stack:
            x = stack.pop()
            for y in sorted(nodes):
                if adj[x][y]:
                    nodes.remove(y); component.add(y); stack.append(y)
        if any(not adj[a][b] for a,b in combinations(sorted(component), 2)):
            return False
    return True

# Dynamic face enumeration avoids using the cluster criterion.
valid = bytearray(1<<V)
valid[0] = 1
for m in range(1, 1<<V):
    lb = m & -m
    valid[m] = int(bool(valid[m^lb]) and not any(
        (b & lb) and (m & b) == b for b in bad_triples))
    assert bool(valid[m]) == cluster_pred(m)
F = defaultdict(list)
for m,ok in enumerate(valid):
    if ok and m:
        F[m.bit_count()-1].append(m)
assert [len(F[k]) for k in range(6)] == [15,105,275,240,66,10]
assert sum(map(len,F.values())) == 711
facets = Counter(m.bit_count() for d,faces in F.items() for m in faces
                 if not any((not (m&(1<<i))) and valid[m|(1<<i)] for i in range(V)))
assert facets == Counter({3:15,4:60,5:6,6:10})

# Exhaustive elementary simplicial collapses: f has exactly one
# immediate surviving coface g, and therefore g is its only coface.
present = set().union(*F.values())
cof = {m: [] for m in present}
for m in present:
    for b in all_bits(m):
        f = m^b
        if f:
            cof[f].append(m)
deg = {m: len(cof[m]) for m in present}
h = []
for m in present:
    if deg[m] == 1:
        heapq.heappush(h, (1-m.bit_count(),m))
collapses = []
while h:
    _,f = heapq.heappop(h)
    if f not in present or deg[f] != 1:
        continue
    upper = [g for g in cof[f] if g in present]
    assert len(upper) == 1
    g = upper[0]
    assert g.bit_count() == f.bit_count() + 1 and (g&f) == f
    collapses.append((f,g))
    present.remove(f)
    present.remove(g)
    for x in (f,g):
        for b in all_bits(x):
            y = x^b
            if y and y in present:
                deg[y] -= 1
                if deg[y] == 1:
                    heapq.heappush(h, (1-y.bit_count(),y))
assert len(collapses) == 76
assert Counter((f.bit_count()-1,g.bit_count()-1) for f,g in collapses) == Counter({(4,5):10,(3,4):56,(2,3):10})
R = {d: sorted(m for m in present if m.bit_count() == d+1) for d in range(4)}
assert [len(R[d]) for d in range(4)] == [15,105,265,174]

# Van Kampen after contracting the star spanning tree of the complete 1-skeleton.
# Each recorded triangle kills exactly one remaining edge generator; its
# other two boundary edges have already been killed.
all_edges = set(R[1])
killed = {m for m in all_edges if m & 1}
assert len(killed) == 14
kill_cert = []
while True:
    choice = None
    for t in R[2]:
        boundary = tuple(t^b for b in all_bits(t))
        remaining = [e for e in boundary if e not in killed]
        if len(remaining) == 1:
            choice = (remaining[0],t,boundary)
            break
    if choice is None:
        break
    e,t,boundary = choice
    assert e not in killed and all(x in killed for x in boundary if x != e)
    kill_cert.append((e,t))
    killed.add(e)
assert killed == all_edges and len(kill_cert) == 91

# Exact Z-matrix of the third boundary after elementary collapses.
rows = {f:i for i,f in enumerate(R[2])}
columns = []
for m in R[3]:
    signed = {rows[m^b]:(-1)**i for i,b in enumerate(all_bits(m))}
    assert len(signed) == 4
    columns.append(signed)

# Integral unit-pivot Smith elimination. Every Schur update below is
# an integer row/column unimodular transformation; each pivot is +1 or -1.
# The remaining matrix must be identically zero to certify the rank.
C = {j: dict(c) for j,c in enumerate(columns)}
ROW = {i:{} for i in range(len(R[2]))}
for j,c in C.items():
    for i,a in c.items():
        ROW[i][j] = a
unit_pivots = 0
max_abs = 1
while True:
    candidates = []
    for j,c in C.items():
        for i,a in c.items():
            if abs(a)==1:
                candidates.append(((len(c)-1)*(len(ROW[i])-1),len(c)+len(ROW[i]),j,i,a))
    if not candidates: break
    _,_,j,i,v = min(candidates)
    assert abs(v)==1
    for k,a in list(ROW[i].items()):
        if k==j:continue
        for row,b in list(C[j].items()):
            if row==i:continue
            z = C[k].get(row,0)-a*v*b
            if z:
                C[k][row] = z
                ROW[row][k] = z
                max_abs = max(max_abs,abs(z))
            else:
                C[k].pop(row,None)
                ROW[row].pop(k,None)
        del C[k][i]
    for row in C[j]:
        if row != i: ROW[row].pop(j,None)
    del C[j]
    del ROW[i]
    unit_pivots += 1
assert unit_pivots == 159 and len(C)==15
assert all(not c for c in C.values())
assert max_abs == 1

# Separate mod-2 rank computation on original (uncollapsed) chains.
def gf2_rank(cols):
    piv = {}
    for v in cols:
        while v:
            k = v.bit_length()-1
            if k in piv:v ^= piv[k]
            else:piv[k] = v;break
    return len(piv)
ranks = {}
for d in range(1,6):
    lower = {m:i for i,m in enumerate(F[d-1])}
    vecs = []
    for m in F[d]:
        z = 0
        for b in all_bits(m): z ^= (1<<lower[m^b])
        vecs.append(z)
    ranks[d] = gf2_rank(vecs)
assert tuple(ranks[d] for d in range(1,6)) == (14,91,169,56,10)
assert [len(F[d])-ranks.get(d,0)-ranks.get(d+1,0)-(d==0) for d in range(6)] == [0,0,15,15,0,0]

# The 91 triangular relations kill pi_1, and unimodular Smith reduction
# certifies H_2=Z^15, H_3=Z^15. A simply connected 3-CW complex with
# free homology in degrees 2,3 is a wedge of 2- and 3-spheres.
assert len(R[2])-91-unit_pivots == 15
assert len(R[3])-unit_pivots == 15
print('PASS: 15 vertices; 180 forbidden triples; 711 nonempty faces')
print('PASS: 76 elementary collapses to (15,105,265,174)')
print('PASS: 91 triangular relators kill all edge generators; pi_1=1')
print('PASS: third boundary has 159 unit Smith pivots, zero residual, max |a|=1')
print('PASS: independent GF(2) chain ranks (14,91,169,56,10)')
print('CHECKED by exact finite reductions: homotopy type wedge of 15 S^2 and 15 S^3')
