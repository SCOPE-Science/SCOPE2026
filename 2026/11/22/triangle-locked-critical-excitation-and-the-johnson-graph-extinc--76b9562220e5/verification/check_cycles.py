#!/usr/bin/env python3
"""Exhaustive finite checks of rounded-half-contact excitation.
No external packages. Labels are fixed and no graph automorphisms are quotiented.
"""
from itertools import combinations


def fixtures():
    def make(n, edges, label):
        ns = [set() for _ in range(n)]
        for a, b in edges:
            ns[a].add(b)
            ns[b].add(a)
        assert all(len(ns[v]) >= 1 for v in range(n))
        return (label, tuple(tuple(sorted(nbr)) for nbr in ns))
    ans = []
    for n in (4, 5):
        sets = list(combinations(range(n), 2))
        edges = [(i, j) for i in range(len(sets))
                 for j in range(i + 1, len(sets))
                 if set(sets[i]).intersection(sets[j])]
        ans.append(make(len(sets), edges, f"J({n},2)"))
    for m in (3, 4):
        edges = []
        for a in range(3):
            for t in range(m):
                v = a*m + t
                for b in range(a + 1, 3):
                    edges.append((v, b*m + t))
                edges.append((v, a*m + ((t+1) % m)))
        ans.append(make(3*m, edges, f"K3xC{m}"))
    edges = []
    for i in range(3):
        a, b = 2*i+1, 2*i+2
        edges += [(0, a), (0, b), (a, b)]
    ans.append(make(7, edges, 'friendship_3'))
    ans.append(make(4, [(0, 2),(0, 3),(1, 2),(1, 3)], 'K2,2'))
    return ans


def periods(nbr):
    n = len(nbr)
    N = 3**n
    thresholds = [((len(a)+1)//2) for a in nbr]
    nxt = [-1]*N

    def update(v):
        digits = []
        y = v
        for _ in range(n):
            digits.append(y % 3)
            y //= 3
        out = 0
        pos = 1
        for i, a in enumerate(digits):
            if a == 1:
                b = 2
            elif a == 2:
                b = 0
            else:
                b = int(sum(digits[j] == 1 for j in nbr[i]) >= thresholds[i])
            out += b*pos
            pos *= 3
        return out

    # Functional-graph traversal, with each configuration visited once.
    marked = bytearray(N)
    path_index = [-1]*N
    found = {}
    for initial in range(N):
        if marked[initial]:
            continue
        path = []
        x = initial
        while not marked[x]:
            marked[x] = 1
            path_index[x] = len(path)
            path.append(x)
            if nxt[x] == -1:
                nxt[x] = update(x)
            x = nxt[x]
        if marked[x] == 1:
            p = len(path) - path_index[x]
            found[p] = found.get(p, 0) + 1
        for x in path:
            marked[x] = 2
            path_index[x] = -1
    assert all(marked)
    return found


def verify():
    expected = {
        'J(4,2)': {1: 1, 3: 2},
        'J(5,2)': {1: 1},
        'K3xC3': {1: 1, 3: 4},
        'K3xC4': {1: 1},
        'friendship_3': {1: 1, 3: 8},
        'K2,2': {1: 1, 4: 2},
    }
    for name, graph in fixtures():
        p = periods(graph)
        print(f'{name}: vertices={len(graph)}, states={3**len(graph)}, primitive_period_counts={dict(sorted(p.items()))}')
        assert p == expected[name], (name, p, expected[name])
    print('ALL_FINITE_CHECKS_PASS')


if __name__ == '__main__':
    verify()
