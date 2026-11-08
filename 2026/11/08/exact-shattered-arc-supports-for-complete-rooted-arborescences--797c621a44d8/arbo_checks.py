"""Independent finite checks for rooted complete-digraph arborescence shattering.
Python 3 standard library only.  Run: python arbo_checks.py
"""
from itertools import product
from collections import Counter
from math import comb
from random import Random

def prufer_trees(n):
    if n == 2:
        yield [(0, 1)]
        return
    for code in product(range(n), repeat=n - 2):
        deg = [1] * n
        for x in code:
            deg[x] += 1
        edges = []
        for x in code:
            leaf = next(i for i in range(n) if deg[i] == 1)
            edges.append((leaf, x))
            deg[leaf] -= 1
            deg[x] -= 1
        ends = [i for i in range(n) if deg[i] == 1]
        edges.append(tuple(ends))
        yield edges

def oriented_edges(n, edges):
    neigh = [[] for _ in range(n)]
    for a, b in edges:
        neigh[a].append(b)
        neigh[b].append(a)
    parent = [-1] * n
    parent[0] = 0
    queue = [0]
    for v in queue:
        for w in neigh[v]:
            if parent[w] < 0:
                parent[w] = v
                queue.append(w)
    assert len(queue) == n
    return {(parent[w], w) for w in range(1, n)}

def is_branching(n, arcs):
    heads = set()
    neighbors = [[] for _ in range(n)]
    for u, v in arcs:
        if v in heads:
            return False
        heads.add(v)
        neighbors[u].append(v)
    color = [0] * n
    def dfs(v):
        color[v] = 1
        for w in neighbors[v]:
            if color[w] == 1 or (color[w] == 0 and not dfs(w)):
                return False
        color[v] = 2
        return True
    return all(color[v] or dfs(v) for v in range(n))

def check_support(n, arc_list, hypotheses, mask):
    arcs = [arc_list[j] for j in range(len(arc_list)) if mask & (1 << j)]
    expected = (len(arcs) <= n - 2 and is_branching(n, arcs))
    actual = len({h & mask for h in hypotheses}) == 2 ** len(arcs)
    assert actual == expected, (n, arcs, actual, expected)
    return len(arcs) if actual else None

def verify(n, exhaustive, sampled=0):
    arc_list = [(u, v) for v in range(1, n) for u in range(n) if u != v]
    hypotheses = []
    for t in prufer_trees(n):
        edges = oriented_edges(n, t)
        hypotheses.append(sum(1 << j for j, a in enumerate(arc_list) if a in edges))
    assert len(hypotheses) == n ** (n - 2)
    if exhaustive:
        masks = range(1 << len(arc_list))
    else:
        rng = Random(28731)
        masks = [rng.getrandbits(len(arc_list)) for _ in range(sampled)]
        # force cardinalities around the predicted maximal face size
        masks += [sum(1 << j for j in rng.sample(range(len(arc_list)), s))
                  for s in range(n - 3, n) for _ in range(100)]
    seen = Counter()
    count = 0
    for mask in masks:
        k = check_support(n, arc_list, hypotheses, mask)
        if k is not None:
            seen[k] += 1
        count += 1
    if exhaustive:
        expected = {s: comb(n - 1, s) * (n - s) * n ** (s - 1)
                    for s in range(n - 1)}
        assert all(seen[s] == v for s, v in expected.items()), (n, seen, expected)
    return count, dict(sorted(seen.items()))

if __name__ == '__main__':
    total = 0
    for n in range(2, 6):
        tested, counts = verify(n, True)
        print('n', n, 'supports', tested, 'shattered_by_size', counts)
        total += tested
    tested, counts = verify(6, False, sampled=500)
    total += tested
    print('n 6 sampled', tested, 'shattered_by_size', counts)
    print('ROOTED_ARBORESCENCE_SHATTER_PASS', total)
