#!/usr/bin/env python3
"""Self-contained exact finite verification of a Paley-13 neighborhood-complex matching.
Run with Python >= 3.9; uses only the standard library.
"""
from collections import Counter, defaultdict, deque
from pathlib import Path
import json
from itertools import combinations

P = 13
Q = {1, 3, 4, 9, 10, 12}
assert {(v*v) % P for v in range(1, P)} == Q
universe = (1 << P) - 1
neighbors = [sum(1 << v for v in range(P) if (v - u) % P in Q) for u in range(P)]
assert all(x.bit_count() == 6 for x in neighbors)
assert all((neighbors[u] & (1 << u)) == 0 for u in range(P))
assert all((neighbors[u] >> v) & 1 == (neighbors[v] >> u) & 1 for u in range(P) for v in range(P))
assert all((neighbors[u] & neighbors[v]).bit_count() == (2 if (neighbors[u] >> v) & 1 else 3)
           for u in range(P) for v in range(u + 1, P))
# Every induced vertex neighborhood is a six-cycle, not merely six vertices.
for u in range(P):
    local = [v for v in range(P) if (neighbors[u] >> v) & 1]
    assert len(local) == 6
    assert all((neighbors[v] & neighbors[u]).bit_count() == 2 for v in local)
    reached = {local[0]}
    frontier = [local[0]]
    while frontier:
        v = frontier.pop()
        for w in local:
            if ((neighbors[v] >> w) & 1) and w not in reached:
                reached.add(w); frontier.append(w)
    assert len(reached) == 6

# First construction: faces are nonempty subsets of the thirteen open neighborhoods.
faces = set()
for nb in neighbors:
    sub = nb
    while sub:
        faces.add(sub)
        sub = (sub - 1) & nb

# Independent construction: a set has a common neighbor iff this intersection is nonempty.
faces2 = set()
for f in range(1, 1 << P):
    common = universe
    for i in range(P):
        if (f >> i) & 1:
            common &= neighbors[i]
    if common:
        faces2.add(f)
assert faces == faces2
assert len(faces) == 598
fvec = tuple(sum(f.bit_count() == k for f in faces) for k in range(1, 7))
assert fvec == (13, 78, 221, 195, 78, 13), fvec
assert sum((-1)**(k-1)*fvec[k-1] for k in range(1, 7)) == 26

# A deterministic matching on the nonempty face poset. At step v, pair each available
# face not containing v with its available coface obtained by adjoining v.
unmatched = faces.copy()
matched_pairs = []
for v in range(P):
    bit = 1 << v
    for f in sorted(unmatched):
        if (f & bit) == 0 and (f | bit) in unmatched:
            unmatched.remove(f)
            unmatched.remove(f | bit)
            matched_pairs.append((f, f | bit))
assert len(matched_pairs) == 286
critical = sorted(unmatched)
critvec = Counter(f.bit_count()-1 for f in critical)
assert critvec == {0:1, 2:25}, critvec
assert [f for f in critical if f.bit_count()==1] == [1]

# Explicit topological sorting of the *full* directed Hasse diagram of all nonempty
# faces, reversing only incidences chosen in the matching.
up = set(matched_pairs)
out = defaultdict(list)
indegree = {f:0 for f in faces}
incidences=0
for high in faces:
    t=high
    while t:
        bit = t & -t
        low = high ^ bit
        t -= bit
        if not low: continue
        if (low, high) in up:
            src, dst = low, high
        else:
            src, dst = high, low
        out[src].append(dst)
        indegree[dst] += 1
        incidences += 1
queue = deque(f for f in faces if indegree[f] == 0)
visited = 0
while queue:
    f = queue.popleft()
    visited += 1
    for g in out[f]:
        indegree[g] -= 1
        if indegree[g] == 0: queue.append(g)
assert visited == len(faces), (visited, len(faces))

# Independently inspect a complete explicit certificate, including a topological order.
cert_path = Path(__file__).with_name('paley13_certificate.json')
certificate = json.loads(cert_path.read_text(encoding='utf-8'))
assert certificate['graph_order'] == P
assert certificate['quadratic_residues'] == sorted(Q)
assert certificate['face_vector'] == list(fvec)
assert {tuple(pair) for pair in certificate['matched_pairs']} == set(matched_pairs)
assert len(certificate['matched_pairs']) == len(matched_pairs)
assert certificate['critical_faces'] == critical
assert len(certificate['directed_hasse_topological_order']) == len(faces)
order = {face: i for i,face in enumerate(certificate['directed_hasse_topological_order'])}
assert len(order) == len(faces) and set(order) == faces
assert all(order[f] < order[g] for f in faces for g in out[f])

# Independent finite-field boundary-rank test, using sparse column dictionaries.
# Oriented boundary of [v0<...<vk] is alternating deletion of vi.
bydim = [sorted(f for f in faces if f.bit_count()==k+1) for k in range(6)]
def rank_mod(degree, prime):
    rows = {face:i for i,face in enumerate(bydim[degree-1])}
    pivots = {}
    for f in bydim[degree]:
        col = {}
        verts = [v for v in range(P) if (f >> v) & 1]
        for j,v in enumerate(verts):
            row = rows[f^(1<<v)]
            col[row] = 1 if j%2 == 0 else prime-1
        while col:
            k = min(col)
            if k not in pivots:
                factor = pow(col[k],-1,prime)
                pivots[k] = {i:(a*factor)%prime for i,a in col.items()}
                break
            a = col[k]
            for i,b in pivots[k].items():
                nv=(col.get(i,0)-a*b)%prime
                if nv: col[i]=nv
                else: col.pop(i,None)
    return len(pivots)
for prime in (2,3,5,7):
    ranks = [rank_mod(d,prime) for d in range(1,6)]
    assert ranks == [12,66,130,65,13], (prime,ranks)
    betti = [13-ranks[0]-1] + [len(bydim[d])-ranks[d-1]-ranks[d] for d in range(1,5)] + [len(bydim[5])-ranks[4]]
    assert betti == [0,0,25,0,0,0], (prime,betti)
    print('boundary ranks modulo',prime, ranks,'reduced betti',betti)

print('quadratic residues:', sorted(Q))
print('nonempty simplices:', len(faces), 'f-vector:', fvec)
print('matching pairs:', len(matched_pairs),'critical counts:',dict(sorted(critvec.items())))
print('Hasse incidences:', incidences,'topological sort vertices:',visited)
print('critical triangle masks:', [f for f in critical if f.bit_count()==3])
print('ALL_CHECKS_PASS')
