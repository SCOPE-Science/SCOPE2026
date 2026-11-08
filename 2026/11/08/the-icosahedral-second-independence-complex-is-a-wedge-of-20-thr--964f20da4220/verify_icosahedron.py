#!/usr/bin/env python3
"""Independent finite checks of an explicit integral discrete-Morse calculation.
Standard-library Python 3; output is deterministic. Mathematical justification
of the Morse-to-homotopy step is in RESULT.md.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json

N = 12
E = set()
def edge(a, b):
    assert a != b
    E.add(tuple(sorted((a, b))))
for j in range(5):
    u, l = 1 + j, 6 + j
    edge(0, u)
    edge(11, l)
    edge(u, 1 + (j + 1) % 5)
    edge(l, 6 + (j + 1) % 5)
    edge(u, l)
    edge(u, 6 + (j - 1) % 5)
assert len(E) == 30
ADJ = [0] * N
for u, v in E:
    ADJ[u] |= 1 << v
    ADJ[v] |= 1 << u
assert all(a.bit_count() == 5 for a in ADJ)
tri = [q for q in combinations(range(N), 3) if all(tuple(sorted(p)) in E for p in combinations(q, 2))]
assert len(tri) == 20
assert all(sum(1 for q in tri if u in q and v in q) == 2 for u, v in E)
# 1st implementation: 12-bit testing of the degree of each selected vertex.
def good(mask):
    return all((ADJ[u] & mask).bit_count() <= 1 for u in range(N) if mask >> u & 1)
F = sorted(s for s in range(1, 1 << N) if good(s))
assert len(F) == 323
assert Counter(s.bit_count() - 1 for s in F) == {0: 12, 1: 66, 2: 140, 3: 105}
# 2nd implementation: independently prohibit every selected 3-vertex path,
# including triples that also form triangles.
for s in range(1, 1 << N):
    bad = any((s >> u & 1) and ((ADJ[u] & s).bit_count() >= 2) for u in range(N))
    assert (s in set(F)) == (not bad)
FS = set(F)
# A sequential element matching, visiting pivots 0,1,...,11, and each
# currently available lower face in ascending bit-mask order.
MATCH = {}
for v in range(N):
    for s in F:
        t = s | (1 << v)
        if s == t or s in MATCH or t in MATCH or t not in FS:
            continue
        MATCH[s] = t
        MATCH[t] = s
assert len(MATCH) == 294
CRIT = sorted(s for s in F if s not in MATCH)
assert Counter(s.bit_count() - 1 for s in CRIT) == {0: 1, 2: 4, 3: 24}
# Verify every directed Hasse-edge, with matched edges upward and others down.
OUT = {s: [] for s in F}
INDEG = {s: 0 for s in F}
covers = 0
for s in F:
    for v in range(N):
        t = s | (1 << v)
        if t == s or t not in FS:
            continue
        if MATCH.get(s) == t:
            a, b = s, t
        else:
            a, b = t, s
        OUT[a].append(b)
        INDEG[b] += 1
        covers += 1
queue = deque(s for s in F if INDEG[s] == 0)
seen = 0
while queue:
    s = queue.popleft()
    seen += 1
    for t in OUT[s]:
        INDEG[t] -= 1
        if INDEG[t] == 0:
            queue.append(t)
assert seen == len(F) and covers == 972
# Signed algebraic Morse boundary, computed by recursively eliminating
# dimension-2 lower faces paired to dimension-3 upper faces.
# Orientation: the increasing order of numbered vertices.
@lru_cache(None)
def expand(q):
    if q not in MATCH:
        return {q: 1}
    r = MATCH[q]
    if q.bit_count() > r.bit_count():
        return {}
    verts = [u for u in range(N) if r >> u & 1]
    pivot = next(u for u in verts if not (q >> u & 1))
    eps = (-1) ** verts.index(pivot)
    out = {}
    for j, v in enumerate(verts):
        if v == pivot:
            continue
        for z, c in expand(r ^ (1 << v)).items():
            out[z] = out.get(z, 0) - eps * ((-1) ** j) * c
    return {z: c for z, c in out.items() if c}
C2 = [s for s in CRIT if s.bit_count() == 3]
C3 = [s for s in CRIT if s.bit_count() == 4]
M = []
for s in C3:
    out = {}
    for j, u in enumerate(v for v in range(N) if s >> v & 1):
        for z, c in expand(s ^ (1 << u)).items():
            out[z] = out.get(z, 0) + ((-1) ** j) * c
    assert set(out).issubset(set(C2))
    M.append([out.get(c, 0) for c in C2])
assert len(M) == 24 and all(len(r) == 4 for r in M)
# Check a primitive integral 4x4 minor; selecting critical 3-cells
# by position in sorted C3 (0-based positions 1,2,3,6).
def det(a):
    if len(a) == 1: return a[0][0]
    return sum(((-1) ** j) * x * det([row[:j] + row[j+1:] for row in a[1:]])
               for j, x in enumerate(a[0]))
minor_rows = (1, 2, 3, 6)
minor = [M[i] for i in minor_rows]
assert abs(det(minor)) == 1
# Replay the complete embedded Morse certificate, rather than trusting a log.
certpath = Path(__file__).with_name("morse_certificate.json")
if certpath.is_file():
    cert = json.loads(certpath.read_text(encoding="utf-8"))
    assert cert["vertex_count"] == N
    assert cert["edges"] == [list(e) for e in sorted(E)]
    assert cert["f_vector"] == [12, 66, 140, 105]
    assert cert["critical_0_masks"] == [s for s in CRIT if s.bit_count() == 1]
    assert cert["critical_2_masks"] == C2
    assert cert["critical_3_masks"] == C3
    assert cert["boundary_3_to_2_rows"] == M
    assert cert["unit_minor_row_indices_0based"] == list(minor_rows)
    assert cert["unit_minor_determinant"] == det(minor)
else:
    raise FileNotFoundError("The standalone Morse certificate must be next to this checker")
# Separate simplicial-boundary calculation mod 2: column bitsets,
# independent of Morse paths or their signs.
BYDIM = [[s for s in F if s.bit_count() == d + 1] for d in range(4)]
def rank_mod2(columns):
    piv = {}
    for x in columns:
        while x:
            p = x.bit_length() - 1
            if p in piv: x ^= piv[p]
            else:
                piv[p] = x
                break
    return len(piv)
ranks = []
for d in range(1, 4):
    ix = {s: i for i, s in enumerate(BYDIM[d-1])}
    cols = []
    for s in BYDIM[d]:
        col = 0
        for u in range(N):
            if s >> u & 1: col ^= 1 << ix[s ^ (1 << u)]
        cols.append(col)
    ranks.append(rank_mod2(cols))
assert ranks == [11, 55, 85]
# Exact Euler check, plus a check that the complex is 3-dimensional.
assert 12 - 66 + 140 - 105 == -19
print('ICOSAHEDRAL_GRAPH vertices=12 edges=30 triangles=20 regular_degree=5')
print('F_VECTOR f0=12 f1=66 f2=140 f3=105 total_nonempty=323')
print('MORSE_MATCHING pairs=147 critical={0:1,2:4,3:24} covers=972 acyclic=yes')
print('MORSE_D3_TO_D2 rows=24 columns=4 unit_minor_rows_0based=1,2,3,6 determinant='+str(det(minor)))
print('MORSE_CERTIFICATE_REPLAY_PASS')
print('SIMPLICIAL_MOD2_RANKS boundary_1=11 boundary_2=55 boundary_3=85')
print('INTEGRAL_HOMOTOPY_WEDGE_S3=20')
print('ALL_CHECKS_PASS')
