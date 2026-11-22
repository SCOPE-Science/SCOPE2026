#!/usr/bin/env python3
"""Exact independent-set census and reduced Morse-boundary certificate for C7 x K3.
Only Python standard library is required. Vertices have indices 3*i+c.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

N=21
adj=[]
for i in range(7):
    for c in range(3):
        m=0
        for j in ((i-1)%7,(i+1)%7):
            for d in range(3):
                if c!=d:m|=1<<(3*j+d)
        adj.append(m)

faces=[0]
for v in range(N):
    b=1<<v
    faces += [s|b for s in faces if not (s & adj[v])]
assert len(faces)==5282 and len(set(faces))==len(faces)
face_set=set(faces)
assert all(all((s&adj[v])==0 for v in range(N) if s&(1<<v)) for s in face_set)
counts=Counter(s.bit_count()-1 for s in faces)
assert [counts[k] for k in range(-1,9)]==[1,21,168,658,1365,1554,1022,402,84,7]

def boundary(s):
    return [(s ^ (1<<v), (-1)**j) for j,v in enumerate(v for v in range(N) if s & (1<<v))]

def matching():
    active=set(faces)
    lo2hi={}
    hi2lo={}
    for v in range(N):
        b=1<<v
        for s in list(active):
            t=s|b
            if not (s&b) and t in active:
                lo2hi[s]=t
                hi2lo[t]=s
                active.remove(s);active.remove(t)
    return active,lo2hi,hi2lo

critical,lo2hi,hi2lo=matching()
assert len(lo2hi)==2636 and len(critical)==10
assert Counter(s.bit_count()-1 for s in critical)=={3:4,4:6}
# Verify the full reversed Hasse graph has no directed cycle.
# Orient an unmatched facet edge high -> low and a matched facet edge low -> high.
indeg={s:0 for s in face_set}; out=defaultdict(list); edge_count=0
for high in face_set:
    for low,_ in boundary(high):
        if lo2hi.get(low)==high:
            u,v=low,high
        else:
            u,v=high,low
        out[u].append(v);indeg[v]+=1;edge_count+=1
queue=deque(s for s in face_set if indeg[s]==0)
seen=0
while queue:
    s=queue.popleft();seen+=1
    for t in out[s]:
        indeg[t]-=1
        if indeg[t]==0:queue.append(t)
assert seen==len(face_set)

# Signed algebraic Morse projection to the critical chains. Matched upper
# simplices project to zero. A matched lower simplex is replaced by the
# signed other facets of its partner upper simplex; acyclicity ensures
# termination and is proved above by exhaustive directed-Hasse test.
@lru_cache(None)
def project(s):
    if s in critical:return {s:1}
    if s in hi2lo:return {}
    assert s in lo2hi
    upper=lo2hi[s]
    pivot=dict(boundary(upper))[s]
    out={}
    for facet,sgn in boundary(upper):
        if facet==s:continue
        for crit,coef in project(facet).items():
            out[crit]=out.get(crit,0)-pivot*sgn*coef
    return {c:z for c,z in out.items() if z}

lower=sorted(s for s in critical if s.bit_count()==4)
upper=sorted(s for s in critical if s.bit_count()==5)
B=[]
for q in upper:
    target={}
    for facet,sgn in boundary(q):
        for c,z in project(facet).items():target[c]=target.get(c,0)+sgn*z
    B.append([target.get(s,0) for s in lower])
assert B==[[-1,0,0,0],[0,0,0,-1],[-1,0,0,0],[-1,1,1,-1],[0,0,0,-1],[-1,1,1,-1]]
# rank exactly 3: columns 2 and 3 agree, and the minor on rows 0,1,3
# and columns 0,1,3 has determinant +1 or -1. Thus coker(B^t) = Z.
def det3(a):
    return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
minor=det3([[B[r][c] for c in (0,1,3)] for r in (0,1,3)])
assert abs(minor)==1 and all(row[1]==row[2] for row in B)
# Unreduced Morse CW complex has one 0-cell, four 3-cells, six 4-cells;
# its boundary matrix has Smith diagonal (1,1,1,0), hence H3=Z,H4=Z^3.
# Independent mod-two full simplicial boundary ranks corroborate this.
def rank_mod2(k):
    rows=sorted(s for s in face_set if s.bit_count()==k)
    cols=sorted(s for s in face_set if s.bit_count()==k+1)
    loc={s:j for j,s in enumerate(rows)}
    basis={}
    for col in cols:
        val=0
        for facet,_ in boundary(col):val ^= 1<<loc[facet]
        while val:
            p=val.bit_length()-1
            if p in basis:val ^=basis[p]
            else:basis[p]=val;break
    return len(basis)
ranks={k:rank_mod2(k) for k in range(1,10)}
bettis={d:counts[d]-ranks.get(d,0)-ranks.get(d+1,0) for d in range(0,9)}
assert bettis[0]==1 and bettis[3]==1 and bettis[4]==3 and all(bettis[d]==0 for d in range(1,9) if d not in (3,4)),bettis
print('VERTICES',N,'FACES',len(faces),'HASSE_EDGES',edge_count)
print('FACE_COUNTS_BY_DIM',sorted(counts.items()))
print('ACYCLIC_HASSE',seen,'MATCHED_PAIRS',len(lo2hi),'CRITICAL_3',len(lower),'CRITICAL_4',len(upper))
print('CRITICAL_3_MASKS',lower,'CRITICAL_4_MASKS',upper)
print('SIGNED_MORSE_B_ROWS',B,'UNIT_MINOR',minor,'RANK',3,'TORSION_NONE')
print('FULL_MOD2_BETTI',sorted(bettis.items()))
print('HOMOTOPY','S^3 wedge 3 S^4','VERIFY_OK')
