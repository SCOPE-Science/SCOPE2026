#!/usr/bin/env python3
"""Independent finite verification of the commutator-to-determinant law.
All calculations use integer group multiplication and exact integer combinatorics.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd

def mul(x,y,p,c,k):
    base=p**(c+k); mod=p**k; lam=1+p**c
    return ((x[0]+pow(lam,x[1],base)*y[0])%base,(x[1]+y[1])%mod)

def inv(x,p,c,k):
    base=p**(c+k); mod=p**k; lam=1+p**c
    return (-pow(pow(lam,x[1],base),-1,base)*x[0]%base,(-x[1])%mod)

def direct_hist(p,c,k):
    base=p**(c+k); mod=p**k
    elems=list(product(range(base),range(mod)))
    inverse={x:inv(x,p,c,k) for x in elems}
    hist=Counter()
    for x in elems:
        xi=inverse[x]
        for y in elems:
            z=mul(mul(mul(x,y,p,c,k),xi,p,c,k),inverse[y],p,c,k)
            assert z[1]==0 and z[0]%p**c==0
            hist[(z[0]//p**c)%mod]+=1
    return hist, len(elems)

def ramanujan(p,s,z):
    if s==0:return 1
    m=p**s
    if z%m==0: return (p-1)*p**(s-1)
    if z%(m//p)==0: return -p**(s-1)
    return 0

def prob(p,k,t,z):
    return sum((Fraction(ramanujan(p,s,z),p**(2*s*t)) for s in range(k+1)),Fraction(0,1))/p**k

def check(p,c,k):
    hist,n=direct_hist(p,c,k); r=p**k
    assert len(hist)==r
    for z in range(r):
        assert hist[z]==prob(p,k,1,z)*n*n,(p,c,k,z,hist[z],prob(p,k,1,z)*n*n)
    # all-t predicted law must match convolution of literal group counts
    dist={z:Fraction(hist[z],n*n) for z in range(r)}
    for t in (2,3):
        conv={z:sum((dist[x]*Fraction(hist[(z-x)%r],n*n) for x in range(r)),Fraction(0,1)) for z in range(r)}
        assert all(conv[z]==prob(p,k,t,z) for z in range(r))
        dist=conv
    assert sum(hist.values())==n*n
    print(f'PASS p={p} c={c} k={k} |G|={n} identity={hist[0]} hist={[hist[i] for i in range(r)]} convolution t<=3')

def heisenberg_hist(p,k):
    r=p**k
    # H(R) horizontal coordinates (x,y); center unrestricted; the commutator is xy'-x'y.
    h=Counter((u*t-v*s)%r for u,v,s,t in product(range(r),repeat=4))
    return h

if __name__=='__main__':
    for p,c,k in ((3,1,1),(3,1,2),(3,2,1),(2,2,1),(2,2,2),(5,1,1),(3,3,1)):
        check(p,c,k)
    for p,k in ((2,1),(2,2),(3,1),(3,2)):
        h=heisenberg_hist(p,k)
        assert all(h[z]==prob(p,k,1,z)*p**(4*k) for z in range(p**k))
        print(f'PASS Heisenberg p={p} k={k} horizontal determinant law')
    print('ALL_CHECKS_PASS')
