#!/usr/bin/env python3
"""Independent exhaustive checks of proper conflict-free wheel recoloring.
Uses the literal adjacency graph, not the singleton characterization.
"""
from itertools import product
from collections import Counter, deque


def wheel(n):
    adj = [set() for _ in range(n + 1)]
    for i in range(n):
        for j in ((i - 1) % n, (i + 1) % n, n):
            adj[i].add(j)
            adj[j].add(i)
    return adj


def is_pcf(colors, adj):
    for u, N in enumerate(adj):
        if any(colors[u] == colors[v] for v in N):
            return False
        if N and 1 not in Counter(colors[v] for v in N).values():
            return False
    return True


def all_states(n):
    # Fix hub color 3; all rim assignments from {0,1,2}, without assuming
    # anything about PCF structure. Other hub colors give four isomorphic blocks.
    graph = wheel(n)
    return {seq for seq in product(range(3), repeat=n)
            if is_pcf(seq + (3,), graph)}


def components(states, n):
    state_set = states
    adj = {u: set() for u in state_set}
    for u in state_set:
        for pos in range(n):
            for col in range(3):
                if col == u[pos]:
                    continue
                v = u[:pos] + (col,) + u[pos + 1:]
                if v in state_set:
                    adj[u].add(v)
    assert all((u in adj[v]) for u in state_set for v in adj[u])
    unseen = set(state_set)
    comps = []
    while unseen:
        start = unseen.pop()
        comp = {start}
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if v in unseen:
                    unseen.remove(v)
                    comp.add(v)
                    queue.append(v)
        comps.append(comp)
    return adj, sorted(len(c) for c in comps)


def verify():
    for n in range(3, 12):
        states = all_states(n)
        adj, sizes = components(states, n)
        expected_per_hub = 6 if n == 3 else 12 if n == 4 else 6 * n
        expected_sizes = ([1] * expected_per_hub if n in (3, 4) or n >= 7
                          else [15, 15] if n == 5 else [6] * 6)
        assert len(states) == expected_per_hub, (n, len(states), expected_per_hub)
        assert sizes == expected_sizes, (n, sizes, expected_sizes)
        expected_degrees = 2 if n in (5, 6) else 0
        assert all(len(adj[u]) == expected_degrees for u in states)
        # Verify that the PCF characterization is equivalent to a unique
        # singleton rim color on every properly colored wheel.
        for rim in product(range(3), repeat=n):
            if all(rim[i] != rim[(i + 1) % n] for i in range(n)):
                assert (rim in states) == (1 in Counter(rim).values())
        print(f"RIM={n} PCF4={4 * len(states)} COMPONENTS={4 * len(sizes)} "
              f"SIZES={Counter(sizes)} EDGES={4 * sum(map(len, adj.values())) // 2}")
    print("VERIFY_OK")

if __name__ == '__main__':
    verify()
