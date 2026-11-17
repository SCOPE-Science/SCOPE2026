#!/usr/bin/env python3
"""Independent finite-state, rank-integral, and Bessel-series checks for wheel RSA.
Requires Python >=3.9; no third-party packages.
"""
import itertools
import math
from fractions import Fraction
from functools import lru_cache


def vacancy_by_available_edge_recursion(n):
    """Exact probability from all uncovered rim subsets, hub still vacant."""
    if n < 4:
        raise ValueError('Wheel rim length must be at least 4.')

    @lru_cache(None)
    def q(mask):
        if not mask:
            return Fraction(1)
        edges = [(a, (a + 1) % n) for a in range(n)
                 if mask & (1 << a) and mask & (1 << ((a + 1) % n))]
        denominator = mask.bit_count() + len(edges)
        return sum((q(mask ^ (1 << a) ^ (1 << b))
                    for a, b in edges), Fraction(0)) / denominator

    return q((1 << n) - 1)


def vacancy_by_rank_integrals(m):
    """Exact integral over ordered exponential matching-edge clocks.

    Each of m intervening edges contributes its minimum of two adjacent
    matched clock variables, including both parallel index contributions
    when m=2 (the actual cycle still has distinct intervening edges).
    """
    if m < 2:
        raise ValueError('m must be at least 2.')
    total = Fraction(0)
    for order in itertools.permutations(range(m)):
        rank = [0] * m
        for rank_no, vertex in enumerate(order):
            rank[vertex] = rank_no
        coefficients = [3] * m
        for j in range(m):
            k = (j + 1) % m
            coefficients[j if rank[j] < rank[k] else k] += 1
        denominator = 1
        running = 0
        for index in reversed(order):
            running += coefficients[index]
            denominator *= running
        total += Fraction(1, denominator)
    return 2 * total


def vacancy_by_all_edge_orders(n):
    """Enumerate all edge arrival rankings (only n=4 is feasible)."""
    if n != 4:
        raise ValueError('Only the 4-rim case is used for factorial enumeration.')
    edges = [(a, (a + 1) % n) for a in range(n)]
    edges += [(n, a) for a in range(n)]
    favorable = 0
    for order in itertools.permutations(edges):
        covered = 0
        for a, b in order:
            if not ((covered >> a) & 1 or (covered >> b) & 1):
                covered |= (1 << a) | (1 << b)
        favorable += not bool(covered & (1 << n))
    return Fraction(favorable, math.factorial(len(edges)))


def modified_bessel_i(nu, x):
    """Convergent power series at small positive x (nu = +/- 1/4, 3/4)."""
    value = (x / 2)**nu / math.gamma(nu + 1)
    term = value
    for k in range(1, 100):
        term *= (x*x/4) / (k * (k+nu))
        new = value + term
        if abs(new - value) < 1e-16 * abs(new):
            return new
        value = new
    raise ArithmeticError('Bessel series did not converge')


def solve_positive_bessel_root():
    f = lambda x: 2*x*modified_bessel_i(.75, x) - modified_bessel_i(-.25, x)
    lo, hi = .25, 1.5
    assert f(lo) < 0 < f(hi)
    for _ in range(64):
        mid = (lo + hi) / 2
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main():
    expected = {
        4: Fraction(1, 6),
        6: Fraction(1, 21),
        8: Fraction(19, 1386),
        10: Fraction(41, 10395),
        12: Fraction(523, 460845),
        14: Fraction(890, 2725569),
        16: Fraction(5323909, 56664579510),
    }
    assert vacancy_by_all_edge_orders(4) == Fraction(1, 6)
    assert vacancy_by_available_edge_recursion(5) == 0
    for n, correct in expected.items():
        a = vacancy_by_available_edge_recursion(n)
        b = vacancy_by_rank_integrals(n // 2)
        assert a == b == correct, (n, a, b, correct)
        print(f'rim={n:2d} exact_probability={a} decimal={float(a):.13g}')
    root = solve_positive_bessel_root()
    lam = 1/(4*root*root)
    assert abs(root - 0.9321309848066271) < 2e-13
    assert abs(lam - 0.28773064524141925) < 2e-13
    assert abs(modified_bessel_i(-.25, root) - 2*root*modified_bessel_i(.75, root)) < 2e-14
    print('bessel_root=', format(root, '.16f'))
    print('dominant_eigenvalue=', format(lam, '.16f'))
    print('ratio_probabilities_16_over_14=',
          float(expected[16] / expected[14]))
    print('ALL_CHECKS_PASS')

if __name__ == '__main__':
    main()
