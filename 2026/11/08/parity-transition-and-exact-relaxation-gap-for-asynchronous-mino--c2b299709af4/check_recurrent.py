"""Exhaustive transition-graph test for closed-neighborhood minority dynamics.

Requires Python >=3.9; standard library only. Every selected-vertex update
is reconstructed from the full closed neighborhood, not a reduced formula.
"""
from math import comb


def analyze(m):
    n = 2 * m
    size = 1 << n
    adj = [[] for _ in range(size)]
    rev = [[] for _ in range(size)]
    for s in range(size):
        for v in range(n):
            count = sum((s >> w) & 1 for w in range(n) if w != (v ^ 1))
            nextbit = 1 if 2 * count < n - 1 else 0
            t = (s & ~(1 << v)) | (nextbit << v)
            if t != s:
                adj[s].append(t)
                rev[t].append(s)

    visited = bytearray(size)
    order = []
    for s in range(size):
        if visited[s]:
            continue
        visited[s] = 1
        stack = [(s, 0)]
        while stack:
            v, j = stack[-1]
            if j < len(adj[v]):
                w = adj[v][j]
                stack[-1] = (v, j + 1)
                if not visited[w]:
                    visited[w] = 1
                    stack.append((w, 0))
            else:
                order.append(v)
                stack.pop()

    comp_id = [-1] * size
    comps = []
    for s in reversed(order):
        if comp_id[s] >= 0:
            continue
        i = len(comps)
        stack = [s]
        comp_id[s] = i
        vertices = []
        while stack:
            v = stack.pop()
            vertices.append(v)
            for w in rev[v]:
                if comp_id[w] < 0:
                    comp_id[w] = i
                    stack.append(w)
        comps.append(vertices)

    closed = []
    for j, cc in enumerate(comps):
        if all(comp_id[t] == j for s in cc for t in adj[s]):
            closed.append(cc)
    states = {s for c in closed for s in c}
    maxset = set()
    maxcut = (m * m if m % 2 == 0 else m * m - 1)
    for s in range(size):
        score = sum(((s >> i) & 1) != ((s >> j) & 1)
                    for i in range(n) for j in range(i + 1, n) if j != (i ^ 1))
        if score == maxcut:
            maxset.add(s)
    assert states == maxset, (m, len(states), len(maxset))
    if m % 2 == 0:
        assert len(closed) == comb(m, m // 2)
        assert all(len(c) == 1 for c in closed)
    else:
        assert len(closed) == 1
        assert len(states) == (m + 3) * comb(m, (m - 1) // 2)
    return (m, size, len(comps), len(closed), len(states), maxcut)


if __name__ == '__main__':
    for m in range(2, 8):
        print('m=%d total=%d scc=%d recurrent_classes=%d recurrent_states=%d maxcut=%d' % analyze(m))
    print('FULL_TRANSITION_CHECK_PASS')
