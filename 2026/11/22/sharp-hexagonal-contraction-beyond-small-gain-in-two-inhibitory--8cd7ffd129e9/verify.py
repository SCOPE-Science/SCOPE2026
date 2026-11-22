"""Finite exact and numerical supplementary checks for a two-event delay recurrence.
Run with python3 verify.py; only standard library is required.
The main theorem is proved analytically in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import product
from math import tanh

def norm(u, v):
    return max(abs(u), abs(v), abs(u + v))

def linear_step(u, v, a, b):
    w = -a * (u + v)
    z = -b * (v + w)
    return w, z

r = [Q(0), Q(1, 8), Q(1, 4), Q(2, 5), Q(1, 2),
     Q(3, 5), Q(4, 5), Q(9, 10), Q(1)]
checked = 0
for a, b in product(r, repeat=2):
    q = a + b - a*b
    for u, v in product(range(-4, 5), repeat=2):
        w, z = linear_step(Q(u), Q(v), a, b)
        assert norm(w, z) <= q * norm(Q(u), Q(v)), (a,b,u,v)
        checked += 1
    w,z = linear_step(Q(0),Q(1),a,b)
    assert norm(w,z) == q  # exact sharpness of the one-step bound
print(f"exact rational contraction cases: {checked}")

# Explicit boundary: gain 1 for the first operator, gain 0 for the second.
for j in range(-10,11):
    p = Q(1) + Q(j,50)
    for k in range(12):
        p = Q(2)-p
        assert Q(4,5) <= p <= Q(6,5)
    assert p == Q(1)+Q(j,50)
print("exact boundary two-cycle cases: 21")

# Admissible tanh responses on [1.7, 2.3], with D=[0.9,1.1]
# and timing perturbation in [-0.1, 0.1].
def f(t):
    return 1.0 - 0.1 * tanh(8.0*(t-2.0))

def step(p,n,eta_p=0.,eta_n=0.):
    pp = f(p+n+eta_p)
    nn = f(n+pp+eta_n)
    return pp,nn

q=0.96
for ip,inn,jp,jn in product(range(-3,4),repeat=4):
    p,n=1+ip/30,1+inn/30
    s,t=1+jp/30,1+jn/30
    x,y=step(p,n)
    z,w=step(s,t)
    assert 0.9 < x < 1.1 and 0.9 < y < 1.1
    assert norm(x-z,y-w)<=q*norm(p-s,n-t)+1e-12
print("nonlinear unforced one-step comparisons: 2401")

# Nonautonomous forced stability, not a proof of the infinite-horizon assertion.
for ip in range(-4,5):
    p=1.0+ip/50; n=1.0-ip/100
    s=1.0-ip/100; t=1.0+ip/75
    for k in range(120):
        ep=0.1*tanh((k%11)-5)
        en=0.1*tanh((k%17)-8)
        m=norm(p-s,n-t)
        p,n=step(p,n,ep,en)
        s,t=step(s,t,ep,en)
        assert norm(p-s,n-t)<=q*m+1e-12
print("nonlinear forced contraction steps: 1080")

# Sharpness for the nonlinear admissible example: derivative in direction (0,1).
for eps in [1e-3, 1e-4, 1e-5, 1e-6]:
    pp,nn=step(1.,1.+eps)
    ratio=norm(pp-1,nn-1)/eps
    assert abs(ratio-q)<1e-5
print("nonlinear derivative sharpness: 4")

# Above gain 1 the scalar inhibitory recurrence has a nonzero two-cycle.
for a in [1.01,1.2,1.8,3.]:
    lo=0.;hi=0.1
    for i in range(80):
        m=(lo+hi)/2
        if 0.1*tanh((a/0.1)*m)>m:lo=m
        else:hi=m
    h=(lo+hi)/2
    assert 0<h<0.1
    assert abs(0.1*tanh((a/0.1)*h)-h)<1e-13
    deriv=a*(1-tanh((a/0.1)*h)**2)
    assert deriv<1
print("supercritical two-cycle parameters: 4")
