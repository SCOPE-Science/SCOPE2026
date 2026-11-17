#!/usr/bin/env python3
"""Independent maximum-packing gap enumerator for squared cycles.

Builds every cyclic spacing vector of sum N, then reconstructs allowed slides.
Standard Python 3; no dependencies.
"""
from collections import Counter, deque
from itertools import combinations_with_replacement


def states(N):
    m, s = divmod(N, 3)
    out = set()
    for a in range(N):
        for extra in combinations_with_replacement(range(m), s):
            p = a
            mask = 0
            for j in range(m):
                mask |= 1 << p
                p = (p + 3 + extra.count(j)) % N
            assert p == a
            out.add(mask)
    return out


def build(N):
    ss = states(N)
    adj = {x: set() for x in ss}
    for x in ss:
        for u in range(N):
            if x & (1 << u):
                for delta in (-2, -1, 1, 2):
                    v = (u + delta) % N
                    if not (x & (1 << v)):
                        y = x ^ (1 << u) ^ (1 << v)
                        if y in ss:
                            adj[x].add(y)
    assert all(x in adj[y] for y, vs in adj.items() for x in vs)
    return adj


def components(adj):
    unseen = set(adj)
    comp = []
    while unseen:
        root = unseen.pop()
        c = {root}
        todo = [root]
        for v in todo:
            for w in adj[v]:
                if w in unseen:
                    unseen.remove(w)
                    c.add(w)
                    todo.append(w)
        comp.append(len(c))
    return sorted(comp, reverse=True)


def triangle_count(adj):
    return sum(len(adj[u] & adj[v]) for u in adj for v in adj[u]) // 6


def check(N):
    m, s = divmod(N, 3)
    adj = build(N)
    if s == 0:
        assert len(adj) == 3
        assert sorted(map(len, adj.values())) == [0]*3
        assert components(adj) == [1, 1, 1]
        assert triangle_count(adj) == 0
    elif s == 1:
        assert len(adj) == N
        assert all(len(x) == 2 for x in adj.values())
        assert components(adj) == [N]
        assert triangle_count(adj) == 0
    else:
        assert len(adj) == N*(m+1)//2
        assert all(len(x) == 4 for x in adj.values())
        assert components(adj) == [len(adj)]
        assert triangle_count(adj) == N
        # Exact incidence by state: 2 for a unique 5-gap; for m>=3,
        # 1 for adjacent 4-gaps and 0 for nonadjacent 4-gaps.
        triangle_degrees = Counter(sum(len(adj[u] & adj[v]) for v in adj[u]) // 2 for u in adj)
        if m == 2:
            assert triangle_degrees == {2: 12}
        else:
            expected = {2:N, 1:N}
            if m >= 4: expected[0] = N*(m-3)//2
            assert triangle_degrees == Counter(expected), (N, triangle_degrees, expected)
    return (N, len(adj), sum(map(len, adj.values()))//2, triangle_count(adj))


if __name__ == '__main__':
    for N in range(6, 75):
        row = check(N)
        if N < 32 or N%10 == 0: print(*row)
    print('GAP_RECONSTRUCTION_PASS')
