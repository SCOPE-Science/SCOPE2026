#!/usr/bin/env python3
"""Exact rational diagnostics for the four-site Schatten-sixth shift theorem.
The general assertion relies on the accompanying analytic proof.
"""
from fractions import Fraction as Q
from itertools import product

def matmul(a,b):
    n=len(a)
    return [[sum((a[i][k]*b[k][j] for k in range(n)),Q(0))
             for j in range(n)] for i in range(n)]
def matpow(a,n):
    z=[[Q(i==j) for j in range(len(a))] for i in range(len(a))]
    for _ in range(n):
        z=matmul(z,a)
    return z
def trace(a):
    return sum((a[i][i] for i in range(len(a))),Q(0))
def p(r):
    return r**4+3*r**3-4*r-3
def g(r):
    return (r+2)*(r*r+4*r+1)/(r**3+2)
def deriv(r):
    return -6*p(r)/(r**3+2)**2
def f(x,y,z):
    return (x+y+z)**3-3*x*z*(x+y+z)

count=0
for a,b,c in product(range(-3,4),repeat=3):
    w=(Q(a),Q(b),Q(c))
    t=[[Q(0) for _ in range(4)] for _ in range(4)]
    for j,weight in enumerate(w):
        t[j+1][j]=weight
    h=[[Q(t[i][j]+t[j][i],2) for j in range(4)] for i in range(4)]
    lhs=trace(matpow(h,6))
    x,y,z=(w[0]**2,w[1]**2,w[2]**2)
    rhs=f(x,y,z)/32
    assert lhs==rhs,(w,lhs,rhs)
    assert sum((k**6 for k in w),Q(0))==x**3+y**3+z**3
    count+=2

for x,y,z in product((Q(0),Q(1,3),Q(1),Q(5,2)),repeat=3):
    if x+z==0: continue
    u=(x+z)/2
    m=x**3+z**3
    exact=m+y**3+6*u*y*y+8*u*u*y+m*y/(2*u)
    assert f(x,y,z)==exact
    count+=1

# Degree-bound polynomial identity: compare the rational derivatives directly,
# and exact normalized path values for selected scalar arguments.
for j in range(1,51):
    r=Q(j,11)
    pnum=Q(j,11)
    # derivative of (r+2)(r^2+4r+1)/(r^3+2) by quotient rule
    N=(r+2)*(r*r+4*r+1)
    dN=3*r*r+12*r+9
    d=(dN*(r**3+2)-N*3*r*r)/(r**3+2)**2
    assert d==deriv(r)
    count+=1
assert p(Q(1))<0<p(Q(2))
assert g(Q(1))==Q(6)
assert g(Q(0))==Q(1)
assert Q(4)<g(Q(1))
print("SCHATTEN_SIXTH_FOUR_SITE_EXACT_CHECK_OK",count)
