#!/usr/bin/env python3
"""Exact integer-cyclotomic certificate for parking-function Fourier zero sets.
Python 3 standard library only. Run: python verify.py
"""
from itertools import product, combinations_with_replacement
from collections import Counter
from math import factorial

PHI = {3: (1,1,1), 4: (1,0,1), 5: (1,1,1,1,1), 6: (1,-1,1)}

def parking(word):
    return all(x <= i for i, x in enumerate(sorted(word)))

def division_remainder(coeff, phi):
    v = list(coeff)
    d = len(phi)-1
    for k in range(len(v)-1,d-1,-1):
        q = v[k]
        if q:
            for j in range(d+1):
                v[k-d+j] -= q*phi[j]
    assert all(c==0 for c in v[d:])
    return tuple(v[:d])

def orbit_size(sorted_freq):
    c=Counter(sorted_freq)
    x=factorial(len(sorted_freq))
    for num in c.values(): x//=factorial(num)
    return x

def exact_census(n):
    m=n+1
    pfs=[w for w in product(range(n),repeat=n) if parking(w)]
    assert len(pfs)==m**(n-1)
    # Check Pollak's transversal by identifying diagonal-shift classes.
    orbitkeys={tuple((w[i]-w[0])%m for i in range(1,n)) for w in pfs}
    assert len(orbitkeys)==len(pfs)
    forced=0; extras=[]; examined=0; zero_orbits=[]
    for u in combinations_with_replacement(range(m),n):
        counts=[0]*m
        for a in pfs:
            residue=sum(x*y for x,y in zip(u,a))%m
            counts[residue]+=1
        iszero=not any(division_remainder(counts,PHI[m]))
        isforced=(sum(u)%m==0 and any(u))
        if isforced: assert iszero,(n,u)
        sz=orbit_size(u)
        examined+=sz
        if iszero:
            zero_orbits.append((u,sz))
            if isforced:forced+=sz
            else:extras.append((u,sz))
    assert examined==m**n
    expected={2:((m**(n-1)-1),0),3:(m**(n-1)-1,0),4:(m**(n-1)-1,0),5:(m**(n-1)-1,360)}[n]
    assert (forced,sum(size for _,size in extras))==expected
    return m,len(pfs),len(zero_orbits),forced,extras

def independently_simulate_parking(word):
    n=len(word)
    used=[False]*n
    for prefer in word:
        j=prefer
        while j<n and used[j]:j+=1
        if j==n:return False
        used[j]=True
    return True

for n in range(2,6):
    for w in product(range(n),repeat=n):
        assert parking(w)==independently_simulate_parking(w)
    m,total,zero_orbits,forced,extras=exact_census(n)
    print(f'n={n} m={m} support={total} zero_orbits={zero_orbits} forced={forced} extras={sum(z for _,z in extras)} rank={m**n-forced-sum(z for _,z in extras)}')
    if n==5:
        print('exact additional zero orbits:')
        for u,sz in extras:print('  ',u,'size',sz)
        assert sorted((tuple(u),sz) for u,sz in extras)==sorted([
            ((1,2,3,3,4),60),((1,2,3,3,5),60),((1,2,3,4,5),120),
            ((1,3,3,4,5),60),((2,3,3,4,5),60)])
print('ALL EXACT CHECKS PASSED')
