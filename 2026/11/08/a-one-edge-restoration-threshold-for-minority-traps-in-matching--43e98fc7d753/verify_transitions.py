#!/usr/bin/env python3
"""Exhaustive transition-graph checks for asynchronous closed-neighborhood minority.

Uses only the Python standard library. Each graph has vertex sets
L_0,...,L_{n-1} and R_0,...,R_{n-1}; L_iR_j is present unless i=j<t.
"""
from collections import Counter
from math import comb


def update(x, v, neighbors):
    current = (x >> v) & 1
    ones = current + sum((x >> w) & 1 for w in neighbors[v])
    size = 1 + len(neighbors[v])
    preferred = current if 2 * ones == size else int(2 * ones < size)
    return x if current == preferred else (x ^ (1 << v))


def graph(n, t):
    neighbors = [[] for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i == j and i < t:
                continue
            neighbors[i].append(n+j)
            neighbors[n+j].append(i)
    return neighbors


def terminal_components(adj):
    # Iterative Kosaraju, to avoid third-party graph packages.
    size = len(adj)
    seen = bytearray(size)
    order = []
    for root in range(size):
        if seen[root]:
            continue
        seen[root] = 1
        stack = [(root, 0)]
        while stack:
            u, i = stack[-1]
            if i == len(adj[u]):
                order.append(u)
                stack.pop()
            else:
                stack[-1] = (u, i+1)
                v = adj[u][i]
                if not seen[v]:
                    seen[v] = 1
                    stack.append((v, 0))
    reverse = [[] for _ in range(size)]
    for u, nb in enumerate(adj):
        for v in nb:
            reverse[v].append(u)
    component = [-1]*size
    components = []
    for root in reversed(order):
        if component[root] != -1:
            continue
        identifier = len(components)
        component[root] = identifier
        stack = [root]
        vertices = []
        while stack:
            u = stack.pop()
            vertices.append(u)
            for v in reverse[u]:
                if component[v] == -1:
                    component[v] = identifier
                    stack.append(v)
        components.append(vertices)
    closed = [True]*len(components)
    for u, nb in enumerate(adj):
        for v in nb:
            if component[u] != component[v]:
                closed[component[u]] = False
    return [c for c, yes in zip(components, closed) if yes]


def run():
    total_states = 0
    total_graphs = 0
    for n in range(3, 7):
        for t in range(n+1):
            neighbors = graph(n, t)
            num = 1 << (2*n)
            adj = []
            for x in range(num):
                # Self-loops are irrelevant to communicating classes.
                adj.append([y for v in range(2*n)
                            if (y := update(x, v, neighbors)) != x])
            components = terminal_components(adj)
            expected = (2 + comb(n, n//2)) if n % 2 == 0 and t == n else 2
            assert len(components) == expected, (n, t, len(components), expected)
            assert all(len(c) == 1 for c in components), (n, t)
            stable = [c[0] for c in components]
            polar = {(1 << n)-1, ((1 << n)-1)<<n}
            assert polar.issubset(stable), (n, t)
            if n % 2 == 0 and t == n:
                for s in stable:
                    if s not in polar:
                        left = s & ((1<<n)-1)
                        right = s >> n
                        assert left == right and left.bit_count() == n//2
            else:
                assert set(stable) == polar
            total_states += num
            total_graphs += 1
            print(f'n={n} t={t} states={num} recurrent_classes={len(components)} all_absorbing=1')
    print(f'PASS: {total_graphs} graphs; {total_states} state-space vertices checked')

if __name__ == '__main__':
    run()
