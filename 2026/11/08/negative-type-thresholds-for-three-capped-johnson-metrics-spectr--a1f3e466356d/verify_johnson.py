#!/usr/bin/env python3
"""Exact low-order Johnson-shell verification and numerical asymptotic diagnostics.
Standard library only. The numerical diagnostics are not a proof of the infinite-family theorem.
"""
from itertools import combinations
from math import comb, expm1, log

def eigen(n, k, j):
    t = (k-j)*(n-k-j)-j
    assert (t*t-(n-2)*t-k*(n-k)) % 4 == 0
    u = (t*t-(n-2)*t-k*(n-k))//4
    return t,u

def lam(n,k,j,a):
    t,u=eigen(n,k,j)
    s=expm1(a*log(3.0))
    r=expm1(a*log(2.0))
    return -1-s*(1+t)-(s-r)*u

def endpoint(n,k):
    lo,hi=0.0,1.0
    for _ in range(68):
        mid=(lo+hi)/2
        if max(lam(n,k,j,mid) for j in range(1,k+1)) <= 0: lo=mid
        else:hi=mid
    return (lo+hi)/2

def exact_test(n,k):
    all_points=frozenset(range(2*k))
    universe=range(n)
    sets=[frozenset(c) for c in combinations(universe,k)]
    assert sum(comb(n,j)-comb(n,j-1) for j in range(1,k+1))+1==len(sets)
    for j in range(1,k+1):
        def f(S):
            out=1
            for a in range(j):
                out*=int(2*a in S)-int(2*a+1 in S)
            return out
        vals=[f(S) for S in sets]
        assert any(vals) and sum(vals)==0
        t,u=eigen(n,k,j)
        for S in sets:
            outsiders=set(universe)-S
            e1=sum(f((S-{a})|{b}) for a in S for b in outsiders)
            e2=sum(f((S-set(x))|set(y)) for x in combinations(S,2) for y in combinations(outsiders,2))
            assert e1==t*f(S), (n,k,j,S,e1,t*f(S))
            assert e2==u*f(S), (n,k,j,S,e2,u*f(S))
    print('exact_johnson_harmonics',n,k,'PASS',len(sets))

for n,k in [(8,4),(9,4),(10,5),(12,5)]: exact_test(n,k)
assert abs(endpoint(8,4)-log(2)/log(3))<1e-11
for k in [4,5,6,8,10]:
    for n in [2*k,3*k,4*k,6*k]:
        a=endpoint(n,k)
        j=max(range(1,k+1),key=lambda i:lam(n,k,i,a))
        if n>=4*k: assert j==k-1
        assert 0<a<1
        print('power',n,k,round(a,10),'j',j)
L=log(1.5)
for c in [2,2.1,2.5,3,4,8]:
    if c==2: D=2
    else:
        r=(c+2)/(2*(c-2)); near=max(0,round(r));a=(c-2)*near-1
        D=c*a+c-1-a*a
    target=4/(L*D)
    for k in [100,500]:
        n=round(c*k)
        got=endpoint(n,k)*k*k
        print('asymptotic',c,k,'target',round(target,6),'observed',round(got,6))
        assert abs(got/target-1)<0.3, (c,k,target,got)
print('JOHNSON_THREE_CAP_SPECTRAL_CHECKS_PASS')
