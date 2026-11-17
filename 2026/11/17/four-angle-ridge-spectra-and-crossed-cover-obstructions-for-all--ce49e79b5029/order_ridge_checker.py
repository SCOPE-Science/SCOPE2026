"""Exact facet-pair spectrum checks for Euclidean order polytopes.

Run: python order_ridge_checker.py
Requires NumPy. Finite checks support, but do not replace, the general proof.
"""
from itertools import combinations
from math import comb
import random
import numpy as np


def relation(n, mask):
    R = [[False] * n for _ in range(n)]
    for k, (i, j) in enumerate(combinations(range(n), 2)):
        R[i][j] = bool(mask & (1 << k))
    for k in range(n):
        for i in range(n):
            if R[i][k]:
                for j in range(n):
                    R[i][j] |= R[k][j]
    return R


def check(n, R):
    covers = [(i, j) for i in range(n) for j in range(n)
              if R[i][j] and not any(R[i][k] and R[k][j] for k in range(n))]
    mins = [i for i in range(n) if not any(R[j][i] for j in range(n))]
    maxs = [i for i in range(n) if not any(R[i][j] for j in range(n))]
    # Extend by bottom -1 and top n: every facet corresponds to a cover.
    edges = [(-1, i) for i in mins] + covers + [(i, n) for i in maxs]
    def leq(i, j):
        return i == j or i == -1 or j == n or (0 <= i < n and 0 <= j < n and R[i][j])
    def length_interval(a, c):
        return sum(leq(a, t) and leq(t, c) for t in [-1, *range(n), n])
    def predicted(e, f):
        a, b = e
        c, d = f
        if b == c:
            if length_interval(a, d) > 3:
                return None
            if a == -1 or d == n:
                return 45
            return 60
        if d == a:
            if length_interval(c, b) > 3:
                return None
            if c == -1 or b == n:
                return 45
            return 60
        if a == c or b == d:
            if a == c == -1 or b == d == n:
                return 90
            return 120
        if len(set(e + f)) == 4 and leq(a, d) and leq(c, b):
            return None
        return 90
    normals = []
    for a, b in edges:
        x = np.zeros(n, dtype=int)
        if a != -1:
            x[a] += 1
        if b != n:
            x[b] -= 1
        normals.append(x)
    verts = [np.array([(mask >> i) & 1 for i in range(n)], dtype=int)
             for mask in range(1 << n)
             if all(not (mask >> i & 1) or (mask >> j & 1)
                    for i in range(n) for j in range(n) if R[i][j])]
    def tight(edge, v):
        a, b = edge
        return (a == -1 and v[b] == 0) or (b == n and v[a] == 1) or (
            a != -1 and b != n and v[a] == v[b])
    counts = {45: 0, 60: 0, 90: 0, 120: 0}
    failures = 0
    for i, j in combinations(range(len(edges)), 2):
        e, f = edges[i], edges[j]
        vs = [v for v in verts if tight(e, v) and tight(f, v)]
        if not vs:
            observed = None
        elif n - (np.linalg.matrix_rank(np.array(vs[1:]) - vs[0]) if len(vs)>1 else 0) != 2:
            observed = None
        else:
            x, y = normals[i], normals[j]
            dot = int(x @ y)
            norms = (int(x @ x), int(y @ y))
            if dot == 0:
                observed = 90
            elif dot == -1:
                observed = 45 if sorted(norms) == [1, 2] else 60
            elif dot == 1 and norms == (2, 2):
                observed = 120
            else:
                raise AssertionError((n, e, f, dot, norms))
            counts[observed] += 1
        if observed != predicted(e, f):
            raise AssertionError((n, edges, e, f, observed, predicted(e, f)))
    paths = []
    cross = 0
    for e, f in combinations(edges, 2):
        a, b = e
        c, d = f
        if b == c:
            paths.append((a, b, d))
        if d == a:
            paths.append((c, d, b))
        if len(set(e + f)) == 4 and leq(a, d) and leq(c, b):
            cross += 1
    bad_paths = sum(length_interval(a, c) > 3 for a, b, c in paths)
    good_paths = [(a, b, c) for a, b, c in paths if length_interval(a, c) == 3]
    p45 = sum(a == -1 or c == n for a, b, c in good_paths)
    p60 = len(good_paths) - p45
    p120 = sum(comb(sum(b == v for a, b in edges), 2)
               + comb(sum(a == v for a, b in edges), 2) for v in range(n))
    Rn = comb(len(edges), 2) - bad_paths - cross
    assert counts[45] == p45 and counts[60] == p60 and counts[120] == p120
    assert sum(counts.values()) == Rn
    return counts, bad_paths, cross


def main():
    total = 0
    for n in range(2, 7):
        seen = set()
        for mask in range(1 << comb(n, 2)):
            R = relation(n, mask)
            fingerprint = tuple(tuple(row) for row in R)
            if fingerprint in seen:
                continue
            seen.add(fingerprint)
            check(n, R)
        print(f'ALL_NATURALLY_LABELED_PASS n={n} posets={len(seen)}')
        total += len(seen)
    gen = random.Random(20261114)
    for n in (7, 8):
        for _ in range(200):
            check(n, relation(n, gen.getrandbits(comb(n, 2))))
        print(f'RANDOM_POSETS_PASS n={n} cases=200')
    print(f'ORDER_RIDGE_ANGLE_PASS total_exhaustive={total} random=400')


if __name__ == '__main__':
    main()
