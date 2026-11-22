"""Exact, standalone verification of the signed Coxeter-graph dimer spectrum.

Run with CPython 3.9+ (no dependencies): python verify.py
Graph is specified solely by Fano-plane triples in sorted order.
"""

from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import gcd


def graph():
    lines = {tuple(sorted((j % 7, (j + 1) % 7, (j + 3) % 7)))
             for j in range(7)}
    vertices = sorted(set(combinations(range(7), 3)) - lines)
    assert len(vertices) == 28 and len(lines) == 7
    edges = [(i, j) for i in range(28) for j in range(i + 1, 28)
             if set(vertices[i]).isdisjoint(vertices[j])]
    adj = [[] for _ in vertices]
    for k, (u, v) in enumerate(edges):
        adj[u].append((v, k))
        adj[v].append((u, k))
    assert len(edges) == 42 and all(len(a) == 3 for a in adj)
    return vertices, edges, adj


def matching_list(adj):
    out = []
    def visit(remaining, edge_bits):
        if not remaining:
            out.append(edge_bits)
            return
        bit = remaining & -remaining
        u = bit.bit_length() - 1
        remainder = remaining ^ bit
        for v, e in adj[u]:
            if (remainder >> v) & 1:
                visit(remainder ^ (1 << v), edge_bits | (1 << e))
    visit((1 << len(adj)) - 1, 0)
    assert len(out) == len(set(out)) == 84
    for m in out:
        assert m.bit_count() == 14
        assert all(sum((m >> e) & 1 for _, e in adj[u]) == 1
                   for u in range(28))
    return out


def signed_counts_by_deletion(edges, adj):
    """Independent vertex-deletion recurrence, never using matching_list."""
    neighbors = [sum(1 << v for v, _ in adj[u]) for u in range(28)]
    @lru_cache(None)
    def count(vertices):
        if vertices == 0:
            return 1
        ubit = vertices & -vertices
        u = ubit.bit_length() - 1
        rest = vertices ^ ubit
        result = 0
        candidates = neighbors[u] & rest
        while candidates:
            vbit = candidates & -candidates
            result += count(rest ^ vbit)
            candidates ^= vbit
        return result

    all_vertices = (1 << 28) - 1
    def edge_ends(e):
        u, v = edges[e]
        return (1 << u) | (1 << v)
    assert count(all_vertices) == 84
    one = Counter()
    for e in range(42):
        one[count(all_vertices ^ edge_ends(e))] += 1
    assert one == Counter({28: 42}), one
    two = Counter()
    pair_values = {}
    for e, f in combinations(range(42), 2):
        ends_e = edge_ends(e)
        ends_f = edge_ends(f)
        value = (count(all_vertices ^ (ends_e | ends_f))
                 if not (ends_e & ends_f) else 0)
        two[value] += 1
        pair_values[(e, f)] = value
        assert value % 2 == 0
    assert two == Counter({0: 84, 4: 21, 6: 168, 8: 168,
                           10: 84, 12: 168, 14: 168}), two
    return one, two, pair_values


def tree_chords(adj, edges):
    visited = {0}
    queue = [0]
    tree = []
    for u in queue:
        for v, edge_id in sorted(adj[u]):
            if v not in visited:
                visited.add(v)
                queue.append(v)
                tree.append(edge_id)
    assert len(visited) == 28 and len(tree) == 27
    tree_ids = set(tree)
    chords = [k for k in range(len(edges)) if k not in tree_ids]
    assert len(chords) == 15
    return chords


def transform(a):
    a = list(a)
    step = 1
    while step < len(a):
        for start in range(0, len(a), 2 * step):
            for j in range(start, start + step):
                x, y = a[j], a[j + step]
                a[j], a[j + step] = x + y, x - y
        step *= 2
    return a


def main():
    vertices, edges, adj = graph()
    matching_masks = matching_list(adj)
    one, two, pair_values = signed_counts_by_deletion(edges, adj)
    # Check these independent methods give identical 1- and 2-edge counts.
    for e in range(42):
        assert sum((m >> e) & 1 for m in matching_masks) == 28
    for e, f in combinations(range(42), 2):
        raw = sum(((m >> e) & 1) & ((m >> f) & 1)
                  for m in matching_masks)
        assert raw == pair_values[(e, f)], (e, f, raw, pair_values[(e, f)])
    chords = tree_chords(adj, edges)
    reduced = [sum(((m >> k) & 1) << i for i, k in enumerate(chords))
               for m in matching_masks]
    assert len(set(reduced)) == 84
    kernel = [0] * (1 << 15)
    for m in reduced:
        kernel[m] += 1
    walsh = transform(kernel)
    assert all(v % 8 == 4 for v in walsh)
    assert 0 not in walsh
    assert sum(v * v for v in walsh) == (1 << 15) * 84
    expected = {-84: 1, -36: 14, -28: 150, -20: 945, -12: 4774,
                -4: 10500, 4: 10500, 12: 4774, 20: 945,
                28: 150, 36: 14, 84: 1}
    assert Counter(walsh) == Counter(expected)
    # Independent direct signed evaluation at EVERY reduced frequency.
    for s, value in enumerate(walsh):
        direct = sum(1 - 2 * ((s & m).bit_count() % 2) for m in reduced)
        assert value == direct, (s, value, direct)
    assert gcd(*walsh) == 4
    print('PASS')
    print('Coxeter graph: vertices=28 edges=42 matchings=84')
    print('single-edge matching count:', sorted(one.items()))
    print('two-edge matching count histogram:', sorted(two.items()))
    print('chord edge indices:', chords)
    print('distinct gauge signings: 32768')
    print('signed Walsh histogram:', sorted(Counter(walsh).items()))
    print('all Walsh coefficients congruent to 4 (mod 8)')
    print('full Walsh convolution rank: 2^42')
    print('minimum absolute multiplier: 4')
    print('maximum absolute multiplier: 84')
    print('exact l2 condition number: 21')
    print('independent direct Fourier comparison: 32768/32768')


if __name__ == '__main__':
    main()
