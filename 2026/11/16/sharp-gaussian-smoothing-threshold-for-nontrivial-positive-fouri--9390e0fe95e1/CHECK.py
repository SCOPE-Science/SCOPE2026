#!/usr/bin/env python3
"""Independent standard-library algebra sanity checks for the stated Gaussian mixture example."""
from fractions import Fraction as F
from math import exp, sqrt
from itertools import product

def conv(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

A=[1,5,6];B=[3,7,2]
assert conv([1,2],[1,3])==A
assert conv([1,2],[3,1])==B
assert conv(A,A[::-1])==conv(B,B[::-1]);print('autocorrelation:',conv(A,A[::-1]))
assert sum(A)==sum(B)==12

def cm(w,n):
    mu=sum(F(i*w[i],12) for i in range(3))
    return sum(F(w[i],12)*(i-mu)**n for i in range(3))
assert [cm(A,n) for n in [1,2,3]]==[F(0),F(59,144),F(-145,864)]
assert [cm(B,n) for n in [1,2,3]]==[F(0),F(59,144),F(17,864)]
# Check the rational identity for conditional variance with exact rational u,lambda.
for lam in [F(1,2),F(3),F(4),F(13),F(51,2)]:
    for u in [F(1,5),F(2,3),F(1),F(7,3),F(11)]:
        zz=u+1/u
        p=[F(1),lam*u,u*u];Z=sum(p)
        m=(p[1]+2*p[2])/Z
        v=(p[1]+4*p[2])/Z-m*m
        assert v==(lam*zz+4)/(zz+lam)**2
# Verify derivative numerator by exact polynomial algebra:
# d/dz ((lam*z+4)/(z+lam)^2) has sign lam^2-8-lam*z.
for lam,z in product([F(1),F(3),F(4),F(9)], [F(2),F(7),F(11)]):
    derivative=(lam*(z+lam)-2*(lam*z+4))/(z+lam)**3
    assert derivative==(lam*lam-8-lam*z)/(z+lam)**3
# The displayed unique root is merely a numerical illustration (global proof is analytic).
from math import isfinite
lo,hi=.25,1/3
Froot=lambda t:(t-.25)*((25/6)*exp(1/t)-4)-1
assert Froot(lo)<0<Froot(hi)
for i in range(80):
    mid=(lo+hi)/2
    if Froot(mid)>0:hi=mid
    else:lo=mid
t=(lo+hi)/2
assert abs(t-.2548339622562054)<1e-13
print('44+ exact/rational checks passed; variance threshold (numerical only):',t)
