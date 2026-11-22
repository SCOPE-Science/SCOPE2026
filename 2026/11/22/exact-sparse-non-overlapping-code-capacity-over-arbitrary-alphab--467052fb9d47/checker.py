#!/usr/bin/env python3
"""Exact finite checks for sparse non-overlapping codes.

Run with Python 3 (standard library) for direct construction checks.
Pass --milp for additional independently formulated maximum-independent-set
checks (requires scipy>=1.9).
"""
from itertools import combinations, product
from math import floor
import argparse


def optimum_formula(q, n):
    assert q >= 2 and n >= 2
    s = q - 1
    if n % 2:
        return (n - 1) // 2 * s * s
    return (n - 2) // 2 * s * s + s * s // 4


def canonical_words(q, n):
    s = q - 1
    m = (n - 2) // 2
    a_set = range(1, 1 + s // 2)
    b_set = range(1 + s // 2, q)
    words = []
    for gap in range(n - 1):
        other = n - 2 - gap
        if gap > other:
            for a, b in product(range(1, q), repeat=2):
                words.append((0,) * gap + (a,) + (0,) * other + (b,))
    if n % 2 == 0:
        for a, b in product(a_set, b_set):
            words.append((0,) * m + (a,) + (0,) * m + (b,))
    return words


def overlap(u, v):
    n = len(u)
    return any(u[:k] == v[n-k:] for k in range(1, n))


def check_construction(q, n):
    c = canonical_words(q, n)
    assert len(c) == optimum_formula(q, n), (q, n, len(c))
    assert len(c) == len(set(c))
    for u in c:
        assert sum(z != 0 for z in u) == 2
        for v in c:
            assert not overlap(u, v), (q, n, u, v)
    return len(c), len(c)**2


def exact_independent_set(q, n):
    """Full candidate conflict graph, independently optimized by HiGHS MILP."""
    from scipy.optimize import Bounds, LinearConstraint, milp
    from scipy.sparse import coo_array
    words = []
    for i, j in combinations(range(n), 2):
        for a, b in product(range(1, q), repeat=2):
            w = [0] * n
            w[i], w[j] = a, b
            words.append(tuple(w))
    nvars = len(words)
    edges, looped = [], []
    for i, u in enumerate(words):
        if overlap(u, u):
            looped.append(i)
        for j in range(i + 1, nvars):
            v = words[j]
            if overlap(u, v) or overlap(v, u):
                edges.append((i, j))
    rr, cc, data = [], [], []
    for k, (i, j) in enumerate(edges):
        rr.extend((k, k))
        cc.extend((i, j))
        data.extend((1., 1.))
    for k, i in enumerate(looped, len(edges)):
        rr.append(k)
        cc.append(i)
        data.append(1.)
    import numpy as np
    mat = coo_array((np.array(data, dtype=float),
                     (np.array(rr, dtype=np.int32), np.array(cc, dtype=np.int32))),
                    shape=(len(edges) + len(looped), nvars)).tocsr()
    rhs = np.concatenate((np.ones(len(edges)), np.zeros(len(looped))))
    res = milp(c=-np.ones(nvars), integrality=np.ones(nvars, dtype=np.int32),
               bounds=Bounds(np.zeros(nvars), np.ones(nvars)),
               constraints=LinearConstraint(mat, -np.inf, rhs),
               options={'time_limit': 60.0, 'mip_rel_gap': 0.0})
    assert res.status == 0, (q, n, res.message)
    found = round(-res.fun)
    assert abs(-res.fun - found) < 1e-5
    assert found == optimum_formula(q, n), (q, n, found, optimum_formula(q, n))
    return nvars, len(edges), len(looped), found


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--milp', action='store_true')
    args = parser.parse_args()
    pairs = 0
    for q in range(2, 8):
        for n in range(2, 15):
            size, p = check_construction(q, n)
            pairs += p
    print('PASS: 91 all-pairs construction checks,', pairs, 'ordered pairs')
    if args.milp:
        tests = [(q, n) for q in range(2, 6) for n in range(2, 7)]
        results = [exact_independent_set(q, n) for q, n in tests]
        print('PASS: exact full candidate-graph MILP,', len(results), 'cases; sizes:',
              [t[-1] for t in results])


if __name__ == '__main__':
    main()
