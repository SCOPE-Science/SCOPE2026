#!/usr/bin/env python3
"""Reproducible finite checks for the path matching-game nucleon theorem.

Python 3 standard library only. The proof for all orders is in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations_with_replacement


def matching_value(n, mask):
    # Independent dynamic program for a maximum cardinality matching on a path.
    dp = [0] * (n + 1)
    for j in range(2, n + 1):
        dp[j] = dp[j - 1]
        if mask & (1 << (j - 2)) and mask & (1 << (j - 1)):
            dp[j] = max(dp[j], 1 + dp[j - 2])
    return dp[n]


def proposed_payoffs(n):
    if n % 2:
        return [Fraction(i % 2) for i in range(n)]  # indices 0,2,... -> 0
    m = n // 2
    return [Fraction(j, m + 1) if i % 2 == 0
            else Fraction(m + 1 - j, m + 1)
            for i in range(n) for j in [(i // 2) + 1]]


def base_pair_union(n, mask):
    return all(bool(mask & (1 << (2 * j))) == bool(mask & (1 << (2 * j + 1)))
               for j in range(n // 2))


def coalition_ratio(payoffs, mask, value):
    return sum((payoffs[i] for i in range(len(payoffs)) if mask & (1 << i)), Fraction(0)) / value


def test_order(n):
    x = proposed_payoffs(n)
    assert sum(x) == n // 2
    assert all(t >= 0 for t in x)
    core_tests = 0
    refinement_tests = 0
    smallest_refinement = None
    for mask in range(1, (1 << n) - 1):
        v = matching_value(n, mask)
        if not v:
            continue
        r = coalition_ratio(x, mask, v)
        assert r >= 1, (n, mask, r)
        core_tests += 1
        if n % 2 == 0:
            if base_pair_union(n, mask):
                assert r == 1, (n, mask, r)
            else:
                assert r > 1, (n, mask, r)
                target = Fraction(1) + Fraction(1, (n // 2) ** 2 - 1)
                assert r >= target, (n, mask, r)
                smallest_refinement = r if smallest_refinement is None else min(smallest_refinement, r)
                refinement_tests += 1
    if n % 2 == 0:
        m = n // 2
        # m+1 explicit tight coalitions, indexed by the m+1 gaps.
        tests = [((1 << n) - 1) ^ (1 << 1)]
        for j in range(1, m):
            tests.append(((1 << n) - 1) ^ (1 << (2*j - 2)) ^ (1 << (2*j + 1)))
        tests.append(((1 << n) - 1) ^ (1 << (2*m - 2)))
        for mask in tests:
            assert matching_value(n, mask) == m - 1
            assert coalition_ratio(x, mask, m - 1) == Fraction(1) + Fraction(1, m*m-1)
        assert smallest_refinement == Fraction(1) + Fraction(1, m*m-1)
    return core_tests, refinement_tests


def test_rational_grid(n):
    # Independent finite grid: every first-stage-optimal core allocation on an
    # even path is (a_1,1-a_1,...,a_m,1-a_m) with 0<=a_1<=...<=a_m<=1.
    m = n // 2
    d = m + 1
    xstar = proposed_payoffs(n)
    active = [(s, matching_value(n, s)) for s in range(1, (1 << n) - 1)
              if not base_pair_union(n, s) and matching_value(n, s) > 0]
    best = Fraction(-1)
    maximizers = []
    for a in combinations_with_replacement(range(d + 1), m):
        x = [y for z in a for y in (Fraction(z, d), 1-Fraction(z, d))]
        least = min(coalition_ratio(x, mask, v) for mask, v in active)
        if least > best:
            best, maximizers = least, [a]
        elif least == best:
            maximizers.append(a)
    assert best == Fraction(1) + Fraction(1, m*m - 1)
    assert maximizers == [tuple(range(1, m+1))], (n, best, maximizers)
    assert xstar == [y for z in maximizers[0] for y in (Fraction(z, d), 1-Fraction(z, d))]
    return len(list(combinations_with_replacement(range(d+1), m)))


def main():
    total = 0
    for n in range(3, 17):
        a, b = test_order(n)
        total += a
        print(f'P_{n}: {a} positive-coalition checks; {b} nonfixed second-layer checks')
    grid = 0
    for n in (4, 6, 8, 10):
        k = test_rational_grid(n)
        grid += k
        print(f'P_{n}: {k} rational core-grid candidates checked; unique optimum')
    print(f'VERIFIED: {total} positive coalitions; {grid} rational-grid candidates')

if __name__ == '__main__':
    main()
