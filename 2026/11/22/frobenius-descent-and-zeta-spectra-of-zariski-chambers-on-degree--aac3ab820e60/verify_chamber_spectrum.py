#!/usr/bin/env python3
"""Exact independent reconstructions of the degree-five del Pezzo chamber Galois set.
No external dependencies.  Run: python3 verify_chamber_spectrum.py
"""
from itertools import combinations, permutations
from collections import Counter
from math import gcd

LABELS = tuple(combinations(range(5), 2))
PARTS = [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,)]
EXPECTED = {
 (1,1,1,1,1): ((1,76),),
 (2,1,1,1): ((1,24),(2,26)),
 (2,2,1): ((1,8),(2,34)),
 (3,1,1): ((1,7),(3,23)),
 (3,2): ((1,3),(2,2),(3,7),(6,8)),
 (4,1): ((1,2),(2,3),(4,17)),
 (5,): ((1,1),(5,15)),
}
FIXED_POLYS={
 (1,1,1,1,1):(1,10,30,30,5),
 (2,1,1,1):(1,4,6,10,3),
 (2,2,1):(1,2,2,2,1),
 (3,1,1):(1,1,0,3,2),
 (3,2):(1,1,0,1,0),
 (4,1):(1,0,0,0,1),
 (5,):(1,0,0,0,0),
}

def inter(v,w):
    # v, w are (H,E1,E2,E3,E4) coefficient vectors.
    return v[0]*w[0]-sum(a*b for a,b in zip(v[1:],w[1:]))

def classes():
    E=[]
    for i in range(4):
        v=[0]*5;v[i+1]=1;E.append(tuple(v))
    L=[]
    for i,j in combinations(range(4),2):
        v=[1,0,0,0,0];v[i+1]=-1;v[j+1]=-1
        L.append((i,j,tuple(v)))
    mapping={tuple(sorted((i,4))):E[i] for i in range(4)}
    for i,j,v in L:
        mapping[tuple(a for a in range(4) if a not in (i,j))]=v
    assert len(mapping)==10
    return mapping

D=classes()
assert all(inter(D[v],D[v])==-1 for v in LABELS)
assert all(inter(D[v],D[w])==(1 if not (set(v)&set(w)) else 0)
           for v,w in combinations(LABELS,2))
assert all(inter((3,-1,-1,-1,-1),D[v])==1 for v in LABELS)

# The first reconstruction uses the geometric intersection matrix directly.
CHAMBERS=[]
for bits in range(1<<10):
    chosen=[LABELS[i] for i in range(10) if bits & (1<<i)]
    if all(inter(D[u],D[v])==0 for u,v in combinations(chosen,2)):
        CHAMBERS.append(bits)
assert len(CHAMBERS)==76
assert Counter(x.bit_count() for x in CHAMBERS)=={0:1,1:10,2:30,3:30,4:5}

# The second reconstruction uses the complete classification of pairwise-intersecting
# edge families on K5: empty, single edge, length-two star, triangle, three-star,
# four-star.  It does not use the intersection matrix enumeration.
INDEPENDENT_RECONSTRUCTION=set([0])
for v in LABELS:INDEPENDENT_RECONSTRUCTION.add(1<<LABELS.index(v))
for v in range(5):
    incident=[LABELS.index(e) for e in LABELS if v in e]
    for k in (2,3,4):
        for subset in combinations(incident,k):
            INDEPENDENT_RECONSTRUCTION.add(sum(1<<i for i in subset))
for tri in combinations(range(5),3):
    INDEPENDENT_RECONSTRUCTION.add(sum(1<<LABELS.index(e) for e in combinations(tri,2)))
assert set(CHAMBERS)==INDEPENDENT_RECONSTRUCTION


def cycle_type(perm):
    seen=set();p=[]
    for i in range(5):
        if i in seen:continue
        count=0;v=i
        while v not in seen:
            seen.add(v);v=perm[v];count+=1
        p.append(count)
    return tuple(sorted(p,reverse=True))

def canonical_perm(partition):
    out=list(range(5));start=0
    for size in partition:
        for j in range(size):out[start+j]=start+(j+1)%size
        start+=size
    return tuple(out)

def action(bits,perm):
    image=0
    for i,e in enumerate(LABELS):
        if bits & (1<<i):
            image |=1<<LABELS.index(tuple(sorted(perm[x] for x in e)))
    return image

def orbits(perm):
    unseen=set(CHAMBERS);result=[]
    while unseen:
        current=min(unseen);length=0;initial=current
        while True:
            assert current in unseen
            unseen.remove(current);length+=1
            current=action(current,perm)
            if current==initial:break
        result.append(length)
    return Counter(result)

def inv_subsets(poly,r):
    c=[1]+[0]*r
    for length in poly:
        if length>r:continue
        for i in range(r,length-1,-1):c[i]+=c[i-length]
    return c[r]

def fixed_formula(part):
    # Count the two-element/three-element invariant label sets, and invariant
    # star supports with a fixed center.  The five combinatorial types are disjoint.
    f=part.count(1)
    two=inv_subsets(part,2)
    three=inv_subsets(part,3)
    residual=list(part);residual.remove(1) if f else None
    two_away=inv_subsets(residual,2) if f else 0
    return 1+two+three+f*two_away+f*f

for part in PARTS:
    g=canonical_perm(part)
    prof=orbits(g)
    assert tuple(sorted(prof.items()))==EXPECTED[part]
    fixed=tuple(sum(action(b,g)==b and b.bit_count()==k for b in CHAMBERS)
                for k in range(5))
    assert fixed==FIXED_POLYS[part]
    assert sum(fixed)==fixed_formula(part)==prof[1]
    assert sum(d*m for d,m in prof.items())==76
    order=1
    for n in part:order=order*n//gcd(order,n)
    for extension in range(1,2*order+1):
        h=tuple(range(5))
        for _ in range(extension):h=tuple(g[h[i]] for i in range(5))
        counted=sum(action(b,h)==b for b in CHAMBERS)
        counted_from_orbits=sum(d*m for d,m in prof.items() if extension%d==0)
        assert counted==counted_from_orbits

# Every permutation in S5 is covered by the seven cycle-type rows.
counts=Counter()
for p in permutations(range(5)):
    part=cycle_type(p);counts[part]+=1
    assert tuple(sorted(orbits(p).items()))==EXPECTED[part]
assert counts=={(1,1,1,1,1):1,(2,1,1,1):10,(2,2,1):15,
                (3,1,1):20,(3,2):20,(4,1):30,(5,):24}

print('DEGREE5_CHAMBER_FROBENIUS_ALL_120_OK')
for part in PARTS:
    print(str(part), 'zeta_orbit_profile=',dict(EXPECTED[part]),
          'fixed_support_sizes=',FIXED_POLYS[part])
