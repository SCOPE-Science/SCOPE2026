#!/usr/bin/env python3
"""Exact combinatorial checks for graph-metric Vietoris--Rips complexes of the Pappus graph.
Python 3 standard library; no external files, packages or downloads are needed.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, product
from math import comb

N = 18
LCF = (5, 7, -7, 7, -7, -5) * 3
EDGES = {tuple(sorted((i, (i+1) % N))) for i in range(N)}
EDGES.update(tuple(sorted((i, (i+d) % N))) for i, d in enumerate(LCF))
assert len(EDGES) == 27
adj = [set() for _ in range(N)]
for a,b in EDGES:
    adj[a].add(b); adj[b].add(a)
assert all(len(t)==3 for t in adj)

D = []
for root in range(N):
    ds = [-1]*N; ds[root]=0
    todo=deque([root])
    while todo:
        u=todo.popleft()
        for v in sorted(adj[u]):
            if ds[v]<0:
                ds[v]=ds[u]+1; todo.append(v)
    assert Counter(ds) == {0:1,1:3,2:6,3:6,4:2}
    D.append(ds)
assert all(D[i][j] == D[j][i] for i in range(N) for j in range(N))
X=set(range(0,N,2)); Y=set(range(1,N,2))
assert all((a in X)!=(b in X) for a,b in EDGES)

DIST4 = {tuple(sorted((i,j))) for i in range(N) for j in range(i+1,N) if D[i][j]==4}
TRIPLES = [frozenset(t) for t in ((0,10,14),(2,6,16),(4,8,12),(1,11,15),(3,7,17),(5,9,13))]
assert len(DIST4) == 18
assert len(set().union(*TRIPLES)) == 18
assert all(not (a & b) for i,a in enumerate(TRIPLES) for b in TRIPLES[i+1:])
assert DIST4 == {tuple(sorted(ab)) for t in TRIPLES for ab in combinations(t,2)}

# The graph-distance-r clique complex, with faces represented by bitmasks.
def clique_faces(r):
    masks = set()
    def extend(candidates, mask):
        for pos, v in enumerate(candidates):
            new = mask | (1 << v)
            masks.add(new)
            extend([w for w in candidates[pos+1:] if D[v][w] <= r], new)
    extend(list(range(N)),0)
    return masks

K1=clique_faces(1)
K2=clique_faces(2)
assert K1 == {(1 << v) for v in range(N)} | {(1<<a)|(1<<b) for a,b in EDGES}
assert len(K2)==225
assert Counter(m.bit_count()-1 for m in K2) == {0:18,1:81,2:108,3:18}

# Construct the cover independently of the clique finder, using only incidence.
def all_nonempty_submasks(mask):
    sub=mask
    while sub:
        yield sub
        sub=(sub-1)&mask

def clique_side(S):
    return {m for m in K2 if not (m & ~sum(1<<v for v in S))}

A=clique_side(X); B=clique_side(Y)
assert Counter(m.bit_count()-1 for m in A) == {0:9,1:27,2:27}
assert Counter(m.bit_count()-1 for m in B) == {0:9,1:27,2:27}
U=set(A);V=set(B)
for v in Y:
    mask=(1<<v)|sum(1<<p for p in adj[v])
    U.update(all_nonempty_submasks(mask))
for v in X:
    mask=(1<<v)|sum(1<<ell for ell in adj[v])
    V.update(all_nonempty_submasks(mask))
assert len(U)==len(V)==135
assert U|V==K2
assert U&V == K1

# Staged elementary-face matching: no computer homology or Morse output is assumed.
remaining=set(K2); pairs=[]
for v in range(N):
    bit=1<<v
    for a in sorted((q for q in remaining if not(q&bit)),key=lambda t:(t.bit_count(),t)):
        b=a|bit
        if b in remaining:
            remaining.remove(a);remaining.remove(b);pairs.append((a,b))
assert len(pairs)==99
assert Counter(q.bit_count()-1 for q in remaining)=={0:1,2:26}

# Verify the full gradient Hasse graph is acyclic, not just that pairs are disjoint.
paired=set(pairs)
indegree={f:0 for f in K2}
adjacency={f:[] for f in K2}
for high in K2:
    t=high
    while t:
        bit=t & -t
        low=high^bit
        t-=bit
        if not low:continue
        if (low, high) in paired: u,v=low,high
        else: u,v=high,low
        adjacency[u].append(v);indegree[v]+=1
q=deque([f for f in K2 if indegree[f]==0]); seen=0
while q:
    u=q.popleft();seen+=1
    for v in adjacency[u]:
        indegree[v]-=1
        if indegree[v]==0:q.append(v)
assert seen==len(K2)

# Independent mod-2 simplicial boundary-rank computation for the first stages.
def betti_mod2(faces):
    by_dim=defaultdict(list)
    for m in faces:by_dim[m.bit_count()-1].append(m)
    for c in by_dim.values():c.sort()
    ranks={}
    for k in range(1,max(by_dim)+1):
        rows={face:i for i,face in enumerate(by_dim[k-1])}
        pivots={}
        for higher in by_dim[k]:
            col=0
            for v in range(N):
                if higher & (1<<v):
                    col ^= 1<<rows[higher^(1<<v)]
            while col:
                p=col.bit_length()-1
                if p not in pivots:
                    pivots[p]=col;break
                col^=pivots[p]
        ranks[k]=len(pivots)
    betti={k:len(masks)-ranks.get(k,0)-ranks.get(k+1,0) for k,masks in by_dim.items()}
    return betti, ranks, {k:len(v) for k,v in by_dim.items()}

b1,rank1,f1=betti_mod2(K1)
b2,rank2,f2=betti_mod2(K2)
assert b1=={0:1,1:10}
assert b2=={0:1,1:0,2:26,3:0}

# At scale 3, precisely the distance-4 pairs are forbidden; their graph is 6 K_3.
K3=clique_faces(3)
constructed={0}
for tri in TRIPLES:
    constructed={a | bit for a in constructed for bit in [0]+[1<<v for v in sorted(tri)]}
constructed.remove(0)
assert K3==constructed
assert len(K3)==4095
assert Counter(m.bit_count()-1 for m in K3) == {k:comb(6,k+1)*3**(k+1) for k in range(6)}
b3,rank3,f3=betti_mod2(K3)
assert b3=={0:1,1:0,2:0,3:0,4:0,5:64}
assert max(max(row) for row in D)==4

print('PAPPUS_GRAPH_VERTICES',N,'EDGES',len(EDGES),'DIAMETER',4)
print('DISTANCE4_TRIANGLES',','.join('/'.join(map(str,sorted(t))) for t in TRIPLES))
print('SCALE_1_FACES',len(K1),'REDUCED_BETTI', {k:v for k,v in b1.items() if k>0})
print('SCALE_2_FACES',len(K2),'FVECTOR',tuple(f2[k] for k in range(4)))
print('SCALE_2_COVER','U',len(U),'V',len(V),'INTERSECTION',len(U&V))
print('SCALE_2_MATCHING','PAIRS',len(pairs),'CRITICAL',dict(Counter(m.bit_count()-1 for m in remaining)),'HASSE_DAG',seen)
print('SCALE_2_GF2_BETTI',b2,'BOUNDARY_RANKS',rank2)
print('SCALE_3_FACES',len(K3),'FVECTOR',tuple(f3[k] for k in range(6)))
print('SCALE_3_GF2_BETTI',b3,'BOUNDARY_RANKS',rank3)
print('SCALE_4_COMPLETE_SIMPLEX', True)
print('PAPPUS_RIPS_EXACT_FINITE_CHECK_PASS')
