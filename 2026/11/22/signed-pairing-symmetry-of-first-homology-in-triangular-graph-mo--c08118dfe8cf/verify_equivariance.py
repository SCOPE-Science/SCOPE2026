#!/usr/bin/env python3
"""Independent checks for the signed matching-pair module and Specht dimensions."""
from itertools import combinations, permutations
from math import comb, factorial

def module(n):
    edges=list(combinations(range(n),2)); I={e:i for i,e in enumerate(edges)}
    pairs=[(i,j) for i,e in enumerate(edges) for j,f in enumerate(edges) if i<j and set(e).isdisjoint(f)]
    return edges,I,pairs

def action_character(n,sigma):
    edges,I,pairs=module(n); S=set(pairs); total=0
    for i,j in pairs:
        a=I[tuple(sorted(map(lambda t:sigma[t],edges[i])))]
        b=I[tuple(sorted(map(lambda t:sigma[t],edges[j])))]
        if tuple(sorted((a,b)))==(i,j):total+=1 if a<b else -1
    return total

def partitions_interlaced(n):
    # Pieri: all partitions lambda containing (3,1) with lambda/(3,1) a horizontal strip.
    ans=[]
    for l2 in (1,2,3):
        for l3 in (0,1):
            l1=n-l2-l3
            if l1>=3 and l1>=l2:
                p=tuple(x for x in (l1,l2,l3) if x)
                ans.append(p)
    return sorted(set(ans))

def specht_dim(p):
    n=sum(p); h=1
    for i,row in enumerate(p):
        for j in range(row):
            h*=row-j+sum(r>j for r in p[i+1:])
    return factorial(n)//h

# The 3-dimensional signed matching-pair module of S4 is the (3,1) Specht module,
# whose character equals the number of fixed ground vertices minus one.
for sigma in permutations(range(4)):
    assert action_character(4,sigma)==sum(i==sigma[i] for i in range(4))-1,(sigma,action_character(4,sigma))

for n in range(4,10):
    edges,I,pairs=module(n)
    dim=3*comb(n,4)
    assert len(pairs)==dim
    parts=partitions_interlaced(n)
    assert sum(specht_dim(p) for p in parts)==dim,(n,parts)
    for sig in (tuple(range(n)),tuple([1,0]+list(range(2,n))),tuple(list(range(1,n))+[0])):
        assert isinstance(action_character(n,sig),int)
    print(n,'dim',dim,'Pieri',parts,'Specht dims',[specht_dim(p) for p in parts])
print('EQUIVARIANCE_OK')
