#!/usr/bin/env python3
"""Pure-Python integer-lattice consistency checks for even-degree curve chambers.

The infinite topological theorem is proved in RESULT.md. These finite examples
check its algebraic presentation by determinantal divisors (Smith invariants).
No external software package or network connection is required.
"""
from itertools import product, combinations, permutations
from math import gcd
from functools import reduce


def determinant(matrix):
    n = len(matrix)
    out = 0
    for p in permutations(range(n)):
        inv = sum(p[i] > p[j] for i in range(n) for j in range(i+1,n))
        z = (-1)**inv
        for i in range(n):
            z *= matrix[i][p[i]]
        out += z
    return out


def expected(degrees, epsilon):
    assert all(x > 0 and x % 2 == 0 for x in degrees)
    assert epsilon in (0, 1)
    d = reduce(gcd, degrees)
    m = [x // d for x in degrees]
    subgroup = {sum(a * (v // 2) for a, v in zip(coeff, degrees)) % d
                for coeff in product(range(2), repeat=len(degrees))}
    assert subgroup == {0, d // 2}
    assert any(v % 2 for v in m)
    return d, (d // 2) * (2 ** epsilon)


def model_index(degrees, epsilon, h):
    # Codomain Z^h plus torsion Z/d. Each column is a real-region generator
    # or a defining relation d*t=0. Torsion shifts on free lifts are arbitrary.
    d = reduce(gcd, degrees)
    rows = h + 1
    columns = []
    for j in range(h):
        col = [0] * rows
        col[j] = 2 if j == 0 and epsilon else 1
        col[-1] = (j + 1) % d
        columns.append(col)
    for x in degrees:
        col = [0] * rows
        col[-1] = x // 2
        columns.append(col)
    relation = [0] * rows
    relation[-1] = d
    columns.append(relation)
    # For an integer matrix with full row rank, the absolute index of its
    # column image is the gcd of all maximal minors (Smith's theorem).
    index = 0
    for chosen in combinations(columns, rows):
        M = [[chosen[col][row] for col in range(rows)] for row in range(rows)]
        index = gcd(index, abs(determinant(M)))
    assert index > 0
    return index


def main():
    cases = 0
    for r in range(1, 4):
        for degrees in product((2,4,6,8,10,12), repeat=r):
            for epsilon in (0,1):
                d, target = expected(degrees, epsilon)
                for h in (0,1,2):
                    if epsilon and h == 0:
                        continue  # eta nonzero requires a complex graph cycle
                    actual = model_index(degrees, epsilon, h)
                    assert actual == target, (degrees, epsilon, h, actual, target)
                    cases += 1
    assert expected((2,2), 0) == (2,1)
    assert expected((2,2), 1) == (2,2)
    assert expected((4,4), 0) == (4,2)
    assert expected((4,4), 1) == (4,4)
    print(f"PASS: {cases} integral determinantal-divisor models and parity tests")


if __name__ == '__main__':
    main()
