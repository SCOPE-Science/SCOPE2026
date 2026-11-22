"""Independent finite corroboration of a universal-cycle transition theorem.

Run with Python 3.10+. No third-party packages or network needed.
"""
from collections import defaultdict
from math import comb


def rotations_min(x, n):
    mask = (1 << n) - 1
    return min(((x << i) & mask) | (x >> (n-i)) for i in range(n))


def bridge_indices(n, k):
    # Build the distinct-weight necklace connection multigraph directly.
    edges = []
    neighbors = defaultdict(list)
    labels = {rotations_min(x, n) for x in range(1 << n) if x.bit_count() <= k}
    for v in range(1 << (n-1)):
        if v.bit_count() >= k:
            continue
        lo = rotations_min(v, n)
        hi = rotations_min((1 << (n-1)) | v, n)
        i = len(edges)
        edges.append((lo, hi, v))
        neighbors[lo].append((hi, i))
        neighbors[hi].append((lo, i))
    seen, low, bridges = {}, {}, set()
    t = 0
    def visit(x, parent_edge):
        nonlocal t
        seen[x] = low[x] = t
        t += 1
        for y, eid in neighbors[x]:
            if eid == parent_edge:
                continue
            if y not in seen:
                visit(y, eid)
                low[x] = min(low[x], low[y])
                if low[y] > seen[x]:
                    bridges.add(edges[eid][2])
            else:
                low[x] = min(low[x], seen[y])
    for x in labels:
        if x not in seen:
            visit(x, -1)
    assert len(seen) == len(labels), (n, k, 'disconnected')
    return bridges


def predicted_bridge_indices(n, k):
    expected = {0}
    if k >= 2 and n % k == 0:
        d = n // k
        v = ('0' * (d-1)) + (('1' + '0' * (d-1)) * (k-1))
        assert len(v) == n-1
        expected.add(int(v, 2))
    return expected


def exhaustive_next_factors(n, k):
    # Independently test each potential transition by contracting a forced
    # consecutive edge pair in the directed overlap graph. A compatible
    # pair belongs to an Euler circuit iff the contracted balanced graph
    # is strongly connected on its nonzero-degree vertices.
    mask = (1 << (n-1)) - 1
    edges = {x: ((x >> 1) & mask, x & mask)
             for x in range(1 << n) if x.bit_count() <= k}
    possible = set()
    absent = set()
    for word in range(1 << (n+1)):
        a, b = word >> 1, word & ((1 << n) - 1)
        if a not in edges or b not in edges:
            continue
        possible.add(word)
        if a == b:
            absent.add(word)
            continue
        adj, rev = defaultdict(list), defaultdict(list)
        active = set()
        for label, (src, dst) in edges.items():
            if label == a or label == b:
                continue
            adj[src].append(dst)
            rev[dst].append(src)
            active.update((src, dst))
        src, dst = edges[a][0], edges[b][1]
        adj[src].append(dst)
        rev[dst].append(src)
        active.update((src, dst))
        root = next(iter(active))
        def reachable(graph):
            seen = {root}
            queue = [root]
            for x in queue:
                for y in graph[x]:
                    if y not in seen:
                        seen.add(y)
                        queue.append(y)
            return len(seen) == len(active)
        if not reachable(adj) or not reachable(rev):
            absent.add(word)
    return possible, absent


def predicted_absent(n, k):
    vs = predicted_bridge_indices(n, k)
    return {w for v in vs for w in ((v << 1), ((1 << n) | (v << 1) | 1))}


def main():
    tree_checks = 0
    for n in range(1, 14):
        for k in range(1, min(n, 6) + 1):
            actual = bridge_indices(n, k)
            expect = predicted_bridge_indices(n, k)
            assert actual == expect, ('bridge mismatch', n, k, actual, expect)
            tree_checks += 1
    contraction_checks = 0
    for n in range(1, 10):
        for k in range(1, n+1):
            all_candidates, absent = exhaustive_next_factors(n, k)
            prediction = predicted_absent(n, k)
            assert absent == prediction, ('next-window mismatch', n, k, absent, prediction)
            expected_candidates = sum(comb(n+1,j) for j in range(k+1)) + comb(n-1,k-1) if n >= 2 else 4
            assert len(all_candidates) == expected_candidates, (n,k, len(all_candidates), expected_candidates)
            contraction_checks += 1
    print(f'BRIDGE_CHECKS_OK {tree_checks}')
    print(f'EULER_CONTRACTION_CHECKS_OK {contraction_checks}')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
