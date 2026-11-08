#!/usr/bin/env python3
"""Independent enumeration via complement of cyclic Latin-square graph.
Python standard library only. Does not use the Cayley generators or saved matching list.
"""
from itertools import combinations
from collections import deque
V=range(16)
rc=[divmod(i,4) for i in V]
adj=[set() for _ in V]
for u in V:
    r,c=rc[u]
    adj[u]={v for v in V if v!=u and rc[v][0]!=r and rc[v][1]!=c and (sum(rc[v])%4)!=(r+c)%4}
assert {len(a) for a in adj}=={6}
E=[(u,v) for u in V for v in range(u+1,16) if v in adj[u]]
assert len(E)==48
# Conflict masks independently computed using graph-neighborhood intersections.
conflict=[0]*48
for i,(a,b) in enumerate(E):
    C=0
    for j,(c,d) in enumerate(E):
        if {a,b}&{c,d} or any(p in adj[q] for q in (a,b) for p in (c,d)):
            C|=1<<j
    conflict[i]=C
assert all((conflict[i]>>i)&1 for i in range(48))
pairs=[]
triples=[]
for i in range(48):
    for j in range(i+1,48):
        if (conflict[i]>>j)&1:continue
        pairs.append((i,j))
        for k in range(j+1,48):
            if not ((conflict[i]|conflict[j])>>k)&1:
                triples.append((i,j,k))
# Independent quadruple would contain a viable triple with a compatible last edge.
assert all(all(((conflict[i]|conflict[j]|conflict[k])>>e)&1 or e in (i,j,k) for e in range(48)) for i,j,k in triples)
assert len(triples)==32
A=[set() for _ in triples]
for a,b in combinations(range(32),2):
    intersection=len(set(triples[a]) & set(triples[b]))
    assert intersection != 2
    if intersection==1:A[a].add(b);A[b].add(a)
assert sum(map(len,A))//2==48
assert all(len(row)==3 for row in A)
for s in range(32):
    D={s:0};q=deque([s])
    while q:
        v=q.popleft()
        for w in A[v]:
            if w not in D:D[w]=D[v]+1;q.append(w)
    assert len(D)==32 and max(D.values())==5
# Separately count triangles in this representation and their intersections.
tri=[t for t in combinations(V,3) if all(b in adj[a] for a,b in combinations(t,2))]
assert len(tri)==32
te=sum(len(set(x)&set(y))==2 for x,y in combinations(tri,2))
assert te==48
print('VERIFY_OK Latin-square complement: 48 edges, 32 induced matching triples, no quadruples')
print('VERIFY_OK 32 frozen one-exchanges; 48 two-exchanges, degree 3, diameter 5; 32 triangles and 48 shared-edge adjacencies')
