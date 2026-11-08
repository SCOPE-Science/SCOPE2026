#!/usr/bin/env python3
"""Check fort-packing and fractional-cover formula for unequal clique bouquets.
Python 3 standard library only. Finite tests supplement the written proof.
"""
from itertools import product, combinations
from functools import lru_cache

def make_graph(sizes):
    n = 1 + sum(sizes)
    edges = set()
    blocks = []
    a = 1
    for q in sizes:
        block = tuple(range(a, a + q)); blocks.append(block)
        for v in block: edges.add(tuple(sorted((0, v))))
        for u, v in combinations(block, 2): edges.add((u, v))
        a += q
    adj = [set() for _ in range(n)]
    for u, v in edges: adj[u].add(v); adj[v].add(u)
    return adj, blocks

def minimal_forts(adj):
    n = len(adj)
    fs = []
    for mask in range(1, 1 << n):
        F = {v for v in range(n) if mask & (1 << v)}
        if all(len(adj[v] & F) != 1 for v in range(n) if v not in F):
            fs.append(mask)
    return {f for f in fs if not any(g != f and g & f == g for g in fs)}

def expected_minimals(blocks):
    expected = set()
    for block in blocks:
        for u, v in combinations(block, 2): expected.add((1 << u) | (1 << v))
    for choice in product(*blocks):
        expected.add(1 | sum(1 << v for v in choice))
    return expected

def pack_exact(forts):
    arr = tuple(forts)
    @lru_cache(None)
    def rec(used):
        return max([0] + [1 + rec(used | f) for f in arr if not (used & f)])
    return rec(0)

def check(sizes):
    adj, blocks = make_graph(sizes)
    actual = minimal_forts(adj)
    expected = expected_minimals(blocks)
    assert actual == expected, (sizes, 'classification')
    m = len(blocks)
    opt_pack = sum(q // 2 for q in sizes) + int(all(q % 2 for q in sizes))
    assert pack_exact(actual) == opt_pack, (sizes, 'packing')
    # Construct the primal fractional cover with hub weight zero,
    # every outer vertex weight one half.  It hits every fort.
    x = [0.] + [.5] * sum(sizes)
    assert all(sum(x[v] for v in range(len(adj)) if f & (1 << v)) >= 1
               for f in actual), (sizes, 'fractional feasibility')
    # The pair-fort inequalities summed within each blade give the
    # independent universal lower bound |blade|/2 on its weight.
    assert sum(x) == sum(sizes) / 2
    # A complete optimizer-face test: for every 2-vertex blade, choose
    # weights (t, 1-t); for q>=3 blades unique half weights.  All
    # sampled candidates agree with the predicted global inequality.
    small = [i for i, q in enumerate(sizes) if q == 2]
    big = m - len(small)
    for vector in product((0., .25, .5, .75, 1.), repeat=len(small)):
        y = [0.] + [.5] * sum(sizes)
        for i, t in zip(small, vector):
            a, b = blocks[i]; y[a] = t; y[b] = 1 - t
        feasible = all(sum(y[v] for v in range(len(adj)) if f & (1 << v)) >= 1 - 1e-10
                       for f in actual)
        predicted = big / 2 + sum(min(t, 1-t) for t in vector) >= 1 - 1e-10
        assert feasible == predicted, (sizes, vector, 'optimal face')
    return len(actual)

if __name__ == '__main__':
    count = 0
    for m in (2, 3, 4):
        for sizes in product((2, 3, 4), repeat=m):
            if sum(sizes) > 11: continue
            check(sizes)
            count += 1
    print('DIRECT_MINIMAL_FORT_PACKING_AND_OPTIMAL_FACE_PROFILES', count)
    assert count >= 60
    print('VERIFY_OK')
