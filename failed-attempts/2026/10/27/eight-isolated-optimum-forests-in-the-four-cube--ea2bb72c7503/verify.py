#!/usr/bin/env python3
"""Exhaustive independent checks for extremal induced forests of Q3 and Q4."""
from collections import Counter, deque
from itertools import combinations


def neighbors(d):
    return [tuple(v ^ (1 << j) for j in range(d)) for v in range(1 << d)]


def forest_dfs(mask, nbr):
    """Test acyclicity by independent depth-first traversals."""
    seen = set()
    for start in range(len(nbr)):
        if not (mask >> start) & 1 or start in seen:
            continue
        seen.add(start)
        stack = [(start, -1)]
        while stack:
            v, parent = stack.pop()
            for w in nbr[v]:
                if not (mask >> w) & 1 or w == parent:
                    continue
                if w in seen:
                    return False
                seen.add(w)
                stack.append((w, v))
    return True


def forest_union_find(mask, nbr):
    """Independently scan the induced edge set with disjoint-set union."""
    parent = list(range(len(nbr)))
    def root(a):
        while parent[a] != a:
            a = parent[a]
        return a
    for v in range(len(nbr)):
        if (mask >> v) & 1:
            for w in nbr[v]:
                if w > v and (mask >> w) & 1:
                    a, b = root(v), root(w)
                    if a == b:
                        return False
                    parent[a] = b
    return True


def parity_mask(d, parity):
    return sum(1 << v for v in range(1 << d) if v.bit_count() % 2 == parity)


def expected_q4():
    n = 16
    full = (1 << n) - 1
    sets = set()
    for parity in (0, 1):
        bulk = parity_mask(4, parity)
        for v in range(n):
            if v.bit_count() % 2 != parity:
                w = v ^ 15
                if v < w:
                    sets.add(bulk | (1 << v) | (1 << w))
    return sets


def exchange_graph(sets):
    masks = set(sets)
    graph = {m: set() for m in masks}
    n = max(masks).bit_length()
    for x in masks:
        for u in range(n):
            if not x & (1 << u):
                continue
            for v in range(n):
                if x & (1 << v):
                    continue
                y = x ^ (1 << u) ^ (1 << v)
                if y in masks and y != x:
                    graph[x].add(y)
    assert all(x in graph[y] for x, ys in graph.items() for y in ys)
    return graph


def components(graph):
    remaining = set(graph)
    out = []
    while remaining:
        s = remaining.pop()
        reached = {s}
        q = deque([s])
        while q:
            for t in graph[q.popleft()]:
                if t not in reached:
                    reached.add(t)
                    remaining.discard(t)
                    q.append(t)
        out.append(reached)
    return out


def main():
    for d in (1, 2, 3, 4):
        nbr = neighbors(d)
        N = 1 << d
        max_size, maxima = 0, set()
        distribution = Counter()
        for mask in range(1 << N):
            a = forest_dfs(mask, nbr)
            b = forest_union_find(mask, nbr)
            assert a == b, (d, mask, a, b)
            if not a:
                continue
            k = mask.bit_count()
            distribution[k] += 1
            if k > max_size:
                max_size, maxima = k, {mask}
            elif k == max_size:
                maxima.add(mask)
        g = exchange_graph(maxima)
        c = sorted((len(t) for t in components(g)), reverse=True)
        if d == 1:
            assert (max_size, len(maxima), c) == (2, 1, [1])
        elif d == 2:
            assert (max_size, len(maxima), c) == (3, 4, [4])
        elif d == 3:
            assert (max_size, len(maxima), c) == (5, 32, [32])
            assert sum(map(len, g.values())) // 2 == 144
            assert set(map(len, g.values())) == {9}
            e = parity_mask(3, 0)
            o = parity_mask(3, 1)
            # Show a four-term exchange bridge through the two parity cores.
            deletion_path = [(0,3,5), (2,3,5), (1,2,5), (1,2,4)]
            forest_path = [((1<<8)-1)^sum(1<<j for j in t) for t in deletion_path]
            assert all(m in maxima for m in forest_path)
            assert all(y in g[x] for x, y in zip(forest_path, forest_path[1:]))
            assert all(((1<<8)-1)^m & e for m in maxima)
        else:
            assert max_size == 10
            assert maxima == expected_q4()
            assert c == [1]*8
            assert sum(map(len, g.values())) == 0
            assert distribution[10] == 8
            assert distribution[9] == 1008
            # Every maximum is two disjoint four-leaf stars: 10 vertices, 8 edges.
            for m in maxima:
                deg = [sum((m >> w) & 1 for w in nbr[v]) for v in range(N) if m >> v & 1]
                assert sorted(deg) == [1]*8 + [4]*2
        print(f'Q{d}_EXHAUSTIVE_OK vertices={N} maximum_forest={max_size} maximizing_sets={len(maxima)} components={c} exchange_edges={sum(map(len,g.values()))//2}')
    print('ALL_VERIFY_OK')


if __name__ == '__main__':
    main()
