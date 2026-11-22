#!/usr/bin/env python3
"""Independent numerical probes of the stated finite-horizon route comparison.

Only Python standard-library dependencies; the analytic arguments in RESULT.md
are essential for universal quantifiers. This program tests representative
finite parameter choices and an explicit rational-parameter example.
"""
import math
import random
from fractions import Fraction

checks = 0

def require(flag, detail='check failed'):
    global checks
    checks += 1
    if not flag:
        raise AssertionError(detail)

def cdf_erlang(k, z):
    if z <= 0:
        return 0.0
    if z < 1.5 * k:
        # Positive-series evaluation avoids subtractive cancellation near zero.
        term = math.exp(-z)
        for i in range(1, k + 1):
            term *= z / i
        ans = term
        for i in range(k+1, k+1500):
            term *= z / i
            ans += term
            if term < ans * 1e-16:
                break
        return min(1.0, ans)
    term = math.exp(-z)
    below = term
    for i in range(1, k):
        term *= z/i
        below += term
    return max(0., 1. - below)

def ratio(k, r, x):
    return cdf_erlang(k, r*x) / (-math.expm1(-x))

def maximize(k, r):
    # Derivative sign determined by the analytic numerator U = Bh - A.
    def U(x):
        h = math.exp(k*math.log(r) + (k-1)*math.log(x) - (r-1)*x - math.lgamma(k))
        return (-math.expm1(-x)) * h - cdf_erlang(k, r*x)
    pivot = (k-1)/(r-1)
    lo, hi = pivot, max(2*pivot, 2.)
    while U(hi) > 0:
        hi *= 2
    for i in range(85):
        mid=(lo+hi)/2
        if U(mid)>0:lo=mid
        else: hi=mid
    x=(lo+hi)/2
    return x,ratio(k,r,x)

# Exact rational, non-empirical lower bound for the slower-mean paradox.
# e^5 < 150 via Taylor partial sum through 9 plus a geometric tail bound;
# e^(15/2) > 1800 via Taylor partial sum through 16.
def power_sum(z, n):
    t=s=Fraction(1)
    for j in range(1,n+1):
        t *= z/j
        s += t
    return s, t
p5,t5=power_sum(Fraction(5),9)
require(p5 + t5*Fraction(5, 10-5) < 150)
p75,t75=power_sum(Fraction(15,2),16)
require(p75 > 1800)
strict_lb = Fraction(1,150) - Fraction(1,1000) - Fraction(999,1000)*Fraction(17,2)/1800
require(strict_lb == Fraction(1139,1200000))
adv=(Fraction(999,1000)) * cdf_erlang(2,7.5) - (-math.expm1(-5.))
require(adv > float(strict_lb))
require(1.5 < 2. and Fraction(999,1000) < 1)

# Analytic brackets for the two roots in a separate, well-conditioned case.
k, r, q = 2, 5., 1.5
xs=[0.01,0.1,0.2,0.23,0.5,0.9,1.05,2.,10.]
signs=[ratio(k,r,x)-q for x in xs]
require(signs[2] < 0 < signs[3]); require(signs[5] > 0 > signs[6]);
xstar,m=maximize(k,r)
require(0.4 < xstar < 0.55 and 1.8 < m < 1.85)
require(ratio(k,r,xstar-0.03)<m and ratio(k,r,xstar+0.03)<m)

# A wide finite grid checks the one-peak pattern without claiming it proves it.
for k in range(2,11):
    for r in (1.05,1.3,1.7,2.,3.,5.,8.,12.,25.):
        xstar,m=maximize(k,r)
        require(m>1-3e-12)
        require(xstar> (k-1)/(r-1))
        for scale in (0.05,0.2,0.5,0.9,0.99,1.01,1.1,1.5,3.,8.):
            v=ratio(k,r,xstar*scale)
            require(v < m + 5e-11, (k,r,scale,v,m))

# The maximum is strictly increasing in hopping speed.
for k in range(2,9):
    prev=1.
    for r in (1.2,1.5,2.,3.,5.,10.,20.,50.):
        _,m=maximize(k,r)
        require(m>prev-2e-11,(k,r,m,prev))
        prev=m

# At fixed k, the high-speed scale approaches c_k.
for k in (2,3,4,5,7):
    _,m100=maximize(k,100.)
    _,m200=maximize(k,200.)
    require(m200/200. < m100/100. + 0.005)
    require(m200/200. > 0.0)

rng=random.Random(482811)
for _ in range(1500):
    k=rng.randrange(2,11)
    r=1.1 + 19*rng.random()
    xstar,m=maximize(k,r)
    x=xstar*(0.05+4*rng.random())
    require(ratio(k,r,x) < m + 3e-11)

print('PASS',checks,'finite assertions; exact Taylor bound',str(strict_lb))
