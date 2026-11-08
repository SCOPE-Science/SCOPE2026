#!/usr/bin/env python3
"""Exact arithmetic tests for the isolation-indicator covariance in random even graphs."""
from fractions import Fraction as Q
from math import comb

def even_probability(n,p):
    assert n>=0 and Q(0)<p<Q(1)
    if n==0: return Q(1)
    x=1-2*p
    return sum((Q(comb(n,k), 2**n)*x**(k*(n-k)) for k in range(n+1)), Q(0))

def formula(n,p):
    q=1-p
    a=even_probability(n,p)
    single=q**(n-1)*even_probability(n-1,p)/a
    pair=q**(2*n-3)*even_probability(n-2,p)/a
    return pair-single**2

def direct_distribution(n):
    edges=[(i,j) for i in range(n) for j in range(i+1,n)]
    N=len(edges)
    counts=[[0]*(N+1) for _ in range(4)]
    for mask in range(1<<N):
        parity=0
        for t,(u,v) in enumerate(edges):
            if mask>>t&1: parity^=(1<<u)|(1<<v)
        if parity: continue
        ec=mask.bit_count()
        iso=[all(not ((mask>>i)&1) for i,(u,v) in enumerate(edges) if w in (u,v)) for w in (0,1)]
        counts[0][ec]+=1
        counts[1][ec]+=int(iso[0])
        counts[2][ec]+=int(iso[1])
        counts[3][ec]+=int(iso[0] and iso[1])
    return counts

def direct_cov(n,p,coeff):
    N=n*(n-1)//2
    vals=[sum((Q(c)*p**k*(1-p)**(N-k) for k,c in enumerate(row)),Q(0)) for row in coeff]
    assert vals[0]>0
    return vals[3]/vals[0] - vals[1]*vals[2]/vals[0]**2

def tests():
    checks=0
    for n in range(3,7):
        coeff=direct_distribution(n)
        assert sum(coeff[0])==2**((n-1)*(n-2)//2); checks+=1
        for a,b in [(1,11),(1,5),(1,2),(2,3),(4,5),(9,10),(19,20)]:
            p=Q(a,b)
            assert formula(n,p)==direct_cov(n,p,coeff),(n,p); checks+=1
    for n in range(3,19):
        assert formula(n,Q(1,2))==Q(1,2**(2*n-4)),n;checks+=1
    for a in range(1,100):
        p=Q(a,100)
        actual=formula(4,p)
        claimed=p**3*(1-p)**2*(2-3*p)/(6*p*p-4*p+1)**2
        assert actual==claimed,(p,actual,claimed);checks+=1
    for n in range(4,24,2):
        assert formula(n,Q(1,2))>0;checks+=1
        assert formula(n,Q(99,100))<0,(n,formula(n,Q(99,100)));checks+=1
    for n in range(3,24,2):
        assert formula(n,Q(9999,10000))>0,n; checks+=1
        ratio=formula(n,Q(9999,10000))/Q(1,10000)**(2*n-3)
        assert Q(9,10)<ratio<Q(11,10),(n,ratio); checks+=1
    print('PASS: %d exact comparisons; exhaustive parity-filtered graph enumeration for n=3..6.'%checks)

if __name__=='__main__': tests()
