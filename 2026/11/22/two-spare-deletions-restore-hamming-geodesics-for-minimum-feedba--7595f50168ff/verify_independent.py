#!/usr/bin/env python3
"""Independent structural and monotone-path certificate with a cyclic Fano model.

Uses a different point/line model and DFS cycle test from the exhaustive verifier.
"""
from itertools import combinations
from collections import Counter

# The Singer difference set {0,1,3} gives the Fano lines by cyclic shifts.
LINES = [frozenset((j, (j + 1) % 7, (j + 3) % 7)) for j in range(7)]
assert len(set(LINES)) == 7
G = [set() for _ in range(14)]
for i, line in enumerate(LINES):
    for v in line:
        G[v].add(i + 7)
        G[i + 7].add(v)


def is_acyclic_after_deletion(deleted):
    deleted = set(deleted)
    visited = set()
    def visit(v, parent):
        visited.add(v)
        for w in G[v]:
            if w in deleted or w == parent:
                continue
            if w in visited or not visit(w, v):
                return False
        return True
    for v in range(14):
        if v not in deleted and v not in visited and not visit(v, -1):
            return False
    return True


def graph_states(cap):
    A = [frozenset(t) for k in range(4, cap + 1)
         for t in combinations(range(14), k) if is_acyclic_after_deletion(t)]
    where = {s: i for i, s in enumerate(A)}
    adj = [set() for _ in A]
    for i, s in enumerate(A):
        if len(s) == cap:
            continue
        for a in range(14):
            if a not in s:
                j = where.get(s | {a})
                if j is not None:
                    adj[i].add(j)
                    adj[j].add(i)
    return A, adj


def components(adj):
    todo = set(range(len(adj)))
    cc = []
    while todo:
        start = todo.pop()
        stack = [start]
        seen = {start}
        while stack:
            v = stack.pop()
            for w in adj[v]:
                if w in todo:
                    todo.remove(w)
                    seen.add(w)
                    stack.append(w)
        cc.append(seen)
    return cc


def monotone_path_exists(a, b):
    """Only add target elements/remove source elements: Hamming geodesic search."""
    goal = frozenset(b)
    target = set(b) - set(a)
    source = set(a) - set(b)
    start = frozenset(a)
    q = [start]
    seen = {start}
    for s in q:
        if s == goal:
            return True
        candidates = []
        if len(s) < 6:
            candidates.extend(s | {x} for x in target if x not in s)
        if len(s) > 4:
            candidates.extend(s - {x} for x in source if x in s)
        for nxt in candidates:
            if nxt not in seen and is_acyclic_after_deletion(nxt):
                seen.add(nxt)
                q.append(nxt)
    return False


def main():
    a4, _ = graph_states(4)
    assert len(a4) == 70
    # Check the previously-known Fano geometry afresh rather than trust it.
    kernels = []
    for j, line in enumerate(LINES):
        kernels.append(frozenset(set(range(7)) - line | {7 + j}))
    for point in range(7):
        kernels.append(frozenset({point} | {7 + j for j in range(7) if point not in LINES[j]}))
    assert all(len(K) == 5 for K in kernels)
    expected4 = {frozenset(K - {v}) for K in kernels for v in K}
    assert set(a4) == expected4
    a5, g5 = graph_states(5)
    assert len(a5) == 882
    assert Counter(map(len, components(g5))) == {1: 168, 51: 14}
    a6, g6 = graph_states(6)
    assert len(a6) == 3136
    assert len(components(g6)) == 1
    checks = 0
    # Test all unordered pairs; monotone paths automatically have exact
    # Hamming length and never use vertices outside the endpoint union.
    for a, b in combinations(a4, 2):
        assert monotone_path_exists(a, b), (sorted(a), sorted(b))
        checks += 1
    assert checks == 2415
    print('VERIFIED Singer-Fano geometry 14 five-vertex kernels, 70 four-vertex minima')
    print('VERIFIED B5 components=14x51+168 isolates; B6 connected on 3136 states')
    print('VERIFIED all 2415 optimum pairs have monotone feasible Hamming geodesics')

if __name__ == '__main__':
    main()
