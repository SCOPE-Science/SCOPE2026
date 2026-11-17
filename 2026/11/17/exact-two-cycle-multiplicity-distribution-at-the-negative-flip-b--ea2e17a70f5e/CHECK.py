"""Exact finite-parameter regression tests for negative affine floor-map cycle counts.

The analytic theorems are established in RESULT.md.  This script tests independent
integer-orbit enumeration against the proposed parity/window formula and checks
interval-probability arithmetic; it is not an exhaustive proof.
"""
from fractions import Fraction as Q
from math import floor, ceil


def direct(e, mu):
    lam = e - 1
    bound = 2 * ceil(1 / e) + 8
    f = lambda x: floor(lam * x + mu)
    return sum(1 for x in range(-bound, bound + 1) if x < f(x) and f(f(x)) == x)


def window_count(e, mu):
    d = 2 - e
    v = mu / d
    v -= floor(v)
    sigma = int(2 * v)
    w = v - Q(sigma, 2)
    K = ceil(1 / e) - 1
    return sum(1 for k in range(1, K + 1)
               if k % 2 == sigma and e*k <= 2*d*w
               and e*k < 2*(1-d*w))


def tail(e, m):
    d = 2 - e
    return (max(Q(0), 1 - e * (2*m-1))
            + max(Q(0), 1 - e * 2*m)) / d

cases = 0
for e in (Q(1,2), Q(1,3), Q(1,4), Q(2,9), Q(1,11), Q(3,29), Q(1,67)):
    d = 2 - e
    K = ceil(1 / e) - 1
    for j in range(121):
        mu = d * Q(j,121)
        a, b = direct(e, mu), window_count(e, mu)
        assert a == b, (e,mu,a,b)
        v = Q(j, 121)
        w = v - Q(int(2*v),2)
        F = min(2*w, 1-2*w)
        assert abs(e*a-F) <= Q(3,2)*e, (e,mu,F,a)
        cases += 1
    # An exact expectation identity, using the closed tail and cycle-gap sums.
    E_tail = sum((tail(e,m) for m in range(1,K+1)), Q(0))
    E_gaps = sum((1-e*k for k in range(1,K+1)), Q(0))/d
    assert E_tail == E_gaps, (e,E_tail,E_gaps)
    assert tail(e,1) <= 1
    assert all(tail(e,m) >= tail(e,m+1) for m in range(1,K+1))
print(f"QUASI_AFFINE_NEAR_FLIP_LAW_OK: {cases} exact integer-orbit cases")
