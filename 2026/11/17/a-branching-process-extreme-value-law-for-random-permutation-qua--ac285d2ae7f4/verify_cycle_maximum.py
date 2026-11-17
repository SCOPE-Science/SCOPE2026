#!/usr/bin/env python3
"""Reproducible finite checks for random-permutation equilibrium maxima.

The analytic theorem is proved in RESULT.md; these finite checks are supplementary.
Requires only the Python standard library.
"""
import itertools
import math
import random


def gamma_upper_tail(k, t):
    # P(Gamma(k,1)>k*t), for integer k. Accurate for the tests below.
    y = k * t
    # Start at the last Poisson term and work down: avoids overflow for k>>1.
    term = math.exp(-y + (k - 1) * math.log(y) - math.lgamma(k))
    partial = term
    for j in range(k-1, 0, -1):
        term *= j / y
        partial += term
    return partial


def coeff_cdf(n, t):
    p = [0.0] + [1.0 - gamma_upper_tail(k, t) for k in range(1, n + 1)]
    a = [1.0]
    for j in range(1, n + 1):
        a.append(sum(p[k] * a[j - k] for k in range(1, j + 1)) / j)
    return a[-1]


def cycles(perm):
    n = len(perm)
    seen = set()
    for i in range(n):
        if i in seen:
            continue
        c, j = [], i
        while j not in seen:
            seen.add(j)
            c.append(j)
            j = perm[j]
        yield c


def brute_cycle_index(n, t):
    total = 0.0
    p = [0] + [1 - gamma_upper_tail(k, t) for k in range(1, n + 1)]
    for perm in itertools.permutations(range(n)):
        prod = 1.0
        for c in cycles(perm):
            prod *= p[len(c)]
        total += prod
    return total / math.factorial(n)


def extinction_probability(t):
    if t <= 1:
        return 1.0
    lo, hi = 0.0, 1.0 - 1e-14
    for _ in range(110):
        x = (lo + hi) / 2
        if x - math.exp(-t * (1 - x)) < 0:
            lo = x
        else:
            hi = x
    return (lo + hi) / 2


def test_qso_limit():
    n = 6
    perm = (2, 1, 0, 4, 5, 3)
    init = (0.09, 0.07, 0.11, 0.14, 0.17, 0.12, 0.30)
    expected = [0.0] * n
    for c in cycles(perm):
        v = sum(init[j] for j in c) / (2 * len(c) * sum(init[:n]))
        for j in c:
            expected[j] = v
    for alpha in (0.17, 0.71):
        x = list(init)
        for _ in range(800):
            z = x[-1]
            x = [2*z*(alpha*x[i] + (1-alpha)*x[perm[i]]) for i in range(n)] + [z*z + (1-z)*(1-z)]
        assert abs(x[-1] - 0.5) < 2e-13
        assert max(abs(x[j]-expected[j]) for j in range(n)) < 3e-12, (alpha,x, expected)


def test_finite_enumeration():
    for n in (1, 2, 3, 4, 5, 6):
        for t in (1.2, 2.0):
            v, w = coeff_cdf(n, t), brute_cycle_index(n, t)
            assert abs(v - w) < 2e-13, (n,t,v,w)


def test_branching_identity():
    for t in (1.1, 1.5, 2.0, 3.0):
        rho = extinction_probability(t)
        s = sum(gamma_upper_tail(k,t)/k for k in range(1, 2501))
        assert abs(math.exp(-s) - (1 - rho)) < 2e-5, (t,s,rho)
        if t >= 1.5:
            assert abs(coeff_cdf(300,t) - (1-rho)) < 2e-12


def test_sampling():
    rng = random.Random(20261110)
    n, repetitions = 350, 3400
    for t in (1.5,2.0):
        count = 0
        for _ in range(repetitions):
            perm = list(range(n))
            rng.shuffle(perm)
            marks = [rng.expovariate(1) for j in range(n)]
            denom = sum(marks)
            u = max(sum(marks[j] for j in c)/len(c) for c in cycles(perm))
            count += (n*u/denom <= t)
        empirical = count/repetitions
        predicted = 1 - extinction_probability(t)
        assert abs(empirical - predicted) < 0.045, (t,empirical,predicted)
        print('sample n=%s, t=%.1f, empirical=%.5f, limit=%.5f' % (n,t,empirical,predicted))


if __name__ == '__main__':
    test_qso_limit()
    test_finite_enumeration()
    test_branching_identity()
    test_sampling()
    print('PERMUTATION_QSO_MAXIMUM_BRANCHING_CHECK_OK')
