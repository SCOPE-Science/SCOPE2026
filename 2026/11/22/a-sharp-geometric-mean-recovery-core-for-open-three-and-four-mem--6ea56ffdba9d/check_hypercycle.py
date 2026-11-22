#!/usr/bin/env python3
"""Finite reproducibility tests for the exact recovery-core theorem.

Exact algebra and sample trajectories supplement, but do not replace, the
all-parameter dynamical argument in RESULT.md.
"""
from fractions import Fraction
from math import exp
from random import Random


def qcycle(x):
    return sum(x[i] * x[(i - 1) % len(x)] for i in range(len(x)))


def bisection(func, lo, hi, iterations=90):
    f_lo = func(lo)
    f_hi = func(hi)
    assert f_lo * f_hi < 0
    for _ in range(iterations):
        mid = (lo + hi) / 2
        if func(mid) * f_lo > 0:
            lo = mid
            f_lo = func(mid)
        else:
            hi = mid
    return (lo + hi) / 2


def rhs(x, gamma, d):
    phi = exp(-gamma * sum(x))
    return [x[i] * (phi * x[(i - 1) % len(x)] - d) for i in range(len(x))]


def rk4(x, h, gamma, d):
    a = rhs(x, gamma, d)
    b = rhs([v + h * z / 2 for v, z in zip(x, a)], gamma, d)
    c = rhs([v + h * z / 2 for v, z in zip(x, b)], gamma, d)
    e = rhs([v + h * z for v, z in zip(x, c)], gamma, d)
    return [v + h * (z1 + 2*z2 + 2*z3 + z4)/6
            for v, z1, z2, z3, z4 in zip(x, a, b, c, e)]


def exact_identities():
    rng = Random(407)
    for _ in range(100):
        w = [Fraction(rng.randrange(1, 50), rng.randrange(1, 20))
             for j in range(4)]
        s3 = sum(w[:3]); q3 = qcycle(w[:3])
        pair3 = sum((w[i] - w[(i + 1) % 3])**2 for i in range(3))
        assert s3**2 / 3 - q3 == pair3 / 6
        s4 = sum(w); q4 = qcycle(w)
        p = w[0] + w[2]; q = w[1] + w[3]
        assert q4 == p*q
        assert s4*s4/4 - q4 == (p-q)**2/4
    w5 = list(map(Fraction, (3, 2, 1, 1, 2)))
    assert qcycle(w5) == 17
    assert qcycle(w5) > sum(w5)**2/5


def numerical_bounds_and_diagonal():
    gamma = 1.0
    for n in (3, 4):
        d = 0.12 / n
        f = lambda s: s*exp(-gamma*s)-n*d
        s_minus = bisection(f, 1.e-10, 1.0)
        s_plus = bisection(f, 1.0, 10.0)
        assert 0 < s_minus < 1/gamma < s_plus
        rng = Random(100+n)
        for trial in range(8):
            x = [rng.uniform(0.6, 1.4) for _ in range(n)]
            x = [v * (0.7 + 1.0*trial/8) / sum(x) for v in x]
            gm = _product(x)**(1/n)
            assert sum(x) < s_plus and gm > s_minus/n
            p0 = _product(x)
            for step in range(3500):
                x = rk4(x, 0.02, gamma, d)
                assert all(v > 0 for v in x)
                assert sum(x) < s_plus + 2e-9
                assert _product(x) >= p0 * (1-3e-9)
                assert all(v >= p0 / s_plus**(n-1) * (1-2e-9) for v in x)
        r0 = s_minus/(2*n)
        extinct = [r0]*n
        for step in range(10000):
            extinct = rk4(extinct, 0.05, gamma, d)
        assert max(extinct) < r0/4
        # On the diagonal above the lower branch, recovery is monotone.
        recovered = [(s_minus+s_plus)/(2*n)]*n
        for step in range(10000):
            recovered = rk4(recovered, 0.05, gamma, d)
        assert max(abs(x-s_plus/n) for x in recovered) < 1e-5


def _product(values):
    result = 1
    for v in values:
        result *= v
    return result


if __name__ == '__main__':
    exact_identities()
    numerical_bounds_and_diagonal()
    print('PASS: exact cyclic identities, five-type barrier counterexample,')
    print('two-root computation, forward bounds, and diagonal sharpness samples.')
