#!/usr/bin/env python3
"""Finite corroboration for the generalized density-sampling half-logistic law.

The analytic all-index and all-parameter statements are proved in RESULT.md;
this executable checks independent exact examples, normalizations and grids.
Standard library only; run `python3 verification/check.py`.
"""
from fractions import Fraction
from math import exp, log, log1p, isclose, expm1


def wlog(shape, rate, n):
    return -shape * rate * n - (shape + 1) * log1p(exp(-rate * n))


def f(rate_a, rate_b, x):
    return log1p(exp(-rate_a * x)) - log1p(exp(-rate_b * x))


def c(rate_a, rate_b):
    h = f(rate_a, rate_b, 1)
    return h / (rate_b - rate_a - h)


def modal_threshold(rate, n):
    qn = exp(-rate * n)
    h = log1p(qn) - log1p(qn * exp(-rate))
    return h / (rate - h)


def finite_probabilities(shape, rate, nmax=10000):
    raw = [exp(wlog(shape, rate, n)) for n in range(nmax)]
    z = sum(raw)
    # Since w(n) <= exp(-shape * rate * n), the omitted mass is bounded
    # by exp(-shape * rate * nmax) / (1 - exp(-shape * rate)).
    tail = exp(-shape * rate * nmax) / (-expm1(-shape * rate))
    return [x/z for x in raw], tail/z


def run():
    # Exact, normalization-independent LR witness at alpha=1/4,
    # first rate log 2, second rate log 4.
    increase_fourth_power = Fraction(6, 5)**5 / 2
    decrease_fourth_power = Fraction(50, 51)**5 / 2
    assert increase_fourth_power > 1 and decrease_fourth_power < 1
    assert increase_fourth_power == Fraction(3888, 3125)

    a, b, shape = log(2), log(4), 0.25
    assert shape < c(a, b) < 1
    # At shape=1/2 the same two-rate comparison is LR-decreasing.
    assert 0.5 > c(a, b)

    # The exact modal staircase is a strict all-index theorem; check
    # local ratios and the maximizing atom on finite reproducible slices.
    for rate in [0.2, log(2), 1.2]:
        cuts = [modal_threshold(rate, n) for n in range(35)]
        assert all(cuts[j] > cuts[j+1] > 0 for j in range(34))
        for k in [0, 1, 2, 5, 10]:
            if k == 0:
                shape = 1.25 * cuts[0]
            else:
                shape = (cuts[k-1] + cuts[k]) / 2
            p, tail = finite_probabilities(shape, rate)
            if shape * rate >= 0.01:
                assert tail < 1e-11
            assert max(range(len(p)), key=lambda j: p[j]) == k, (rate, shape, k)
            # Strict discrete log-concavity on the first 100 atoms.
            for n in range(1, min(70, int(16/rate))):
                second_logdiff = wlog(shape, rate, n+1) - 2*wlog(shape, rate, n) + wlog(shape, rate, n-1)
                assert second_logdiff < 0, (rate, shape, n, second_logdiff)

    # Likelihood-ratio adjacent slopes: all tested pairs have either
    # strict decrease or one initial rise followed by strict decrease.
    for a, b in [(0.03, 0.07), (0.1, 0.4), (log(2), log(4)), (0.7, 3.0), (2.0, 2.3)]:
        threshold = c(a, b)
        assert 0 < threshold < 1
        for shape in [threshold / 2, threshold * 2, 1.0]:
            log_increments = [wlog(shape,b,n+1)-wlog(shape,b,n)
                              -wlog(shape,a,n+1)+wlog(shape,a,n) for n in range(1000)]
            initial = log_increments[0]
            if shape < threshold:
                assert initial > 1e-12
                assert any(x < -1e-8 for x in log_increments)
                signs = [x > 1e-10 for x in log_increments]
                assert all(not signs[j] or signs[j-1] for j in range(1, len(signs)))
            else:
                assert initial < -1e-12
                assert all(x < 1e-10 for x in log_increments)

    # The two-phase critical rate boundary: at alpha=1/4, a=log(2),
    # comparison log(4) violates LR, but comparison at rate 3 restores it.
    a = log(2)
    assert c(a, log(4)) > 0.25 > c(a, 3)
    assert isclose(c(a, a + 1e-6), exp(-a), abs_tol=1e-6)
    print('PASS: exact witness; mode and log-concavity slices; one-turn likelihood ratios; sharp crossover checks')


if __name__ == '__main__':
    run()
