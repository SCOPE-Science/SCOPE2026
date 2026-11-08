#!/usr/bin/env python3
"""Exact finite-field corroboration of a rank-two Segre configuration motive.

Mathematical proof for all characteristics and parameters is separate.
"""
from itertools import product
from math import prod


def projective_points(q, m):
    out = set()
    for a in product(range(q), repeat=m + 1):
        if not any(a):
            continue
        j = next(i for i, z in enumerate(a) if z)
        inv = pow(a[j], -1, q)
        out.add(tuple((z * inv) % q for z in a))
    return sorted(out)


def tensor(vectors, q):
    a = (1,)
    for v in vectors:
        a = tuple(x * y % q for x in a for y in v)
    return a


def rank_mod(vectors, q):
    a = [list(v) for v in vectors]
    rank = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][j] % q), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][j], -1, q)
        a[rank] = [z * inv % q for z in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][j] % q:
                z = a[i][j]
                a[i] = [(u - z * v) % q for u, v in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def count(q, dimensions, n):
    factors = [projective_points(q, d) for d in dimensions]
    points = [tensor(tup, q) for tup in product(*factors)]
    exhaustive = sum(rank_mod(v, q) <= 2 for v in product(points, repeat=n))
    xcount = prod(len(f) for f in factors)
    lsum, ksum = 0, 0
    for j, d in enumerate(dimensions):
        pcount = len(factors[j])
        base = xcount // pcount
        numerator = prod(q ** (d + 1 - i) - 1 for i in range(2))
        denominator = prod(q ** (2 - i) - 1 for i in range(2))
        grassmann = numerator // denominator
        lsum += base * (pcount + grassmann * ((q + 1) ** n - (q + 1)))
        ksum += base * pcount ** 2
    n_bipartitions = 2 ** (n - 1) - 1
    formula = (lsum - (len(dimensions) - 1) * xcount
               + n_bipartitions * (xcount ** 2 - ksum
                                   + (len(dimensions) - 1) * xcount))
    assert exhaustive == formula, (q, dimensions, n, exhaustive, formula)
    print("SEGRE_RANK2_COUNT_OK", q, dimensions, n, exhaustive)
    return exhaustive


def main():
    cases = [(2, (1, 1), 3, 261),
             (2, (1, 1), 4, 729),
             (3, (1, 1), 3, 928),
             (2, (1, 2), 3, 1449),
             (2, (1, 1, 1), 3, 2295)]
    for q, dims, n, expected in cases:
        assert count(q, dims, n) == expected
    print("SEGRE_RANK2_FIVE_CASES_VERIFIED")


if __name__ == "__main__":
    main()
