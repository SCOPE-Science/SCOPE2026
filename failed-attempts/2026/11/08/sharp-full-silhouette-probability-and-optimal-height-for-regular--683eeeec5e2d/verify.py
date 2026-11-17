#!/usr/bin/env python3
"""Independent finite checks for a geometric theorem on regular polygonal pyramid shadows.
Requires Python 3, NumPy, SciPy, mpmath. All random samples use a fixed seed.
Finite Monte Carlo checks are not proofs of asymptotic or all-parameter claims.
"""
import math
import numpy as np
import mpmath as mp
from scipy.spatial import ConvexHull


def p_exact(n, h):
    c = math.cos(math.pi / n)
    t = h / math.hypot(h, c)
    return n / math.pi * (2 * math.asin(t * math.sin(math.pi/n))
                          - math.asin(t * math.sin(2*math.pi/n)))


def h_opt(n):
    c = math.cos(math.pi/n)
    return c / math.sqrt(3*c*c - 1)


def projected_count(v, w):
    a = np.cross(w, [0.0, 0.0, 1.0])
    if np.linalg.norm(a) < 1.e-9:
        a = np.cross(w, [0.0, 1.0, 0.0])
    a /= np.linalg.norm(a)
    b = np.cross(w, a)
    return len(ConvexHull(v @ np.stack((a, b), axis=1)).vertices)


rng = np.random.default_rng(202611010147)
for n in [5, 6, 8, 12]:
    for multiplier in [0.55, 1.0, 2.2]:
        h = h_opt(n) * multiplier
        a = 2*math.pi*np.arange(n)/n
        vertices = np.vstack((np.column_stack((np.cos(a), np.sin(a),np.zeros(n))),
                                 np.array([[0.0,0.0,h]])))
        directions = rng.standard_normal(size=(7000,3))
        directions /= np.linalg.norm(directions,axis=1)[:,None]
        count = sum(projected_count(vertices, direction)==n+1 for direction in directions)
        estimate = count/len(directions)
        p = p_exact(n,h)
        tolerance = 6*math.sqrt(p*(1-p)/len(directions))+0.002
        assert abs(estimate-p)<tolerance,(n,h,p,estimate,tolerance)
        print('hull',n,round(h,6),round(p,8),round(estimate,8))
    h=h_opt(n)
    assert p_exact(n,h)>p_exact(n,h*0.97)
    assert p_exact(n,h)>p_exact(n,h*1.03)

mp.mp.dps=75
constant=2*mp.pi**2/(3*mp.sqrt(3))
for n in [40,100,1000,10000]:
    x=mp.pi/n
    c=mp.cos(x)
    t=1/(mp.sqrt(3)*c)
    p=n/mp.pi*(2*mp.asin(t*mp.sin(x))-mp.asin(t*mp.sin(2*x)))
    assert abs(n*n*p/constant-1)<mp.mpf(20)/(n*n)
    print('asymptotic',n,mp.nstr(n*n*p,18))

for n in [5,6,8,16]:
    h=h_opt(n)
    t=h/math.hypot(h,math.cos(math.pi/n))
    assert abs(t**2 - 1/(3*math.cos(math.pi/n)**2)) <1.e-13

print('ALL_REGULAR_PYRAMID_FULL_SHADOW_CHECKS_PASSED')
