#!/usr/bin/env python3
"""Finite cellular checks for asymmetric deleted products of simplex skeleta.

This independently implements the signed cellular product boundary. The uniform
orientation and fundamental-group statements have proofs in RESULT.md; these
finite computations are consistency tests, not substitutes for those proofs.
"""
from itertools import combinations
from collections import Counter
from math import comb


def cells(p, q):
    n = p + q + 3
    vertices = tuple(range(n))
    by_dim = [[] for _ in range(p + q + 1)]
    for na in range(1, p + 2):
        for a in combinations(vertices, na):
            rem = tuple(x for x in vertices if x not in a)
            for nb in range(1, q + 2):
                for b in combinations(rem, nb):
                    by_dim[na + nb - 2].append((a, b))
    return by_dim


def boundaries(cell, p):
    a, b = cell
    for i in range(len(a)):
        if len(a) > 1:
            yield (a[:i] + a[i + 1:], b), (-1) ** i
    for j in range(len(b)):
        if len(b) > 1:
            yield (a, b[:j] + b[j + 1:]), (-1) ** (len(a) - 1 + j)


def sign_partition(cell, n):
    a, b = cell
    remaining = tuple(x for x in range(n) if x not in a and x not in b)
    assert len(remaining) == 1
    seq = a + b + remaining
    inversions = sum(seq[i] > seq[j] for i in range(n) for j in range(i + 1, n))
    return (-1) ** inversions


def check_orientation(p, q):
    by_dim = cells(p, q)
    n = p + q + 3
    top = by_dim[-1]
    boundary = Counter()
    ridge_incidence = Counter()
    for c in top:
        for face, s in boundaries(c, p):
            boundary[face] += sign_partition(c, n) * s
            ridge_incidence[face] += 1
    assert set(ridge_incidence.values()) == {2}
    assert all(z == 0 for z in boundary.values())
    expected = comb(n, p + 1) * (n - p - 1)
    assert len(top) == expected
    return len(top), len(boundary)


def rank_mod_prime(columns, nrows, prime):
    pivots = {}
    for col in columns:
        vec = {i: (a % prime) for i, a in col.items() if a % prime}
        while vec:
            r = min(vec)
            if r not in pivots:
                inv = pow(vec[r], -1, prime)
                pivots[r] = {i: (v * inv) % prime for i, v in vec.items()}
                break
            factor = vec[r]
            for i, a in pivots[r].items():
                v = (vec.get(i, 0) - factor * a) % prime
                if v: vec[i] = v
                else: vec.pop(i, None)
    return len(pivots)


def check_three_manifold():
    p, q = 1, 2
    by_dim = cells(p, q)
    assert tuple(map(len, by_dim)) == (30, 120, 150, 60)
    ranks = {}
    for d in range(1, 4):
        idx = {c: i for i, c in enumerate(by_dim[d - 1])}
        cols = [{idx[f]: s for f, s in boundaries(c, p)} for c in by_dim[d]]
        rank2 = rank_mod_prime(cols, len(by_dim[d - 1]), 2)
        rank3 = rank_mod_prime(cols, len(by_dim[d - 1]), 3)
        assert rank2 == rank3
        ranks[d] = rank2
    assert [ranks[d] for d in (1, 2, 3)] == [29, 81, 59]
    betti = (
        len(by_dim[0]) - ranks[1],
        len(by_dim[1]) - ranks[1] - ranks[2],
        len(by_dim[2]) - ranks[2] - ranks[3],
        len(by_dim[3]) - ranks[3],
    )
    assert betti == (1, 10, 10, 1)
    assert sum((-1) ** i * v for i, v in enumerate(map(len, by_dim))) == 0
    return tuple(map(len, by_dim)), tuple(ranks[d] for d in (1, 2, 3)), betti


if __name__ == "__main__":
    for p in range(1, 6):
        for q in range(1, 6):
            f, r = check_orientation(p, q)
            print(f"orientation p={p} q={q}: facets={f} ridges={r} PASS")
    faces, ranks, betti = check_three_manifold()
    print(f"X_(1,2) cell counts={faces}; boundary ranks GF(2)=GF(3)={ranks}")
    print(f"X_(1,2) Betti numbers over GF(2), GF(3)={betti}")
    print("All cellular tests passed.")
