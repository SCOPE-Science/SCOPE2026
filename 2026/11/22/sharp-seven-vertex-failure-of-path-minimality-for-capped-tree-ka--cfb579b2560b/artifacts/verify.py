#!/usr/bin/env python3
"""Independent exact checks of three-distance one-point types on capped trees.
Standard-library only.  No randomized steps or network access.
"""
from collections import deque
from fractions import Fraction
from itertools import product
from math import prod


def adjacency(n, edges):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        assert a != b and b not in adj[a]
        adj[a].add(b)
        adj[b].add(a)
    return adj


def from_prufer(seq, n):
    if n == 1:
        assert not seq
        return [[]]
    deg = [1] * n
    for a in seq:
        deg[a] += 1
    edges = []
    for a in seq:
        leaf = next(i for i in range(n) if deg[i] == 1)
        edges.append((leaf, a))
        deg[leaf] -= 1
        deg[a] -= 1
    a, b = [i for i in range(n) if deg[i] == 1]
    edges.append((a, b))
    return adjacency(n, edges)


def path(n):
    return adjacency(n, [(i, i + 1) for i in range(n - 1)])


def spider(arms):
    n = 1 + sum(arms)
    edges = []
    new = 1
    for length in arms:
        last = 0
        for _ in range(length):
            edges.append((last, new))
            last, new = new, new + 1
    return adjacency(n, edges)


def graph_dist(adj):
    n = len(adj)
    D = []
    for root in range(n):
        row = [n + 1] * n
        row[root] = 0
        q = deque([root])
        while q:
            v = q.popleft()
            for u in adj[v]:
                if row[u] > row[v] + 1:
                    row[u] = row[v] + 1
                    q.append(u)
        assert max(row) <= n - 1 or n == 1
        D.append(row)
    return D


def subset_count(adj):
    """Support sum, independent of local-neighbor-degree formula."""
    n = len(adj)
    dist = graph_dist(adj)
    total = 2 ** n
    closed = [(1 << v) | sum(1 << u for u in adj[v]) for v in range(n)]
    for mask in range(1, 1 << n):
        S = [v for v in range(n) if mask & (1 << v)]
        if any(dist[u][v] >= 3 for i, u in enumerate(S) for v in S[i + 1:]):
            continue
        covered = 0
        for v in S:
            covered |= closed[v]
        total += 1 << (n - covered.bit_count())
    return total


def local_count(adj):
    """Local formula, using exact rational arithmetic independently of subset_count."""
    n = len(adj)
    d = list(map(len, adj))
    f = Fraction(1)
    f += sum((Fraction(1, 2 ** (a + 1)) for a in d), Fraction(0))
    for u in range(n):
        for v in adj[u]:
            if u < v:
                f += Fraction(1, 2 ** (d[u] + d[v]))
    for c in range(n):
        r = [Fraction(1, 2 ** d[v]) for v in adj[c]]
        r2 = [2 * a for a in r]
        A = prod(1 + a for a in r) - 1 - sum(r)
        B = prod(1 + a for a in r2) - 1 - sum(r2)
        f += (A + Fraction(B, 2 ** d[c])) / 2
    ans = 2 ** n * f
    assert ans.denominator == 1, (adj, ans)
    return int(ans)


def direct_katetov(adj):
    """Brute-force three-distance vectors, checking all triangle inequalities."""
    n = len(adj)
    D = graph_dist(adj)
    total = 0
    for f in product((1, 2, 3), repeat=n):
        if all(abs(f[i] - f[j]) <= min(3, D[i][j]) <= f[i] + f[j]
               for i in range(n) for j in range(i + 1, n)):
            total += 1
    return total


def leaf_arm_lengths(adj):
    n = len(adj)
    degree = list(map(len, adj))
    centers = [v for v in range(n) if degree[v] == 3]
    if len(centers) != 1 or any(d not in (1, 2, 3) for d in degree):
        return None
    c = centers[0]
    if degree.count(1) != 3:
        return None
    D = graph_dist(adj)
    return tuple(sorted(D[c][v] for v in range(n) if degree[v] == 1))


def verify():
    # Direct Katetov versus support and degree-local formulas.
    direct_instances = 0
    for n in range(1, 6):
        for seq in product(range(n), repeat=max(n - 2, 0)):
            adj = from_prufer(seq, n)
            d = direct_katetov(adj)
            s = subset_count(adj)
            f = local_count(adj)
            assert d == s == f, (n, seq, d, s, f)
            direct_instances += 1
    for n in range(6, 10):
        for adj in (path(n), spider((2, 2, n - 5))):
            assert direct_katetov(adj) == subset_count(adj) == local_count(adj)
            direct_instances += 1

    # Exhaustive Pruefer enumeration of all labeled trees of each order <=7;
    # this covers every unlabeled tree, no isomorphism-generation assumption.
    minima, maxima, minimizer_checks = {}, {}, {}
    for n in range(1, 8):
        vmin, vmax = None, None
        min_count = 0
        all_codes = 0
        min_trees = []
        for seq in product(range(n), repeat=max(n - 2, 0)):
            adj = from_prufer(seq, n)
            k = local_count(adj)
            all_codes += 1
            if vmin is None or k < vmin:
                vmin, min_count, min_trees = k, 0, []
            if k == vmin:
                min_count += 1
                min_trees.append(adj)
            if vmax is None or k > vmax:
                vmax = k
        if n == 7:
            assert all(leaf_arm_lengths(adj) == (2, 2, 2) for adj in min_trees)
        if 4 <= n <= 6:
            assert all(sorted(map(len, adj)) == [1, 1] + [2] * (n - 2) for adj in min_trees)
        assert all_codes == (n ** (n - 2) if n >= 2 else 1)
        minima[n], maxima[n] = vmin, vmax
        minimizer_checks[n] = min_count
        print(f'n={n} trees={all_codes} min={vmin} max={vmax} labeled_minimizers={min_count}')
    assert [minima[n] for n in range(1, 8)] == [3, 7, 17, 37, 82, 180, 384]
    assert [maxima[n] for n in range(1, 8)] == [3, 7, 17, 43, 113, 307, 857]
    assert local_count(spider((2, 2, 2))) == 384
    assert local_count(path(7)) == 392

    # Verify exact infinite-family identities by local formula across sizable n.
    for n in range(8, 81):
        expected_p = (4 * n + 21) * (2 ** (n - 4))
        expected_s = (8 * n + 41) * (2 ** (n - 5))
        assert local_count(path(n)) == expected_p
        assert local_count(spider((2, 2, n - 5))) == expected_s
        assert expected_p - expected_s == 2 ** (n - 5)
    print(f'direct_instances={direct_instances}')
    print('all_order_formulas_checked=8..80')
    print('finite_exhaustive_orders=1..7')
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
