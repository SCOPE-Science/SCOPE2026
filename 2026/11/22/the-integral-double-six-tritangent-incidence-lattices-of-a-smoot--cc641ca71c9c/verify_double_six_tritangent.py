#!/usr/bin/env python3
"""Exact Smith certificates for double-six--tritangent incidence of cubic surfaces.

Uses only Python's standard library. All arithmetic is integral.
"""
from itertools import combinations
from collections import Counter


def smith_factors(matrix):
    """Smith diagonal by reversible integral row/column operations.

    At each stage Euclidean division reduces a pivot until it divides every
    entry of the trailing block; that proves each successive diagonal entry
    divides all later ones. Row and column swaps, additions, and sign changes
    are unimodular and therefore preserve the cokernel.
    """
    a = [list(map(int, row)) for row in matrix]
    m, n = len(a), len(a[0])
    def rs(i, j):
        a[i], a[j] = a[j], a[i]
    def cs(i, j):
        for row in a:
            row[i], row[j] = row[j], row[i]
    k = steps = 0
    while k < min(m, n):
        nz = next(((i, j) for i in range(k, m) for j in range(k, n)
                   if a[i][j]), None)
        if nz is None:
            break
        i, j = nz
        rs(k, i)
        cs(k, j)
        while True:
            steps += 1
            assert steps < 100000
            pivot = a[k][k]
            assert pivot != 0
            changed = False
            for i in range(k + 1, m):
                if a[i][k]:
                    q = a[i][k] // pivot
                    a[i] = [u - q * v for u, v in zip(a[i], a[k])]
                    if a[i][k]:
                        rs(i, k)
                    changed = True
                    break
            if changed:
                continue
            pivot = a[k][k]
            for j in range(k + 1, n):
                if a[k][j]:
                    q = a[k][j] // pivot
                    if q:
                        for row in a:
                            row[j] -= q * row[k]
                    if a[k][j]:
                        cs(j, k)
                    changed = True
                    break
            if changed:
                continue
            pivot = a[k][k]
            bad = next(((i, j) for i in range(k + 1, m)
                        for j in range(k + 1, n) if a[i][j] % pivot), None)
            if bad is not None:
                i, _ = bad
                a[k] = [u + v for u, v in zip(a[k], a[i])]
                continue
            break
        if a[k][k] < 0:
            a[k] = [-x for x in a[k]]
        k += 1
    d = [a[i][i] for i in range(k)]
    assert all(x > 0 for x in d)
    assert all(y % x == 0 for x, y in zip(d, d[1:]))
    assert all(a[i][j] == 0 for i in range(m) for j in range(n) if i != j)
    return d, steps


def main():
    # Coordinates (degree in H; multiplicities of the six exceptional E_i).
    def E(i):
        return (0,) + tuple(-int(j == i) for j in range(6))
    def L(i, j):
        return (1,) + tuple(int(k in (i, j)) for k in range(6))
    def Q(i):
        return (2,) + tuple(1 - int(k == i) for k in range(6))
    v = [E(i) for i in range(6)]
    v += [L(i, j) for i, j in combinations(range(6), 2)]
    v += [Q(i) for i in range(6)]
    assert len(v) == 27 and len(set(v)) == 27
    def pair(u, w):
        return u[0] * w[0] - sum(a * b for a, b in zip(u[1:], w[1:]))
    assert all(pair(u, u) == -1 for u in v)
    assert all(pair(u, w) in (0, 1)
               for i, u in enumerate(v) for w in v[i + 1:])

    # Two independent enumerations of all 36 double-sixes.
    sixers = []
    def add_sixer(s, start):
        if len(s) == 6:
            sixers.append(tuple(s))
            return
        for i in range(start, 27):
            if all(pair(v[i], v[j]) == 0 for j in s):
                add_sixer(s + [i], i + 1)
    add_sixer([], 0)
    assert len(sixers) == 72
    pairs = []
    for a in sixers:
        b = tuple(i for i in range(27)
                  if sum(pair(v[i], v[j]) for j in a) == 5)
        assert len(b) == 6 and all(pair(v[i], v[j]) == 0
                                    for i, j in combinations(b, 2))
        pairs.append(tuple(sorted((a, b))))
    double_sixes = sorted({tuple(sorted(set(a) | set(b)))
                           for a, b in pairs})
    assert len(double_sixes) == 36
    assert all(len(d) == 12 for d in double_sixes)

    roots = []
    for i, j in combinations(range(6), 2):
        roots.append(tuple(x - y for x, y in zip(E(i), E(j))))
    for i, j, k in combinations(range(6), 3):
        roots.append((1,) + tuple(int(t in (i, j, k)) for t in range(6)))
    roots.append((2, 1, 1, 1, 1, 1, 1))
    assert len(roots) == 36 and all(pair(r, r) == -2 for r in roots)
    by_roots = sorted(tuple(i for i in range(27) if pair(v[i], r) != 0)
                      for r in roots)
    assert double_sixes == by_roots
    assert all(sum(pair(x, r) == 1 for x in v) == 6 and
               sum(pair(x, r) == -1 for x in v) == 6 for r in roots)

    canonical = (3, 1, 1, 1, 1, 1, 1)
    tritangents = [tuple(t) for t in combinations(range(27), 3)
                   if tuple(sum(v[i][j] for i in t) for j in range(7))
                   == canonical]
    assert len(tritangents) == 45
    assert all(sum(i in t for t in tritangents) == 5 for i in range(27))

    counts = Counter(len(set(d) & set(t))
                     for d in double_sixes for t in tritangents)
    assert counts == {0: 540, 2: 1080}, counts
    matrix = [[int(len(set(d) & set(t)) == 2) for t in tritangents]
              for d in double_sixes]
    complement = [[1 - x for x in row] for row in matrix]
    assert all(sum(row) == 30 for row in matrix)
    assert all(sum(matrix[i][j] for i in range(36)) == 24
               for j in range(45))
    assert all(sum(row) == 15 for row in complement)
    assert all(sum(complement[i][j] for i in range(36)) == 12
               for j in range(45))
    d1, steps1 = smith_factors(matrix)
    d0, steps0 = smith_factors(complement)
    assert Counter(d1) == {1: 15, 3: 5, 18: 1}, (d1, steps1)
    assert Counter(d0) == {1: 14, 3: 7}, (d0, steps0)
    # Independent Gram consistency identities:
    # spectra 720,18^20,0^15 and 180,18^20,0^15.
    def mm(a, b):
        return [[sum(x * y for x, y in zip(row, col))
                 for col in zip(*b)] for row in a]
    def gram_relation(a, large):
        z = mm(a, list(map(list, zip(*a))))
        ident = [[int(i == j) for j in range(36)] for i in range(36)]
        t = [[z[i][j] - 18 * ident[i][j] for j in range(36)]
             for i in range(36)]
        w = mm(z, t)
        # x*(x-18)*(x-large) = 0 on the Gram matrix.
        r = mm(w, [[z[i][j] - large * ident[i][j]
                    for j in range(36)] for i in range(36)])
        assert all(all(x == 0 for x in row) for row in r)
        assert sum(z[i][i] for i in range(36)) == 36 * sum(a[0])
    gram_relation(matrix, 720)
    gram_relation(complement, 180)
    print('DOUBLE_SIX_TRITANGENT_INTEGRAL_INCIDENCE_OK')
    print('36 double-sixes, 45 tritangents, row/column valencies 30/24')
    print('shared-two SNF:', d1, 'steps', steps1)
    print('shared-zero SNF:', d0, 'steps', steps0)

if __name__ == '__main__':
    main()
