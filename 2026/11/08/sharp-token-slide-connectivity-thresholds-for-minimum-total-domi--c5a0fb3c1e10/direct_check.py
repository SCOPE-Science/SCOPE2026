"""Independent direct graph-subset verification for minimum total-domination mobility."""
from itertools import combinations, product
from collections import Counter, deque
from math import comb


def components(adj):
    visited = set()
    sizes = []
    for start in range(len(adj)):
        if start in visited:
            continue
        q = [start]
        visited.add(start)
        size = 0
        for u in q:
            size += 1
            for v in adj[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        sizes.append(size)
    return Counter(sizes)


def examine(m, n):
    vertices = list(product(range(m), range(n)))
    neighborhoods = {v: {u for u in vertices if u[0] != v[0] and u[1] != v[1]} for v in vertices}
    assert not any(all(any(u in neighborhoods[v] for u in s) for v in vertices) for s in combinations(vertices, 2))
    optimum = [frozenset(t) for t in combinations(vertices, 3)
               if all(any(u in neighborhoods[v] for u in t) for v in vertices)]
    target = 6 * comb(m, 3) * comb(n, 3)
    assert len(optimum) == target, (m, n, len(optimum), target)
    assert all(len({u[0] for u in s}) == len({u[1] for u in s}) == 3 for s in optimum)
    numbers = {s: i for i, s in enumerate(optimum)}
    adj_slide = [set() for _ in optimum]
    adj_jump = [set() for _ in optimum]
    for i, s in enumerate(optimum):
        for old in s:
            for new in set(vertices) - set(s):
                t = frozenset((set(s) - {old}) | {new})
                j = numbers.get(t)
                if j is not None:
                    adj_jump[i].add(j)
                    if new in neighborhoods[old]:
                        adj_slide[i].add(j)
    for adj in (adj_slide, adj_jump):
        assert all(i in adj[j] for j, ns in enumerate(adj) for i in ns)
    pred_degree = 3 * (m - 3) * (n - 3)
    assert all(len(ns) == pred_degree for ns in adj_slide)
    actual_components = components(adj_slide)
    if min(m, n) == 3:
        expected = Counter({1: target})
    elif m == n == 4:
        expected = Counter({4: 24})
    else:
        expected = Counter({target: 1})
    assert actual_components == expected, (m, n, actual_components, expected)
    if m == n == 3:
        assert components(adj_jump) == Counter({1: 6})
    else:
        assert components(adj_jump) == Counter({target: 1})
    return (m, n, target, sum(map(len, adj_slide)) // 2, sorted(actual_components.items()))

if __name__ == '__main__':
    for m, n in [(3,3), (3,4), (3,5), (3,6), (4,4), (4,5), (4,6), (5,5), (5,6)]:
        print('direct', *examine(m, n))
    print('DIRECT_CHECK_PASS')
