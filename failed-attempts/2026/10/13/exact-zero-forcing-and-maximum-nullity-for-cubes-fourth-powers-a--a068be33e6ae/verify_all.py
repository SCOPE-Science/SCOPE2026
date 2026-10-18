#!/usr/bin/env python3
"""Finite spectral-support and zero-forcing checks for powered equal-leg spiders.

Run with: python3 verify_all.py
Uses only the Python 3 standard library. Finite checks illustrate and stress-test
but do not establish the all-parameter claim; see the written proof.
"""
from collections import deque
from itertools import combinations
from math import cos, pi, sin


def spider(m, ell):
    n = 1 + m * ell
    adj = [set() for _ in range(n)]
    def edge(u, v):
        adj[u].add(v)
        adj[v].add(u)
    for a in range(m):
        base = 1 + a * ell
        edge(0, base)
        for j in range(ell - 1):
            edge(base + j, base + j + 1)
    return adj


def distance_rows(adj):
    D = []
    for s in range(len(adj)):
        d = [-1] * len(adj)
        d[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if d[v] < 0:
                    d[v] = d[u] + 1
                    q.append(v)
        D.append(d)
    return D


def power_graph(adj, k, D=None):
    if D is None:
        D = distance_rows(adj)
    return [set(v for v in range(len(adj)) if 0 < D[u][v] <= k)
            for u in range(len(adj))]


def forces_all(adj, initial):
    black = set(initial)
    while True:
        forced = None
        for u in sorted(black):
            white = adj[u] - black
            if len(white) == 1:
                forced = next(iter(white))
                break
        if forced is None:
            return len(black) == len(adj)
        black.add(forced)


def p_of_adjacency(adj, k, ell):
    n = len(adj)
    B = [[int(u == v) for v in range(n)] for u in range(n)]
    lambdas = [2 * cos(j * pi / (ell + 1)) for j in range(1, k + 1)]
    for root in lambdas:
        # B <- B(A-root I), multiplying by sparse adjacency on the right.
        B = [[sum(B[u][w] for w in adj[v]) - root * B[u][v]
              for v in range(n)] for u in range(n)]
    return B


def check_instance(m, k, ell):
    T = spider(m, ell)
    D = distance_rows(T)
    H = power_graph(T, k, D)
    B = p_of_adjacency(T, k, ell)
    margin = float('inf')
    for u in range(len(T)):
        for v in range(u + 1, len(T)):
            x = abs(B[u][v])
            if D[u][v] <= k:
                assert x > 1e-6, ('support edge vanished', m, k, ell, u, v, x)
                margin = min(margin, x)
            else:
                assert x < 1e-6, ('support nonedge appeared', m, k, ell, u, v, x)
    residual = 0.0
    for j in range(1, k + 1):
        vec = [sin(j * pi * t / (ell + 1)) for t in range(1, ell + 1)]
        for a in range(m - 1):
            x = [0.] * len(T)
            for t in range(ell):
                x[1 + a * ell + t] = vec[t]
                x[1 + (m - 1) * ell + t] = -vec[t]
            residual = max(residual, *(abs(sum(B[u][v]*x[v]
                    for v in range(len(T)))) for u in range(len(T))))
    assert residual < 2e-6, (m, k, ell, residual)
    initial = {1 + a * ell + j for a in range(m - 1)
               for j in range(ell - k, ell)}
    assert len(initial) == (m - 1) * k
    assert forces_all(H, initial), (m, k, ell, 'upper bound fails')
    return margin, residual


def smaller_cardinality_exhaustive(m, k, ell):
    T = spider(m, ell)
    H = power_graph(T, k)
    bound = (m - 1) * k
    ntests = 0
    for initial in combinations(range(len(T)), bound - 1):
        ntests += 1
        assert not forces_all(H, initial), (m, k, ell, 'too small', initial)
    return ntests


def main():
    count = 0
    minmargin = float('inf')
    maxerror = 0.0
    for m in range(2, 6):
        for k in range(3, 7):
            for ell in range(k + 1, 14):
                if not (k <= 4 or ell >= 2*k - 1):
                    continue
                margin, error = check_instance(m, k, ell)
                count += 1
                minmargin = min(minmargin, margin)
                maxerror = max(maxerror, error)
    print('spectral-support, eigenvector, and forcing-witness instances:', count)
    print('minimum supported absolute matrix entry: %.9f' % minmargin)
    print('maximum eigenvector residual: %.6g' % maxerror)
    total = 0
    for m, k, ell in ((3,3,4), (3,3,5), (4,3,4), (3,4,5), (3,4,6)):
        ntests = smaller_cardinality_exhaustive(m,k,ell)
        total += ntests
        print('all size %d subsets, spider(m=%d,k=%d,ell=%d): %d; none forces all' %
              ((m-1)*k-1,m,k,ell,ntests))
    print('exhaustive suboptimality attempts:', total)
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    main()
