#!/usr/bin/env python3
"""Finite exact checks for the primitive cyclic-word Walsh frame theorem.

Python 3 standard library only. Numerical diagonalization is not needed:
exact Gram entries and Fourier eigen-equations are tested separately.
"""
from itertools import product
from math import cos, sin, pi, isqrt, gcd

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def mu(n):
    p=2; ans=1
    while p*p<=n:
        if n%p==0:
            n//=p;ans=-ans
            if n%p==0:return 0
            while n%p==0:n//=p
        p+=1
    if n>1:ans=-ans
    return ans

def primes(n):
    return [d for d in divisors(n) if d>1 and all(d%j for j in range(2,isqrt(d)+1))]

def primitive(x):
    n=len(x)
    return all(any(x[i]!=x[(i+d)%n] for i in range(n)) for d in divisors(n) if d<n)

def model(n):
    ds=divisors(n)
    count=sum(mu(q)*2**(n//q) for q in ds)
    eig=[sum(mu(q)*q*2**(n//q) for q in ds if k%q==0) for k in range(n)]
    return count,eig

for n in range(2,14):
    words=[x for x in product((-1,1),repeat=n) if primitive(x)]
    N,L=model(n)
    assert len(words)==N
    G=[[sum(x[i]*x[j] for x in words) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            expect=sum(mu(q)*2**(n//q) for q in divisors(n) if (i-j)%(n//q)==0)
            assert G[i][j]==expect, (n,i,j)
    # Independent Fourier-eigen-equation check (floating point roots of unity).
    for k in range(n):
        for i in range(n):
            got=sum(G[i][j]*complex(cos(2*pi*k*j/n),sin(2*pi*k*j/n)) for j in range(n))
            exp=L[k]*complex(cos(2*pi*k*i/n),sin(2*pi*k*i/n))
            assert abs(got-exp)<1.e-8*max(1,N),(n,k,i,got,exp)
    assert sum(L)==n*N
    if n>=3:
        assert min(L)>0 and max(L)==2**n
for n in range(3,201):
    ps=primes(n)
    subsets=[]
    for bits in product((0,1), repeat=len(ps)):
        S=frozenset(p for p,b in zip(ps,bits) if b)
        d=1
        for p in S:d*=p
        F=sum(mu(q)*q*2**(n//q) for q in divisors(d))
        subsets.append((S,F))
    D=dict(subsets)
    for S,v in subsets:
        for p in ps:
            if p not in S:
                w=D[S|{p}]
                assert v>=w
                if v==w:
                    assert n==2*p and p%2==1 and S==frozenset((2,)),(n,S,p)
    N,L=model(n)
    assert min(L)==D[frozenset(ps)]
    assert max(L)==2**n
print('PRIMITIVE_CYCLIC_WALSH_PASS enumerate_n=2..13; exact_Mobius_n=3..200; Fourier_eigenchecks_n=2..13')
