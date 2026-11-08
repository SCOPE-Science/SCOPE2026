#!/usr/bin/env python3
"""Exact finite comparisons for square-gcd cyclic run counts.

Does not establish the unrestricted theorem, which follows by local counting
and the Chinese remainder theorem. Standard-library Python only.
"""
from collections import Counter
from math import gcd, isqrt


def factor(n):
    out=[]
    d=2
    while d*d<=n:
        if n%d==0:
            a=0
            while n%d==0:
                n//=d
                a+=1
            out.append((d,a))
        d=3 if d==2 else d+2
    if n>1:out.append((n,1))
    return out


def beta_prime_power(p,a):
    assert a>=0
    return (p**(a+1)+(-1)**a)//(p+1)


def local(p,a,r):
    assert r>=1 and a>=1
    if a==1:
        return max(0,p-r)
    b=beta_prime_power(p,a-2)
    if r<=p:
        return (p-r)*p**(a-1)+r*b
    if r<=2*p:
        return (2*p-r)*b
    return 0


def count_formula(n,r):
    z=1
    for p,a in factor(n):
        z*=local(p,a,r)
    return z


def max_formula(n):
    return min(p-1 if a==1 else 2*p-1 for p,a in factor(n))


def direct(n):
    return [isqrt(gcd(x,n))**2==gcd(x,n) for x in range(n)]


def direct_runs(f):
    n=len(f)
    runs=Counter()
    for x in range(n):
        if f[x] and not f[(x-1)%n]:
            l=0
            while f[(x+l)%n]:
                l+=1
                assert l<n
            runs[l]+=1
    return runs

cases=windows=runs_count=0
for n in range(2,901):
    good=direct(n)
    L=max_formula(n)
    assert 1<=L<n and count_formula(n,L)>0 and count_formula(n,L+1)==0
    tested=min(n+2,18)
    for r in range(1,tested+1):
        observed=sum(all(good[(x+j)%n] for j in range(r)) for x in range(n))
        predicted=count_formula(n,r)
        assert observed==predicted,(n,r,observed,predicted)
        windows+=1
    hist=direct_runs(good)
    assert sum(l*c for l,c in hist.items())==sum(good)
    assert max(hist)==L
    for l in range(1,L+1):
        expected=count_formula(n,l)-2*count_formula(n,l+1)+count_formula(n,l+2)
        assert hist[l]==expected,(n,l,hist[l],expected)
        runs_count+=1
    cases+=1
print('VERIFY_OK moduli=',cases,'window_checks=',windows,'run_multiplicity_checks=',runs_count)
for n in [4,9,25,72,225]:
    hist=direct_runs(direct(n))
    print('EXAMPLE',n,'beta=',sum(direct(n)),'max_run=',max_formula(n),'run_multiplicities=',dict(sorted(hist.items())))
