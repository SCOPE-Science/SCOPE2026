#!/usr/bin/env python3
"""Exact finite stress test of two-shift pseudoperiod circle criterion.

Enumerates every endpoint of the coding and shifted coding intervals,
then one rational point per intervening open interval. The infinite
irrational theorem is proved separately by elementary interval geometry.
"""
from fractions import Fraction as Q


def all_circle_positions_agree(alpha, a, b):
    a %= 1
    b %= 1
    cuts = {Q(0), alpha, (-a) % 1, (alpha - a) % 1,
            (-b) % 1, (alpha - b) % 1}
    cuts = sorted(cuts)

    def flips(x, shift):
        return (x < alpha) != (((x + shift) % 1) < alpha)

    probes = cuts + [(left + right) / 2
                     for left, right in zip(cuts, cuts[1:] + [Q(1)])]
    return all(not (flips(x, a) and flips(x, b)) for x in probes)


def main():
    test_slopes = [Q(233, 610), Q(239, 577), Q(577, 1393),
                   Q(127, 401), Q(37, 1000), Q(659, 1001)]
    checks = 0
    boundary_equalities = 0
    for alpha in test_slopes:
        assert 0 < alpha < 1
        for p in range(1, 81):
            for q in range(p + 1, 81):
                a, b = (p * alpha) % 1, (q * alpha) % 1
                assert a and b and a != b
                predicted = abs(a - b) >= max(alpha, 1 - alpha)
                actual = all_circle_positions_agree(alpha, a, b)
                assert predicted == actual, (alpha, p, q, predicted, actual)
                boundary_equalities += (abs(a-b) == max(alpha, 1-alpha))
                checks += 1
    assert checks == 18960
    assert boundary_equalities > 0
    print('VERIFY_OK exact_rational_pairs=',checks,
          'sharp_boundary_cases=',boundary_equalities)


if __name__ == '__main__':
    main()
