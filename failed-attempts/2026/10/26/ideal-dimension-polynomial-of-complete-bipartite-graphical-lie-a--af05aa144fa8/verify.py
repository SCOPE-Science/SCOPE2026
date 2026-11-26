#!/usr/bin/env python3
"""Finite exact checks for ideal counts of complete-bipartite graphical Lie algebras.
Python 3 stdlib only. This program enumerates RREF subspaces independently of
its Gaussian-binomial closed formula. It does not certify infinite cases.
"""
from itertools import combinations, product
from math import prod


def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    return prod(q ** (n - i) - 1 for i in range(k)) // prod(q ** (k - i) - 1 for i in range(k))


def gl_order(n, q):
    return prod(q ** n - q ** j for j in range(n))


def formula(a, b, q):
    M, N = a * b, a + b + a * b
    out = [0] * (N + 1)
    for r in range(a + 1):
        for s in range(b + 1):
            k = r * b + a * s - r * s
            for h in range(min(r, s) + 1):
                t = r + s - h
                w = (gaussian(a, r, q) * gaussian(b, s, q)
                     * gaussian(r, h, q) * gaussian(s, h, q)
                     * gl_order(h, q))
                for d in range(k, M + 1):
                    out[t + d] += w * gaussian(M - k, d - k, q) * q ** (t * (M - d))
    return out


def rref_spaces(n, q):
    for d in range(n + 1):
        for pivots in combinations(range(n), d):
            ps = set(pivots)
            free = [(i, col) for i, pivot in enumerate(pivots)
                    for col in range(pivot + 1, n) if col not in ps]
            for values in product(range(q), repeat=len(free)):
                rows = [[0] * n for _ in pivots]
                for i, p in enumerate(pivots):
                    rows[i][p] = 1
                for (i, col), value in zip(free, values):
                    rows[i][col] = value
                yield pivots, rows


def contained(v, pivots, rows, q):
    v = list(v)
    n = len(v)
    for p, row in zip(pivots, rows):
        z = v[p]
        if z:
            for j in range(p, n):
                v[j] = (v[j] - z * row[j]) % q
    return not any(v)


def brute(a, b, q):
    n, M, off = a + b + a * b, a * b, a + b
    counts = [0] * (n + 1)
    total = 0
    for pivots, rows in rref_spaces(n, q):
        total += 1
        okay = True
        # Check [row, e_i] lies in the subspace, for every ambient noncentral basis vector.
        for row in rows:
            if not okay:
                break
            for i in range(a + b):
                comm = [0] * n
                if i < a:
                    for j in range(b):
                        comm[off + i * b + j] = (-row[a + j]) % q
                else:
                    j = i - a
                    for ii in range(a):
                        comm[off + ii * b + j] = row[ii]
                if not contained(comm, pivots, rows, q):
                    okay = False
                    break
        if okay:
            counts[len(rows)] += 1
    return counts, total


if __name__ == '__main__':
    for a, b, q in [(1, 1, 2), (1, 1, 3), (1, 2, 2), (1, 2, 3),
                     (1, 3, 2), (2, 2, 2)]:
        predicted = formula(a, b, q)
        observed, allspaces = brute(a, b, q)
        assert predicted == observed, (a, b, q, predicted, observed)
        assert observed[1] == gaussian(a * b, 1, q)
        assert observed[-2] == gaussian(a + b, 1, q)
        print(f'PASS a={a} b={b} q={q}: {observed}, checked_subspaces={allspaces}')
    print('ALL_SMALL_CASES_PASS')
