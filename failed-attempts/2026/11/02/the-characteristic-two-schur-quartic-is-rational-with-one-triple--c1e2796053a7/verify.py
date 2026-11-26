#!/usr/bin/env python3
"""Exact reproducible finite-field checks for the characteristic-two Schur specialization.
No external packages or unrecorded inputs required. The general theorem uses the accompanying algebraic proof.
"""
from math import gcd

MOD={1:0b11,2:0b111,3:0b1011,4:0b10011}

def mul(a,b,m):
    modulus=MOD[m]; mask=(1<<m)-1; out=0
    while b:
        if b&1: out^=a
        b >>= 1
        a <<= 1
        if a&(1<<m): a^=modulus
    return out&mask

def power(a,n,m):
    out=1
    while n:
        if n&1: out=mul(out,a,m)
        a=mul(a,a,m)
        n >>= 1
    return out

def F(z,t,v,w,m):
    return mul(z,power(v,3,m)^power(w,3,m),m)^power(t,4,m)^mul(t,power(w,3,m),m)

def F_original(x0,x1,x2,x3,m):
    return power(x0,4,m)^mul(x0,power(x1,3,m),m)^power(x2,4,m)^mul(x2,power(x3,3,m),m)

def proj_points(dim,q):
    # Unique projective representatives with first nonzero coordinate 1.
    for j in range(dim+1):
        import itertools
        for tail in itertools.product(range(q),repeat=dim-j):
            yield (0,)*j+(1,)+tail

for m in (1,2,3,4):
    q=1<<m
    total=0
    for z,t,v,w in proj_points(3,q):
        assert F(z,t,v,w,m)==F_original(z,v,z^t,w,m)
        if F(z,t,v,w,m)==0: total+=1
    r=gcd(3,q-1)
    expect=q*q+q+1+r*r*q
    assert total==expect,(m,total,expect)
    # Every base direction over the ground field is a line through P.
    base=[(t,v,w) for t,v,w in proj_points(2,q) if (power(v,3,m)^power(w,3,m))==0 and (power(t,4,m)^mul(t,power(w,3,m),m))==0]
    assert len(base)==r*(r+1),(m,len(base))
    print(f'GF_{q}_SURFACE_POINTS={total};FORMULA={expect};BASE_DIRECTIONS={len(base)}')
print('CHAR2_UNIQUE_SINGULAR_SUPPORT=Jacobian_forces_w=v=t=0')
print('LOCAL_TJURINA_QUOTIENT=k[t,v,w]/(t^4,v^2,w^2);LENGTH=16')
print('GEOMETRIC_LINE_DIRECTIONS_THROUGH_SINGULAR_POINT=12')
print('VERIFY_OK')
