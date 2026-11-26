#!/usr/bin/env python3
"""Computational checks for the binary weight-two one-deletion code optimum.
Python 3 standard library only. All words use one-indexed mathematical positions.
"""
from itertools import combinations


def descendants(n, pair):
    a, b = pair
    w = [0] * n
    w[a - 1] = w[b - 1] = 1
    return {tuple(w[:i] + w[i + 1:]) for i in range(n)}


def construction(n):
    m = n - 1
    c = [(i, i + 1) for i in range(1, m + 1, 2)]
    c += [(4 * r + 2, 4 * r + 5) for r in range(m // 4)]
    return c


def exact_independent_number(n):
    """Tomita-style color upper-bound search on the compatibility graph."""
    words = list(combinations(range(1, n + 1), 2))
    balls = [descendants(n, pair) for pair in words]
    N = len(words)
    adj = [0] * N
    for i in range(N):
        for j in range(i + 1, N):
            if not balls[i].intersection(balls[j]):
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    best = 0
    def color_sort(P):
        order = []
        ub = []
        rest = P
        col = 0
        while rest:
            col += 1
            Q = rest
            while Q:
                bit = Q & -Q
                v = bit.bit_length() - 1
                order.append(v)
                ub.append(col)
                rest ^= bit
                Q ^= bit
                Q &= ~adj[v]
        return order, ub
    def dfs(P, d):
        nonlocal best
        if not P:
            if d > best: best = d
            return
        order, ub = color_sort(P)
        for z in range(len(order) - 1, -1, -1):
            if d + ub[z] <= best:
                return
            v = order[z]
            dfs(P & adj[v], d + 1)
            P ^= (1 << v)
    dfs((1 << N) - 1, 0)
    return best


def run():
    tested_sources = 0
    all_decks = 0
    for n in range(2, 85):
        m = n - 1
        c = construction(n)
        expected = (3*n - 2)//4
        assert len(c) == expected, (n, len(c), expected)
        assert all(1 <= a < b <= n for a, b in c)
        balls = [descendants(n, x) for x in c]
        for i in range(len(c)):
            for j in range(i + 1, len(c)):
                assert not balls[i].intersection(balls[j]), (n,c[i],c[j])
        seen = set()
        for pair in combinations(range(1, n+1), 2):
            D = descendants(n, pair)
            assert len(D) <= 5
            one = {x.index(1) + 1 for x in D if sum(x) == 1}
            if pair[1] == pair[0] + 1:
                assert one == {pair[0]}
            else:
                assert one == {pair[0],pair[1]-1}
            tested_sources += 1
            all_decks += len(D)
        assert (m+(m+1)//2)//2 == expected
    independent = {}
    for n in range(2, 12):
        independent[n] = exact_independent_number(n)
        assert independent[n] == (3*n-2)//4, (n,independent[n])
    print("WEIGHT_TWO_DELETION_ALL_CHECKS_PASS")
    print("construction_n=2..84; direct_source_balls=",tested_sources, "; deck_outputs=",all_decks)
    print("independent_exact_n=2..11:",independent)

if __name__ == '__main__':
    run()
