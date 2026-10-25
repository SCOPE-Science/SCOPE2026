"""Exact finite verification of the graph-metric Rips filtration of the Pappus graph.

Only the Python standard library is needed.  This checks the finite
incidence/metric assertions in the accompanying structural proof.
"""
from collections import deque, Counter
from itertools import combinations

N = 18
LCF = (5, 7, -7, 7, -7, -5) * 3
EDGES = {tuple(sorted((i, (i + 1) % N))) for i in range(N)}
EDGES |= {tuple(sorted((i, (i + LCF[i]) % N))) for i in range(N)}
assert len(EDGES) == 27
adj = [set() for _ in range(N)]
for u,v in EDGES:
    adj[u].add(v); adj[v].add(u)
assert all(len(x) == 3 for x in adj)
assert all(u % 2 != v % 2 for u,v in EDGES)
D = []
for s in range(N):
    d = [-1] * N
    d[s] = 0
    todo = deque([s])
    while todo:
        u = todo.popleft()
        for v in adj[u]:
            if d[v] < 0:
                d[v] = d[u] + 1
                todo.append(v)
    assert -1 not in d
    D.append(d)
assert max(map(max, D)) == 4
assert all(D[u][v] in (2,4) for u in range(N) for v in range(N) if u != v and u % 2 == v % 2)
assert all(D[u][v] in (1,3) for u in range(N) for v in range(N) if u % 2 != v % 2)

# There are six disjoint distance-four triples, with three in each color.
four = [{v for v in range(N) if D[u][v] == 4} for u in range(N)]
assert all(len(s) == 2 for s in four)
TRIPLES = sorted({tuple(sorted({u} | four[u])) for u in range(N)})
assert len(TRIPLES) == 6 and all(len(t)==3 for t in TRIPLES)
assert sorted(v for t in TRIPLES for v in t) == list(range(N))
assert all(len({v%2 for v in t})==1 for t in TRIPLES)
assert all(set(t)-{u} == four[u] for t in TRIPLES for u in t)

# Verify exact simplex lists, rather than merely their Euler characteristics.
def faces_at(r):
    nbr = [sum(1 << v for v in range(N) if v != u and D[u][v] <= r) for u in range(N)]
    good = bytearray(1 << N)
    good[0] = 1
    by_dim = {}
    for m in range(1, 1 << N):
        b = m & -m
        v = b.bit_length() - 1
        sub = m ^ b
        if good[sub] and not (sub & ~nbr[v]):
            good[m] = 1
            by_dim.setdefault(m.bit_count()-1, []).append(m)
    return by_dim

def rank_mod2(simplices_lower, simplices_upper):
    pos = {m:i for i,m in enumerate(simplices_lower)}
    pivots = {}
    rank = 0
    for face in simplices_upper:
        column = 0
        m = face
        while m:
            b = m & -m
            m ^= b
            column ^= 1 << pos[face ^ b]
        while column:
            p = column.bit_length()-1
            if p in pivots:
                column ^= pivots[p]
            else:
                pivots[p] = column
                rank += 1
                break
    return rank

EXPECTED = {
    1: ((18,27), (17,), (1,10)),
    2: ((18,81,108,18), (17,64,18), (1,0,26,0)),
    3: ((18,135,540,1215,1458,729), (17,118,422,793,665), (1,0,0,0,0,64)),
}
for r in (1,2,3):
    faces = faces_at(r)
    fv = tuple(len(faces[k]) for k in range(max(faces)+1))
    ranks = tuple(rank_mod2(faces[k-1],faces[k]) for k in range(1,len(fv)))
    betti = tuple(fv[k] - (ranks[k-1] if k else 0) - (ranks[k] if k+1<len(fv) else 0) for k in range(len(fv)))
    assert (fv,ranks,betti) == EXPECTED[r], (r,fv,ranks,betti)
    print('rips',r,'faces',fv,'ranks',ranks,'betti',betti)

# At radius two, the two color-side induced flag complexes are
# the joins of their three disjoint three-vertex sets.
F2=faces_at(2)
for parity in (0,1):
    side = [v for v in range(N) if v%2==parity]
    ts = [set(t) for t in TRIPLES if t[0]%2==parity]
    assert len(ts)==3 and set.union(*ts)==set(side)
    for u,v in combinations(side,2):
        assert (D[u][v]==4) == any({u,v}<=t for t in ts)

for k,flist in F2.items():
    for f in flist:
        evens = sum(1 for v in range(0,N,2) if (f>>v)&1)
        odds = f.bit_count() - evens
        assert evens<=1 or odds<=1, (k, f)
        if evens==odds==1:
            u,v = [i for i in range(N) if (f>>i)&1]
            assert tuple(sorted((u,v))) in EDGES

# A tetrahedron of radius two is exactly a full closed radius-one ball.
tetra={f for f in F2[3]}
balls={sum(1<<v for v in {u}|adj[u]) for u in range(N)}
assert tetra==balls and len(tetra)==18
# Every tetrahedron has a triangular face absent from all others.
tris=Counter(f ^ (f & -f) for f in ())
for f in tetra:
    for v in range(N):
        if (f>>v)&1:
            tris[f ^ (1<<v)] += 1
assert all(any(tris[f ^ (1<<v)]==1 for v in range(N) if (f>>v)&1) for f in tetra)

# Optional independent graph-presentation check: all non-tree edges
# vanish under the 108 triangular relators at scale two.
TREE = {(0,1),(0,2),(0,4),(0,5),(0,6),(0,8),(0,12),(0,16),(0,17),
        (1,3),(1,7),(1,9),(1,13),(2,10),(2,14),(3,11),(3,15)}
E2={tuple(sorted((u,v))) for u in range(N) for v in range(u+1,N) if D[u][v]<=2}
assert len(E2)==81 and TREE<=E2 and len(TREE)==17
seen={0}
while True:
    new=seen|{v for u,v in TREE if u in seen}|{u for u,v in TREE if v in seen}
    if new==seen: break
    seen=new
assert len(seen)==N
known=set(TREE)
rounds=0
while True:
    additions=set()
    for face in F2[2]:
        verts=[v for v in range(N) if (face>>v)&1]
        es={tuple(sorted(e)) for e in combinations(verts,2)}
        if len(es-known)==1:
            additions|=es-known
    if not additions: break
    known |= additions
    rounds += 1
assert known==E2, ('missing π1 generators',len(E2-known))

# Radius-three complex is exactly the join of six discrete triples.
# Its maximal simplices select one vertex from each triple (3^6=729).
F3=faces_at(3)
assert len(F3[5])==3**6
assert all(sum(bool(f & sum(1<<v for v in t)) for t in TRIPLES)==6 for f in F3[5])
print('distance-four triples:',TRIPLES)
print('VERIFY_OK PAPPUS_VR homotopy structural evidence, 64 sphere join, 26 sphere gluing, persistence ranks')
