#!/usr/bin/env python3
"""Integer-only enumeration of labelled undirected cycle packings."""
from math import comb, factorial


def packing_count(m):
    values = [0] * (m + 1)
    values[0] = 1
    for j in range(1, m + 1):
        values[j] = sum(comb(j - 1, ell - 1) * factorial(ell - 1) // 2 * values[j - ell]
                        for ell in range(5, j + 1))
    return values[m]


expected = {6: 72, 7: 420, 8: 2880, 9: 22680, 10: 201600, 11: 2195424}
for n in range(6, 17):
    actual = n * packing_count(n - 1)
    if n in expected:
        assert actual == expected[n], (n, actual)
    print(n, actual)
# Exact count of a pair of disjoint 5-cycles, leaving one isolated label.
assert 11 * comb(10, 5) * 12 * 12 // 2 == 199584
assert 11 * factorial(9) // 2 + 199584 == expected[11]
print("CYCLE_ENUMERATOR_OK")
