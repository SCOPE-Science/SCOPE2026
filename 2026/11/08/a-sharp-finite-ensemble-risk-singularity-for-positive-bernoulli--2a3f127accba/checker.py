#!/usr/bin/env python3
"""Exact finite-state verification for a Bernoulli control-variate sketch.

Scientific reproducibility: standard-library only; prints numerical cross-checks
for a theorem proved analytically in RESULT.md. Finite enumeration is not used
as a replacement for the all-batch-size proof.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial

STATES = tuple(product((0, 1), repeat=3))
PROBS = tuple(Q(1, 3)**sum(g) * Q(2, 3)**(3-sum(g)) for g in STATES)
assert sum(PROBS) == 1


def compositions(n, d):
    if d == 1:
        yield (n,)
    else:
        for j in range(n+1):
            for tail in compositions(n-j, d-1):
                yield (j,)+tail


def exact_risk(n, m):
    """Take epsilon=1/m**2 and delta=sqrt(epsilon)=1/m."""
    e, d = Q(1, m*m), Q(1, m)
    ts = tuple(2*g[0]+(2+e)*g[1]+g[2] for g in STATES)
    ys = tuple(t+d*g[1] for t, g in zip(ts, STATES))
    target_t, target_y = (5+e)/3, (5+e+d)/3
    squared_risk, negprob = Q(0), Q(0)
    for counts in compositions(n, len(STATES)):
        prob = Q(factorial(n))
        for c, stateprob in zip(counts, PROBS):
            prob *= stateprob**c / factorial(c)
        mt = sum(c*t for c, t in zip(counts, ts))/n
        my = sum(c*y for c, y in zip(counts, ys))/n
        vt = sum(c*(t-mt)**2 for c, t in zip(counts, ts))
        cov = sum(c*(t-mt)*(y-my) for c, t, y in zip(counts, ts, ys))
        bhat = cov/vt if vt else Q(0)
        corrected = my-bhat*(mt-target_t)
        squared_risk += prob*(corrected-target_y)**2
        if corrected < 0:
            negprob += prob
    return squared_risk, negprob


def coefficients(n):
    # Two near-tied level classes of T_0=2g1+2g2+g3.
    a = Q(8,27)**n-2*Q(4,27)**n
    b = Q(4,27)**n-2*Q(2,27)**n
    return (a+16*b)/9, a+b


def check():
    for n in (2,3,4):
        leading, negative_limit = coefficients(n)
        assert leading > 0 and negative_limit > 0
        last_error = None
        for m in (10,30,100):
            risk, negative = exact_risk(n,m)
            assert negative == negative_limit
            assert risk > 0
            scaled = risk / (m*m)
            distance = abs(scaled-leading)
            if last_error is not None:
                assert distance < last_error
            last_error = distance
        print(f"n={n} asymptotic_coefficient={leading} negative_probability={negative_limit} exact_tests=3")
    print("CHECKS_OK")

if __name__ == "__main__":
    check()
