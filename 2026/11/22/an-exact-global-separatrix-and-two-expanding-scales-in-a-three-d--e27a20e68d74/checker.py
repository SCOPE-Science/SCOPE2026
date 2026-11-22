#!/usr/bin/env python3
"""Standalone algebraic and numerical diagnostics for the polynomial map.

Run: python checker.py
The finite examples are not a substitute for the all-real spectral proof.
"""
from fractions import Fraction as Q
from math import log, sqrt
from decimal import Decimal, getcontext
from random import Random


def F(a, b, p):
    x, y, z = p
    return (a * y * y, b * y * (1 - z), 1 - x)


def root():
    lo, hi = 1., 2.
    for _ in range(70):
        m = (lo + hi) / 2
        if m ** 3 - m ** 2 - 2 > 0:
            hi = m
        else:
            lo = m
    return (lo + hi) / 2


def log_h(a, b, p, r):
    x, y, z = p
    return (.5 * r*r * log(float(a*b)) + (r+1)*log(float(b))
            + log(abs(float(x))) + r*r*log(abs(float(y)))
            + r*log(abs(1-float(z))))


def rational_test():
    rng = Random(12092023)
    trials = 0
    for _ in range(84):
        a = Q(rng.randint(1, 4), rng.randint(1, 3))
        b = Q(rng.randint(1, 4), rng.randint(1, 3))
        x = Q(rng.randint(-3, 3), rng.randint(1, 5))
        y = Q(rng.randint(-3, 3), rng.randint(1, 5))
        z = Q(rng.randint(-3, 3), rng.randint(1, 5))
        yy = []
        p = (x, y, z)
        for n in range(7):
            yy.append(p[1])
            p = F(a, b, p)
        for n in range(4):
            assert yy[n+3] == a*b*yy[n+2]*yy[n]*yy[n]
            trials += 1
    return trials


def invariant_test(r):
    rng = Random(1023)
    trials = 0
    for _ in range(401):
        a = rng.uniform(.2, 2.7)
        b = rng.uniform(.3, 3.2)
        x = rng.choice([-1,1]) * rng.uniform(.2, 2.3)
        y = rng.choice([-1,1]) * rng.uniform(.1, 2.7)
        h = rng.choice([-1,1]) * rng.uniform(.15, 1.6)
        p = (x, y, 1-h)
        v = log_h(a,b,p,r)
        u = log_h(a,b,F(a,b,p),r)
        assert abs(u-r*v) < 6e-13 * (1+abs(v))
        trials += 1
    return trials


def sign_and_boundary_tests(r):
    count = 0
    for sx in [-1,1]:
        for sy in [-1,1]:
            for sh in [-1,1]:
                p = (Q(sx), Q(sy), Q(1-sh))
                assert abs(log_h(1,1,p,r)) < 1e-12
                for _ in range(5):
                    p = F(Q(1),Q(1),p)
                assert p in [(Q(1),Q(1),Q(0)),(Q(1),Q(-1),Q(0))]
                count += 1
    for x, expected in [(Q(1,4), -1), (Q(4), 1)]:
        p = (x, Q(1), Q(0))
        v = log_h(1,1,p,r)
        assert v * expected > 0
        count += 1
    # Work at high precision: a floating cancellation would grow in the r mode.
    getcontext().prec = 110
    rd = Decimal(17)/10
    for _ in range(30):
        rd -= (rd**3-rd**2-2)/(3*rd**2-2*rd)
    L0, L1 = Decimal('0.03'), Decimal('0.03')
    L2 = -(rd*rd-rd)*L0-(rd-1)*L1
    L = [L0,L1,L2]
    for n in range(180):
        L.append(L[n+2] + 2*L[n])
    assert max(L[45:]) > 300 and min(L[45:]) < -300
    assert abs((rd*rd-rd)*L0+(rd-1)*L1+L2) < Decimal('1e-100')
    count += 2
    return count, float(min(L[45:])), float(max(L[45:]))


def main():
    r = root()
    assert abs(r**3-r*r-2) < 1e-13
    assert 1 < sqrt(2/r) < r
    assert abs(2/r - (r*r-r)) < 1e-13
    assert abs(2/r**2 - (r-1)) < 1e-13
    a = rational_test()
    b = invariant_test(r)
    c, low, high = sign_and_boundary_tests(r)
    print(f'PASS: {a} exact rational recurrence comparisons, '
          f'{b} log-eigenfunction tests, {c} threshold/exception tests.')
    print(f'r={r:.15f}, s={(2/r)**.5:.15f}; '
          f'critical-mode sampled log range [{low:.4g}, {high:.4g}]')


if __name__ == '__main__':
    main()
