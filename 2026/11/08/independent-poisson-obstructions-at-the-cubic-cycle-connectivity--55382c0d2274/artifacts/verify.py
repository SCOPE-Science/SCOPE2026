#!/usr/bin/env python3
"""Independent finite checks of edge supports for cycle-cube bond percolation.

This script confirms local support enumerations; it does not prove the
asymptotic Poisson or connectivity statements, which need analytic arguments.
"""
from collections import Counter


def edge(a, b, n):
    return tuple(sorted((a % n, b % n)))


def host_edges(n):
    return {edge(i, i + d, n) for i in range(n) for d in (1, 2, 3)}


def isolated_edges(i, n):
    return {edge(i, i + j, n) for j in (-3, -2, -1, 1, 2, 3)}


def wall_edges(i, n):
    # The gap has left endpoint i and right endpoint i+1.
    return {
        edge(i - u, i + v + 1, n)
        for u in range(3) for v in range(3) if u + v + 1 <= 3
    }


def cut_edges(S, edges):
    return sum((a in S) != (b in S) for a, b in edges)


def run():
    count = 0
    for n in (15, 16, 17, 18, 24, 40):
        E = host_edges(n)
        assert len(E) == 3 * n
        count += 1
        I = [isolated_edges(i, n) for i in range(n)]
        W = [wall_edges(i, n) for i in range(n)]
        for a in I + W:
            assert len(a) == 6 and a <= E
            count += 1
        for i in range(n):
            for j in range(n):
                if i != j:
                    assert len(I[i] | I[j]) >= 11
                    assert len(W[i] | W[j]) >= 9
                    count += 2
                assert len(I[i] | W[j]) >= 9
                count += 1
        for i in range(n):
            for separation in (1, 2):
                S = {i, (i + separation) % n}
                assert cut_edges(S, E) == 10
                count += 1
            S = {i, (i + 1) % n, (i + 2) % n}
            assert cut_edges(S, E) == 12
            count += 1
    for n in (12, 14, 16):
        E = host_edges(n)
        # Enumerate nontrivial cuts, fixing vertex n-1 on the other side.
        tally = Counter()
        for mask in range(1, 1 << (n - 1)):
            S = {i for i in range(n - 1) if (mask >> i) & 1}
            b = cut_edges(S, E)
            assert b >= 6
            if b == 6:
                assert len(S) == 1 or len(S) == n - 1
            if len(S) > 1 and len(S) < n - 1:
                assert b >= 10
            tally[b] += 1
            count += 1
        assert tally[6] == n
        count += 1
        print(f'cycle n={n}: min cut=6, next cut=10, singleton cuts={tally[6]}')
    for m in range(2, 16):
        wall = m * (m + 1) // 2
        isol = 2 * m
        assert (wall < isol) == (m == 2)
        assert (wall == isol) == (m == 3)
        assert (wall > isol) == (m >= 4)
        count += 3
    print('LOCAL_SUPPORT_CHECKS_PASSED', count)


if __name__ == '__main__':
    run()
