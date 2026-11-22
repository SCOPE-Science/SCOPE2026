"""Standalone exact checks for the wheel spanning-tree chord polynomial.

No external dependencies. Run: python check_wheel_chords.py
"""
from collections import Counter
from itertools import combinations
from math import isclose, sqrt

# Polynomial entries in ascending powers of z. These matrices are specified
# independently from the edge-set enumerator below.
A = [
    [[1, 1], [0, 1]],
    [[1], [0, 1]],
]
M = [
    [[2, 2], [0, 2], [0, 2], [0, 0, 1]],
    [[2], [1, 1], [1], [0, 1]],
    [[2], [1], [1, 1], [0, 1]],
    [[1], [1], [1], [0, 1]],
]

def trace_power(mat, degree):
    d = len(mat)
    ans = [0] * (degree + 1)
    for initial in range(d):
        dp = [[0] * (degree + 1) for _ in range(d)]
        dp[initial][0] = 1
        for _ in range(degree):
            ndp = [[0] * (degree + 1) for _ in range(d)]
            for a in range(d):
                for b in range(d):
                    for shift, coefficient in enumerate(mat[a][b]):
                        if coefficient:
                            for k in range(degree - shift + 1):
                                ndp[b][k + shift] += dp[a][k] * coefficient
            dp = ndp
        ans = [x + y for x, y in zip(ans, dp[initial])]
    return ans

def wheel_polynomial(n):
    p = trace_power(M, n)
    correction = trace_power(A, n)
    return [p[k] - 4 * correction[k] + (4 if k == n else 0)
            for k in range(n + 1)]

def spanning_tree_masks(n):
    # n spoke edges (0,i+1), n rim edges (i+1,i+2).
    edges = [(0, i + 1) for i in range(n)] + [
        (i + 1, (i + 1) % n + 1) for i in range(n)
    ]
    ret = []
    for idx in combinations(range(2 * n), n):
        parent = list(range(n + 1))
        def root(x):
            while x != parent[x]:
                x = parent[x]
            return x
        ok = True
        bits = 0
        for j in idx:
            u, v = edges[j]
            u, v = root(u), root(v)
            if u == v:
                ok = False
                break
            parent[u] = v
            bits |= 1 << j
        if ok:
            ret.append(bits)
    return ret

def lucas_even(n):
    # L_{2n}; L_0=2, L_1=1.
    a, b = 2, 1
    for _ in range(2*n):
        a, b = b, a + b
    return a

def verify():
    tested_pairs = 0
    for n in range(3, 9):
        trees = spanning_tree_masks(n)
        assert len(trees) == lucas_even(n) - 2, (n, len(trees))
        counts = [0] * (n + 1)
        for t in trees:
            for u in trees:
                counts[(t & u).bit_count()] += 1
        poly = wheel_polynomial(n)
        assert counts == poly, (n, counts, poly)
        assert sum(poly) == len(trees) ** 2
        assert poly[0] == 2**(n + 1) - 4
        assert poly[n] == len(trees)
        tested_pairs += len(trees) ** 2
        print('n', n, 'trees', len(trees), 'ordered_pairs', len(trees)**2, 'counts', poly)
    mu = (7 - 2*sqrt(5))/5
    sigma2 = (22*sqrt(5) - 30)/125
    for n in (20, 40, 80):
        poly = wheel_polynomial(n)
        total = sum(poly)
        e = sum(k*v for k, v in enumerate(poly))/total
        variance = sum(k*k*v for k,v in enumerate(poly))/total - e*e
        assert abs(e/n - mu) < 0.2/n
        assert abs(variance/n - sigma2) < 0.8/n
        print('asymptotic', n, 'mean_per_rim', e/n, 'var_per_rim', variance/n)
    print('WHEEL_TREE_CHORD_PASS', 'ordered_pairs_checked', tested_pairs)

if __name__ == '__main__':
    verify()
