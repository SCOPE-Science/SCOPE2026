#!/usr/bin/env python3
"""Exact finite checks for distinct-part signed weights and eta cusp arithmetic."""
from fractions import Fraction
from math import gcd

def sigma_sieve(n):
    a=[0]*(n+1)
    for j in range(1,n+1):
        for k in range(j,n+1,j): a[k]+=j
    return a

def calculate(n):
    # Explicit combinatorial insertion/removal of each distinct part.
    q=[0]*(n+1); w=[0]*(n+1); q[0]=1
    for j in range(1,n+1):
        wt=j if j&1 else -j
        for k in range(n,j-1,-1):
            w[k]+=w[k-j]+wt*q[k-j]
            q[k]+=q[k-j]
    # Independently calculate Euler-quotient coefficients by the exact log derivative.
    s=sigma_sieve(n)
    b=[0]+[-7*s[k]+(6*s[k//2] if k%2==0 else 0) for k in range(1,n+1)]
    c=[0]*(n+1);c[0]=1
    for k in range(1,n+1):
        v=sum(b[j]*c[k-j] for j in range(1,k+1))
        assert v%k==0,(k,v)
        c[k]=v//k
        assert q[k]-8*w[k]==c[k],(k,q[k],w[k],c[k])
    return q,w,c

def cusp_tests():
    N=1152
    assert (24*7-48*3)%24==0
    assert ((N//24)*7-(N//48)*3)%24==0
    assert (7-3)//2==2
    assert (24**7//48**3) == 2**9*3**4
    divs=[c for c in range(1,N+1) if N%c==0]
    orders=[]
    for c in divs:
        x=gcd(c,24);y=gcd(c,48)
        bracket=Fraction(7*x*x,24)-Fraction(3*y*y,48)
        assert y in (x,2*x)
        assert bracket == (Fraction(11*x*x,48) if y==x else Fraction(x*x,24))
        order=Fraction(N,24*gcd(c,N//c)*c)*bracket
        assert order>0,(c,order)
        orders.append(order)
    assert len(divs)==24 # 1152=2^7*3^2 -> (8)(3)=24
    assert Fraction(1) in orders and Fraction(11) in orders
    print('ETA_MODULARITY_CONGRUENCES_OK weight=2 level=1152 character=Kronecker(2/d)')
    print('ALL_CUSP_ORDERS_STRICTLY_POSITIVE_OK divisors=24 min='+str(min(orders))+' max='+str(max(orders)))

if __name__=='__main__':
    cusp_tests()
    q,w,c=calculate(1100)
    print('INDEPENDENT_COEFFICIENT_IDENTITY_OK n=0..1100')
    print('FIRST_CORRECTION_COEFFICIENTS',c[:12])
    print('SAMPLES',[(j,q[j],w[j],c[j]) for j in (1,2,5,20,50,100,200,400,800,1100)])
    print('FINITE_IDENTITY_OK no_claim_of_infinite_computational_proof')
