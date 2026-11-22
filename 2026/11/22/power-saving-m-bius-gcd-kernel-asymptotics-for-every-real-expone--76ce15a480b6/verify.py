#!/usr/bin/env python3
"""Finite diagnostics for real-power Möbius GCD quadratic forms.
The analytic asymptotic and its error term require the written proof.
"""
from fractions import Fraction
from math import gcd, prod, isclose


def mu_sieve(n):
    mu=[1]*(n+1); mu[0]=0; composite=[False]*(n+1); primes=[]
    for i in range(2,n+1):
        if not composite[i]:primes.append(i);mu[i]=-1
        for p in primes:
            if i*p>n:break
            composite[i*p]=True
            if i%p==0:mu[i*p]=0;break
            mu[i*p]=-mu[i]
    return mu,primes


def check_exact(nmax=35):
    mu,_=mu_sieve(nmax)
    tested=0
    for s in (2,3,4):
        for n in range(1,nmax+1):
            lhs=sum(Fraction(mu[m]*mu[nn]*gcd(m,nn)**s,m*nn)
                    for m in range(1,n+1) for nn in range(1,n+1))
            rhs=Fraction(0)
            for d in range(1,n+1):
                J=sum(mu[t]*(d//t)**s for t in range(1,d+1) if d%t==0)
                v=sum((Fraction(mu[d*k],k) for k in range(1,n//d+1)),Fraction(0))
                rhs+=Fraction(J,d*d)*v*v
            assert lhs==rhs,(s,n,lhs,rhs)
            tested+=1
    return tested


def check_weighted_constant(nmax=120):
    mu,primes=mu_sieve(10000)
    checks=0
    for s in (1.25,1.5,2.,2.5,3.,4.):
        local={p:1/(1+(1-p**(-s))/p) for p in primes}
        C=prod((1-1/p)*(1+(1-p**(-s))/p) for p in primes)
        Q=65
        facsets=[set() for _ in range(Q+1)]
        for p in primes:
            for k in range(p,Q+1,p):facsets[k].add(p)
        R=lambda k,l:prod(local[p] for p in facsets[k]|facsets[l])
        Aq=[]; current=0.
        for q in range(1,Q+1):
            cur=mu[q]/q
            current+=cur*cur*R(q,q)+2*cur*sum(mu[k]/k*R(k,q) for k in range(1,q))
            Aq.append(current)
            assert current>=-1e-10,(s,q,current)
        beta=s-1
        cQ=C/beta*sum(Aq[q-1]*(q**(-beta)-(q+1)**(-beta)) for q in range(1,Q+1))
        assert cQ>C/beta*(1-2**(-beta))*.99999
        for n in (35,nmax):
            T=0.
            for d in range(1,n+1):
                if mu[d]==0:continue
                weight=d**(s-2)*prod(1-p**(-s) for p in facsets[d] if d<=Q) if d<=Q else None
                if weight is None:
                    rd=d
                    weight=d**(s-2)
                    for p in primes:
                        if p*p>rd:break
                        if rd%p==0:
                            weight*=1-p**(-s)
                            while rd%p==0:rd//=p
                    if rd>1:weight*=1-rd**(-s)
                v=sum(mu[d*k]/k for k in range(1,n//d+1))
                T+=weight*v*v
            assert T>0
            ratio=T/n**beta
            print('s',s,'N',n,'normalization',round(ratio,7),'positive_constant_lower',round(C/beta*(1-2**(-beta)),7),'truncated_constant',round(cQ,7))
            checks+=1
    return checks

if __name__=='__main__':
    e=check_exact(); c=check_weighted_constant()
    print('MOBIUS_GCD_POWER_DIAGNOSTICS_OK',e,c)
