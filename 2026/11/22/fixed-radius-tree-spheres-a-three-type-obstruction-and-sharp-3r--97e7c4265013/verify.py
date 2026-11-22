#!/usr/bin/env python3
"""Finite cross-checks of fixed-radius spheres on tree metrics; only standard Python."""
from collections import deque
from itertools import combinations, product
from random import Random


def from_prufer(seq, n):
    if n == 1:
        return [[]]
    degree = [1] * n
    for s in seq:
        degree[s] += 1
    out = [[] for _ in range(n)]
    for s in seq:
        leaf = next(i for i in range(n) if degree[i] == 1)
        out[leaf].append(s)
        out[s].append(leaf)
        degree[leaf] -= 1
        degree[s] -= 1
    u, v = (i for i in range(n) if degree[i] == 1)
    out[u].append(v)
    out[v].append(u)
    return out


def dists(g):
    n = len(g)
    out = []
    for s in range(n):
        dist = [-1] * n
        dist[s] = 0
        queue = deque([s])
        while queue:
            u = queue.popleft()
            for v in g[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        assert -1 not in dist
        out.append(dist)
    return out


def trace_set(dist, support, r):
    return {tuple(int(dist[x][a] == r) for a in support) for x in range(len(dist))}


def shattered(dist, support, r):
    return len(trace_set(dist, support, r)) == 2**len(support)


def path(g, start, target):
    parent = {start: None}
    queue = deque([start])
    while queue:
        u = queue.popleft()
        if u == target:
            ans = []
            while u is not None:
                ans.append(u)
                u = parent[u]
            return ans[::-1]
        for v in g[u]:
            if v not in parent:
                parent[v] = u
                queue.append(v)
    raise AssertionError("not connected")


def triple_criterion(g, dist, support, r):
    if r < 2:
        return False
    a, b, c = support
    for m in range(len(g)):
        h = dist[m][a]
        if not (1 <= h < r and dist[m][b] == h and dist[m][c] == h):
            continue
        if any(dist[x][y] != 2*h for x, y in combinations(support, 2)):
            continue
        t = r-h
        directed = {path(g, m, x)[1] for x in support}
        fourth = any(path(g, m, y)[1] not in directed
                     for y in range(len(g)) if dist[m][y] == t)
        if not fourth:
            continue
        qualifies = True
        for x in support:
            p = path(g, m, x)
            # A singleton witness branches off after positive depth u, with
            # precisely t+u further steps; extra vertices along the branch
            # can be discarded to realize that exact distance.
            valid = False
            for u, pivot in enumerate(p[1:], start=1):
                for y in range(len(g)):
                    if dist[pivot][y] != t+u:
                        continue
                    # The unique path pivot -> y is not along the m--x path.
                    if y not in p and path(g, pivot, y)[1] not in p:
                        valid = True
                        break
                if valid:
                    break
            if not valid:
                qualifies = False
                break
        if qualifies:
            return True
    return False


def extremal(r):
    assert r >= 2
    edges = []
    q = 1
    support = []
    for _ in range(3):
        parent = 0
        first = None
        for depth in range(1, r):
            edges.append((parent, q))
            if depth == 1:
                first = q
            parent = q
            q += 1
        support.append(parent)
        edges.extend([(first, q), (q, q+1)])
        q += 2
    edges.append((0, q))
    q += 1
    g = [[] for _ in range(q)]
    for a,b in edges:
        g[a].append(b)
        g[b].append(a)
    assert q == 3*r + 5
    return g, support


def run():
    checks = 0
    # All labelled trees through six vertices, including all six world pathologies.
    for n in range(2, 7):
        for seq in product(range(n), repeat=n-2):
            g = from_prufer(seq, n)
            ds = dists(g)
            for r in range(1, n):
                for support in combinations(range(n), 3):
                    assert shattered(ds, support, r) == triple_criterion(g, ds, support, r), (n, seq, r, support)
                    checks += 1
                for support in combinations(range(n), 4):
                    assert not shattered(ds, support, r)
                    checks += 1
    # Sharp explicit witnesses at arbitrary tested radii.
    for r in range(2, 16):
        g, support = extremal(r)
        ds = dists(g)
        assert shattered(ds, support, r)
        assert triple_criterion(g, ds, support, r)
        checks += 2
    # Random larger trees and radii test the independent structural criterion.
    rng = Random(190274)
    for trial in range(250):
        n = rng.randrange(7, 45)
        g = from_prufer([rng.randrange(n) for _ in range(n-2)], n)
        ds = dists(g)
        r = rng.randrange(1, min(n, 18))
        for _ in range(7):
            support = tuple(rng.sample(range(n), 3))
            assert shattered(ds, support, r) == triple_criterion(g, ds, support, r), (trial, r, support)
            checks += 1
        for _ in range(3):
            support = tuple(rng.sample(range(n), 4))
            assert not shattered(ds, support, r), (trial, r, support)
            checks += 1
    # Radius-one witness on the five-vertex path.
    g = from_prufer((1,2,3), 5)
    ds = dists(g)
    assert any(shattered(ds, ss, 1) for ss in combinations(range(5), 2))
    checks += 1
    print('VERIFY_OK', checks)


if __name__ == '__main__':
    run()
