#!/usr/bin/env python3
"""Exact finite verification of set-partition deletion-code threshold.

Run: python3 verify.py
Only Python's standard library and the companion CERTIFICATES.json are needed.
The search explores all compatible subsets subject to a provably valid
proper-color upper bound; no floating point is used.
"""
from __future__ import annotations
import json
from pathlib import Path
from functools import lru_cache


def canonical(seq):
    seen = {}
    result = []
    for v in seq:
        if v not in seen:
            seen[v] = len(seen)
        result.append(seen[v])
    return tuple(result)


@lru_cache(None)
def growth_words(n):
    if n == 0:
        return ((),)
    return tuple(s + (j,) for s in growth_words(n - 1)
                 for j in range(max(s, default=-1) + 2))


def block_words(n):
    # Independent generation by adding the largest ground-set element
    blocks = [()]
    for i in range(n):
        nxt = []
        for p in blocks:
            nxt.append(p + ((i,),))
            for j in range(len(p)):
                q = list(p)
                q[j] += (i,)
                nxt.append(tuple(q))
        blocks = nxt
    result = set()
    for p in blocks:
        word = [None] * n
        for label, b in enumerate(p):
            for i in b:
                word[i] = label
        result.add(tuple(word))
    return result


def shadows(n):
    src = growth_words(n)
    out = growth_words(n - 1)
    inverse_index = {y: i for i, y in enumerate(out)}
    result = []
    for x in src:
        result.append(frozenset(inverse_index[canonical(x[:i] + x[i + 1:])]
                                for i in range(n)))
    return src, out, result


def independent_compatible_graph(sh):
    # Edges mean DISJOINT one-deletion shadows, i.e. simultaneously codeable.
    return tuple(sum(1 << j for j in range(len(sh))
                     if j != i and not sh[i].intersection(sh[j]))
                 for i in range(len(sh)))


def max_code_size(neighbor_masks):
    # Exact maximum clique algorithm using a proper greedy coloring bound.
    # At every recursive node, greedy coloring bounds the clique number of
    # the remaining candidate graph. Every possible next vertex is branched.
    graph = neighbor_masks
    seen_nodes = 0
    best_size = 0

    def color_order(P):
        order, colors = [], []
        color = 0
        while P:
            color += 1
            available = P
            while available:
                vbit = available & -available
                v = vbit.bit_length() - 1
                order.append(v)
                colors.append(color)
                P &= ~vbit
                available &= ~vbit
                available &= ~graph[v]
        return order, colors

    def dfs(P, selected):
        nonlocal seen_nodes, best_size
        seen_nodes += 1
        if not P:
            best_size = max(best_size, selected)
            return
        order, colors = color_order(P)
        for k in range(len(order) - 1, -1, -1):
            if selected + colors[k] <= best_size:
                return
            v = order[k]
            vbit = 1 << v
            if P & vbit:
                dfs(P & graph[v], selected + 1)
                P &= ~vbit

    dfs((1 << len(graph)) - 1, 0)
    return best_size, seen_nodes


def independently_reconstruct_incidence(src, out):
    # Insert a new element into every slot of every received partition.
    # Allow all existing block choices or one new singleton block.
    by_source = {s: set() for s in src}
    for y_idx, y in enumerate(out):
        for pos in range(len(y) + 1):
            for label in range(max(y, default=-1) + 2):
                candidate = canonical(y[:pos] + (label,) + y[pos:])
                assert candidate in by_source
                by_source[candidate].add(y_idx)
    return by_source


def main():
    cert = json.loads(Path(__file__).with_name('CERTIFICATES.json').read_text(encoding='utf-8'))
    assert [len(growth_words(n)) for n in range(1, 7)] == [1, 2, 5, 15, 52, 203]
    for n in (4, 5, 6):
        assert set(growth_words(n)) == block_words(n)
    expected = {2: 1, 3: 2, 4: 3, 5: 6, 6: 14}
    for n, answer in expected.items():
        src, out, sh = shadows(n)
        assert len(set(sh)) <= len(src)
        if n == 6:
            inverse = independently_reconstruct_incidence(src, out)
            assert all(inverse[x] == set(sh[i]) for i, x in enumerate(src))
        best, nodes = max_code_size(independent_compatible_graph(sh))
        assert best == answer, (n, best)
        print('MAX', n, 'source_count', len(src), 'output_count', len(out),
              'capacity', best, 'nodes', nodes)
        if n == 4:
            cover = [0] * len(out)
            assert cert['cover_scale_4'] == 1
            for i, v in cert['cover_4']:
                cover[i] = v
            assert sum(cover) == 3
            assert all(sum(cover[y] for y in S) >= 1 for S in sh)
            print('COVER4', sum(cover), '/', 1)
        if n == 5:
            weight = [0] * len(out)
            assert cert['cover_scale_5'] == 4
            for index, numerator in cert['cover_5']:
                assert 0 <= index < len(out) and numerator >= 0
                assert weight[index] == 0
                weight[index] = numerator
            assert sum(weight) == 25
            assert all(sum(weight[y] for y in S) >= 4 for S in sh)
            print('COVER5', sum(weight), '/', 4)
        if n == 6:
            code = [tuple(int(c) for c in s) for s in cert['code_6']]
            assert len(code) == 14 and len(set(code)) == 14
            ids = {v: i for i, v in enumerate(src)}
            assert all(x in ids for x in code)
            used = set()
            for x in code:
                assert not used.intersection(sh[ids[x]])
                used.update(sh[ids[x]])
            print('CODE6', len(code), 'covered_outputs', len(used))
            alpha = [0] * len(src)
            assert cert['fractional_scale_6'] == 64
            for index, numerator in cert['fractional_6']:
                assert 0 <= index < len(src) and 0 < numerator <= 64
                assert alpha[index] == 0
                alpha[index] = numerator
            assert sum(alpha) == 972
            for y in range(len(out)):
                assert sum(alpha[i] for i, S in enumerate(sh) if y in S) <= 64
            assert sum(alpha) > 15 * 64
            print('FRACTIONAL6', sum(alpha), '/', 64, 'support', sum(x > 0 for x in alpha))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
