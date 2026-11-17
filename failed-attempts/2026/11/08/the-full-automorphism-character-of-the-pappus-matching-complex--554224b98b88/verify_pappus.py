#!/usr/bin/env python3
"""Exact finite certificate for the rational automorphism character on Pappus matching homology.
Needs Python 3.9+ and NetworkX 3.x. All finite sets are rebuilt from the graph's LCF code.
"""
import math
from collections import Counter
import networkx as nx

LCF=[5,7,-7,7,-7,-5]*3
N=18
EDGES=tuple(sorted({tuple(sorted((i,(i+1)%N))) for i in range(N)} | {tuple(sorted((i,(i+LCF[i])%N))) for i in range(N)}))
assert len(EDGES)==27
G=nx.Graph();G.add_nodes_from(range(N));G.add_edges_from(EDGES)
assert sorted(dict(G.degree()).values())==[3]*N
P=sorted({tuple(m[i] for i in range(N)) for m in nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter()})
assert len(P)==216
I={p:i for i,p in enumerate(P)}
ident=tuple(range(N));zero=I[ident]
EIDX={e:i for i,e in enumerate(EDGES)}

def eperm(p):
    return tuple(EIDX[tuple(sorted((p[u],p[v])))] for u,v in EDGES)

def orbit_formula(p):
    ep=eperm(p)
    seen=set();masks=[]
    for i in range(len(EDGES)):
        if i in seen:continue
        orbit=[];j=i
        while j not in seen:
            seen.add(j);orbit.append(j);j=ep[j]
        verts=[a for j in orbit for a in EDGES[j]]
        if len(set(verts)) != len(verts):continue
        masks.append(sum(1<<v for v in verts))
    def f(i,used):
        if i==len(masks):return 1
        x=f(i+1,used)
        if not (used&masks[i]):x-=f(i+1,used|masks[i])
        return x
    return f(0,0)

# Separate enumeration of all simplicial faces (not orbit enumeration).
FACES=[]
def all_faces(start,used,sel):
    if sel:FACES.append(tuple(sel))
    for k in range(start,len(EDGES)):
        a,b=EDGES[k]
        m=(1<<a)|(1<<b)
        if used&m:continue
        sel.append(k);all_faces(k+1,used|m,sel);sel.pop()
all_faces(0,0,[])
assert len(FACES)==35367
size_counts=Counter(len(f) for f in FACES)
assert [size_counts[k] for k in range(1,10)]==[27,297,1719,5643,10557,10737,5319,1026,42]

# A direct signed Lefschetz count, independent of the orbit-subset sign formula.
def simplex_formula(p):
    ep=eperm(p);out=1  # negative of empty-face Lefschetz contribution
    for face in FACES:
        img=[ep[j] for j in face]
        if set(img)!=set(face):continue
        # Permutation sign of transformed vertices relative to sorted original face.
        inversions=sum(1 for i in range(len(img)) for j in range(i+1,len(img)) if img[i]>img[j])
        oriented_sign=(-1)**inversions
        # The negative reduced Lefschetz trace is the homological trace in degree five.
        out+=(-1)**len(face)*oriented_sign
    return out

A=[orbit_formula(p) for p in P]
assert A[zero]==40
B=[simplex_formula(p) for p in P]
assert A==B

# Conjugacy classes, using independently composed permutations.
def compose(p,q):return tuple(p[q[i]] for i in range(N))
C=[[I[compose(p,q)] for q in P] for p in P]
INV=[next(j for j in range(len(P)) if C[i][j]==zero) for i in range(len(P))]
classes=[];remaining=set(range(len(P)))
while remaining:
    i=min(remaining)
    orbit={C[C[j][i]][INV[j]] for j in range(len(P))}
    assert orbit<=remaining
    classes.append(sorted(orbit));remaining.difference_update(orbit)
assert len(classes)==13 and sum(len(c) for c in classes)==216
assert all(len({A[k] for k in c})==1 for c in classes)

def cycles(p):
    seen=set();out=[]
    for i in range(len(p)):
        if i in seen:continue
        path=[];j=i
        while j not in seen:
            seen.add(j);path.append(j);j=p[j]
        if len(path)>1:out.append('('+' '.join(map(str,path))+')')
    return ''.join(out) or '1'

print('GRAPH vertices=18 edges=27 automorphisms=216')
print('MATCHINGS', ','.join(str(size_counts[k]) for k in range(1,10)), 'faces=35367')
print('INDEPENDENT_TRACE_METHODS_ORBIT_AND_SIMPLICES agree_for=216')
print('CONJUGACY_CLASSES=13')
for j,c in enumerate(classes):
    p=P[c[0]]
    order=1
    q=ident
    while True:
        q=compose(p,q)
        if q==ident:break
        order+=1
    print(f'CLASS {j:02d} SIZE {len(c):3d} ORDER {order:2d} TRACE {A[c[0]]:3d} REP {cycles(p)}')
assert sum(A)==0
print('INVARIANT_DIMENSION=0')
colors=nx.algorithms.bipartite.color(G)
H=[i for i,p in enumerate(P) if colors[p[0]]==colors[0]]
assert len(H)==108 and sum(A[i] for i in H)==0
print('BIPARTITION_PRESERVING_INVARIANT_DIMENSION=0')
assert sum(x*x for x in A)==216*12
print('CHARACTER_INNER_PRODUCT=12')
print('PAPPUS_AUTOMORPHISM_CHARACTER_PASS')
