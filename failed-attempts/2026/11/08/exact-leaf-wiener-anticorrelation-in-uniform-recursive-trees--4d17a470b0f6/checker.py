#!/usr/bin/env python3
"""Exact independent checks for local-global statistics of recursive trees.

Standard library only. Run: python3 checker.py
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import factorial


def harmonic(n):
    return sum((F(1, k) for k in range(1, n + 1)), F(0))


def predicted(n):
    return n * harmonic(n) - F(n * (n + 5), 4) + F(1, 2)


def parse_tree(parents):
    """Parent of vertex v is parents[v-1], using zero-based vertex labels."""
    n = len(parents) + 1
    adj = [[] for _ in range(n)]
    for v in range(1, n):
        u = parents[v - 1]
        adj[u].append(v)
        adj[v].append(u)
    leaves = [v for v in range(n) if v not in parents]
    trans = []
    for root in range(n):
        dst = [-1] * n
        dst[root] = 0
        queue = [root]
        for u in queue:
            for v in adj[u]:
                if dst[v] == -1:
                    dst[v] = dst[u] + 1
                    queue.append(v)
        trans.append(sum(dst))
    return len(leaves), sum(trans) // 2, sum(trans[i] for i in leaves)


def check_exhaustion():
    assertions = 0
    for n in range(2, 10):
        sums = [0, 0, 0, 0]
        total = 0
        for parents in product(*[range(v) for v in range(1, n)]):
            L, W, Q = parse_tree(parents)
            total += 1
            sums[0] += L
            sums[1] += W
            sums[2] += L * W
            sums[3] += Q
        assert total == factorial(n - 1)
        meanL, meanW, meanLW, meanQ = (F(s, total) for s in sums)
        actual = meanLW - meanL * meanW
        expectationW = n * (n + 1) * harmonic(n) - 2 * n * n
        assert meanW == expectationW, ('W', n, meanW)
        assert meanL == F(n, 2), ('L', n, meanL)
        assert meanQ - meanW == F((n - 1) * (n - 2), 4), ('Q', n)
        assert actual == predicted(n), ('Cov', n, actual, predicted(n))
        assertions += 4
        print(f'n={n}, count={total}, covariance={actual}, E[Q]-E[W]={meanQ-meanW}')
    return assertions


def check_recurrences():
    assertions = 0
    L, W, Q, C = F(1), F(0), F(0), F(0)
    for m in range(1, 501):
        newC = (F(m + 1, m) * C + 2 * L * W / (m * m) - Q / m)
        newQ = Q + m + (1 - F(1, m)) * L + 2 * W / m
        newW = W * F(m + 2, m) + m
        newL = L * F(m - 1, m) + 1
        L, W, Q, C = newL, newW, newQ, newC
        n = m + 1
        assert C == predicted(n), ('recurrence covariance', n)
        assert Q - W == F((n - 1) * (n - 2), 4), ('recurrence Q', n)
        assert W == n * (n + 1) * harmonic(n) - 2 * n * n
        assert L == F(n, 2)
        if n >= 4:
            assert C < 0
        elif n in (2, 3):
            assert C == 0
        assertions += 5
    return assertions


def main():
    a = check_exhaustion() + check_recurrences()
    print(f'PASS: {a} exact assertions; exhaustive recursive trees up to n=9; symbolic-rational recurrence through n=501')


if __name__ == '__main__':
    main()
