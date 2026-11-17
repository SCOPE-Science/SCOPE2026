"""Finite exact checker for the partial-whiskering two-independence theorem.

This file is self-contained and uses only the Python standard library.
The general theorem is proved mathematically; finite checks are corroboration.
"""
from collections import defaultdict, deque
from itertools import combinations
from random import Random


def graph_edges(n, mask):
    return [e for j, e in enumerate(combinations(range(n), 2)) if (mask >> j) & 1]


def connected(n, edges):
    N = [set() for _ in range(n)]
    for u, v in edges:
        N[u].add(v); N[v].add(u)
    reach = {0}; work = [0]
    while work:
        for u in N[work.pop()]:
            if u not in reach:
                reach.add(u); work.append(u)
    return len(reach) == n


def expected(n, edges, root):
    other = set(range(n)) - {root}
    E = [(u, v) for u, v in edges if u in other and v in other]
    perfect = len(E) * 2 == n - 1 and len({v for e in E for v in e}) == n - 1
    if perfect:
        return {0: 1, n - 2: 1}
    return {0: 1}


def faces(n, edges, root):
    others = [u for u in range(n) if u != root]
    N = 2 * n - 1
    neighbors = [0] * N
    for u, v in edges:
        neighbors[u] |= 1 << v; neighbors[v] |= 1 << u
    for j, u in enumerate(others):
        leaf = n + j
        neighbors[u] |= 1 << leaf
        neighbors[leaf] |= 1 << u
    out = []
    for mask in range(1 << N):
        if all((neighbors[u] & mask).bit_count() <= 1
               for u in range(N) if (mask >> u) & 1):
            out.append(mask)
    return out, others


def betti_mod_two(n, edges, root):
    F, _ = faces(n, edges, root)
    by_dim = defaultdict(list)
    for f in F:
        if f:
            by_dim[f.bit_count() - 1].append(f)
    rank = {}
    for d in sorted(by_dim, reverse=True):
        if not d:
            continue
        index = {f: i for i, f in enumerate(by_dim[d - 1])}
        pivots = {}
        for f in by_dim[d]:
            r = 0
            mask = f
            while mask:
                b = mask & -mask
                r ^= 1 << index[f ^ b]
                mask ^= b
            while r:
                j = r.bit_length() - 1
                if j not in pivots:
                    pivots[j] = r
                    break
                r ^= pivots[j]
        rank[d] = len(pivots)
    return {d: len(a) - rank.get(d, 0) - rank.get(d + 1, 0)
            for d, a in by_dim.items()
            if len(a) - rank.get(d, 0) - rank.get(d + 1, 0)}


def check_matching(n, edges, root):
    F, others = faces(n, edges, root)
    face_set = set(F)
    core_mask = (1 << n) - 1
    E = set(tuple(sorted(e)) for e in edges)
    pair = {}
    for f in F:
        core = f & core_mask
        eligible = []
        for j, u in enumerate(others):
            if not ((core >> u) & 1):
                eligible.append(n + j)
            elif not any((core >> v) & 1 for v in range(n)
                         if (min(u, v), max(u, v)) in E):
                eligible.append(n + j)
        if eligible:
            flip = 1 << eligible[0]
            g = f ^ flip
            assert g in face_set
            pair[f] = g
    # Remove the augmented empty-to-leaf pair, exposing one vertex.
    first_leaf = pair[0]
    del pair[0]
    del pair[first_leaf]
    critical = {f for f in F if f and f not in pair}
    expect_critical = {first_leaf}
    if expected(n, edges, root) != {0: 1}:
        expect_critical.add(core_mask ^ (1 << root))
    assert critical == expect_critical, (n, edges, root, critical, expect_critical)
    # Directed Hasse graph: matched upward, all other covers downward.
    indeg = {f: 0 for f in F}
    arrows = defaultdict(list)
    for g in F:
        if not g:
            continue
        sub = g
        while sub:
            bit = sub & -sub
            f = g ^ bit
            if pair.get(f) == g:
                src, dst = f, g
            else:
                src, dst = g, f
            arrows[src].append(dst); indeg[dst] += 1
            sub ^= bit
    queue = deque(f for f in F if indeg[f] == 0)
    seen = 0
    while queue:
        f = queue.popleft(); seen += 1
        for g in arrows[f]:
            indeg[g] -= 1
            if indeg[g] == 0:
                queue.append(g)
    assert seen == len(F), (n, edges, root, 'cyclic matching')
    return len(F), len(pair) // 2, len(critical)


def main():
    total, sphere_cases = 0, 0
    per_n = {}
    for n in (3, 4, 5):
        tested = 0
        for mask in range(1 << (n * (n - 1) // 2)):
            edges = graph_edges(n, mask)
            if not connected(n, edges):
                continue
            for root in range(n):
                actual = betti_mod_two(n, edges, root)
                goal = expected(n, edges, root)
                assert actual == goal, (n, edges, root, actual, goal)
                total += 1; tested += 1
                sphere_cases += goal != {0: 1}
        per_n[n] = tested
    print('Rooted connected labeled base graphs exhaustively checked:', per_n)
    print('Total exact mod-two Betti checks:', total)
    print('Noncontractible predictions among these:', sphere_cases)
    rng = Random(2605)
    checks = 0
    for n in (3, 4, 5, 6):
        for attempt in range(22):
            mask = rng.randrange(1 << (n * (n - 1) // 2))
            edges = graph_edges(n, mask)
            if not connected(n, edges):
                continue
            check_matching(n, edges, attempt % n)
            checks += 1
    # Explicit infinite-family representatives: windmills with m triangles.
    for m in range(1, 4):
        n = 2 * m + 1
        edges = []
        for j in range(m):
            u, v = 2 * j + 1, 2 * j + 2
            edges.extend([(0, u), (0, v), (u, v)])
        count, pairs, critical = check_matching(n, edges, 0)
        assert critical == 2
        print('Windmill m=', m, 'faces=', count, 'matched pairs=', pairs,
              'critical 0- and', n - 2, '-cells')
        checks += 1
    print('Complete acyclic-matching checks:', checks)
    print('All checks passed; the all-size homotopy result uses the proof, not enumeration.')


if __name__ == '__main__':
    main()
