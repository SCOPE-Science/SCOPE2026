#!/usr/bin/env python3
"""Finite-field flag counts for Singer prime quotients of spherical buildings.
Pure standard-library implementation; exact integer checks only.
"""
from collections import defaultdict
from itertools import combinations

def mul(a,b,n,mod):
    x=0
    while b:
        if b&1:x^=a
        b >>= 1; a<<=1
        if a&(1<<n): a^=mod
    return x

def subspace_catalogue(n):
    all_subspaces={1:0}  # bit zero set means contains vector 0
    waiting=[1]
    while waiting:
        s=waiting.pop()
        basis_members=[v for v in range(1<<n) if s>>v&1]
        for v in range(1,1<<n):
            if s>>v&1:continue
            t=s
            for u in basis_members:t |= 1<<(u^v)
            if t not in all_subspaces:
                all_subspaces[t]=(t.bit_count().bit_length()-1)
                waiting.append(t)
    assert len(all_subspaces)==sum(gaussian(n,k) for k in range(n+1))
    return {s:d for s,d in all_subspaces.items() if 0<d<n}

def gaussian(n,k):
    numerator=1;denominator=1
    for j in range(k):numerator*=2**(n-j)-1; denominator*=2**(k-j)-1
    return numerator//denominator

def fvector(n, subspaces):
    by_dim=defaultdict(list)
    for s,d in subspaces.items():by_dim[d].append(s)
    f=[0]*(n-1)
    for r in range(1,n):
        for dims in combinations(range(1,n),r):
            layers=[by_dim[d] for d in dims]
            def go(prev,idx):
                if idx==len(layers):return 1
                return sum(go(s,idx+1) for s in layers[idx] if prev&s==prev)
            f[r-1]+=sum(go(s,1) for s in layers[0])
    return f

def count_free(n,mod,exponent,p):
    subs=subspace_catalogue(n)
    alpha=2
    beta=1
    for i in range(exponent):beta=mul(beta,alpha,n,mod)
    t=beta; order=1
    while t!=1:
        t=mul(t,beta,n,mod); order+=1
        assert order<=p
    assert order==p
    vectors=list(range(1<<n))
    k=1
    for j in range(1,p):
        k=mul(k,beta,n,mod)
        for s in subs:
            t=0
            for v in vectors:
                if s>>v&1:t|=1<<mul(k,v,n,mod)
            assert t!=s, ('found invariant proper subspace',n,j,s)
    f=fvector(n,subs)
    d=n-2; b=2**(n*(n-1)//2)
    assert 1-sum((-1)**j*x for j,x in enumerate(f))==(-1)**(d+1)*b  # reduced Euler
    assert all(x%p==0 for x in f)
    qf=[x//p for x in f]
    chi=sum((-1)**j*x for j,x in enumerate(qf))
    top=(-1)**d*(chi-1)
    assert top==(b+((-1)**d)*(1-p))//p
    print(f'n={n}, p={p}, field_polynomial={mod:#x}, subgroup_generator={beta}, original_f={f}, quotient_f={qf}, quotient_Euler={chi}, top_Betti={top}')

if __name__=='__main__':
    count_free(4,0b10011,3,5)
    count_free(5,0b100101,1,31)
    print('CHECKS_PASSED')
