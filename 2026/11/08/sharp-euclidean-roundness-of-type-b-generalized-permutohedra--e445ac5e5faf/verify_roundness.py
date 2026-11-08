#!/usr/bin/env python3
"""Finite checks of the sharp type-B orbit-polytope roundness theorem.
All general-dimensional assertions require the analytic proof."""
from itertools import permutations, product
from math import comb, sqrt, isclose


def fit_profile(n):
    return [sqrt(k)-sqrt(k-1) for k in range(1,n+1)]


def rank(rows, eps=1.e-8):
    a=[list(x) for x in rows]
    if not a:return 0
    m=len(a); n=len(a[0]); h=0
    for j in range(n):
        pivot=max(range(h,m),key=lambda i:abs(a[i][j])) if h<m else None
        if pivot is None or abs(a[pivot][j])<eps:continue
        a[h],a[pivot]=a[pivot],a[h]
        q=a[h][j]
        for col in range(j,n):a[h][col]/=q
        for i in range(h+1,m):
            f=a[i][j]
            for col in range(j,n):a[i][col]-=f*a[h][col]
        h+=1
        if h==m:break
    return h


def orbit(b):
    n=len(b)
    return [tuple(s[i]*p[i] for i in range(n)) for p in permutations(b) for s in product((-1,1),repeat=n)]


def normals(n):
    for t in product((-1,0,1), repeat=n):
        if any(t): yield t


def check_n(n):
    b=fit_profile(n); vertices=orbit(b)
    assert len(vertices)==(2**n)*__import__('math').factorial(n)
    expected=3**n-1; count=0
    for v in normals(n):
        k=sum(x!=0 for x in v)
        rhs=sum(b[:k])
        support=max(sum(a*x for a,x in zip(v,z)) for z in vertices)
        assert isclose(rhs,sqrt(k),abs_tol=1e-10,rel_tol=1e-10)
        assert isclose(support,rhs,abs_tol=1e-10,rel_tol=1e-10)
        tight=[z for z in vertices if abs(sum(a*x for a,x in zip(v,z))-rhs)<1e-9]
        # Each signed subset support is a genuine facet of codimension one.
        assert rank([[z[i]-tight[0][i] for i in range(n)] for z in tight[1:]])==n-1
        count+=1
    assert count==expected
    return len(vertices),count


def check_bound(n):
    b=fit_profile(n)
    assert all(b[i]>b[i+1]>0 for i in range(n-1))
    ds=sum(x*x for x in b)
    for k in range(1,n+1):
        assert isclose(sum(b[:k]),sqrt(k),abs_tol=1e-11)
    tests=[list(range(n,0,-1)),[3.0]+[1.0]*(n-1), [1.0/(k+1) for k in range(n)], b]
    for w in tests:
        radius=min(sum(w[:k])/sqrt(k) for k in range(1,n+1))
        outer=sqrt(sum(x*x for x in w))
        assert radius/outer <= 1/sqrt(ds)+1.e-11
    return 1/sqrt(ds)


def main():
    checked=0
    for n in range(2,6):
        vs,fs=check_n(n)
        checked+=fs
        print(f'n={n} vertices={vs} tangent_facets={fs} best_radius_ratio={check_bound(n):.12f}')
    for n in range(6,128):check_bound(n)
    print('TYPE_B_SHARP_ROUNDNESS_CHECKS_PASSED facet_checks=',checked,'dimensions_checked=',126)

if __name__=='__main__':main()
