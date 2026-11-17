#!/usr/bin/env python3
"""Exact finite diagnostics for the complete-bipartite cut classification.

This finite check supplements, but does not prove, the universal formulas.
"""
from fractions import Fraction

checked = 0
pairs = 0
for a in range(2, 14):
    for b in range(2, a + 1):
        n = a + b
        choose = n * (n - 1) // 2
        best = Fraction(0)
        optimizers = set()
        for x in range(a + 1):
            for y in range(b + 1):
                crossing = b * x + a * y - 2 * x * y
                if crossing == 0:
                    continue
                ratio = Fraction(a * b * (x + y) * (n - x - y), choose * crossing)
                if ratio > best:
                    best, optimizers = ratio, {(x, y)}
                elif ratio == best:
                    optimizers.add((x, y))
                checked += 1
        expected = max(Fraction(4 * a * b, n * (n - 1)), Fraction(2 * a, n))
        assert best == expected, (a, b, best, expected)
        if a == b:
            exact = {(j, j) for j in range(1, a)}
        elif a == b + 1:
            exact = {(x, y) for x in range(a + 1) for y in range(b + 1)
                     if x - y in (0, 1) and (x, y) not in ((0, 0), (a, b))}
        else:
            exact = {(1, 0), (a - 1, b)}
        assert optimizers == exact, (a, b, optimizers, exact)
        metric = Fraction(2 * (a*a + b*b + a*b - a - b), n * (n - 1))
        assert metric >= best
        pairs += 1
print('COMPLETE_BIPARTITE_CUT_CENSUS_OK', checked, 'cuts;', pairs, 'part-size pairs')
