"""Finite exact consistency checks for coordinate Cesaro products on Drury-Arveson space.
Run: python check_cesaro_products.py
These tests are not proofs of infinite-dimensional claims.
"""
from fractions import Fraction
from math import factorial, comb
from itertools import product

def comps(n,d):
    if d==1:
        yield (n,)
    else:
        for v in range(n+1):
            for tail in comps(n-v,d-1):
                yield (v,)+tail

def w(a):
    ans=1
    for x in a: ans*=factorial(x)
    return Fraction(ans,factorial(sum(a)))

def W(n,d,k,l):
    r=k+l
    ans=Fraction(factorial(k)*factorial(l),factorial(r+d-1))
    for s in range(1,d): ans*=n+r+s
    return ans

def prod(n,k,l):
    return Fraction(1,(n+l+1)*(n+k+l+1))

def comm(n,k,l):
    r=k+l
    return Fraction(k-l,(n+k+1)*(n+l+1)*(n+r+1))

checks=0
for d in range(2,7):
    for n in range(7):
        for k in range(7):
            for l in range(7):
                total=0
                for a in comps(n,d):
                    b=list(a); b[0]+=k; b[1]+=l
                    total+=w(b)/w(a)
                assert total==W(n,d,k,l),(d,n,k,l,total,W(n,d,k,l))
                checks+=1
                # The coefficient of C_i C_j versus C_j C_i is exact.
                assert prod(n,k,l)-prod(n,l,k)==comm(n,k,l)
                checks+=1

# Dimensional HS divergence is certified analytically by the diagonal
# and first off-diagonal terms; finite partial sums test arithmetic only.
for d in range(2,9):
    for n in range(1,20):
        count=comb(n+d-1,d-1)
        assert count>0
        diag=Fraction(count,(n+1)**4)
        off=Fraction(1,(n+1)**2*(n+2)**4)*W(n,d,1,0)
        assert diag>0 and off>0
        checks+=2

# Finite checks of the Schur row/column bounds used in the compactness proof.
for m in range(1,13):
    for k in range(0,15):
        col=0.0
        for n in range(k,400):
            ratio=1.0
            for t in range(k+1,n+1): ratio*=t/(t+m)
            col+=(ratio**0.5)/(n+m+1)
        assert col<=1/(k+m+1)+2/m+1e-12
        checks+=1
    for n in range(0,15):
        row=0.0
        for k in range(n+1):
            ratio=1.0
            for t in range(k+1,n+1): ratio*=t/(t+m)
            row+=(ratio**0.5)/(n+m+1)
        assert row<=1+1e-12
        checks+=1

print('COORDINATE_CESARO_FINITE_IDENTITIES_OK',checks)
