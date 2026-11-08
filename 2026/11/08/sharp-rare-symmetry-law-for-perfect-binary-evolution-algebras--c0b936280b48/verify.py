#!/usr/bin/env python3
"""Direct binary-matrix verification of algebraic symmetry enumeration.
Only finite tests: unrestricted assertions require separate proof.
"""
from itertools import permutations
from collections import Counter
from math import factorial

def rank(rows,n):
    a=list(rows); r=0
    for bit in range(n):
        pivot=next((j for j in range(r,n) if a[j]>>bit&1),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        for j in range(n):
            if j!=r and (a[j]>>bit&1):a[j]^=a[r]
        r+=1
    return r

def fixed(rows,p,n):
    return all(((rows[p[i]]>>p[j])&1)==((rows[i]>>j)&1) for i in range(n) for j in range(n))

def counts(n):
    perms=list(permutations(range(n))); s=Counter(); total=0
    for bitstring in range(1<<(n*n)):
        rows=[(bitstring>>(i*n))&((1<<n)-1) for i in range(n)]
        if rank(rows,n)!=n:continue
        total+=1; fix=[p for p in perms if fixed(rows,p,n)]
        s[len(fix)]+=1
    assert sum(k*v for k,v in s.items()) % factorial(n)==0
    orbit=sum(k*v for k,v in s.items())//factorial(n)
    tau=tuple([1,0]+list(range(2,n))) if n>=2 else tuple(range(n))
    direct_tau=0
    for bitstring in range(1<<(n*n)):
        rows=[(bitstring>>(i*n))&((1<<n)-1) for i in range(n)]
        if rank(rows,n)==n and fixed(rows,tau,n):direct_tau+=1
    predicted=2**(2*n-3)*gl(n-2) if n>=2 else 1
    assert direct_tau==predicted,(n,direct_tau,predicted)
    assert total==gl(n)
    return total,orbit,s,direct_tau

def gl(n):
    k=1
    for i in range(n):k*=2**n-2**i
    return k

for n, expected_orbits in ((1,1),(2,4),(3,33),(4,908)):
    total,orbits,stabilizers,transfix=counts(n)
    assert orbits==expected_orbits,(n,orbits)
    print('DIRECT_OK', 'n=',n,'GL=',total,'orbits=',orbits,
          'transposition_fixed=',transfix,'stabilizers=',sorted(stabilizers.items()))
print('VERIFY_OK')
