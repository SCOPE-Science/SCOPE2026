#!/usr/bin/env python3
"""Standalone exhaustive certificate for the 2-tree one-type collision theorem.
Requires Python 3.9+ standard library only. No external data or packages.
"""
from itertools import permutations, combinations
from collections import defaultdict
from math import comb

def edge(a,b): return (a,b) if a<b else (b,a)
def canon(E,n):
    best=None
    for p in permutations(range(n)):
        k=tuple(sorted(edge(p[a],p[b]) for a,b in E))
        if best is None or k<best:best=k
    return best

def isos(E,n):
    return canon(E,n)

def levels(nmax=6):
    shapes={(edge(0,1),)}
    yield 2,shapes
    for n in range(3,nmax+1):
        nex=set()
        for E in shapes:
            for a,b in E:
                F=tuple(sorted(E+(edge(a,n-1),edge(b,n-1))))
                nex.add(canon(F,n))
        shapes=nex
        yield n,shapes

def triangles(E,n):
    st=set(E)
    return tuple(tuple(k) for k in combinations(range(n),3)
                 if all(edge(a,b) in st for a,b in combinations(k,2)))

def polynomials(E,n):
    tri=triangles(E,n)
    by_tri=[0]*(n+1);by_forest=[0]*(n+1)
    for mask in range(1<<n):
        size=mask.bit_count()
        if all(not all(mask>>v&1 for v in t) for t in tri):
            by_tri[size]+=1
        # Fully independent check via DSU of the induced subgraph.
        parent=list(range(n))
        def root(x):
            while parent[x]!=x:x=parent[x]
            return x
        cyclic=False
        for a,b in E:
            if (mask>>a&1) and (mask>>b&1):
                a0,b0=root(a),root(b)
                if a0==b0:cyclic=True;break
                parent[a0]=b0
        if not cyclic:by_forest[size]+=1
    assert by_tri==by_forest,(E,by_tri,by_forest)
    return tuple(by_tri)

def containing(E,n,e):
    tri=triangles(E,n)
    arr=[0]*(n+1)
    for mask in range(1<<n):
        if all(mask>>v&1 for v in e) and all(not all(mask>>v&1 for v in t) for t in tri):
            arr[mask.bit_count()]+=1
    return tuple(arr)

def degree_signature(E,n):
    d=[0]*n
    for a,b in E:d[a]+=1;d[b]+=1
    return tuple(sorted(d))

def from_triples(ts):
    return tuple(sorted(set(edge(a,b) for t in ts for a,b in combinations(t,2))))

A=((0,1,2),(0,1,3),(0,2,4),(1,2,5))
B=((0,1,2),(0,1,3),(0,2,4),(1,3,5))
EA,EB=from_triples(A),from_triples(B)
base=(1,6,15,16,6,0,0)
assert triangles(EA,6)==A and triangles(EB,6)==B
assert polynomials(EA,6)==base and polynomials(EB,6)==base
assert degree_signature(EA,6)==(2,2,2,4,4,4)
assert degree_signature(EB,6)==(2,2,3,3,4,4)
assert isos(EA,6)!=isos(EB,6)
Be=(0,0,1,2,1,0,0)
assert containing(EA,6,(0,1))==Be
assert containing(EB,6,(0,1))==Be

expected={2:1,3:1,4:1,5:2,6:5}
collisions_by_order={}
print('Exhaustive nonisomorphic 2-tree census; coefficients ascending:')
for n,forms in levels(6):
    assert len(forms)==expected[n],(n,len(forms))
    cells=defaultdict(list)
    for E in forms:
        cells[polynomials(E,n)].append(E)
    pairs=sum(len(v)*(len(v)-1)//2 for v in cells.values())
    collisions_by_order[n]=pairs
    print('order',n,'shapes',len(forms),'pairs',pairs)
    for p,vs in sorted(cells.items(),reverse=True):
        print(' ',','.join(map(str,p)),'multiplicity',len(vs))
assert collisions_by_order=={2:0,3:0,4:0,5:0,6:1}

# Repeatedly attach t simplicial vertices to fixed edge (0,1).
# Verify the all-t symbolic polynomial by an independent binomial-coefficient computation.
def mul_oneplus(a,t):
    out=[0]*(len(a)+t)
    for i,v in enumerate(a):
        for j in range(t+1):out[i+j]+=v*comb(t,j)
    return out
for t in range(0,9):
    F=[]
    for E in (EA,EB):
        F.append(tuple(sorted(E+tuple(edge(0,k) for k in range(6,6+t))+tuple(edge(1,k) for k in range(6,6+t)))))
    valA=polynomials(F[0],6+t)
    valB=polynomials(F[1],6+t)
    assert valA==valB
    C=[a-b for a,b in zip(base,Be)]
    predicted=mul_oneplus(C,t)
    for i,b in enumerate(Be):predicted[i]+=b
    assert tuple(predicted)==valA
    assert 3 not in degree_signature(F[0],6+t)
    if t>=1:assert 3 in degree_signature(F[1],6+t)
    print('fan length',t,'type total',sum(valA),'polynomial verified')

print('PASS: exact first collision, unique six-vertex pair, all-order fan identity')
