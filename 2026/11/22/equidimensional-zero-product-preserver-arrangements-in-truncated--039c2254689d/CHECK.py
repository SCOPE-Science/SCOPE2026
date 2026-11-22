"""Finite checks for linear zero-product preservers of truncated polynomials.

Run with the Python standard library: python3 CHECK.py
"""
from itertools import product, combinations
from math import comb, prod


def valid(n, v):
    return all(v[i] + v[j] >= n for i in range(1, n) for j in range(1, n) if i + j >= n)


def minimal_profiles(n):
    return [v for v in product(range(n + 1), repeat=n - 1)
            if valid(n, (0,) + v) and not any(v[i] > 0 and valid(n, (0,) + v[:i] + (v[i]-1,) + v[i+1:]) for i in range(n-1))]


def exact_count(n, q):
    weight = [(q-1) * q**(n-i-1) for i in range(n)] + [1]
    return q**n * sum(prod(weight[a] for a in vs) for vs in product(range(n+1), repeat=n-1) if valid(n, (0,) + vs))


def union_count(n,q, profiles):
    total=0
    for r in range(1,len(profiles)+1):
        for ss in combinations(profiles,r):
            exp=n*n-sum(max(t[i] for t in ss) for i in range(n))
            total+=(-1)**(r+1)*q**exp
    return total


def multiply(x,y,q):
    n=len(x)
    a=[0]*n
    for i,u in enumerate(x):
        for j,v in enumerate(y[:n-i]):
            a[i+j]=(a[i+j]+u*v)%q
    return tuple(a)


def explicit_matrix_enumeration(n,q):
    all_vectors=list(product(range(q),repeat=n))
    zeros=tuple([0]*n)
    # Uses actual truncated polynomial multiplication, not the valuation criterion.
    pids={(i,j) for i in range(n) for j in range(n) if i+j>=n}
    zero_pair={(a,b) for a,x in enumerate(all_vectors) for b,y in enumerate(all_vectors) if multiply(x,y,q)==zeros}
    total=0
    for cols in product(range(len(all_vectors)),repeat=n):
        if all((cols[i],cols[j]) in zero_pair for i,j in pids):total+=1
    return total


def check():
    for n in range(2,8):
        profiles=minimal_profiles(n)
        assert len(profiles)==comb(n-1,(n-1)//2)
        assert all(sum(p)==n*(n-1)//2 for p in profiles)
        assert all(all(p[i]<=p[i+1] for i in range(n-2)) for p in profiles)
        assert all(all(p[i-1]+p[n-i-1]==n for i in range(1,n)) for p in profiles)
        assert all(any(all(u[i]<=v[i] for i in range(n-1)) for u in profiles)
                   for v in product(range(n+1),repeat=n-1) if valid(n,(0,)+v))
        if n<=5:
            for q in (2,3):
                assert exact_count(n,q)==union_count(n,q,[(0,)+x for x in profiles])
        print('PROFILE',n,len(profiles),'DIM',n*(n+1)//2)
    for n,q in ((2,2),(2,3),(3,2),(3,3),(4,2)):
        a=exact_count(n,q);b=explicit_matrix_enumeration(n,q)
        assert a==b,(n,q,a,b)
        print('EXACT_MATRIX',n,q,a)
    print('ZERO_PRODUCT_COMPONENT_CHECKS_PASSED')

if __name__=='__main__':check()
