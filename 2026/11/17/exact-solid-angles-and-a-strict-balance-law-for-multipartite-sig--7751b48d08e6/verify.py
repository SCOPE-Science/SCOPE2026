#!/usr/bin/env python3
"""Exact finite checks for multipartite positive-root cone angles.

Run with Python 3; no optional packages or external inputs are required.
"""
from fractions import Fraction
from itertools import permutations, product
from math import comb, factorial


def predicted_angle(parts):
    n = sum(parts)
    assert len(parts) >= 2 and min(parts) >= 1
    f = lambda a: Fraction(sum(comb(n, j) for j in range(a)), comb(n, a))
    return (1 + sum(f(a) for a in parts)) / 2**n


def independent_rank_enumeration(parts):
    """Count signs and strict absolute-rank orders, not binomial tails."""
    n = sum(parts)
    group = tuple(g for g, size in enumerate(parts) for _ in range(size))
    cross = tuple((i, j) for i in range(n) for j in range(i + 1, n)
                  if group[i] != group[j])
    accepted = 0
    for ranks in permutations(range(1, n + 1)):
        for signs in product((-1, 1), repeat=n):
            values = tuple(sign * rank for sign, rank in zip(signs, ranks))
            if all(values[i] + values[j] >= 0 for i, j in cross):
                accepted += 1
    return Fraction(accepted, factorial(n) * 2**n)


def compositions(n, r):
    if r == 1:
        yield (n,)
        return
    for a in range(1, n - r + 2):
        for suffix in compositions(n - a, r - 1):
            yield (a,) + suffix


def majorizes(p, q):
    x, y = sorted(p, reverse=True), sorted(q, reverse=True)
    return x != y and all(sum(x[:i]) >= sum(y[:i]) for i in range(1, len(x)))


def main():
    cases = (
        (1, 1), (1, 2), (2, 2), (1, 1, 1), (1, 1, 2),
        (1, 2, 2), (2, 2, 2), (1, 1, 4), (1, 2, 3),
        (1, 1, 1, 3), (2, 2, 3), (1, 1, 1, 1, 2),
    )
    arrangements = 0
    for parts in cases:
        assert independent_rank_enumeration(parts) == predicted_angle(parts), parts
        arrangements += factorial(sum(parts)) * 2 ** sum(parts)

    convex_dimensions = 0
    for n in range(4, 31):
        f = lambda a: Fraction(sum(comb(n, j) for j in range(a)), comb(n, a))
        for a in range(1, n - 2):
            assert f(a + 2) - 2*f(a + 1) + f(a) > 0, (n, a)
            convex_dimensions += 1

    majorization_pairs = 0
    for n in range(3, 13):
        for r in range(3, min(n, 5) + 1):
            profiles = sorted(set(tuple(sorted(c)) for c in compositions(n, r)))
            for i, p in enumerate(profiles):
                for q in profiles[:i]:
                    if majorizes(p, q):
                        assert predicted_angle(p) > predicted_angle(q), (p, q)
                        majorization_pairs += 1
                    elif majorizes(q, p):
                        assert predicted_angle(q) > predicted_angle(p), (p, q)
                        majorization_pairs += 1

    assert predicted_angle((2, 2, 2)) == Fraction(3, 80)
    assert predicted_angle((1, 1, 4)) == Fraction(31, 480)
    print('SIGNED_MULTIPARTITE_ANGLE_PASS',
          'exact_profiles=' + str(len(cases)),
          'rank_sign_arrangements=' + str(arrangements),
          'convexity_inequalities=' + str(convex_dimensions),
          'majorization_pairs=' + str(majorization_pairs))


if __name__ == '__main__':
    main()
