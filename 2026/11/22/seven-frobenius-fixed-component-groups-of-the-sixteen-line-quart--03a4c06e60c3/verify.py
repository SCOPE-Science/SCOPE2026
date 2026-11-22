#!/usr/bin/env python3
"""Recompute the seven Frobenius-fixed graph Jacobian invariant factors.

Only Python's standard library is used.  Every integer operation is exact.
The mathematical reduction from graph coinvariants to rational component
groups is explained in RESULT.md; this program checks its finite matrices.
"""
from itertools import combinations
from math import prod

VERTICES = ([('E', i) for i in range(5)]
            + [('L', i, j) for i, j in combinations(range(5), 2)]
            + [('Q',)])
CYCLES = ((1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1),
          (3, 1, 1), (3, 2), (4, 1), (5,))
EXPECTED = ((4, 4, 4, 4, 8, 32, 32, 32, 32),
            (4, 4, 8, 32, 32, 32),
            (4, 4, 8, 32, 32),
            (8, 32, 32), (8, 32), (2, 4, 32), (8,))


def adjacent(a, b):
    if a == b:
        return False
    if a[0] == 'Q' or b[0] == 'Q':
        return 'E' in (a[0], b[0])
    if a[0] == 'E' and b[0] == 'E':
        return False
    if a[0] == 'L' and b[0] == 'E':
        a, b = b, a
    if a[0] == 'E':
        return a[1] in b[1:]
    return set(a[1:]).isdisjoint(b[1:])


def bareiss_det(rows):
    """Fraction-free integer determinant, with pivoting."""
    a = [row[:] for row in rows]
    n = len(a)
    if not n:
        return 1
    sign, prior = 1, 1
    for k in range(n - 1):
        p = next((i for i in range(k, n) if a[i][k]), None)
        if p is None:
            return 0
        if p != k:
            a[k], a[p] = a[p], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = pivot*a[i][j] - a[i][k]*a[k][j]
                assert numerator % prior == 0
                a[i][j] = numerator // prior
        for i in range(k + 1, n):
            a[i][k] = 0
        prior = pivot
    return sign*a[-1][-1]


def permutation(parts):
    p, first = {}, 0
    for d in parts:
        for i in range(d):
            p[first + i] = first + (i + 1) % d
        first += d
    assert first == 5
    return p


def action(x, perm):
    if x[0] == 'Q':
        return x
    if x[0] == 'E':
        return ('E', perm[x[1]])
    return ('L', *sorted((perm[x[1]], perm[x[2]])))


def orbit_matrix(parts, laplacian):
    p = permutation(parts)
    orbits, seen = [], set()
    for x in VERTICES:
        if x in seen:
            continue
        orbit, y = [], x
        while y not in seen:
            orbit.append(y)
            seen.add(y)
            y = action(y, p)
        assert y == x
        orbits.append(orbit)
    assert len(seen) == 16 and orbits[-1] == [('Q',)]
    index = {x: i for i, x in enumerate(VERTICES)}
    b = [[sum(laplacian[index[x]][index[orb2[0]]] for x in orb1)
          for orb2 in orbits] for orb1 in orbits]
    assert all(sum(b[i][j] for i in range(len(b))) == 0
               for j in range(len(b)))
    assert all(sum(b[i][j]*len(orbits[j]) for j in range(len(b))) == 0
               for i in range(len(b)))
    return [row[:-1] for row in b[:-1]], tuple(map(len, orbits))


def valuation2(z):
    if z == 0:
        return 10**9
    return (z & -z).bit_length() - 1


def smith_2_adic_exponents(rows, exponent=8):
    """Diagonalize over Z/(2**exponent); all invariant exponents are < exponent.

    At each step use a pivot of minimum 2-adic valuation, scale by an
    odd unit, and clear its row and column using invertible operations.
    This gives the actual local Smith valuations, independent of a
    rational Smith-normal-form library.
    """
    modulus = 2**exponent
    a = [[z % modulus for z in row] for row in rows]
    n = len(a)
    es = []
    for k in range(n):
        i, j = min(((i, j) for i in range(k, n) for j in range(k, n)),
                   key=lambda pair: valuation2(a[pair[0]][pair[1]]))
        a[k], a[i] = a[i], a[k]
        for row in a:
            row[k], row[j] = row[j], row[k]
        e = valuation2(a[k][k])
        assert e < exponent, 'Increase the modulus to resolve this invariant.'
        power = 2**e
        inv = pow(a[k][k]//power, -1, modulus)
        a[k] = [inv*x % modulus for x in a[k]]
        assert a[k][k] == power
        for i in range(k + 1, n):
            assert a[i][k] % power == 0
            coef = a[i][k]//power
            a[i] = [(x - coef*y) % modulus for x, y in zip(a[i], a[k])]
        for j in range(k + 1, n):
            assert a[k][j] % power == 0
            coef = a[k][j]//power
            for i in range(n):
                a[i][j] = (a[i][j] - coef*a[i][k]) % modulus
        assert all(a[k][j] == 0 for j in range(k + 1, n))
        assert all(a[i][k] == 0 for i in range(k + 1, n))
        es.append(e)
    assert es == sorted(es)
    return es


def main():
    laplacian = [[(5 if i == j else -int(adjacent(x, y)))
                  for j, y in enumerate(VERTICES)]
                 for i, x in enumerate(VERTICES)]
    assert all(sum(row) == 0 for row in laplacian)
    assert sum(adjacent(x, y) for i, x in enumerate(VERTICES)
               for y in VERTICES[i + 1:]) == 40
    for parts, expected in zip(CYCLES, EXPECTED):
        matrix, sizes = orbit_matrix(parts, laplacian)
        exponents = smith_2_adic_exponents(matrix)
        factors = tuple(2**e for e in exponents if e)
        determinant = bareiss_det(matrix)
        assert factors == expected
        assert determinant == prod(factors)
        assert determinant > 0
        print('cycle=%s; orbits=%s; invariant_factors=%s; determinant=%d'
              % (parts, sizes, factors, determinant))
    print('QUARTIC_DEL_PEZZO_SEVEN_FROBENIUS_COMPONENT_GROUPS_OK')


if __name__ == '__main__':
    main()
