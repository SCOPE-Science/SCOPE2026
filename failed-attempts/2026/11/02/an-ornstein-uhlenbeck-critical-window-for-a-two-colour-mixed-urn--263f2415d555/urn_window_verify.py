#!/usr/bin/env python3
"""Exact finite-state checks for a balanced two-colour mixed urn.

The program uses only the Python standard library. It verifies finite-state
transition laws and moment identities; it is not a proof of weak convergence.
"""
from fractions import Fraction
from math import log, exp, isclose


def exact_law(p, n):
    """Return the exact law of the colour difference after n draws."""
    p = Fraction(p)
    law = {0: Fraction(1)}
    for j in range(1, n + 1):
        total_before = 4 * j
        nxt = {}
        for u, mass in law.items():
            prob_positive = Fraction(total_before + u, 2 * total_before)
            for r, prob_r in ((-2, p), (4, 1 - p)):
                for sign, prob_s in ((1, prob_positive), (-1, 1 - prob_positive)):
                    target = u + r * sign
                    nxt[target] = nxt.get(target, Fraction(0)) + mass * prob_r * prob_s
        law = nxt
        assert sum(law.values(), Fraction(0)) == 1
        assert all(z >= 0 for z in law.values())
        assert all(abs(u) <= 4 * (j + 1) for u in law)
    return law


def moment_by_recursion(p, n):
    p = Fraction(p)
    alpha = Fraction(1) - Fraction(3, 2) * p
    v = Fraction(16) - 12 * p
    m = Fraction(0)
    for j in range(1, n + 1):
        m = (1 + 2 * alpha / j) * m + v
    return m


def test_exact():
    assertions = 0
    for p in (Fraction(1, 3), Fraction(2, 5), Fraction(1, 4), Fraction(3, 5)):
        for n in range(0, 13):
            law = exact_law(p, n)
            m1 = sum(Fraction(u) * mass for u, mass in law.items())
            m2 = sum(Fraction(u * u) * mass for u, mass in law.items())
            assert m1 == 0
            assert m2 == moment_by_recursion(p, n)
            assertions += 2
    for n in range(0, 501):
        h = sum((Fraction(1, j) for j in range(1, n + 2)), Fraction(0))
        assert moment_by_recursion(Fraction(1, 3), n) == 12 * (n + 1) * (h - 1)
        assertions += 1
    for n in range(1, 30):
        for p in (Fraction(1, 3), Fraction(2, 5)):
            law = exact_law(p, min(n, 12))
            alpha = 1 - Fraction(3, 2) * p
            for u in law:
                j = min(n, 12) + 1
                # Exact conditional E[U_next | U_now=u]
                mean_step = Fraction(4) * alpha * Fraction(u, 4 * j)
                assert u + mean_step == (1 + alpha / j) * u
                assertions += 1
    print(f'exact assertions passed: {assertions}')
    return assertions


def F(tau):
    if tau == 0:
        return 1.0
    return -__import__('math').expm1(-2 * tau) / (2 * tau)


def float_moment(p, N):
    alpha = 1 - 1.5 * p
    v = 16 - 12 * p
    m = 0.0
    for j in range(1, N+1):
        m = (1 + 2 * alpha / j) * m + v
    return m


def test_window():
    assertions = 0
    for tau in (-2, -1, -.5, 0, .5, 1, 2):
        for N in (1000, 10000, 100000):
            p = 1/3 + 2*tau/(3*log(N))
            assert 0 < p < 1
            m = float_moment(p, N)
            target = 12 * F(tau)
            # Check deterministic exact recurrence remains in the predicted
            # broad asymptotic scaling range; this is not used as proof.
            ratio = (m / (N*log(N))) / target
            assert .2 < ratio < 1.8, (tau, N, ratio)
            assertions += 2
    for tau in (-2, -1, -.5, 0, .5, 1, 2):
        # This deterministic integral is the limiting predictable-bracket factor.
        integral = sum(exp(2*tau*(j + .5)/5000) / 5000 for j in range(5000))
        analytic = 1 if tau == 0 else __import__('math').expm1(2*tau)/(2*tau)
        assert isclose(integral, analytic, rel_tol=1e-6)
        assert isclose(exp(-2*tau)*integral, F(tau), rel_tol=1e-6)
        assertions += 2
    print(f'asymptotic diagnostics passed: {assertions}')
    return assertions


if __name__ == '__main__':
    total = test_exact() + test_window()
    print('Total passed:', total)
