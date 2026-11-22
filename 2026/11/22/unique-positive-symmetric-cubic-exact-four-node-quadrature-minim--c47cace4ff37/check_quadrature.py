#!/usr/bin/env python3
"""Independent numerical and rational spot checks of the four-node quadrature theorem.

The universal optimality proof is analytic and is stated in RESULT.md.
This script is corroborative, not an infinite-range certificate.
"""
from fractions import Fraction
from random import Random
from math import sqrt


def poly(d):
    return 9*d*d-32*d*d*d-Fraction(1,12)

lo=Fraction(1321655207489665,10**16)
hi=Fraction(1321655207489667,10**16)
assert poly(lo)<0<poly(hi)
assert Fraction(1,8)<lo<hi<Fraction(1,7)
print('EXACT_RATIONAL_UNIQUE_ROOT_BRACKET_PASS')

# Bisection root; exact comparisons are above.
a=float((lo+hi)/2)
b=3*a
v=2*a
w=.5-v
nodes=[.5-b,.5-a,.5+a,.5+b]
weights=[w,v,v,w]
for k in range(4):
    rule=sum(ww*(xx**k) for xx,ww in zip(nodes,weights))
    assert abs(rule-1/(k+1)) < 4e-15,(k,rule)
print('CUBIC_EXACTNESS_PASS')


def discrepancy(nodes,weights):
    f=0.
    d=0.
    for x,weight in zip(nodes,weights):
        d=max(d,abs(f-x),abs(f+weight-x))
        f+=weight
    assert abs(f-1)<1e-10
    return d

assert abs(discrepancy(nodes,weights)-a)<1e-14
for x in (nodes[0],nodes[1]):
    # strict-tail step function f(t)=1_{(x,1]} is BV-normalized;
    # integral=1-x, rule=sum(weights at nodes >x).
    q=sum(z for t,z in zip(nodes,weights) if t>x)
    assert abs(abs(q-(1-x))-a)<1e-13
print('SHARP_UNIT_JUMP_WITNESSES_PASS')

rng=Random(20261117)
tests=0
for i in range(35000):
    u=rng.random()*.5
    z=u+(.5-u)*rng.random()
    if z*z-u*u<1e-15:continue
    # 2v*u^2+(1-2v)*z^2=1/12.
    vv=(z*z-1/12)/(2*(z*z-u*u))
    if not (0<=vv<=.5):continue
    w0=.5-vv
    pts=[.5-z,.5-u,.5+u,.5+z]
    d=discrepancy(pts,[w0,vv,vv,w0])
    assert d+5e-12>=a,(u,z,vv,d)
    tests+=1
assert tests>1000
print('FEASIBLE_RULE_RANDOM_STRESS_PASS',tests)

# Independent direct bound for d<1/7: derivative of F_d(b) positive
# whenever b<=3d, because F_d'(b)=2d^2+2b(1-3b+2d)
for i in range(10000):
    d=.125+(a-.125)*rng.random()
    bb=(.5-d)+(3*d-(.5-d))*rng.random()
    der=2*d*d+2*bb*(1-3*bb+2*d)
    assert der>0
    upper=2*(bb-d)*d*d+(1-2*bb+2*d)*bb*bb
    assert upper<=9*d*d-32*d**3+1e-13
print('SHARP_MOMENT_ENVELOPE_SPOT_CHECK_PASS')

try:
    from scipy.special import roots_legendre
    x,p=roots_legendre(4)
    g=discrepancy((x+1)/2,p/2)
    assert g>a and abs(g-0.16999052179242813)<1e-10
    print('GAUSS_FOUR_DISCREPANCY_BENCHMARK_PASS',format(g,'.15f'))
except ImportError:
    print('GAUSS_FOUR_OPTIONAL_BENCHMARK_SKIPPED')
print('ALL_FOUR_NODE_MOMENT_DISCREPANCY_CHECKS_PASS')
