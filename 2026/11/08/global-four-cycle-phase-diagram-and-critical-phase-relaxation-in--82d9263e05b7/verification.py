#!/usr/bin/env python3
"""Finite, reproducible checks of a rational negative-feedback limit map.

These tests are not a proof of the universal classification or measure claims.
Run with Python 3 standard library: python3 verification.py
"""
from fractions import Fraction as Q
from math import comb, exp, log, sinh, sqrt, isclose

checks = 0

def ok(pred, msg):
    global checks
    assert pred, msg
    checks += 1

def h(x, m, b):
    return b / (1 + x**m)

def f(pt, m, b):
    x, y = pt
    return (y, h(x, m, b))

def f_pow(pt, n, m, b):
    for _ in range(n):
        pt = f(pt, m, b)
    return pt

# Exact real rational test, m=2, b=5/2, L=1/2, H=2.
m, b = 2, Q(5, 2)
L, H = Q(1, 2), Q(2, 1)
cycle = [(L,L),(L,H),(H,H),(H,L)]
for i, pt in enumerate(cycle):
    ok(f(pt,m,b) == cycle[(i+1)%4], "exact four-cycle transition")
    ok(f_pow(pt,4,m,b) == pt, "exact four-cycle return")
# Derivative h'(x) = -bm x^(m-1)/(1+x^m)^2.
def hp(x, m, b):
    return -b*m*x**(m-1)/(1+x**m)**2
mu = hp(L,m,b)*hp(H,m,b)
ok(mu == Q(16,25), "exact four-step multiplier m=2 b=5/2")

# Normalized critical map G(1+s)=m/(m-1+(1+s)^m).
# Compute cubic coefficients by formal arithmetic, checking cubic return.
for m in range(2,11):
    den = [Q(comb(m,k),m) if k else Q(1) for k in range(4)]
    coef = [Q(1)]
    for n in range(1,4):
        coef.append(-sum(den[k]*coef[n-k] for k in range(1,n+1)))
    a, beta = coef[2], coef[3]
    cubic_return = -2*(beta+a*a)
    ok(coef[1] == -1, "critical slope")
    ok(cubic_return == -Q(m*m-1,6), "exact cubic return coefficient")

# Parameterized cycle family, including noninteger m.
for m in (1.1, 1.25, 1.5, 2, 3, 4, 7):
    bc = m*(m-1)**(-1-1/m)
    old_b = bc
    for s in (0.005,0.02,0.1,0.5,1.0,1.5):
        r = (sinh(s)/sinh((m-1)*s))**(1/m)
        bb = r*sinh(m*s)/sinh((m-1)*s)
        ll,hh = r*exp(-s),r*exp(s)
        tol = 5e-10*max(1,bb)
        ok(bb > old_b*(1-1e-12), "strictly increasing cycle parameter")
        ok(abs(h(ll,m,bb)-hh) < tol, "lower-to-upper exchange")
        ok(abs(h(hh,m,bb)-ll) < tol, "upper-to-lower exchange")
        multiplier = hp(ll,m,bb)*hp(hh,m,bb)
        expected = (m*sinh(s)/sinh(m*s))**2
        ok(0 < multiplier < 1 and abs(multiplier-expected)<1e-9,
           "cycle stable multiplier")
        old_b = bb

# Universal critical power law for both signs using direct iterations.
for m in (1.5,2.0,3.0,4.0):
    u = (m-1)**(-1/m)
    b = m*u/(m-1)
    expected = u*sqrt(3/(m*m-1))
    for v in (u/2, 2*u):
        w = v
        n = 30000
        for _ in range(n):
            w = h(h(w,m,b),m,b)
        measured = sqrt(n)*(w-u)
        ok(abs(abs(measured)-expected)/expected < .035,
           "critical n^-1/2 law within finite-n tolerance")
        ok((measured>0) == (v>u), "orientation preserved")

# Two- and four-step identity for a range of points.
for m in (0.6,1.2,2,3.5):
    for b in (0.3,1.5,4.0):
        for x in (0.01,0.2,0.7,2.0,7.0):
            for y in (0.03,0.4,1.5):
                lhs = f_pow((x,y),4,m,b)
                rhs = (h(h(x,m,b),m,b), h(h(y,m,b),m,b))
                ok(all(isclose(a,c,rel_tol=1e-13,abs_tol=1e-13)
                       for a,c in zip(lhs,rhs)), "F^4 diagonal identity")

print(f"PASS: {checks} independent finite/exact checks; no universal claim inferred from sampling.")
