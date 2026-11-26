#!/usr/bin/env python3
"""Finite exhaustive checks for pointed orbit spectra of random-graph reducts.

The finite action is on all adjacency strings to an individually named base.
The theorem's unrestricted quantifiers are proved independently of these checks.
"""
from itertools import combinations

NAMES=("graph", "complement", "switching", "both", "equality")

def finite_base_orbits(m,kind):
    if kind=="equality":return 1
    shifts=set()
    for s in range(1<<(m+1)):
        if kind in ("graph","complement") and s:continue
        for c in range(2):
            if kind in ("graph","switching") and c:continue
            if any((((s>>i)^(s>>j)^c)&1) != 0 for i,j in combinations(range(m),2)):
                continue
            mask=sum((((s>>i)^(s>>m)^c)&1)<<i for i in range(m))
            shifts.add(mask)
    assert shifts
    unseen=set(range(1<<m)); orbits=[]
    while unseen:
        b=min(unseen)
        orbit={b^shift for shift in shifts}
        assert orbit <= unseen
        unseen.difference_update(orbit)
        orbits.append(orbit)
    return len(orbits)

def formula(m,kind):
    if kind=="graph":return 1<<m
    if kind=="complement":return 1 if m<=1 else 1<<m
    if kind=="switching":return 1 if m==0 else 1<<(m-1)
    if kind=="both":return 1 if m<=2 else 1<<(m-1)
    if kind=="equality":return 1
    raise ValueError(kind)

def edge_orbits(n,kind):
    edges=list(combinations(range(n),2));E=len(edges)
    if kind=="equality":return 1
    shifts=set()
    for s in range(1<<n):
        if kind in ("graph","complement") and s:continue
        for c in range(2):
            if kind in ("graph","switching") and c:continue
            mask=sum(((((s>>i)^(s>>j)^c)&1)<<k) for k,(i,j) in enumerate(edges))
            shifts.add(mask)
    unseen=set(range(1<<E));count=0
    while unseen:
        b=min(unseen)
        orb={b^shift for shift in shifts}
        assert orb <= unseen
        unseen.difference_update(orb)
        count+=1
    return count

def tuple_formula(n,kind):
    E=n*(n-1)//2
    if kind=="graph":return 2**E
    if kind=="complement":return 2**(E-1) if E else 1
    if kind=="switching":return 2**((n-1)*(n-2)//2) if n>=1 else 1
    if kind=="both":return 2**(n*(n-3)//2) if n>=3 else 1
    if kind=="equality":return 1
    raise ValueError(kind)

def main():
    for m in range(0,8):
        found=[finite_base_orbits(m,k) for k in NAMES]
        target=[formula(m,k) for k in NAMES]
        assert found==target,(m,found,target)
        print('base m=%d %s'%(m,','.join(map(str,found))))
    for n in range(1,6):
        found=[edge_orbits(n,k) for k in NAMES]
        target=[tuple_formula(n,k) for k in NAMES]
        assert found==target,(n,found,target)
        print('injective n=%d %s'%(n,','.join(map(str,found))))
    assert len(set(tuple(formula(m,k) for m in range(0,4)) for k in NAMES))==5
    assert len(set(tuple(formula(m,k) for m in range(0,3)) for k in NAMES))<5
    assert all(formula(m,"graph")==formula(m,"complement") for m in range(2,100))
    assert all(formula(m,"switching")==formula(m,"both") for m in range(3,100))
    print('SHARP_WINDOW_AND_TAIL_COLLISIONS_PASS')
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()
