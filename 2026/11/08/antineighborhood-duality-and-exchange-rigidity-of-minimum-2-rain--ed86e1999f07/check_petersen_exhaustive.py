#!/usr/bin/env python3
"""Exhaustive independent generalized-Petersen model for two-rainbow domination."""
from itertools import product
from collections import Counter
n=5
N=[set() for _ in range(10)]
for i in range(n):
    for x,y in ((i,(i+1)%n),(i,n+i),(n+i,n+(i+2)%n)):
        N[x].add(y);N[y].add(x)
assert all(len(z)==3 for z in N)

# Label mask 0 empty, 1 first color, 2 second color, 3 both.
def legal(labels):
    return all(labels[v] or (sum((labels[u]&1)>0 for u in N[v])>0 and
                              sum((labels[u]&2)>0 for u in N[v])>0) for v in range(10))

minimum=50; optimum=[]
for labels in product(range(4),repeat=10):
    weight=sum(x.bit_count() for x in labels)
    if weight>minimum:continue
    if not legal(labels):continue
    if weight<minimum:minimum=weight;optimum=[]
    optimum.append(labels)
assert minimum==5 and len(optimum)==60,(minimum,len(optimum))
opt=set(optimum)
counts=Counter((sum(x&1>0 for x in f),sum(x&2>0 for x in f),sum(x==3 for x in f)) for f in optimum)
assert counts=={(2,3,0):30,(3,2,0):30},counts
jumps=set();slides=set()
for f in optimum:
    for c in (1,2):
        for x in range(10):
            if not f[x]&c:continue
            for y in range(10):
                if f[y]&c:continue
                candidate=list(f);candidate[x]^=c;candidate[y]|=c
                cand=tuple(candidate)
                if cand not in opt:continue
                jumps.add(tuple(sorted((f,cand))))
                if y in N[x]:slides.add(tuple(sorted((f,cand))))
assert not jumps and not slides
print('Generalized Petersen P(5,2): minimum weight 5; 60 optimal colorings')
print('Support-size and overlap distribution: '+repr(dict(sorted(counts.items()))))
print('All 4^10 labelings checked; no legal single-color relocation: PASS')
