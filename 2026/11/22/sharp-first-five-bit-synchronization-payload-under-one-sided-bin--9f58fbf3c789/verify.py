#!/usr/bin/env python3
"""Exact finite search for non-overlapping codes in words avoiding 11.

Usage: python3 verify.py
Requires only Python 3.10+ standard library. The search is finite, uses exact
integer bitsets, and proves upper bounds by proper greedy coloring at every
branch. Every reported lower bound is a directly checked codebook.
"""
import json
from itertools import product
from pathlib import Path

EXPECTED = [None, 2, 1, 1, 1, 1, 1, 2, 2, 3, 5, 7, 9, 14, 20, 30, 42]
EXPECTED_MARKER = 24

def fibonacci_words(n):
    out = ['']
    for _ in range(n):
        out = [w + a for w in out for a in '01' if not (w.endswith('1') and a == '1')]
    return out

def suffix_equals_prefix(a, b):
    return any(a[-length:] == b[:length] for length in range(1, len(a)))

def self_unbordered(w):
    return not suffix_equals_prefix(w, w)

def eligible_words(n):
    return [w for w in fibonacci_words(n) if self_unbordered(w)]

def graph(words):
    adjacency = [0] * len(words)
    for i, a in enumerate(words):
        for j in range(i + 1, len(words)):
            b = words[j]
            if not suffix_equals_prefix(a, b) and not suffix_equals_prefix(b, a):
                adjacency[i] |= 1 << j
                adjacency[j] |= 1 << i
    return adjacency

def max_clique(adjacency):
    # Each color class is independent in the compatible-pair graph.
    # A clique in the remaining search set has size at most its color count.
    size = len(adjacency)
    best = []
    visited = 0
    def visit(chosen, possible):
        nonlocal best, visited
        visited += 1
        if not possible:
            if len(chosen) > len(best):
                best = chosen[:]
            return
        vertices = []
        colors = []
        uncolored = possible
        color = 0
        while uncolored:
            color += 1
            avail = uncolored
            while avail:
                bit = avail & -avail
                v = bit.bit_length() - 1
                vertices.append(v)
                colors.append(color)
                uncolored ^= bit
                avail ^= bit
                avail &= ~adjacency[v]
        # At iteration i, possible is a subset of vertices[0:i+1].
        for i in range(len(vertices) - 1, -1, -1):
            if len(chosen) + colors[i] <= len(best):
                return
            v = vertices[i]
            visit(chosen + [v], possible & adjacency[v])
            possible &= ~(1 << v)
    visit([], (1 << size) - 1)
    return best, visited

def validate_codebook(words):
    assert len(words) == len(set(words))
    if not words:
        return
    n = len(words[0])
    assert all(len(w) == n and '11' not in w for w in words)
    for a in words:
        for b in words:
            assert not suffix_equals_prefix(a, b), (a, b)

def check_independent_graph(n, words, adjacency):
    # Alternative integer-mask prefix/suffix comparison, independent of the
    # string slicing implementation above. Compare every pair.
    mask = (1 << n) - 1
    as_int = [int(w, 2) for w in words]
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            x, y = as_int[i], as_int[j]
            overlap = any(
                (x & ((1 << k) - 1)) == (y >> (n - k))
                or (y & ((1 << k) - 1)) == (x >> (n - k))
                for k in range(1, n)
            )
            assert bool(adjacency[i] & (1 << j)) == (not overlap), (n, i, j)
    assert all(not ((adjacency[i] >> i) & 1) for i in range(len(words)))

def marker_family_size(n, words):
    # Reversal of the binary Chee--Levenshtein zero-marker construction,
    # intersected with the language avoiding 11.
    candidates = []
    for k in range(2, n - 1):
        code = [w for w in words if w.startswith('1') and w[-k:] == '0' * k
                and w[-k - 1] == '1' and ('0' * k not in w[:-k])]
        validate_codebook(code)
        candidates.append((len(code), k))
    return max(candidates, default=(0, 0))

def main():
    cert = {'definition': 'binary words avoiding adjacent 11; all proper prefix-suffix overlaps prohibited', 'table': [], 'codebooks': {}}
    for n in range(1, 17):
        words = eligible_words(n)
        assert words == sorted(words)
        if n <= 10:
            assert words == [''.join(p) for p in product('01', repeat=n)
                             if '11' not in ''.join(p) and self_unbordered(''.join(p))]
        edges = graph(words)
        check_independent_graph(n, words, edges)
        ids, nodes = max_clique(edges)
        code = [words[i] for i in ids]
        validate_codebook(code)
        assert len(code) == EXPECTED[n], (n, len(code), EXPECTED[n])
        assert all((edges[ids[i]] >> ids[j]) & 1 for i in range(len(ids)) for j in range(i + 1, len(ids)))
        row = {'n': n, 'admissible': len(fibonacci_words(n)),
               'unbordered': len(words), 'capacity': len(code),
               'search_nodes': nodes}
        if n >= 4:
            size, k = marker_family_size(n, fibonacci_words(n))
            row['marker_max'] = size
            row['marker_k'] = k
        cert['table'].append(row)
        cert['codebooks'][str(n)] = sorted(code)
        print('n=%d sources=%d eligible=%d max=%d nodes=%d' %
              (n, row['admissible'], len(words), len(code), nodes), flush=True)
    assert cert['table'][-1]['marker_max'] == EXPECTED_MARKER
    data_file = Path(__file__).with_name('certificates.json')
    if data_file.exists():
        existing = json.loads(data_file.read_text('utf-8'))
        assert existing == cert, 'Published certificate differs from recomputed data'
    else:
        data_file.write_text(json.dumps(cert, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
