#!/usr/bin/env python3
"""Finite verification of the squarefree-word semiring homomorphism census.
Usage: python3 verify.py
No external dependencies.
"""
from itertools import product
from math import comb, factorial

Z = -1

def elems(n):
    return tuple([Z] + list(range(1,1<<n)))

def plus(a,b):
    return Z if a == Z or b == Z else a | b

def times(a,b):
    return Z if a == Z or b == Z or (a & b) else a | b

def valid(k,m,table):
    source=elems(k)
    target=set(elems(m))
    if len(table)!=len(source) or any(t not in target for t in table): return False
    f=dict(zip(source,table))
    return all(f[plus(a,b)]==plus(f[a],f[b]) and
               f[times(a,b)]==times(f[a],f[b])
               for a in source for b in source)

def from_atoms(k,m,images):
    f={Z:Z}
    for a in range(1,1<<k):
        v=0
        for i in range(k):
            if a & (1<<i):
                im=images[i]
                if im==Z or (v&im):
                    v=Z;break
                v|=im
        f[a]=v
    return tuple(f[a] for a in elems(k))

def compatible(images):
    return all(a==Z or b==Z or (a&b)==0
               for i,a in enumerate(images) for b in images[i+1:])

def rank_counter(k,m):
    out={}
    for images in product(elems(m),repeat=k):
        if not compatible(images):continue
        table=from_atoms(k,m,images)
        assert valid(k,m,table)
        s=sum(a!=Z for a in images)
        assert len(set(table))==1<<s
        out[s]=out.get(s,0)+1
    assert sum(out.values())==(k+1)**m
    for s,n in out.items():
        predicted=comb(k,s)*sum((-1)**i*comb(s,i)*(s+1-i)**m for i in range(s+1))
        assert n==predicted,(k,m,s,n,predicted)
    return out

# Independent exhaustive verification of all source-to-target *functions*,
# not just the proposed form, in three small hom-sets.
for k,m in ((1,3),(2,2),(2,3),(3,2)):
    source=elems(k);target=elems(m)
    total=0
    for table in product(target,repeat=len(source)):
        if valid(k,m,table):
            total+=1
            atoms=tuple(table[source.index(1<<i)] for i in range(k))
            assert compatible(atoms)
            assert table==from_atoms(k,m,atoms)
    assert total==(k+1)**m,(k,m,total)
    print('FULL_FUNCTIONS',k,m,total)

for k in range(1,6):
    d=rank_counter(k,k)
    idempotents=0
    automorphisms=0
    for images in product(elems(k),repeat=k):
        if not compatible(images):continue
        table=from_atoms(k,k,images)
        f=dict(zip(elems(k),table))
        if all(f[f[a]]==f[a] for a in elems(k)):
            idempotents+=1
            assert all(v==Z or v==(1<<i) for i,v in enumerate(images))
        automorphisms += len(set(table))==len(elems(k))
    assert idempotents==(1<<k)
    assert automorphisms==factorial(k)
    print('ENDOMORPHISMS',k, (k+1)**k,'RANKS',sorted(d.items()),'RETRACTIONS',idempotents,'AUTOS',automorphisms)
print('VERIFY_OK')
