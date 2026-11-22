#!/usr/bin/env python3
"""Finite sum-incidence graph checks for the stated unicyclic examples.

Only finite graphs are enumerated; the infinite stabilization is established by
an independent maximum-edge argument in the proof.
"""
from collections import defaultdict, deque


def finite_graph(sums):
    adj = defaultdict(set)
    for d in sums:
        for i in range(d + 1):
            left, right = (0, i), (1, d-i)
            adj[left].add(right)
            adj[right].add(left)
    return adj


def cycle_rank(adj):
    vertices = set(adj)
    seen = set()
    components = 0
    for root in vertices:
        if root in seen:
            continue
        components += 1
        stack = [root]
        seen.add(root)
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
    edges = sum(map(len, adj.values())) // 2
    return edges - len(vertices) + components


def girth(adj):
    ans = float('inf')
    for root in adj:
        parent = {root: None}
        distance = {root: 0}
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if v not in distance:
                    distance[v] = distance[u] + 1
                    parent[v] = u
                    queue.append(v)
                elif parent[u] != v:
                    ans = min(ans, distance[u] + distance[v] + 1)
    return ans


def main():
    checked = 0
    for r in range(2, 12):
        base = (0, r-1, r)
        scale = 2*r+1
        # Each appended sum exceeds twice the previous largest sum.
        for extra in range(4):
            sums = base + tuple(scale * 3**j for j in range(1, extra+1))
            adj = finite_graph(sums)
            assert cycle_rank(adj) == 1, (r, extra, 'rank')
            assert girth(adj) == 2*r, (r, extra, 'girth')
            checked += 1
        print(f'r={r}: base girth {2*r}, one independent cycle after 0..3 distant additions')
    print(f'GIRTH_CHECKS_OK finite_graphs={checked}')


if __name__ == '__main__':
    main()
