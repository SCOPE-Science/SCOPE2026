#!/usr/bin/env python3
"""Exact-rational verification for the two-offer target-hitting theorem.

Only Python's standard library is needed.  All connected labelled simple graphs
on 2--6 vertices are enumerated, with the fixed target at vertex 0; moving an
arbitrary target to 0 by relabelling loses no instances.
"""
from fractions import Fraction
from itertools import combinations


def solve_exact(A, b):
    """Gauss elimination on an exact rational augmented matrix."""
    n = len(b)
    T = [[Fraction(x) for x in A[i]] + [Fraction(b[i])]
         for i in range(n)]
    for j in range(n):
        p = next((i for i in range(j, n) if T[i][j]), None)
        assert p is not None, "nonproper preference policy"
        T[j], T[p] = T[p], T[j]
        pivot = T[j][j]
        for i in range(j + 1, n):
            if T[i][j] == 0:
                continue
            f = T[i][j] / pivot
            for k in range(j + 1, n + 1):
                T[i][k] -= f * T[j][k]
            T[i][j] = 0
    out = [Fraction(0)] * n
    for j in reversed(range(n)):
        out[j] = (T[j][-1] - sum(T[j][k] * out[k]
                        for k in range(j + 1, n))) / T[j][j]
    return out


def graph_from_mask(n, mask):
    adj = [[] for _ in range(n)]
    bit = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (mask >> bit) & 1:
                adj[i].append(j)
                adj[j].append(i)
            bit += 1
    return adj


def connected(adj):
    seen = {0}
    queue = [0]
    for v in queue:
        for u in adj[v]:
            if u not in seen:
                seen.add(u)
                queue.append(u)
    return len(seen) == len(adj)


def distances(adj, target):
    d = [-1] * len(adj)
    d[target] = 0
    queue = [target]
    for v in queue:
        for u in adj[v]:
            if d[u] < 0:
                d[u] = d[v] + 1
                queue.append(u)
    assert min(d) >= 0
    return d


def optimal_hitting_values(adj, target=0):
    """Exact policy iteration with an exact Bellman-certificate at termination."""
    n = len(adj)
    live = [v for v in range(n) if v != target]
    pos = {v: j for j, v in enumerate(live)}
    values = [Fraction(d) for d in distances(adj, target)]
    for iteration in range(1, 31):
        orders = [tuple(sorted(adj[v], key=lambda u: (values[u], u)))
                  for v in range(n)]
        matrix = [[0] * len(live) for _ in live]
        right = [0] * len(live)
        for v in live:
            j = pos[v]
            degree = len(adj[v])
            matrix[j][j] = degree ** 2
            right[j] = degree ** 2
            for place, u in enumerate(orders[v]):
                if u != target:
                    matrix[j][pos[u]] -= 2 * (degree - place) - 1
        solution = solve_exact(matrix, right)
        new_values = [Fraction(0)] * n
        for v in live:
            new_values[v] = solution[pos[v]]
        new_orders = [tuple(sorted(adj[v], key=lambda u: (new_values[u], u)))
                      for v in range(n)]
        if all(orders[v] == new_orders[v] for v in live):
            for v in live:
                d = len(adj[v])
                assert new_values[v] == 1 + sum(
                    min(new_values[u], new_values[w])
                    for u in adj[v] for w in adj[v]) / (d*d)
            return new_values, iteration
        values = new_values
    raise AssertionError("policy iteration did not terminate")


def check_minimality():
    counts = {}
    for n in range(2, 7):
        tested = 0
        for mask in range(1 << (n*(n-1)//2)):
            adj = graph_from_mask(n, mask)
            if not connected(adj):
                continue
            values, _ = optimal_hitting_values(adj, target=0)
            dist = distances(adj, 0)
            for v in range(1, n):
                for u, w in combinations(adj[v], 2):
                    assert not (dist[u] < dist[w] and values[u] > values[w]), (
                        'inversion', n, mask, v, u, w)
                    assert not (dist[w] < dist[u] and values[w] > values[u]), (
                        'inversion', n, mask, v, w, u)
            tested += 1
        counts[n] = tested
    assert counts == {2: 1, 3: 4, 4: 38, 5: 728, 6: 26704}
    print('EXHAUSTIVE_CONNECTED_LABELLED_ROOTED', counts,
          'TOTAL', sum(counts.values()))


def decorated_cycle(k):
    adj = [[] for _ in range(k+5)]
    edges = [(0,1), (1,2), (2,3), (3,4), (4,0)]
    edges += [(0, 5+i) for i in range(k)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj


def check_family():
    k0, _ = optimal_hitting_values(decorated_cycle(0), target=1)
    k1, _ = optimal_hitting_values(decorated_cycle(1), target=1)
    assert k0 == [Fraction(16,9), 0, Fraction(16,9),
                  Fraction(28,9), Fraction(28,9)]
    assert k1 == [Fraction(656,249), 0, Fraction(152,83),
                  Fraction(276,83), Fraction(316,83), Fraction(905,249)]
    for k in range(2, 18):
        den = 134*k + 147
        a = Fraction(8*(10*k*k + 54*k + 37), den)
        b = Fraction(2*(k*k + 126*k + 136), den)
        c = Fraction(4*(2*k*k + 118*k + 125), den)
        d = Fraction(2*(13*k*k + 298*k + 298), den)
        assert a - c == Fraction(4*(18*k*k-10*k-51), den) > 0
        assert a + 1 - d == Fraction(3*(18*k*k-10*k-51), den) > 0
        assert 0 < b < c < d
        assert b == 1 + c/4
        assert c == 1 + 3*b/4 + d/4
        assert d == 1 + 3*c/4 + a/4
        assert a == 1 + (2*k+1)*d/(k+2)**2 + k*k*(a+1)/(k+2)**2
        candidate = [a, Fraction(0), b, c, d] + [a+1]*k
        actual, _ = optimal_hitting_values(decorated_cycle(k), target=1)
        assert candidate == actual
    a,_,b,c,d,leaf1,leaf2 = optimal_hitting_values(decorated_cycle(2), target=1)[0]
    assert (a, b, c, d, leaf1, leaf2) == (
        Fraction(296,83), Fraction(784,415), Fraction(1476,415),
        Fraction(1892,415), Fraction(379,83), Fraction(379,83))
    assert a-c == Fraction(4,415)
    print('EXACT_FAMILY_IDENTITIES_OK', 'K=0,1 AND K=2..17',
          'SEVEN_VERTEX_GAP', a-c)


if __name__ == '__main__':
    check_family()
    check_minimality()
    print('VERIFY_OK')
