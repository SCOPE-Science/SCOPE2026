#!/usr/bin/env python3
"""Exact diagnostic checks for five-adic gamma branch-image theorem.

This checker verifies finite levels; the separate mathematical proof handles all levels.
"""
from collections import Counter
from math import prod


def gamma_mod_table(k):
    q=5**k
    a=[0]*q
    a[0]=1
    for n in range(q-1):
        # gamma(n+1)/gamma(n)=-n for n a unit, otherwise -1
        a[n+1]=(a[n]*(-n if n%5 else -1))%q
    return a


def valuation5(x):
    if x==0:
        return 10**9
    j=0
    while x%5==0:
        x//=5;j+=1
    return j


def expected_count(y,k):
    if k==1:
        return {1:3,3:1,4:1}.get(y,0)
    return (2*(y%5==1)+int(y%5==3)+5*(y%25==1)+5*(y%25==24))


def check():
    checks=0
    for k in range(1,6):
        q=5**k
        a=gamma_mod_table(k)
        obs=Counter(a)
        for y in range(q):
            assert obs[y]==expected_count(y,k), (k,y,obs[y],expected_count(y,k))
            checks+=1
        assert len(obs)==(3 if k==1 else 11*5**(k-2))
        checks+=1
        # Gamma5(n+5^k) equals Gamma5(n) mod q via all-unit Wilson product.
        cur=a[-1]
        cur=cur*(-(q-1) if (q-1)%5 else -1)%q
        assert cur==a[0]
        checks+=1
    # Exact input-distance valuations for branch residue classes at modest depth.
    k=5;q=5**k;a=gamma_mod_table(k)
    for aa in range(5):
        lam=2 if aa in (0,1) else 1
        for t in range(40):
            for u in range(t+1,40):
                x,y=aa+5*t,aa+5*u
                lhs=valuation5((a[x]-a[y])%q)
                rhs=lam+valuation5(t-u)
                assert lhs==rhs, (aa,t,u,lhs,rhs)
                checks+=1
    # Product polynomial U_a(T), coefficients, digit-step check.
    for aa in range(5):
        lam=2 if aa in (0,1) else 1
        c=4 if aa in (0,1,3) else 1
        for t in range(25):
            U=(-prod(aa+j+5*t for j in range(5) if (aa+j)%5))
            assert (U-1)//5**lam%5==c
            checks+=1
            for s in (1,2):
                q=5**(lam+s+1)
                r=prod(-prod(aa+i+5*(t+j) for i in range(5) if (aa+i)%5) for j in range(5**s))%q
                assert r==(1+c*5**(lam+s))%q,(aa,t,s,r)
                checks+=1
    print('PASS',checks,'exact finite assertions; depths 1..5, branch differences and digit products.')

if __name__=='__main__':
    check()
