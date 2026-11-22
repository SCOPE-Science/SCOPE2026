#!/usr/bin/env python3
"""Exact finite checks for the exposed-vertex flip core of odd-order trees.
Requires only the Python standard library. Run: python3 verify.py
"""
from collections import deque
from itertools import product, combinations
from random import Random


def prufer_edges(n, word):
    if n == 1:
        return []
    deg = [1] * n
    for x in word:
        deg[x] += 1
    edges = []
    for x in word:
        leaf = min(i for i in range(n) if deg[i] == 1)
        edges.append((leaf, x))
        deg[leaf] -= 1
        deg[x] -= 1
    left = [i for i in range(n) if deg[i] == 1]
    edges.append(tuple(left))
    return edges


def adjacency(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj


def perfect_after_removal(adj, omitted):
    alive = set(range(len(adj))) - {omitted}
    matching = set()
    while alive:
        leaf = next((u for u in alive if len(adj[u] & alive) <= 1), None)
        if leaf is None:
            raise AssertionError('input is not a forest')
        nbr = adj[leaf] & alive
        if not nbr:
            return None
        v = next(iter(nbr))
        matching.add(tuple(sorted((leaf, v))))
        alive -= {leaf, v}
    return frozenset(matching)


def bfs_dists(adj, start):
    dist = {start: 0}
    Q = deque([start])
    while Q:
        u = Q.popleft()
        for v in adj[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                Q.append(v)
    return dist


def check_tree(n, edges, brute=False):
    adj = adjacency(n, edges)
    candidates = {u: p for u in range(n) if (p := perfect_after_removal(adj, u)) is not None}
    if brute:
        target = set()
        for comb in combinations((tuple(sorted(e)) for e in edges), (n-1)//2):
            vertices = [x for edge in comb for x in edge]
            if len(set(vertices)) == n-1:
                target.add(frozenset(comb))
        assert target == set(candidates.values())
    if not candidates:
        return False
    D = set(candidates)
    A = set().union(*(adj[u] for u in D)) - D
    C = set(range(n)) - D - A
    assert not any(adj[u] & D for u in D)
    assert all(len(adj[a] & D) == 2 for a in A)
    assert len(D) == len(A) + 1
    core = adjacency(n, [(a, u) for a in A for u in adj[a] & D])
    assert len(bfs_dists(core, min(D))) == len(A) + len(D)
    # Each remaining component has a forced perfect matching and a single attachment at A.
    left = set(C)
    while left:
        root = next(iter(left))
        comp = {root}
        Q = deque([root])
        while Q:
            for y in adj[Q.popleft()] & C:
                if y not in comp:
                    comp.add(y)
                    Q.append(y)
        left -= comp
        boundary = {(x, y) for x in comp for y in adj[x] - C}
        assert len(boundary) == 1 and next(iter(boundary))[1] in A
        assert len(comp) % 2 == 0
        for matching in candidates.values():
            assert sum(1 for a, b in matching if a in comp and b in comp) == len(comp)//2
    flip = {u: set() for u in D}
    for u, v in combinations(sorted(D), 2):
        if len(candidates[u] ^ candidates[v]) == 2:
            flip[u].add(v)
            flip[v].add(u)
    assert sum(map(len, flip.values())) == 2*(len(D)-1)
    td = {u: bfs_dists(adj, u) for u in D}
    for u in D:
        fd = bfs_dists(flip, u)
        assert set(fd) == D
        for v in D:
            assert 2*fd[v] == td[u][v]
            assert (v in flip[u]) == (td[u][v] == 2)
    assert len(D) <= (n+1)//2
    if len(D) == (n+1)//2:
        assert not C
        assert all(len(adj[a]) == 2 for a in A)
    return True


def subdivision(n, edges):
    e = len(edges)
    out = []
    for j, (u, v) in enumerate(edges):
        out.extend([(u, n+j), (v, n+j)])
    return 2*n-1, out


def main():
    exhaustive = matched = 0
    for n in (1, 3, 5, 7):
        ct = yes = 0
        words = [()] if n == 1 else product(range(n), repeat=n-2)
        for word in words:
            ct += 1
            if check_tree(n, prufer_edges(n, word), brute=True):
                yes += 1
        exhaustive += ct
        matched += yes
        print('EXHAUSTIVE', n, 'trees', ct, 'with_odd_matching', yes, flush=True)
    rng = Random(20261115)
    randomized = 0
    for n in (9, 11, 13, 15, 17, 19):
        for _ in range(250):
            word = [rng.randrange(n) for _ in range(n-2)]
            check_tree(n, prufer_edges(n, word))
            randomized += 1
    print('RANDOM_TREES', randomized, flush=True)
    # Conversely, test the subdivision realization for all labelled trees through 6 vertices.
    count = 0
    for n in range(1, 7):
        words = [()] if n == 1 else product(range(n), repeat=n-2)
        for word in words:
            edges = prufer_edges(n, word)
            m, se = subdivision(n, edges)
            adj = adjacency(m, se)
            exposed = {v: perfect_after_removal(adj, v) for v in range(m)}
            exposed = {v:p for v,p in exposed.items() if p is not None}
            assert set(exposed) == set(range(n))
            for u, v in combinations(range(n), 2):
                assert (len(exposed[u] ^ exposed[v]) == 2) == (tuple(sorted((u,v))) in {tuple(sorted(e)) for e in edges})
            count += 1
    print('REALIZATION_TREES', count, flush=True)
    print('VERIFY_OK', flush=True)

if __name__ == '__main__':
    main()
