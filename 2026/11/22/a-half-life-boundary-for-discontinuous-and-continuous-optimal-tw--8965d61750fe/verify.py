#!/usr/bin/env python3
"""Exact-rational verification of a two-bolus threshold-duration classification.

Only the standard Python library is needed. The infinite-parameter theorem
is proved analytically in RESULT.md; finite checks are corroborative.
"""
from fractions import Fraction as Q
from random import Random

CHECKS = 0
ONE = Q(1)
HALF = Q(1, 2)

def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)

def exposure_factor(q, d, a):
    """Exactly exp(clearance_rate * time above threshold)."""
    return min(max(a, ONE), ONE / q) * max(ONE, d - (ONE - q) * a)

def theorem(q, d):
    """Return exact optimal factor and exact maximizing dose shares (or all)."""
    require(0 < q < 1 and d >= 0, 'input domain')
    if d <= 1:
        return ONE, None
    r = ONE - q
    if q < HALF:
        onset = 4*r
        cap = 2*r/q
        if d < onset:
            return d, (Q(0), d)
        if d == onset:
            return d, (Q(0), Q(2), d)
        if d < cap:
            return d*d/(4*r), (d/(2*r),)
        return (q*d-r)/(q*q), (ONE/q,)
    if d <= ONE/q:
        return d, (Q(0), d)
    return (q*d-r)/(q*q), (ONE/q,)

def candidates(q, d):
    """All endpoints, clipping transitions, and quadratic stationary point."""
    r = ONE-q
    points = [Q(0), d, ONE, ONE/q, (d-ONE)/r, d/(2*r)]
    return sorted(set(x for x in points if 0 <= x <= d))

def check_case(q, d):
    value, opt = theorem(q,d)
    cs = candidates(q,d)
    vals = [(x, exposure_factor(q,d,x)) for x in cs]
    require(max(y for _,y in vals) == value, ('global candidate values',q,d))
    if opt is None:
        require(all(y == ONE for _,y in vals), ('all-zero coverage',q,d))
    else:
        maximizing = tuple(x for x,y in vals if y == value)
        require(maximizing == opt, ('exact maximizing candidates',q,d,maximizing,opt))
        for x in opt:
            require(exposure_factor(q,d,x) == value, ('optimum attained',q,d,x))
    rng = Random(int(q.numerator*317 + q.denominator*241 + d.numerator*67+d.denominator*193))
    for _ in range(30):
        x = d * Q(rng.randrange(10001), 10000)
        require(exposure_factor(q,d,x) <= value, ('sampled global upper bound',q,d,x))

# Exact named boundaries and one-sided neighborhoods.
for q in [Q(1,20), Q(1,4), Q(2,5), Q(49,100), HALF,
          Q(51,100), Q(3,5), Q(3,4), Q(19,20)]:
    boundaries = [ONE, ONE/q, 4*(ONE-q), 2*(ONE-q)/q,
                  4/(ONE+q)]
    ds = set([Q(0), Q(1,2), Q(3,2), Q(2), Q(3), Q(10), Q(30)])
    for b in boundaries:
        for delta in [Q(-1,1000), Q(0), Q(1,1000)]:
            if b+delta >= 0:
                ds.add(b+delta)
    for d in ds:
        check_case(q,d)

# Deterministic rational sweep, including near-zero and near-one retention.
rd = Random(20261121)
for _ in range(5200):
    q = Q(rd.randrange(1,1000), 1000)
    d = Q(rd.randrange(0,20000), 1000)
    check_case(q,d)

# Distinct equal/unequal fractionation outcomes from one explicit benchmark.
q, d = Q(1,4), Q(31,10)
best, (first,) = theorem(q,d)
equal = exposure_factor(q,d,d/2)
one_shot = exposure_factor(q,d,Q(0))
require(first == Q(31,15), 'optimal first bolus')
require(best == Q(961,300), 'optimal factor')
require(equal == Q(961,320), 'equal-split factor')
require(one_shot == Q(31,10), 'one-bolus factor')
require(equal < one_shot < best, 'opposite comparisons')
require(q*first < ONE, 'subthreshold interval before second bolus')

print('VERIFY_OK assertions=' + str(CHECKS))
