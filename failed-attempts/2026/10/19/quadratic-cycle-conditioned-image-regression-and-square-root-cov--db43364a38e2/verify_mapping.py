#!/usr/bin/env python3
"""Exact reproducibility checks for random-mapping cyclic/image dependence.

Requires only the Python standard library. Finite checks are not the proof.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import factorial, comb, exp, pi, sqrt


def falling(a, k):
    v = 1
    for i in range(k):
        v *= a-i
    return v


def cyclic_count(f):
    n=len(f)
    seen=[0]*n
    cnt=0
    for u in range(n):
        if seen[u]:
            continue
        stack=[]
        x=u
        while seen[x]==0:
            seen[x]=1
            stack.append(x)
            x=f[x]
        if seen[x]==1:
            y=x
            while True:
                cnt+=1
                y=f[y]
                if y==x:
                    break
        for y in stack:
            seen[y]=2
    return cnt


def exact_conditional_pmf(n,c,ell):
    if c==n:
        return F(1 if ell==0 else 0)
    m=n-c
    if not 0<=ell<=m:
        return F(0)
    return F(comb(m,ell))*sum(
        ( -1 if j%2 else 1 ) * comb(m-ell,j)*F(n-ell-j,n)**(m-1)
        for j in range(m-ell+1)
    )


def moment(n,c,s):
    if c==n:
        return F(1 if s==0 else 0)
    return F(falling(n-c,s))*F(n-s,n)**(n-c-1) if s<=n-c else F(0)


def conditional_range_mean(n,c):
    return F(n) if c==n else F(n) - F(n-c)*F(n-1,n)**(n-c-1)


def means(n):
    q=F(n-1,n)
    mu=sum((F(falling(n,k),n**k) for k in range(1,n+1)),F(0))
    er=F(n)*(1-q**n)
    return mu,er


def test_exhaustive():
    total=0
    comparisons=0
    for n in range(2,7):
        table=Counter()
        for f in product(range(n),repeat=n):
            c=cyclic_count(f)
            missing=n-len(set(f))
            table[c,missing]+=1
        assert sum(table.values())==n**n
        for c in range(1,n+1):
            count_c=sum(table[c,k] for k in range(n-c+1))
            assert F(count_c,n**n)==F(c*falling(n,c),n**(c+1))
            for ell in range(n-c+1):
                assert F(table[c,ell],count_c)==exact_conditional_pmf(n,c,ell),(n,c,ell)
                comparisons+=1
            lm=sum((F(ell*table[c,ell],count_c) for ell in range(n-c+1)), F(0))
            assert F(n)-lm==conditional_range_mean(n,c)
            for s in range(n-c+1):
                ml=sum((F(falling(ell,s)*table[c,ell],count_c) for ell in range(n-c+1)),F(0))
                assert ml==moment(n,c,s)
                comparisons+=1
        ec=sum((F(c*ct,n**n) for (c,ell),ct in table.items()),F(0))
        er=sum((F((n-ell)*ct,n**n) for (c,ell),ct in table.items()),F(0))
        ecr=sum((F(c*(n-ell)*ct,n**n) for (c,ell),ct in table.items()),F(0))
        mu, mr=means(n)
        mu_prev=means(n-1)[0]
        assert ec==mu and er==mr
        assert ecr-ec*er==F(n)*F(n-1,n)**n*(mu-mu_prev)
        total+=n**n
    print('Exhaustive maps:',total,'conditional pmf/factorial tests:',comparisons,'pass')


def test_symbolic_finite():
    checks=0
    for n in range(2,71):
        q=F(n-1,n)
        for c in range(1,n):
            incr=conditional_range_mean(n,c+1)-conditional_range_mean(n,c)
            expected=F(c,n)*q**(n-c-2)
            assert incr==expected,(n,c)
            checks+=1
        mu=means(n)[0]
        prev=means(n-1)[0]
        cov=F(n)*q**n*(mu-prev)
        assert cov>0
    print('Exact finite-n increase checks:',checks,'pass')


def test_asymptotics():
    target=exp(-1)*sqrt(pi/8)
    for n in (100,500,2000):
        p=1.0
        mu=0.0
        for c in range(1,n+1):
            p*= (n-c+1)/n
            mu+=p
        pn=1.0
        mup=0.0
        for c in range(1,n):
            pn*= (n-c)/(n-1)
            mup+=pn
        cov=n*((n-1)/n)**n*(mu-mup)
        got=cov/sqrt(n)
        print('n=',n,'Cov/sqrt(n)=',round(got,9),'limit=',round(target,9))
        assert abs(got-target)<0.07
    print('Asymptotic checks passed')


if __name__=='__main__':
    test_exhaustive()
    test_symbolic_finite()
    test_asymptotics()
