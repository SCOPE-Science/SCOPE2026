#!/usr/bin/env python3
"""Proof checker for explicit translational torus-dual isomorphism."""
from itertools import product, combinations
from collections import Counter, deque
Z=list(product(range(4),repeat=2))
plus=lambda x,y:((x[0]+y[0])%4,(x[1]+y[1])%4)
minus=lambda x,y:((x[0]-y[0])%4,(x[1]-y[1])%4)
C={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
S0={(0,0),(1,2),(2,1)}
S1={(0,0),(1,3),(2,1)}
F0={(0,0),(1,0),(1,1)}
F1={(0,0),(0,1),(1,1)}
tr=lambda s,x:frozenset(plus(p,x) for p in s)
family=[tr(S,x) for S in (S0,S1) for x in Z]
faces=[tr(F,x) for F in (F0,F1) for x in Z]
assert len(set(family))==len(set(faces))==32
adj=lambda u,v:minus(u,v) in C
N=lambda v:{v}|{w for w in Z if adj(v,w)}
# Rather than repeating all vertex-subsets exhaustive enumeration, certify the
# orbit characterization using only 18 independent triples through the origin.
origin=(0,0)
nonneighbors=[v for v in Z if v!=origin and not adj(origin,v)]
ind0=[frozenset((origin,u,v)) for u,v in combinations(nonneighbors,2) if not adj(u,v)]
dom0={s for s in ind0 if len(set().union(*(N(v) for v in s)))==16}
assert len(ind0)==18 and len(dom0)==6
assert dom0=={s for s in family if origin in s}
assert all(all(not adj(u,v) for u,v in combinations(s,2)) and len(set().union(*(N(v) for v in s)))==16 for s in family)
assert len({v for v in Z if v not in N(origin)})==9
# All size-two independent sets leave at least four undominated vertices.
assert all(len(N(u)|N(v))<16 for u,v in combinations(Z,2) if not adj(u,v))
# Triangle faces are all 32 distinct triangles and every primal edge belongs to two faces.
tris={frozenset(t) for t in combinations(Z,3) if all(adj(u,v) for u,v in combinations(t,2))}
assert tris==set(faces)
edge_faces=Counter(tuple(sorted((u,v))) for f in faces for u,v in combinations(sorted(f),2))
assert len(edge_faces)==48 and set(edge_faces.values())=={2}
# Linear automorphism of Z4^2. det=2*1-3*1=-1 mod4.
L=lambda x:((2*x[0]+3*x[1])%4,(x[0]+x[1])%4)
assert len(set(L(x) for x in Z))==16
mapping={tr(S,x):tr(F,L(x)) for S,F in ((S0,F0),(S1,F1)) for x in Z}
assert len(mapping)==32 and set(mapping.values())==set(faces)
exchange={frozenset((s,t)) for s,t in combinations(family,2) if len(s&t)==2}
dual={frozenset((f,g)) for f,g in combinations(faces,2) if len(f&g)==2}
assert len(exchange)==len(dual)==48
assert {frozenset((mapping[s],mapping[t])) for e in exchange for s,t in [tuple(e)]}==dual
assert all(adj(next(iter(s-t)),next(iter(t-s))) for e in exchange for s,t in [tuple(e)])
# Algebraic neighbor differences prove the isomorphism between 16+16 cosets.
X={x for x in Z if len(tr(S0,(0,0))&tr(S1,x))==2}
Y={x for x in Z if len(tr(F0,(0,0))&tr(F1,x))==2}
assert X=={(0,0),(1,2),(3,1)} and Y=={(0,0),(0,3),(1,0)}
assert {L(x) for x in X}==Y
# Independent shortest-path verification on the triangular-face dual.
H={f:set() for f in faces}
for e in dual:
    u,v=tuple(e);H[u].add(v);H[v].add(u)
for root in faces:
    d={root:0}; queue=deque([root])
    while queue:
        u=queue.popleft()
        for v in H[u]:
            if v not in d:
                d[v]=d[u]+1;queue.append(v)
    assert len(d)==32
    assert [Counter(d.values())[j] for j in range(6)]==[1,3,6,9,9,4]
print('PASS independent toroidal-face-dual all-source distances: 1,3,6,9,9,4')
print('PASS orbit classification: precisely 32 minimum independent dominating triples in two translation orbits')
print('PASS every exchange is a slide, exactly 48 edges')
print('PASS torus dual: 32 triangles, 48 face adjacencies, matrix [[2,3],[1,1]] gives explicit graph isomorphism')
print('PASS neighbor shift sets: {(0,0),(1,2),(3,1)} -> {(0,0),(0,3),(1,0)}')
