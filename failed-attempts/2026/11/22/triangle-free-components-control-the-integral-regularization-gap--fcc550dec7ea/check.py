"""Exact GF(2) checker of the regular/nonregular first path-homology gap.

Uses all allowed length-two walks directly, not the theorem's generating-set
reduction. Intended only as a finite consistency check, not an infinite proof.
"""
from itertools import combinations


def rank_bitvectors(vectors):
    pivots = {}
    for vec in vectors:
        x = vec
        while x:
            pivot = x.bit_length() - 1
            if pivot in pivots:
                x ^= pivots[pivot]
            else:
                pivots[pivot] = x
                break
    return len(pivots)


def count_components(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    seen = set()
    count = 0
    special = 0
    for root in range(n):
        if root in seen:
            continue
        count += 1
        todo = [root]
        comp = {root}
        seen.add(root)
        while todo:
            v = todo.pop()
            for w in adj[v] - seen:
                seen.add(w)
                comp.add(w)
                todo.append(w)
        if any(adj[v] for v in comp):
            triangle = any(u in adj[v] and w in adj[u] and w in adj[v]
                           for v in comp for u in adj[v] for w in adj[v] if u != w)
            special += int(not triangle)
    return count, special


def homology_one_mod_two(n, edges, regular):
    arcs = {(u, v) for u, v in edges} | {(v, u) for u, v in edges}
    columns = []
    forbidden = []
    for u, v in sorted(arcs):
        for w in range(n):
            if (v, w) not in arcs:
                continue
            full = 0
            forb = 0
            for a, b in ((v, w), (u, w), (u, v)):
                if regular and a == b:
                    continue
                bit = 1 << (n * a + b)
                full ^= bit
                if (a, b) not in arcs:
                    forb ^= bit
            columns.append(full)
            forbidden.append(forb)
    component_count, _ = count_components(n, edges)
    rank_d1 = n - component_count
    rank_d2 = rank_bitvectors(columns) - rank_bitvectors(forbidden)
    return len(arcs) - rank_d1 - rank_d2


def main():
    tests = 0
    samples = {}
    for n in range(1, 6):
        pairs = list(combinations(range(n), 2))
        for mask in range(1 << len(pairs)):
            edges = {e for i, e in enumerate(pairs) if (mask >> i) & 1}
            _, expected = count_components(n, edges)
            nr = homology_one_mod_two(n, edges, regular=False)
            reg = homology_one_mod_two(n, edges, regular=True)
            assert nr - reg == expected, (n, mask, nr, reg, expected)
            tests += 1
            if n == 5 and mask in (0, 1, 31, 1023):
                samples[mask] = dict(nonregular=nr, regular=reg, discrepancy=expected)
    for name, n, edges in [
        ('two disconnected triangles', 6, {(0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5)}),
        ('disconnected triangles and edges', 7, {(0, 1), (1, 2), (0, 2), (3, 4), (5, 6)}),
        ('cycle six', 6, {(i, (i+1)%6) for i in range(6)}),
        ('one triangle and one pendant edge', 4, {(0, 1), (1, 2), (0, 2), (2, 3)})
    ]:
        _, expected = count_components(n, edges)
        nr = homology_one_mod_two(n, edges, regular=False)
        reg = homology_one_mod_two(n, edges, regular=True)
        assert nr - reg == expected, (name, nr, reg, expected)
        samples[name] = dict(nonregular=nr, regular=reg, discrepancy=expected)
        tests += 1
    print(f'PASS: {tests} undirected simple graphs; each compared by independent GF(2) allowed-path chain matrices.')
    for key, value in samples.items():
        print(f'  {key}: {value}')
    print('LIMIT: finite field dimensions only; proof handles all finite graphs integrally and naturality.')


if __name__ == '__main__':
    main()
