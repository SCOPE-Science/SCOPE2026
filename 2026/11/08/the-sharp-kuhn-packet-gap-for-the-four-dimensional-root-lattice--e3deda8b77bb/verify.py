#!/usr/bin/env python3
"""Exact, standard-library-only Kuhn packet certificate for the D4 lattice."""
from itertools import permutations, product
from collections import Counter

ZERO=(0,0,0,0)

def sq(a): return sum(x*x for x in a)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def det(A):
    n=len(A)
    val=0
    for p in permutations(range(n)):
        inversions=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=1 if inversions%2==0 else -1
        for i in range(n): term*=A[i][p[i]]
        val+=term
    return val

def independent(B):
    G=[[sum(x*y for x,y in zip(a,b)) for b in B] for a in B]
    return det(G)>0

# All D4 vectors of norm squared at most four.
V=tuple(v for v in product(range(-2,3),repeat=4)
        if sum(v)%2==0 and 0<sq(v)<=4)
assert len(V)==48
assert Counter(sq(v) for v in V)=={2:24,4:24}

# Exhaustive enumeration forced by putative packet radius < sqrt(6)/2.
counts=[0]*5

def rec(B,S):
    k=len(B)
    counts[k]+=1
    if k==4: return
    for v in V:
        added=[add(s,v) for s in S]
        if any(sq(a)>4 for a in added):
            continue
        if not independent(B+[v]):
            continue
        rec(B+[v],S+added)

rec([], [ZERO])
assert counts==[1,48,816,1728,0], counts

# A D4 basis, rows having determinant of absolute value two.
B=[(-1,-1,0,0),(-1,0,-1,0),(0,1,1,0),(1,0,0,-1)]
assert abs(det(B))==2
assert all(sum(b)%2==0 for b in B)
classes=Counter()
certificate=[]
for perm in permutations(range(4)):
    p=[ZERO]
    for i in perm: p.append(add(p[-1], B[i]))
    diameter=max(sq(sub(p[i],p[j])) for i in range(5) for j in range(i+1,5))
    good=[]
    for i in range(5):
        for j in range(i+1,5):
            if sq(sub(p[i],p[j]))!=diameter: continue
            # center=(p_i+p_j)/2; squared radius <= diameter/4.
            center2=add(p[i],p[j])
            maxdist4=max(sq(sub(tuple(2*x for x in q),center2)) for q in p)
            if maxdist4<=diameter: good.append((i,j))
    assert good, (perm,p,diameter)
    assert diameter in (4,6)
    classes[diameter]+=1
    certificate.append((perm,diameter,good[0]))
assert classes==Counter({4:12,6:12}), classes
print('EXACT_OK')
print('candidate vectors',len(V),'squared norms',dict(Counter(sq(v) for v in V)))
print('ordered independent valid prefix counts k=0..4:',counts)
print('basis determinant:',det(B))
print('24 packet simplex squared-diameter classes:',dict(sorted(classes.items())))
print('first six midpoint certificates:',certificate[:6])
