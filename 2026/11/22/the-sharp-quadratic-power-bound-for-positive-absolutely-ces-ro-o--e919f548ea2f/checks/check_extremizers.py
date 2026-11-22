#!/usr/bin/env python3
"""Exact rational supplementary checks for positive two-spike weighted shifts."""
from fractions import Fraction

count = 0
for n in [2, 3, 4, 5, 6, 9, 19, 33, 80]:
    for c in [Fraction(6, 5), Fraction(3, 2), Fraction(2), Fraction(5), Fraction(13, 4)]:
        weights = [c] + [Fraction(1)] * (n - 2) + [c]
        powers = [Fraction(1)]
        for j in range(1, n + 2):
            products = []
            for i in range(n-j+1):
                value = Fraction(1)
                for w in weights[i:i+j]:
                    value *= w
                products.append(value)
            powers.append(max(products, default=Fraction(0)))
        assert powers == [Fraction(1)] + [c]*(n-1) + [c*c, Fraction(0)]
        count += 1
        averages = [sum(powers[:r], Fraction(0))/r for r in range(1, len(powers)+1)]
        k = c + (c-Fraction(1))**2 / (n+1)
        assert max(averages) == k
        count += 1
        assert max(powers) == c*c and c*c <= k*k
        count += 1
        for j in range(1, n+1):
            assert sum(powers[:j+1], Fraction(0))/(j+1) <= k
            count += 1
        for j in range(n+1):
            assert powers[j] * powers[n-j] >= powers[n]
            count += 1
assert count > 1000
print('POSITIVE_AM_SQUARE_SHARP_OK',count)
