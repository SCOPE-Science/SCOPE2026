#!/usr/bin/env python3
"""Independent finite checks for comparison shattering of 231-avoiders.
Run: python3 verify.py (from the directory containing depth8_tree.json).
Requires only the Python standard library.
"""
import json
from itertools import permutations, combinations, product
from pathlib import Path


def avoids231(word):
    n = len(word)
    for i in range(n):
        for j in range(i + 1, n):
            if word[j] <= word[i]:
                continue
            for k in range(j + 1, n):
                if word[k] < word[i]:
                    return False
    return True


def class_and_queries(n):
    cls = [p for p in permutations(range(n)) if avoids231(p)]
    qs = list(combinations(range(n), 2))
    universe = (1 << len(cls)) - 1
    yes = []
    for a, b in qs:
        bitset = 0
        for h, p in enumerate(cls):
            if p[a] < p[b]:
                bitset |= 1 << h
        yes.append(bitset)
    return cls, qs, universe, yes


def support_counts(n):
    cls, qs, universe, yes = class_and_queries(n)
    regions_by_support = {(): (universe,)}
    totals = [1]
    while regions_by_support:
        next_layer = {}
        for support, regions in regions_by_support.items():
            for q in range((support[-1] + 1) if support else 0, len(qs)):
                new_regions = []
                for r in regions:
                    new_regions.extend((r & yes[q], r & (universe ^ yes[q])))
                if all(new_regions):
                    next_layer[support + (q,)] = tuple(new_regions)
        if next_layer:
            totals.append(len(next_layer))
        regions_by_support = next_layer
    coefficients = [1]
    for j in range(1, n):
        extended = [0] * (len(coefficients) + 1)
        for k, v in enumerate(coefficients):
            extended[k] += v
            extended[k + 1] += j * v
        coefficients = extended
    assert totals == coefficients, (n, totals, coefficients)
    return len(cls), totals


def check_tree():
    cert = json.loads((Path(__file__).parent / 'depth8_tree.json').read_text(encoding='utf-8'))
    cls, qs, full, yes = class_and_queries(7)
    assert len(cls) == 429
    assert cert['length'] == 7 and cert['depth'] == 8
    assert cert['queries_zero_based'] == [list(q) for q in qs]
    heap = cert['heap_query_indices']
    assert len(heap) == 255 and all(type(q) == int and 0 <= q < len(qs) for q in heap)
    widths = [0] * 8
    leaves = []
    for bits in product((0, 1), repeat=8):
        state, idx = full, 0
        for depth, bit in enumerate(bits):
            q = heap[idx]
            state &= yes[q] if bit else (full ^ yes[q])
            assert state != 0, (bits, depth)
            widths[depth] += 1
            idx = 2 * idx + 1 + bit
        leaves.append(state)
    assert len(leaves) == 256 and all(s for s in leaves)
    assert sum(s.bit_count() for s in leaves) <= 429
    assert all(widths[j] == 256 for j in range(8))
    assert 429 < 512  # upper bound on Littlestone dimension is eight
    print('LENGTH_SEVEN_DEPTH_EIGHT_CERTIFICATE_PASS leaves=256 hypotheses=429')


if __name__ == '__main__':
    for n in range(1, 9):
        c, counts = support_counts(n)
        print(f'SHATTERING_PROFILE_PASS n={n} hypotheses={c} coefficients={counts}')
    check_tree()
    print('AV231_COMPARISON_SHATTERING_AND_ONLINE_GAP_PASS')
