#!/usr/bin/env python3
"""Finite, independent chain and attachment checks for dihedral permutation complexes.

Runs with Python 3 standard library only. The unrestricted homotopy proof is
mathematical and does not depend on this finite computation.
"""
from itertools import combinations


def face_words(perm):
    n = len(perm)
    return {tuple(perm[j] for j in I)
            for r in range(1, n + 1)
            for I in combinations(range(n), r)}


def rotation_orders(n, reverse=False):
    base = list(range(n - 1, -1, -1)) if reverse else list(range(n))
    return [tuple(base[k:] + base[:k]) for k in range(n)]


def length_faces(perms, n):
    words = set().union(*(face_words(p) for p in perms))
    return [sorted(w for w in words if len(w) == d + 1) for d in range(n)]


def rank_mod_p(columns, prime):
    # columns: sparse dictionaries indexed by row.
    pivots = {}
    for original in columns:
        c = {i: a % prime for i, a in original.items() if a % prime}
        while c:
            p = max(c)
            a = c[p]
            if p not in pivots:
                inverse = pow(a, -1, prime)
                pivots[p] = {i: (v * inverse) % prime for i, v in c.items()}
                break
            for i, v in pivots[p].items():
                w = (c.get(i, 0) - a * v) % prime
                if w:
                    c[i] = w
                else:
                    c.pop(i, None)
    return len(pivots)


def homology_ranks(perms, n, prime):
    cells = length_faces(perms, n)
    ranks = []
    for d in range(1, n):
        idx = {w: j for j, w in enumerate(cells[d - 1])}
        cols = []
        for w in cells[d]:
            col = {}
            for j in range(len(w)):
                i = idx[w[:j] + w[j + 1:]]
                col[i] = (col.get(i, 0) + (-1)**j) % prime
            cols.append(col)
        ranks.append(rank_mod_p(cols, prime))
    betti = []
    for d in range(n):
        lower_rank = ranks[d - 1] if d else 0
        upper_rank = ranks[d] if d < n - 1 else 0
        betti.append(len(cells[d]) - lower_rank - upper_rank)
    betti[0] -= 1
    return tuple(betti)


def check(n):
    assert n >= 3
    plus = rotation_orders(n)
    minus = rotation_orders(n, reverse=True)
    P = [face_words(p) for p in plus]
    M = [face_words(p) for p in minus]
    Pset = set.union(*P)
    Mset = set.union(*M)
    allperms = plus + minus
    B = Pset & Mset
    assert B == {(j,) for j in range(n)} | {(i, j) for i in range(n) for j in range(n) if i != j}
    assert P[0] & P[1] == face_words((0,)) | face_words(tuple(range(1, n)))
    for k in range(2, n):
        A = tuple(range(k))
        C = tuple(range(k, n)) + tuple(range(k - 1))
        actual = P[k] & set.union(*P[:k])
        assert actual == face_words(A) | face_words(C)
        assert set(A) & set(C) == set(range(k-1))
    for w in Pset:
        if len(w) == 3:
            u, v, z = w
            assert int(u > v) + int(v > z) - int(u > z) == 0
    for w in Mset:
        if len(w) == 3:
            u, v, z = w
            assert int(u < v) + int(v < z) - int(u < z) == 0
    # The 2 x 2 winding evaluation determinant is one.
    def wind(loop):
        return (sum(int(u > v) for u, v in loop),
                sum(int(u < v) for u, v in loop))
    digon = [(0, 1), (1, 0)]
    triangle = [(0, 1), (1, 2), (2, 0)]
    a, b = wind(digon), wind(triangle)
    assert a == (1, 1) and b == (1, 2)
    assert a[0] * b[1] - a[1] * b[0] == 1
    # Independently enumerate all ordered faces and boundary matrices.
    expected_betti = tuple([0, 0, (n - 1)**2 - 2] + [0] * (n - 3))
    expected_circle = tuple([0, 1] + [0] * (n - 2))
    for p in [2, 3] if n <= 7 else [2]:
        assert homology_ranks(plus, n, p) == expected_circle
        assert homology_ranks(minus, n, p) == expected_circle
        assert homology_ranks(allperms, n, p) == expected_betti
    print(f"n={n}: intersections, cocycles, winding determinants and chain ranks pass; "
          f"sphere_count={(n-1)**2-2}")


if __name__ == "__main__":
    for n in range(3, 9):
        check(n)
    print("DIHEDRAL_PERMUTATION_COMPLEX_FINITE_CHECK_PASS")
