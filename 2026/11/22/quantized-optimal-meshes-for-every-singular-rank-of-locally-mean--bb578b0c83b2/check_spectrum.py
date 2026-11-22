"""Finite exact and numerical checks for the local-mean Volterra mesh theorem.

These tests are not an infinite-dimensional proof. Uses only Python stdlib.
"""
from fractions import Fraction
from itertools import combinations
from math import isclose


def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for cuts in combinations(range(1, total), parts - 1):
        edges = (0,) + cuts + (total,)
        yield tuple(edges[j + 1] - edges[j] for j in range(parts))


def kth_scaled_singular(lengths, k):
    """Return pi*s_k for local-mean corrected integration, exact fraction."""
    vals = sorted((h / m for h in lengths for m in range(1, k + 1)), reverse=True)
    return vals[k - 1]


def count_strict(lengths, level):
    # For h/ m > level, m=1,...,ceil(h/level)-1.
    total = 0
    for h in lengths:
        z = h / level
        ceil_z = (z.numerator + z.denominator - 1) // z.denominator
        total += ceil_z - 1
    return total


def check():
    tests = 0
    for n in range(1, 6):
        for k in range(1, 9):
            d = n + k - 1
            target = Fraction(1, d)
            good = set()
            for a in compositions(d, n):
                lengths = tuple(Fraction(x, d) for x in a)
                assert kth_scaled_singular(lengths, k) == target
                assert count_strict(lengths, target) == k - 1
                good.add(a)
                tests += 2
            # Exhaustive rational grids with denominators from d through d+3:
            # every sampled partition satisfies the universal bound;
            # equality must have lengths at the quantized composition grid.
            for den in range(n, n + k + 5):
                for a in compositions(den, n):
                    lengths = tuple(Fraction(x, den) for x in a)
                    value = kth_scaled_singular(lengths, k)
                    assert value >= target
                    if value == target:
                        quantized = tuple(x * d for x in lengths)
                        assert all(x.denominator == 1 for x in quantized)
                        assert tuple(int(x) for x in quantized) in good
                    tests += 2
    assert kth_scaled_singular((Fraction(1,2),Fraction(1,2)),2)==Fraction(1,2)
    assert kth_scaled_singular((Fraction(1,3),Fraction(2,3)),2)==Fraction(1,3)
    tests += 2
    for n in range(1, 10):
        uniform=(Fraction(1,n),)*n
        h2=sum(x*x for x in uniform)/6
        assert h2==Fraction(1,6*n)
        tests+=1
    print(f"PASS: {tests} exact rational assertions; indexed value uses units pi*s_k")

if __name__ == '__main__':
    check()
