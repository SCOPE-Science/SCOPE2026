#!/usr/bin/env python3
"""Exact checks for birth-labelled isolated retained vertices in recursive trees.

Standard-library only. This is finite verification, not a replacement for the
analytic point-process proof in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations, product
from math import factorial, gamma


def isolated_probability(n, j, p):
    """Exact probability of a retained singleton at label j (1-indexed)."""
    v = p if j == 1 else p * (1 - p)
    for t in range(j + 1, n + 1):
        v *= 1 - p / Fraction(t - 1)
    return v


def joint_probability(n, S, p):
    """Exact law from conditional independence of parent choices given site states."""
    S = frozenset(S)
    ans = Fraction(0)
    for mask in range(1 << n):
        if any(not (mask & (1 << (j - 1))) for j in S):
            continue
        present = mask.bit_count()
        weight = p ** present * (1 - p) ** (n - present)
        marked_before = 0
        for t in range(1, n + 1):
            if t in S:
                if t > 1:
                    closed_before = (t - 1) - (mask & ((1 << (t - 1)) - 1)).bit_count()
                    weight *= Fraction(closed_before, t - 1)
                marked_before += 1
            elif t > 1 and (mask & (1 << (t - 1))):
                weight *= 1 - Fraction(marked_before, t - 1)
        ans += weight
    return ans


def exhaustive_joint_counts(n, p):
    """Brute force all recursive trees and all retention masks, without the formula."""
    sets = [S for k in range(1, min(n, 3) + 1)
            for S in combinations(range(1, n + 1), k)]
    count = {S: 0 for S in sets}
    num, den = p.numerator, p.denominator
    weights = [num ** m * (den - num) ** (n - m) for m in range(n + 1)]
    for parents in product(*(range(1, t) for t in range(2, n + 1))):
        for mask in range(1 << n):
            isolated_mask = mask
            for t, parent in enumerate(parents, start=2):
                u, v = 1 << (t - 1), 1 << (parent - 1)
                if mask & u and mask & v:
                    isolated_mask &= ~(u | v)
            s = tuple(i for i in range(1, n + 1) if isolated_mask & (1 << (i - 1)))
            weight = weights[mask.bit_count()]
            for k in range(1, min(3, len(s)) + 1):
                for subset in combinations(s, k):
                    count[subset] += weight
    denominator = den ** n * factorial(n - 1)
    return {S: Fraction(v, denominator) for S, v in count.items()}


def one_point_asymptotic(n, p, t):
    """Stable computation of mean number in a scaled window."""
    scale = n ** (float(p) / (1 + float(p)))
    k = min(n, int(t * scale))
    if k == 0:
        return 0.0
    f = 1.0  # for j=n
    expected = 0.0
    for j in range(n, 0, -1):
        prob = float(p) * ((1 - float(p)) if j > 1 else 1.0) * f
        if j <= k:
            expected += prob
        if j > 1:
            f *= 1.0 - float(p) / (j - 1)
    return expected


def run():
    tests = 0
    for p in (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)):
        for n in range(2, 8):
            exact = exhaustive_joint_counts(n, p)
            for S, observed in exact.items():
                expected = joint_probability(n, S, p)
                assert observed == expected, (n, p, S, observed, expected)
                tests += 1
                if len(S) == 1:
                    j, = S
                    assert expected == isolated_probability(n, j, p)
                    tests += 1
    # Independent first-moment check in a larger finite universe; this is
    # intentionally only numerical evidence for, not a proof of, asymptotics.
    for p in (Fraction(1, 2), Fraction(2, 3)):
        for t in (1.0, 2.0):
            n = 1000000
            observed = one_point_asymptotic(n, p, t)
            limit = float(p * (1 - p) / (1 + p)) * t ** (1 + float(p))
            assert abs(observed - limit) < 0.06, (n, p, t, observed, limit)
            tests += 1
    print(f"PASS: {tests} exact/finite/numerical comparisons")

if __name__ == '__main__':
    run()
