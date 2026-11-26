#!/usr/bin/env python3
from itertools import combinations
from collections import Counter


def graph(p, q):
    n = p + q
    a, b = 0, p
    A = list(range(p))
    B = list(range(p, n))
    X = set(range(1, p))
    Y = set(range(p + 1, n))
    adj = [set() for _ in range(n)]
    for block in (A, B):
        for i, u in enumerate(block):
            for v in block[i + 1:]:
                adj[u].add(v)
                adj[v].add(u)
    adj[a].add(b)
    adj[b].add(a)
    return adj, X, Y


def closure(adj, initial):
    blue = set(initial)
    while True:
        forced = None
        for u in sorted(blue):
            white_neighbors = [v for v in adj[u] if v not in blue]
            if len(white_neighbors) == 1:
                forced = white_neighbors[0]
                break
        if forced is None:
            return blue
        blue.add(forced)


def predicted(p, q, initial):
    n = p + q
    _, X, Y = graph(p, q)
    W = set(range(n)) - set(initial)
    return len(W) <= 3 and len(W & X) <= 1 and len(W & Y) <= 1


def expected_counts(p, q):
    n = p + q
    return {
        n - 3: 2 * p * q - p - q,
        n - 2: p * q + p + q - 2,
        n - 1: n,
        n: 1,
    }


def main():
    subset_checks = 0
    minimum_checks = 0
    parameter_pairs = 0
    max_order = 0
    for p in range(3, 7):
        for q in range(3, 7):
            parameter_pairs += 1
            n = p + q
            max_order = max(max_order, n)
            adj, X, Y = graph(p, q)
            counts = Counter()
            minimum_sets = []
            for r in range(n + 1):
                for S_tuple in combinations(range(n), r):
                    subset_checks += 1
                    S = set(S_tuple)
                    actual = len(closure(adj, S)) == n
                    theorem = predicted(p, q, S)
                    if actual != theorem:
                        raise AssertionError((p, q, sorted(S), actual, theorem))
                    if actual:
                        counts[r] += 1
            z = min(counts)
            if z != n - 3:
                raise AssertionError((p, q, 'Z', z, n - 3))
            expected = expected_counts(p, q)
            if dict(counts) != expected:
                raise AssertionError((p, q, 'counts', dict(counts), expected))
            for S_tuple in combinations(range(n), z):
                S = set(S_tuple)
                if len(closure(adj, S)) == n:
                    minimum_checks += 1
                    W = set(range(n)) - S
                    if not (len(W) == 3 and len(W & X) <= 1 and len(W & Y) <= 1):
                        raise AssertionError((p, q, 'minimum classification', sorted(W)))
    print(
        'VERIFY_OK '
        f'parameter_pairs={parameter_pairs} '
        f'subset_checks={subset_checks} '
        f'minimum_checks={minimum_checks} '
        f'max_order={max_order}'
    )


if __name__ == '__main__':
    main()
