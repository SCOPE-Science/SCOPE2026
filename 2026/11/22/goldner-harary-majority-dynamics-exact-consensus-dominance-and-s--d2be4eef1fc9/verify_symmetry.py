#!/usr/bin/env python3
"""Independently enumerate all degree-compatible graph automorphisms and orbit classes."""
from collections import Counter, defaultdict
from itertools import permutations, product

edges={
(0,1),(0,3),(0,4),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,10),
(2,3),(2,7),(3,4),(3,7),(3,8),(3,9),(3,10),(4,5),(4,9),(4,10),
(5,10),(6,7),(6,10),(7,8),(7,10),(8,10),(9,10)}
ns=[set() for _ in range(11)]
for i,j in edges: ns[i].add(j);ns[j].add(i)
classes=defaultdict(list)
for i in range(11):classes[len(ns[i])].append(i)
assert {d:len(v) for d,v in classes.items()}=={3:6,6:2,8:3}
orders=sorted(classes)
autos=[]
for blocks in product(*(permutations(classes[d]) for d in orders)):
    f=list(range(11))
    for deg, b in zip(orders, blocks):
        for i,j in zip(classes[deg],b):f[i]=j
    if all((f[a] in ns[f[b]]) for a,b in edges):autos.append(f)
assert len(autos)==12

def F(x):
    y=0
    for i,neigh in enumerate(ns):
        ones=sum((x>>j)&1 for j in neigh)
        if 2*ones >len(neigh) or (2*ones==len(neigh) and ((x>>i)&1)):
            y |=1<<i
    return y

def act(x,f):return sum(1<<f[i] for i in range(11) if ((x>>i)&1))
assert all(F(act(x,f))==act(F(x),f) for x in range(2048) for f in autos)
recurrent={x for x in range(2048) if F(F(x))==x}
assert len(recurrent)==96
seen=set();orbs=[]
for x in sorted(recurrent):
    cyc=tuple(sorted({x,F(x)}))
    if cyc in seen:continue
    img=set(tuple(sorted({act(x,f),act(F(x),f)})) for f in autos)
    assert all(c[0] in recurrent and c[-1] in recurrent for c in img)
    seen |= img;orbs.append((len(cyc),len(img)))
assert Counter(a for a,b in orbs)=={1:2,2:7}
assert Counter(b for a,b in orbs if a==2)=={2:1,3:1,6:3,12:2}
print('PASS symmetry: 12 automorphisms, 2 fixed classes, 7 two-cycle classes')
print('two-cycle orbit sizes:',dict(sorted(Counter(b for a,b in orbs if a==2).items())))
