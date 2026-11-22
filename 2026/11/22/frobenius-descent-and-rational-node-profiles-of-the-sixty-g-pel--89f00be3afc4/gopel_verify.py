#!/usr/bin/env python3
"""Exact finite combinatorial verification of arithmetic Göpel tetrad spectra.

The 16 nodes are represented as even subsets of a six-element set modulo
complement; representatives have weight zero or two. Output is integer-only.
"""
from itertools import permutations,combinations
from collections import Counter
from math import lcm
I=range(6); FULL=(1<<6)-1
V=tuple(sorted([0]+[(1<<i)|(1<<j) for i,j in combinations(I,2)]))

def normalize(u):
    assert u.bit_count() in (0,2,4,6)
    if u.bit_count()>3: u^=FULL
    assert u in V
    return u

def add(a,b): return normalize(a^b)
def pairing(a,b): return (a&b).bit_count()%2

def permute(a,p): return normalize(sum(1<<p[i] for i in I if a & (1<<i)))

def power_orbit_spectrum(items,action):
    unvisited=set(items); profile=Counter();fixed=[]
    while unvisited:
        start=min(unvisited,key=str);at=start;path=[]
        while at not in path:
            assert at in unvisited
            path.append(at);at=action(at)
        assert at==start
        for v in path:unvisited.remove(v)
        profile[len(path)]+=1
        if len(path)==1:fixed.append(start)
    return dict(sorted(profile.items())), fixed

# 15 maximal isotropic subspaces, four affine cosets each.
L={frozenset((0,a,b,add(a,b))) for a,b in combinations(V[1:],2) if pairing(a,b)==0}
assert len(L)==15
T={frozenset(add(a,u) for a in W) for W in L for u in V}
assert len(T)==60
# Independent geometric characterization: 16 trope node sets.
odd_tropes=[frozenset([0]+[(1<<i)|(1<<j) for j in I if j!=i]) for i in I]
even_tropes=[]
for triple in combinations(I,3):
    s=set(triple)
    if 0 not in s: continue # avoid double-counting complementary triples
    even_tropes.append(frozenset((1<<i)|(1<<j) for i,j in combinations(I,2) if (i in s)==(j in s)))
assert len(even_tropes)==10
TROPES=set(odd_tropes+even_tropes)
assert len(TROPES)==16
assert all(len(a&b)==2 for a,b in combinations(TROPES,2))
T_geometric={frozenset(A) for A in combinations(V,4) if all(len(set(A)&s)<3 for s in TROPES)}
assert T == T_geometric and len(T_geometric)==60

def cycle_type(p):
    unseen=set(I);types=[]
    while unseen:
        start=min(unseen);n=0;i=start
        while i in unseen:
            unseen.remove(i);n+=1;i=p[i]
        assert i==start
        types.append(n)
    return tuple(sorted(types))

rows={}
for p in permutations(I):
    typ=cycle_type(p)
    spN, fixed_nodes=power_orbit_spectrum(V,lambda a:permute(a,p))
    spL, fixed_planes=power_orbit_spectrum(L,lambda W:frozenset(permute(x,p) for x in W))
    spT, fixed_tetrads=power_orbit_spectrum(T,lambda W:frozenset(permute(x,p) for x in W))
    fixedcounts=dict(sorted(Counter(len(W.intersection(fixed_nodes)) for W in fixed_tetrads).items()))
    row=(spN,spL,spT,fixedcounts)
    if typ in rows: assert rows[typ]==row, (typ,row,rows[typ])
    else:rows[typ]=row
assert len(rows)==11
for typ,(N,Ls,Ts,fc) in sorted(rows.items()):
    assert sum(k*v for k,v in N.items())==16
    assert sum(k*v for k,v in Ls.items())==15
    assert sum(k*v for k,v in Ts.items())==60
    assert sum(fc.values()) == Ts.get(1,0)
    print(''.join(map(str,typ)), 'node',N,'lagrangian',Ls,'tetrad',Ts,'fixed-node-profile',fc)
print('GOPEL_FROBENIUS_720_PERMUTATIONS_VERIFIED_OK')
