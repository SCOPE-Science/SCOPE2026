"""Exact finite cell-orbit checks for the five-color pentagon Hom complex.

The homotopy argument in RESULT.md is mathematical and does not depend on
extrapolating from these finite checks. Uses only Python's standard library.
"""
from collections import Counter
from itertools import product

n = 5
patterns = [m for m in range(1 << n)
            if all(not ((m >> i) & 1 and (m >> ((i + 1) % n)) & 1)
                   for i in range(n))]
assert len(patterns) == 11


def rotate(t, k):
    out = [0] * n
    for color, subset in enumerate(t):
        out[(color + k) % n] = subset
    return tuple(out)


orbits = Counter()
number_original = 0
for cell in product(patterns, repeat=n):
    if not all(any(subset & (1 << v) for subset in cell)
               for v in range(n)):
        continue
    # Cell stores which source vertices admit each of the five colors.
    # Each color class is independent, and every source vertex is covered.
    number_original += 1
    assert len({rotate(cell, k) for k in range(n)}) == n, (
        'nontrivial color-cycle stabilizer', cell)
    if cell != min(rotate(cell, k) for k in range(n)):
        continue
    dimension = sum(mask.bit_count() for mask in cell) - n
    orbits[dimension] += 1

expected = {0: 204, 1: 1140, 2: 2600,
            3: 3000, 4: 1750, 5: 414}
assert dict(orbits) == expected, (dict(orbits), expected)
assert number_original == n * sum(orbits.values()) == 45540
assert sum((-1) ** d * c for d, c in orbits.items()) == 0

# A five-cycle on R^5 has eigenvalues 1,zeta,zeta^2,zeta^3,zeta^4.
# Its real four-dimensional sum-zero representation is exactly the pair
# of rotation planes of weights 1 and 2; hence its S^3 quotient is L(5;1,2).
print('color-class patterns:', len(patterns))
print('original cell count:', number_original)
print('free C5 cell orbits:', sorted(orbits.items()))
print('orbit Euler characteristic:', 0)
print('sum-zero representation weights:', (1, 2))
print('PASS: all exact finite checks')
