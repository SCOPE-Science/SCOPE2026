#!/usr/bin/env python3
"""Deterministic finite diagnostics for a three-contact catenary covering theorem.
Not a substitute for the analytic proof. Standard-library Python 3 only.
"""
import math

def h(t):
    return math.cosh(t) + t / math.sinh(t)

def radius_center(a):
    rise = math.cosh(a)-1.0
    if rise <= a:
        return a, rise
    r = (a*a+rise*rise)/(2*rise)
    return r, r

def root_bisect():
    lo, hi=1.0,3.0
    for _ in range(90):
        md=(lo+hi)/2.0
        if math.cosh(md)-1.0>md: hi=md
        else: lo=md
    return (lo+hi)/2.0

a0=root_bisect()
assert abs(a0-1.61613751377431)<2e-14
assert abs(h(.1)-(math.cosh(.1)+.1/math.sinh(.1)))<1e-14
cases=0
for a in (0.02,.1,.3,.75,1.2,1.5,1.615, a0,1.617,1.7,2,2.5,3,4,5):
    r,z=radius_center(a)
    for i in range(10001):
        t=a*i/10000
        d2=t*t+(math.cosh(t)-1-z)**2
        assert d2 <= r*r + 1e-10*max(1,r*r), (a,t,d2,r*r)
        cases+=1
    rise=math.cosh(a)-1
    assert abs(a*a+(rise-z)**2-r*r)<1e-9*max(1,r*r)
    if rise>a: assert abs(z*z-r*r)<1e-10*max(1,r*r)
    elif rise<a: assert z*z<r*r
for t in (.1,.2,.3,.5):
    # Quartic arch is a counterexample to three-point screening.
    assert t*t+(t**4-1)**2>1
for q in (1.2,1.5,1.75,2):
    for a in (.2,.8,1,1.4,2.2):
        rise=a**q
        r,z=(a,rise) if rise<=a else ((a*a+rise*rise)/(2*rise), (a*a+rise*rise)/(2*rise))
        for i in range(501):
            t=a*i/500
            assert t*t+(t**q-z)**2<=r*r+1e-9
print('PASS',cases,'dense catenary containment checks,','20 power-arch cases; critical halfspan',format(a0,'.15f'))
print('critical quadratic onset coefficient',format((math.sinh(a0)-1)**2/(2*a0),'.15f'))
