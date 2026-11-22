#!/usr/bin/env python3
"""Standalone decimal-precision spot checks for two-power moment shifts.

These finite calculations corroborate formulas, but do not establish
all-index sign monotonicity or infinite-dimensional Schatten membership.
"""
from decimal import Decimal, localcontext
from math import comb


def forward_difference(m, exponent, x):
    return sum(
        Decimal((-1) ** (m - j) * comb(m, j))
        * (x + Decimal(j)) ** exponent
        for j in range(m + 1)
    )


def falling(alpha, m):
    p = Decimal(1)
    for j in range(m):
        p *= alpha - Decimal(j)
    return p


def main():
    checks = 0
    with localcontext() as ctx:
        ctx.prec = 85
        for m, alpha, a in (
            (2, Decimal('0.5'), Decimal(1)),
            (3, Decimal('1.5'), Decimal(1)),
            (4, Decimal('2.5'), Decimal(1)),
            (5, Decimal('3.25'), Decimal('1.7')),
        ):
            c = alpha / (Decimal(m) - alpha)
            thresholds = []
            for n in range(32):
                x = a + Decimal(n)
                numerator = forward_difference(m, alpha, x)
                denominator = forward_difference(m, alpha - 1, x)
                assert numerator < 0 < denominator
                checks += 2
                threshold = -numerator / denominator
                thresholds.append(threshold)
                if n:
                    assert threshold - thresholds[-2] > c
                    checks += 1
                beta = x ** alpha + threshold * x ** (alpha - 1)
                assert abs(numerator + threshold * denominator) < Decimal('1e-65')
                assert beta > 0
                checks += 2
            for k in range(5):
                eta = (thresholds[k] + thresholds[k + 1]) / 2
                for n in range(12):
                    x = a + Decimal(n)
                    beta = x ** alpha + eta * x ** (alpha - 1)
                    d = (forward_difference(m, alpha, x)
                         + eta * forward_difference(m, alpha - 1, x)) / beta
                    assert (d > 0) == (n <= k)
                    checks += 1
            for n in (300, 500, 1000):
                x = a + Decimal(n)
                eta = Decimal('0.7')
                beta = x ** alpha + eta * x ** (alpha - 1)
                d = (forward_difference(m, alpha, x)
                     + eta * forward_difference(m, alpha - 1, x)) / beta
                rel = d * (Decimal(n) ** m) / falling(alpha, m)
                assert abs(rel - 1) < Decimal('0.06')
                checks += 1
    print('FRACTIONAL_DEFECT_DIAGNOSTIC_OK', checks)


if __name__ == '__main__':
    main()
