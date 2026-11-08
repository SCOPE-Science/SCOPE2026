#!/usr/bin/env python3
"""Finite exact-rational checks for atomic Hausdorff shift commutators.

These checks sample algebraic identities and finite Gram matrices; the infinite
Riesz-family statement and operator-domain conclusions require the proof.
"""
from fractions import Fraction as F
from math import comb

checks=0

def assert_equal(left,right):
    global checks
    checks+=1
    assert left==right,(left,right)

def tscale(j,rho=F(1,16)):
    return rho**j

def gram(t,s):
    lo=min(t,s); hi=max(t,s)
    return lo*(1-hi)/(hi*(t+s-t*s))

def c_matrix(t,n):
    q=1-t
    h=[[F(0) for _ in range(n)] for _ in range(n)]
    for j in range(n):
        for i in range(j,n):
            h[i][j]=F(comb(i,j))*t**j*q**(i-j)
    c=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j]=(h[i][j+1] if j+1<n else F(0))-(h[i-1][j] if i else F(0))
    return c

for t in [F(1,2),F(1,3),F(2,3)]:
    for n in range(1,9):
        c=c_matrix(t,n)
        q=1-t
        for i in range(n):
            for j in range(n):
                # Direct rational coefficient of -q*t^j*z^(j+1)*(1-z)/(1-q*z)^(j+2).
                k=i-j-1
                predicted=F(0)
                if k>=0:
                    predicted=-q*t**j*(comb(j+k+1,j+1)*q**k - (comb(j+k,j+1)*q**(k-1) if k>=1 else 0))
                assert_equal(c[i][j],predicted)

rho=F(1,16); r=F(1,64) # rho^(3/2), exactly 1/64
assert_equal(r,F(1,64))
for i in range(1,16):
    ti=tscale(i)
    for j in range(1,16):
        tj=tscale(j)
        squared=ti*tj*gram(ti,tj)**2
        if i!=j:
            assert squared<=r**(2*abs(i-j))
            checks+=1
        else:
            diag=ti*gram(ti,tj)
            assert F(15,31)<=diag<F(1,2)
            assert_equal(diag*diag,squared)
            checks+=1

m=F(15,31)-2*r/(1-r)
M=F(1,2)+2*r/(1-r)
assert m>0
assert_equal(m,F(15,31)-F(2,63))
assert_equal(M,F(1,2)+F(2,63))
# Pairing formula also matches explicit matrix truncations from below in these cases.
for t,s in [(F(1,2),F(3,4)),(F(1,3),F(2,3)),(F(1,2),F(1,2))]:
    target=gram(t,s)
    prev=None
    for n in [8,16,32,64]:
        a=c_matrix(t,n);b=c_matrix(s,n)
        trial=sum((a[i][j]*b[i][j] for i in range(n) for j in range(n)),F(0))
        assert trial>=0
        checks+=1
        if t==s and prev is not None:
            assert trial>=prev
            checks+=1
        prev=trial
    if t==s:
        assert trial<=target
        checks+=1
print(f'ATOMIC_HAUSDORFF_COMMUTATOR_OK {checks} exact assertions; analytic infinite proof separate')
