#!/usr/bin/env python3
"""Exact two-round finite chain-binomial checks; Python standard library only."""
from fractions import Fraction as F
from math import comb


def exact_joint_covariance(n, p, mu):
    """Independently enumerate C1, R1, C2 joint events with rational weights."""
    e1 = e2 = e12 = F(0)
    total = F(0)
    for c1 in range(n + 1):
        prob1 = F(comb(n, c1)) * p**c1 * (1 - p)**(n - c1)
        for r, prob_r in ((0, 1 - mu), (1, mu)):
            sus = n - c1
            infectious = 1 - r + c1
            inf_prob = 1 - (1 - p)**infectious
            for c2 in range(sus + 1):
                w = (prob1 * prob_r * comb(sus, c2) *
                     inf_prob**c2 * (1 - inf_prob)**(sus - c2))
                total += w
                e1 += c1 * w
                e2 += c2 * w
                e12 += c1 * c2 * w
    assert total == 1, ('law not normalized', total)
    return e12 - e1 * e2


def closed_covariance(n, p, mu):
    q = 1 - p
    a = q + mu * p
    return n * p * q * (a * q * (1 + n * p) * (1 - p*p)**(n-2) - 1)


def main():
    cases = 0
    for n in range(2, 8):
        for p in (F(1, 7), F(3, 5), F(4, 5)):
            for mu in (F(0), F(1, 3), F(1)):
                direct = exact_joint_covariance(n, p, mu)
                formula = closed_covariance(n, p, mu)
                assert direct == formula, (n, p, mu, direct, formula)
                cases += 1
    assert cases == 54
    assert closed_covariance(3, F(1, 10), F(0)) == F(114669, 10000000)
    assert closed_covariance(3, F(1, 4), F(0)) == -F(711, 16384)
    assert closed_covariance(2, F(1, 2), F(1)) == 0
    for p in (F(1, 7), F(1, 2), F(4, 5)):
        assert closed_covariance(2, p, F(0)) < 0
    print('PASS: 54 full-joint exact-rational checks; two sign witnesses and boundary')

if __name__ == '__main__':
    main()
