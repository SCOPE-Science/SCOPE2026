"""Reproducible finite verification of the DNA five-mer enumeration.

Requires Python 3.9+ standard library only. The proof explains why the
certificate tests and the increasing-index clique recursion are exhaustive.
"""
from collections import Counter
from itertools import permutations, product
import json
from pathlib import Path

ALPHABET = 'ACGT'
COMPLEMENT = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
LENGTH = 5
EXPECTED = (1, 104, 1068, 3472, 4648, 2776, 720, 56)


def reverse_complement(word):
    return ''.join(COMPLEMENT[x] for x in word[::-1])


def gc_near_balance(word):
    return sum(x in 'CG' for x in word) in (2, 3)


def overlap_free(left, right):
    return all(left[:k] != right[-k:] for k in range(1, LENGTH))


def far_enough(left, right):
    return sum(a != b for a, b in zip(left, right)) >= 2


def admissible_pair(pair):
    a, b = pair
    return (all(overlap_free(x, y) for x in pair for y in pair)
            and far_enough(a, b))


def mutually_compatible(pair, other):
    return all(overlap_free(x, y) and overlap_free(y, x)
               and far_enough(x, y)
               for x in pair for y in other)


def graph():
    all_balanced = [''.join(t) for t in product(ALPHABET, repeat=LENGTH)
                    if gc_near_balance(t)]
    assert len(all_balanced) == 640
    used = set()
    pairs = []
    for w in all_balanced:
        if w in used:
            continue
        r = reverse_complement(w)
        assert w != r and gc_near_balance(r)
        used.update((w, r))
        p = (w, r)
        if admissible_pair(p):
            pairs.append(p)
    assert len(used) == 640 and len(pairs) == 104
    edges = [0] * len(pairs)
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            if mutually_compatible(pairs[i], pairs[j]):
                edges[i] |= 1 << j
                edges[j] |= 1 << i
    assert sum(x.bit_count() for x in edges) == 2136
    return pairs, edges


def enumerate_cliques(edges):
    """Each clique has a unique increasing-index listing."""
    counts = Counter()
    optima = []
    def visit(prefix, remaining):
        counts[len(prefix)] += 1
        if len(prefix) == 7:
            optima.append(frozenset(prefix))
        while remaining:
            bit = remaining & -remaining
            remaining ^= bit
            v = bit.bit_length() - 1
            visit(prefix + (v,), remaining & edges[v])
    visit((), (1 << len(edges)) - 1)
    counts_tuple = tuple(counts[i] for i in range(max(counts) + 1))
    assert counts_tuple == EXPECTED
    assert sum(counts.values()) == 12845
    assert len(optima) == 56
    return counts_tuple, optima


def symmetries():
    # The group preserving Watson-Crick complement and the set of two
    # possible GC counts is (C2 x C2) semidirect C2, of order eight.
    for groups in permutations(('AT', 'CG')):
        for flips in product((0, 1), repeat=2):
            p = {}
            for old, new, flip in zip(('AT', 'CG'), groups, flips):
                p[old[0]] = new[flip]
                p[old[1]] = new[1-flip]
            yield p


def orbit_statistics(pairs, optima):
    rep_to_index = {w: i for i, pair in enumerate(pairs) for w in pair}
    symmetries_list = list(symmetries())
    assert len(symmetries_list) == 8
    def transform(optimum, perm):
        return frozenset(rep_to_index[''.join(perm[c] for c in pairs[i][0])]
                         for i in optimum)
    unseen = set(optima)
    size_counts = Counter()
    while unseen:
        optimum = next(iter(unseen))
        orbit = {transform(optimum, perm) for perm in symmetries_list}
        assert orbit <= set(optima)
        assert orbit <= unseen
        size_counts[len(orbit)] += 1
        unseen.difference_update(orbit)
    assert dict(size_counts) == {8: 7}
    return size_counts


def main():
    base = Path(__file__).resolve().parent
    cert = json.loads((base / 'certificate.json').read_text(encoding='utf-8'))
    pairs, edges = graph()
    colors = cert['coloring']
    assert len(colors) == 104 and set(colors) == set(range(7))
    for i in range(len(edges)):
        for j in range(i + 1, len(edges)):
            if (edges[i] >> j) & 1:
                assert colors[i] != colors[j]
    witness = cert['witness_indices']
    assert len(witness) == 7 and len(set(witness)) == 7
    assert all(0 <= i < 104 for i in witness)
    assert all((edges[i] >> j) & 1
               for s, i in enumerate(witness) for j in witness[s + 1:])
    words = [w for i in witness for w in pairs[i]]
    assert len(set(words)) == 14
    assert all(gc_near_balance(w) for w in words)
    assert all(reverse_complement(w) in words for w in words)
    assert all(overlap_free(x, y) for x in words for y in words)
    assert all(far_enough(x, y) for x in words for y in words if x != y)
    assert [pairs[i][0] for i in witness] == cert['witness_representatives']
    counts, optima = enumerate_cliques(edges)
    orbits = orbit_statistics(pairs, optima)
    print('PASS: 640 near-balanced words / 320 reverse-complement pairs')
    print('PASS: 104 individually admissible pairs / 1068 compatibility edges')
    print('PASS: 7-color upper certificate and 7-pair lower witness')
    print('PASS: size enumerator', counts)
    print('PASS: 56 optimal labeled codebooks, 7 orbits of size 8')
    print('PASS: maximum codebook size = 14')


if __name__ == '__main__':
    main()
