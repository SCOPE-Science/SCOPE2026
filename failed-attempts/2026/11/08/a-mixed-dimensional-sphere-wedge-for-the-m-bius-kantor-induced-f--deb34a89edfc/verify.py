#!/usr/bin/env python3
"""Exact finite topological certificate for the induced-forest complex of GP(8,3).

No external dependencies. Run `python3 mk_forest_verify.py`. Independently tests
face membership by union-find and component edge-count; checks every directed
Hasse cover of a staged acyclic matching; computes signed integer Morse
boundaries via gradient projection; and verifies a unimodular 8x8 minor.
"""
from collections import Counter,defaultdict,deque
from functools import lru_cache
from itertools import combinations
N=16
EDGES=[(i,(i+1)%8) for i in range(8)] + [(i,8+i) for i in range(8)] + [(8+i,8+(i+3)%8) for i in range(8)]
assert len(EDGES)==len({tuple(sorted(e)) for e in EDGES})==24
A=[0]*N
for a,b in EDGES:A[a]|=1<<b;A[b]|=1<<a
assert all(a.bit_count()==3 for a in A)

def forest_union_find(mask):
    parent=list(range(N))
    def root(v):
        while parent[v]!=v:
            parent[v]=parent[parent[v]]
            v=parent[v]
        return v
    for a,b in EDGES:
        if mask>>a&1 and mask>>b&1:
            ra,rb=root(a),root(b)
            if ra==rb:return False
            parent[ra]=rb
    return True

def forest_components(mask):
    visited=0;comp=0
    for u in range(N):
        if mask>>u&1 and not (visited>>u&1):
            comp+=1
            stack=[u];visited|=1<<u
            while stack:
                v=stack.pop()
                for w in range(N):
                    if (mask>>w&1) and (A[v]>>w&1) and not (visited>>w&1):
                        visited|=1<<w;stack.append(w)
    edge_count=sum(bool(mask>>a&1 and mask>>b&1) for a,b in EDGES)
    return edge_count==mask.bit_count()-comp

F=set()
for s in range(1,1<<N):
    a=forest_union_find(s)
    assert a==forest_components(s),('distinct cycle tests disagree',s)
    if a:F.add(s)
fvec=Counter(s.bit_count()-1 for s in F)
assert len(F)==50996
assert [fvec[d] for d in range(11)] == [16,120,560,1820,4368,7984,11200,11792,8672,3792,672]

# Deterministic staged vertex-toggle matching in the face poset.
U=set(F);pairs={};upper={}
for v in range(N):
    bit=1<<v
    for s in sorted(U):
        t=s|bit
        if not(s&bit) and t in U:
            pairs[s]=t;upper[t]=s;U.remove(s);U.remove(t)
critical=sorted(U,key=lambda s:(s.bit_count(),s))
critvec=Counter(s.bit_count()-1 for s in U)
assert len(pairs)==25475 and critvec=={0:1,8:8,9:33,10:4}

# Verify acyclicity on ALL nonempty-face covering relations.
indeg={s:0 for s in F};out=defaultdict(list);covers=0
for top in F:
    for v in range(N):
        bit=1<<v
        if top&bit and top!=bit:
            lower=top^bit
            assert lower in F
            src,dst=(lower,top) if pairs.get(lower)==top else (top,lower)
            out[src].append(dst);indeg[dst]+=1;covers+=1
q=deque(s for s in F if indeg[s]==0);visited=0
while q:
    s=q.popleft();visited+=1
    for t in out[s]:
        indeg[t]-=1
        if indeg[t]==0:q.append(t)
assert visited==len(F) and covers>300000

def boundary(s):
    b={};k=0
    for v in range(N):
        if s>>v&1:
            t=s^(1<<v)
            if t:b[t]=1 if k%2==0 else -1
            k+=1
    return b

# Chain-level elementary cancellation: matched upper cells project to zero,
# matched lower cells are solved from their matched upper boundary equation.
@lru_cache(None)
def project(s):
    if s in U:return {s:1}
    if s in upper:return {}
    assert s in pairs
    b=boundary(pairs[s]);eps=b[s];acc=defaultdict(int)
    for t,c in b.items():
        if t==s:continue
        for z,w in project(t).items():acc[z]-=eps*c*w
    return {z:w for z,w in acc.items() if w}

def morse_boundary(d):
    rows=sorted(s for s in U if s.bit_count()-1==d-1)
    cols=sorted(s for s in U if s.bit_count()-1==d)
    ix={s:i for i,s in enumerate(rows)}
    B=[[0]*len(cols) for _ in rows]
    for j,s in enumerate(cols):
        for t,c in boundary(s).items():
            for z,w in project(t).items():B[ix[z]][j]+=c*w
    return B
B9=morse_boundary(9);B10=morse_boundary(10)
assert len(B9)==8 and all(len(row)==33 for row in B9)
assert len(B10)==33 and all(row==[0]*4 for row in B10)
# The following ordered columns form a signed unimodular minor.
minor_columns=[21,3,2,1,5,10,12,18]
minor=[[B9[r][c] for c in minor_columns] for r in range(8)]
assert minor==[[1,0,0,0,0,0,0,0],
              [0,1,0,0,0,0,0,0],
              [0,0,-1,0,0,0,0,0],
              [0,0,0,-1,0,0,0,0],
              [0,0,0,0,-1,0,0,0],
              [0,0,0,0,0,-1,0,0],
              [0,0,0,0,0,1,1,0],
              [0,0,0,0,0,0,0,-1]]
# Determinant is -1 (product of diagonal entries; a row elimination clears (6,5)).
assert all(sum(B9[i][j]*B10[j][k] for j in range(33))==0 for i in range(8) for k in range(4))
assert sum((-1)**d * fvec[d] for d in fvec)==-20
# Reduced Euler character = ordinary Euler characteristic - 1 = -21;
# wedge^{25} S^9 vee wedge^4 S^10 has reduced Euler -25+4 = -21.

print('GRAPH GP(8,3); VERTICES',N,'EDGES',len(EDGES))
print('INDUCED_FOREST_FACES',len(F),'F_VECTOR',[fvec[d] for d in range(11)])
print('MORSE_PAIRS',len(pairs),'CRITICAL',dict(sorted(critvec.items())))
print('CRITICAL_MASKS',[(s.bit_count()-1,s) for s in critical])
print('DIRECTED_HASSE_COVERS',covers,'ACYCLIC_VERTICES',visited)
print('MORSE_B9_SHAPE',(len(B9),len(B9[0])),'MORSE_B9_ROWS',B9)
print('MORSE_B10_SHAPE',(len(B10),len(B10[0])),'ALL_ZERO',True)
print('UNIT_8X8_MINOR_COLUMNS_ZERO_BASED',minor_columns,'DETERMINANT',-1)
print('REDUCED_INTEGRAL_HOMOLOGY',{9:25,10:4},'REDUCED_EULER',-21)
print('MOBIUS_KANTOR_INDUCED_FOREST_CERTIFICATE_PASS')
