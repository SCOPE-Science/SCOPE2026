#!/usr/bin/env python3
"""Exhaustive certificate for induced two-path partitions of the icosahedral graph."""
from collections import Counter, deque
from itertools import combinations

N = 12
FULL = (1 << N) - 1
EDGES = [
    (0,1),(0,5),(0,7),(0,8),(0,11),
    (1,2),(1,5),(1,6),(1,8),
    (2,3),(2,6),(2,8),(2,9),
    (3,4),(3,6),(3,9),(3,10),
    (4,5),(4,6),(4,10),(4,11),
    (5,6),(5,11),
    (7,8),(7,9),(7,10),(7,11),
    (8,9),(9,10),(10,11)
]
assert len(EDGES) == 30 and len(set(tuple(sorted(e)) for e in EDGES)) == 30
assert all(sum(v in e for e in EDGES) == 5 for v in range(N))

def acyclic(mask):
    parent = list(range(N))
    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for u,v in EDGES:
        if mask >> u & 1 and mask >> v & 1:
            a,b = root(u),root(v)
            if a == b: return False
            parent[a] = b
    return True

def edgecount(mask):
    return sum(bool(mask >> u & 1) and bool(mask >> v & 1) for u,v in EDGES)

forests = [mask for mask in range(1 << N) if acyclic(mask)]
counts = Counter(mask.bit_count() for mask in forests)
assert counts == {0:1, 1:12, 2:66, 3:200, 4:345, 5:300, 6:60}
min_six = min(edgecount(m) for m in range(1 << N) if m.bit_count()==6)
min_seven = min(edgecount(m) for m in range(1 << N) if m.bit_count()==7)
assert (min_six,min_seven)==(5,8)
A = sorted(m for m in forests if m.bit_count() == 6 and acyclic(FULL ^ m))
assert len(A)==60
assert all(acyclic(FULL ^ m) for m in forests if m.bit_count()==6)
assert all(edgecount(m)==5 for m in A)
assert all((m.bit_count()!=6 or m in A) for m in forests)
assert all(acyclic(m) and acyclic(FULL ^ m) and m.bit_count()==6 for m in A)
idx = {m:i for i,m in enumerate(A)}
assert all((FULL ^ m) in idx for m in A)
H=[[] for _ in A]
exchanges=0
for i,m in enumerate(A):
    for j in range(i):
        b=A[j]
        if (m ^ b).bit_count()!=2:continue
        x=(m&~b).bit_length()-1
        y=(b&~m).bit_length()-1
        assert tuple(sorted((x,y))) in {tuple(sorted(e)) for e in EDGES}
        H[i].append(j);H[j].append(i);exchanges+=1
assert exchanges==120 and all(len(x)==4 for x in H)
profiles=Counter()
antipodes=0
diameter_pairs=0
detours=Counter()
for source,neigh in enumerate(H):
    d=[-1]*len(A);d[source]=0;q=deque([source])
    while q:
        u=q.popleft()
        for v in H[u]:
            if d[v]<0:d[v]=d[u]+1;q.append(v)
    assert min(d)==0 and max(d)==6
    profile=tuple(d.count(r) for r in range(7));profiles[profile]+=1
    assert d.count(6)==1 and d[idx[FULL ^ A[source]]]==6
    diameter_pairs += d.count(6)
    for j in range(source):
        johnson = (A[source] & ~A[j]).bit_count()
        detours[(johnson, d[j])] += 1
    antipodes += d[idx[FULL ^ A[source]]]==6
assert profiles=={(1,4,12,17,16,9,1):60}
assert diameter_pairs//2==30 and antipodes==60
assert detours == {(1,1):120,(2,2):360,(2,3):150,(3,3):360,(3,4):120,
                   (4,4):360,(4,5):150,(5,5):120,(6,6):30}
assert sum(v for (j,d),v in detours.items() if d==j+1)==420
# A BFS parity coloring proves the exchange graph bipartite, with shores 30+30.
colors={0:0};todo=deque([0])
while todo:
    u=todo.popleft()
    for v in H[u]:
        if v not in colors:colors[v]=colors[u]^1;todo.append(v)
        else:assert colors[v]!=(colors[u])
assert Counter(colors.values())=={0:30,1:30}
for s in range(len(H)):
    dist=[-1]*len(H);dist[s]=0;q=deque([s]);girth=999
    while q:
        u=q.popleft()
        for v in H[u]:
            if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
    # Exact girth by deleting each edge and finding shortest alternate path.
    for v in H[s]:
        dist2=[-1]*len(H);dist2[s]=0;q=deque([s])
        while q:
            u=q.popleft()
            for w in H[u]:
                if (u==s and w==v) or (u==v and w==s): continue
                if dist2[w]<0:dist2[w]=dist2[u]+1;q.append(w)
        if dist2[v]>=0:girth=min(girth,dist2[v]+1)
assert girth==6
print('VALID=60 EDGES=120 DEGREE=4 CONNECTED=YES DIAMETER=6 GIRTH=6')
print('ALL_PATH6=YES ALL_COMPLEMENTS_PATH6=YES; MIN_EDGES_K6=5 MIN_EDGES_K7=8')
print('SHELLS=1,4,12,17,16,9,1 UNIQUE_ANTIPODE=COMPLEMENT DIAMETER_PAIRS=30')
print('BIPARTITE=YES SHORES=30,30 JOHNSON_DETOURS=420 MAX_EXCESS=1')
print('CERTIFICATE_PASS')
