#!/usr/bin/env python3
"""Standalone verification of two-shear identities and threshold classification."""
from fractions import Fraction as Q
from itertools import product
from math import exp, sqrt, isclose, expm1 as math_expm1

def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def mv(A,x):return tuple(sum(A[i][j]*x[j] for j in range(2)) for i in range(2))
def norm2(x):return sum(y*y for y in x)
I=((Q(1),Q(0)),(Q(0),Q(1)))
def mats(u):return (((Q(1),u),(Q(0),Q(1))),((Q(1),Q(0)),(-u,Q(1))))
def avg_moment_sq(n,u,x):
    ms=mats(u); s=Q(0); y=[Q(0),Q(0)]
    for word in product((0,1),repeat=n):
        z=x
        for j in word:z=mv(ms[j],z)
        s+=norm2(z)
        y[0]+=z[0];y[1]+=z[1]
    return s/(2**n),tuple(z/(2**n) for z in y)
checks=0
for u in (Q(1,5),Q(1,2),Q(1),Q(3,2),Q(4)):
    for x in ((Q(1),Q(0)),(Q(1),Q(2)),(Q(-3,2),Q(7,5))):
        for n in range(0,8):
            obs,obs_mean=avg_moment_sq(n,u,x)
            # Omit common scalar damping exp(-a h): verify matrix identity exactly.
            want=(1+u*u/2)**n*norm2(x)
            assert obs==want,(u,x,n,obs,want)
            avg=((Q(1),u/2),(-u/2,Q(1)))
            z=x
            for _ in range(n):z=mv(avg,z)
            assert obs_mean==z
            assert norm2(z)==(1+u*u/4)**n*norm2(x)
            checks+=3
assert checks==360

def G(t):return t-1+exp(-2*t)
lo,hi=Q(1,2),Q(1)
# Use ordinary float bisection: monotonicity is analytically proved.
lo,hi=float(lo),float(hi)
for _ in range(100):
    mid=(lo+hi)/2
    if G(mid)<0:lo=mid
    else:hi=mid
t_star=(lo+hi)/2
r_star=sqrt(2/(t_star*(1-t_star)))
assert isclose(t_star,0.79681213002002,abs_tol=2e-14)
assert isclose(r_star,3.5146990225291,abs_tol=2e-12)
assert isclose(sqrt(2)*r_star,4.97053502532010,abs_tol=2e-12)

def f(r,t):return exp(-2*t)*(1+r*r*t*t/2)
def g(r,t):return exp(-2*t)*(1+r*r*t*t/4)
for r in (Q(1),Q(3),Q(4),Q(5),Q(8)):
    r=float(r)
    for j in range(1,141):
        t=j/50
        F=2*math_expm1(2*t)/(t*t)
        assert (f(r,t)>1)==(r*r>F)
        assert (g(r,t)>1)==(r*r>2*F)
        checks+=2

def bisect(fun,a,b,n=100):
    va=fun(a)
    for _ in range(n):
        c=(a+b)/2
        if fun(c)*va>0:a=c;va=fun(c)
        else:b=c
    return (a+b)/2

# Fixed a=1, k=4, h=0.8 gives a genuine mean/mean-square separation.
assert f(4,0.8)>1 and g(4,0.8)<1
F=lambda t:2*math_expm1(2*t)/(t*t)
roots=(bisect(lambda t:F(t)-16,0.01,t_star),bisect(lambda t:F(t)-16,t_star,2))
assert abs(roots[0]-0.37042521488994)<1e-10
assert abs(roots[1]-1.42133670648418)<1e-10
assert all(f(4,t)<1 for t in (0.05,3.0))
assert all(f(4,t)>1 for t in (0.5,0.8,1.0))
print('VERIFY_OK',checks,'exact/inequality checks', 'tstar',t_star,'Rcrit',r_star,'Rmean',sqrt(2)*r_star,'roots',roots)
