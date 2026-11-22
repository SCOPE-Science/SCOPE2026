#!/usr/bin/env python3
"""Reproducible algebraic/numerical checks for the Briere-I symmetric-thermal theorem.

All observations are finite diagnostics; the analytical proof is in RESULT.md.
No external Python modules are required.
"""
from fractions import Fraction as F
from math import sqrt, isclose

def f(a, x):
    assert a-1e-12 <= x <= 1+1e-12
    x=min(1.0,max(a,x))
    return x * (x - a) * sqrt(max(0.0, 1 - x))

def gap(a, m, d):
    return (f(a, m - d) + f(a, m + d)) / 2 - f(a, m)

def dc(a):
    return (3 - 9*a + sqrt(9 + 2*a - 3*a*a)) / 14

def G(a,d):
    return 7*d*d+(9*a-3)*d+a*(3*a-2)

checks=0
# Verify polynomial identity exactly over rational sampling values.
for an in range(1,10):
    a=F(an,10)
    for dn in range(1,21):
        d=F(dn,100)
        lhs=(a+2*d)**2*(1-a-2*d)-(a+d)**2*(1-a-d)
        assert lhs == -d*G(a,d)
        checks+=1
# Feasible range, root value, and endpoint sign at multiple parameter values.
for ai in range(1,100):
    a=ai/100
    dmax=(1-a)/2
    if a<2/3:
        c=dc(a)
        assert c>0
        assert c<dmax
        assert abs(G(a,c))<2.e-14
        checks+=3
    else:
        assert G(a,.1*dmax)>0
        checks+=1
    assert isclose(G(a,dmax),(a+1)**2/4,abs_tol=2.e-13,rel_tol=0)
    checks+=1
# Monotonicity of Jensen gap in mean and predicted signs on wide in-domain grids.
for ai in range(1,20):
    a=ai/20
    dmax=(1-a)/2
    for k in range(1,18):
        d=dmax*k/18
        lo=a+d; hi=1-d
        vals=[gap(a,lo+(hi-lo)*j/100,d) for j in range(101)]
        # Ignore near-floating rounding in monotone checks at extremely small gaps.
        for j in range(100):
            assert vals[j] > vals[j+1]-2e-14
            checks+=1
        assert vals[-1] < -1e-10
        checks+=1
        if a>=2/3 or d>dc(a)+1e-12:
            assert max(vals)<1e-10
            checks+=1
        elif d<dc(a)-1e-12:
            assert vals[0]>0 and vals[-1]<0
            checks+=1
# Selected dimensional example.
a=.2;d=.1
lo=a+d;hi=1-d
for _ in range(100):
    mid=(lo+hi)/2
    if gap(a,mid,d)>0: lo=mid
    else: hi=mid
mstar=(lo+hi)/2
assert abs(mstar-.5247407404111056)<3e-11
assert gap(.2,.4,.1)>0 and gap(.2,.7,.1)<0
checks+=3
for i in range(101):
    assert gap(.2, .51+(.69-.51)*i/100, .31)<0
    checks+=1
print('PASS: %d diagnostic assertions; a=0.2, dcrit=%.15f, d=0.1 crossover m=%.15f' % (checks,dc(.2),mstar))
