#!/usr/bin/env python3
"""Exact rational supplementary checks for scalar convex proximal semigroups.

The all-functions classification is proved analytically in RESULT.md. This
checker verifies representative explicit models and sharp one-kink defects.
"""
from fractions import Fraction as Q
from itertools import product

def hinge(x, t, a, b):
    assert a <= b and t >= 0
    if x < t*a:
        return x-t*a
    if x > t*b:
        return x-t*b
    return Q(0)

def distance_interval(x, t, a, b, c, d):
    assert a>=0 and b>=0 and c<=d and t>=0
    if x < c:
        return min(c, x+t*a)
    if x > d:
        return max(d, x-t*b)
    return x

def defect_bound(s, t, a, b):
    if a<=0<=b: return Q(0)
    return min(s*min(abs(a),abs(b)),t*(b-a))

def max_defect_exact(s,t,a,b):
    # Every composition is piecewise affine. The kink list below contains
    # all changes for both branches, including points where the inner
    # prox hits the outer prox transition.
    pts={t*a,t*b,(s+t)*a,(s+t)*b}
    for v in (s*a,s*b):
        pts.update((t*a+v,t*b+v))
    pts.update((-Q(100),Q(100)))
    def d(x): return abs(hinge(hinge(x,t,a,b),s,a,b)-hinge(x,s+t,a,b))
    return max(d(x) for x in pts)

checks=0
v = [Q(i,2) for i in range(-12,13)]
for a,b in product(v,repeat=2):
    if a>b: continue
    for s,t in product((Q(1,4),Q(1,2),Q(1),Q(3)),repeat=2):
        assert max_defect_exact(s,t,a,b)==defect_bound(s,t,a,b),(a,b,s,t)
        checks+=1
        # The extremizer is a breakpoint of the first proximal map.
        x=t*b if a>0 else t*a if b<0 else Q(0)
        d=abs(hinge(hinge(x,t,a,b),s,a,b)-hinge(x,s+t,a,b))
        assert d==defect_bound(s,t,a,b)
        checks+=1
for a,b in product((Q(0),Q(1,3),Q(2)),repeat=2):
    for c,d in product((Q(-3),Q(0),Q(2)), repeat=2):
        if c>d:continue
        for s,t in product((Q(0),Q(1,5),Q(1),Q(5)),repeat=2):
            for x in (Q(-10),Q(-3),Q(-1),Q(0),Q(1),Q(3),Q(10)):
                assert distance_interval(distance_interval(x,t,a,b,c,d),s,a,b,c,d)==distance_interval(x,s+t,a,b,c,d)
                checks+=1
for q in (Q(-3),Q(0),Q(3)):
    for s,t in product((Q(0),Q(1,2),Q(4)),repeat=2):
        for x in (Q(-10),Q(0),Q(7)):
            assert (x-t*q)-s*q==x-(s+t)*q
            checks+=1
print('PASS',checks,'exact rational checks')
