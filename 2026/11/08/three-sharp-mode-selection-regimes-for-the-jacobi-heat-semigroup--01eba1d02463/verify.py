#!/usr/bin/env python3
"""Exact finite diagnostics for two-mode Jacobi diffusion fourth norms.

The theorem for all degrees and all times is proved in RESULT.md;
these rational checks guard the normalization and optimization formulas.
"""
from fractions import Fraction as F
from math import comb

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def U(n):
    p,q=[1],[0,2]
    if n==0:return p
    if n==1:return q
    for k in range(2,n+1):
        z=[0]+[2*v for v in q]
        for i,v in enumerate(p):z[i]-=v
        p,q=q,z
    return q

def catalan(n):return F(comb(2*n,n),n+1)
def expect(p):
    return sum(F(co)*catalan(i//2)/4**(i//2) for i,co in enumerate(p) if i%2==0)

def power(p,k):
    z=[1]
    for _ in range(k):z=mul(z,p)
    return z

def qform(m,n,r,x):
    a=m+1;b=n+1
    return a*(1-x)**2+b*r*r*x*x+6*a*r*x*(1-x)

def optimizer(m,n,r):
    a=m+1;b=n+1
    A=F(a);B=b*r*r;C=3*a*r
    if C>A and C>B:
        x=(C-A)/(2*C-A-B)
        return x, (C*C-A*B)/(2*C-A-B), 'mixed'
    if A>=B:return F(0), A, 'low'
    return F(1), B, 'high'

pairs=[(1,2),(1,4),(1,6),(1,18),(2,3),(2,7),(3,4),(3,8),(4,5),(4,13)]
checks=0
for m,n in pairs:
    assert n>m and (m+n)%2==1
    p,q=U(m),U(n)
    cross=expect(mul(power(p,2),power(q,2)))
    assert [expect(power(p,2)),expect(power(q,2)),expect(power(p,4)),expect(power(q,4)),cross,
            expect(mul(power(p,3),q)),expect(mul(p,power(q,3)))]==[1,1,m+1,n+1,m+1,0,0]
    checks+=7
    for r in [F(1),F(9,10),F(1,2),F(1,3),F(1,4),F(1,10),F(1,30)]:
        xstar,v,kind=optimizer(m,n,r)
        assert 0<=xstar<=1 and qform(m,n,r,xstar)==v
        for j in range(101):
            assert qform(m,n,r,F(j,100))<=v
        A=F(m+1);B=(n+1)*r*r;C=3*(m+1)*r
        if kind=='mixed':
            assert C>A and C>B and (2*C-A-B)>0
            for z in (F(0),F(1),F(7,17)):
                assert v-qform(m,n,r,z)==(2*C-A-B)*(z-xstar)**2
        checks+=1
# The two boundary locations, and the separated pure-to-pure transition.
assert optimizer(1,6,F(1))[2]=='high'
assert optimizer(1,6,F(3,4))[2]=='mixed'
assert optimizer(1,6,F(1,4))[2]=='low'
assert optimizer(1,18,F(1))[2]=='high'
assert optimizer(1,18,F(1,4))[2]=='low'
assert optimizer(1,2,F(1))[2]=='mixed'
assert optimizer(1,2,F(1,4))[2]=='low'
print('CHEBYSHEV_MOMENT_AND_BRANCH_EXACT_CHECKS_PASSED',checks,'CASES')
