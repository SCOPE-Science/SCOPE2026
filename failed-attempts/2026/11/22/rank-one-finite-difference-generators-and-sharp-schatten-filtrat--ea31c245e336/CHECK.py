#!/usr/bin/env python3
"""Exact finite checks for critical Gaussian-Fock jet difference identities.

Finite checks only; the proof in RESULT.md handles every integer order and
all infinitely many Fock basis vectors.
"""
from math import comb, factorial, prod

checks=0

def numerator(h, j, k):
    if k < j:
        return 0
    return prod(k - j + a for a in range(1, h + 1))

def difference(h,j,r,k):
    return sum((-1)**(r-s)*comb(r,s)*numerator(h,j+s,k) for s in range(r+1))

def poly_mul(p,q):
    v=[0]*(len(p)+len(q)-1)
    for a,x in enumerate(p):
        for b,y in enumerate(q):
            v[a+b]+=x*y
    return v

def poly_num(h,j):
    p=[1]
    for a in range(1,h+1):
        p=poly_mul(p,[a-j,1])
    return p

for h in range(1,10):
    for j in range(0,10):
        for k in range(0,70):
            d=difference(h,j,h+1,k)
            target=(-1)**(h+1)*factorial(h) if k==j else 0
            assert d==target,(h,j,k,d,target)
            checks+=1
        for r in range(1,h+1):
            p=[0]*(h+1)
            for s in range(r+1):
                q=poly_num(h,j+s)
                for t,z in enumerate(q):
                    p[t]+=(-1)**(r-s)*comb(r,s)*z
            expected=(-1)**r*factorial(h)//factorial(h-r)
            assert all(x==0 for x in p[h-r+1:]),(h,j,r,p)
            assert p[h-r]==expected,(h,j,r,p[h-r],expected)
            for k in (j+r,j+r+1,2*j+r+4,70+j):
                assert difference(h,j,r,k)==sum(p[a]*k**a for a in range(len(p)))
                checks+=1
            checks+=2

# A finite polynomial Vandermonde test certifies the minimality calculation.
# Its proof for arbitrary distinct indices uses det(V)=prod_{i<j}(j_j-j_i).
for h in range(1,9):
    js=[t*t+t+2 for t in range(h+1)]
    determinant=prod(js[b]-js[a] for a in range(h+1) for b in range(a+1,h+1))
    assert determinant!=0
    checks+=1
print('JET_DIFFERENCE_VERIFY_OK',checks)
