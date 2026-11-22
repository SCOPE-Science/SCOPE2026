#!/usr/bin/env python3
"""Exact exhaustive census of uniform-start 1-WL on 2-connected outerplanar graphs.

Standard-library only. Run: python3 verify.py
The graph encoding has a Hamilton cycle (0,1,...,n-1,0) and a set
of noncrossing diagonals (chords). Chord masks use the lexicographically
ordered list of non-boundary pairs (i,j), i<j.
"""
from collections import defaultdict
from itertools import combinations


def enumerate_unlabelled(n):
    chords = [(a, b) for a in range(n) for b in range(a + 1, n)
              if b - a > 1 and not (a == 0 and b == n - 1)]
    pos = {e: i for i, e in enumerate(chords)}
    crosses = [0 for _ in chords]
    for i, (a, b) in enumerate(chords):
        for j, (c, d) in enumerate(chords):
            if (a < c < b < d) or (c < a < d < b):
                crosses[i] |= 1 << j
    # Every automorphism of the unique Hamiltonian cycle is dihedral.
    transforms = []
    for shift in range(n):
        for sign in (1, -1):
            transforms.append(tuple(1 << pos[tuple(sorted(
                ((shift + sign * a) % n, (shift + sign * b) % n)))]
                for a, b in chords))

    representatives = []
    raw_count = 0

    def is_canonical(mask):
        for transform in transforms[1:]:
            transported, rest = 0, mask
            while rest:
                low = rest & -rest
                transported |= transform[low.bit_length() - 1]
                rest ^= low
            if transported < mask:
                return False
        return True

    def visit(i, mask, forbidden):
        nonlocal raw_count
        if i == len(chords):
            raw_count += 1
            if is_canonical(mask):
                representatives.append(mask)
            return
        visit(i + 1, mask, forbidden)
        if not (forbidden & (1 << i)):
            visit(i + 1, mask | (1 << i), forbidden | crosses[i])

    visit(0, 0, 0)
    return chords, representatives, raw_count


def adjacencies(n, chords, masks):
    result = []
    for mask in masks:
        adj = [(1 << ((v + n - 1) % n)) | (1 << ((v + 1) % n))
               for v in range(n)]
        for j, (a, b) in enumerate(chords):
            if mask & (1 << j):
                adj[a] |= 1 << b
                adj[b] |= 1 << a
        result.append(tuple(adj))
    return result


def exact_color_refinement(n, family):
    # Simultaneous normalization on the disjoint union of every representative.
    # At each round all colors are exact dictionary keys, never randomized hashes.
    # The key consists of the old color and a SORTED multiset of neighbor colors.
    colors = [[0] * n for _ in family]
    for round_index in range(3 * n + 10):
        keys = []
        for graph, previous in zip(family, colors):
            for v in range(n):
                neighbors = tuple(sorted(previous[w] for w in range(n)
                                         if graph[v] & (1 << w)))
                keys.append((previous[v], neighbors))
        code = {key: i for i, key in enumerate(sorted(set(keys)))}
        next_colors = [[code[keys[graph_index * n + v]]
                        for v in range(n)]
                       for graph_index in range(len(family))]
        if next_colors == colors:
            return [tuple(sorted(row)) for row in colors], round_index
        colors = next_colors
    raise AssertionError('Refinement did not stabilize in the explicit bound')


def direct_pair_check(n, graph_a, graph_b):
    # Independent two-graph direct refinement. Equal histograms are checked
    # at every round, not just by the all-graph enumeration signature.
    colors = [[0] * n, [0] * n]
    for _ in range(3 * n + 10):
        keys = []
        for graph, prior in zip((graph_a, graph_b), colors):
            keys += [(prior[v], tuple(sorted(prior[w] for w in range(n)
                       if graph[v] & (1 << w)))) for v in range(n)]
        codes = {x: i for i, x in enumerate(sorted(set(keys)))}
        new = [[codes[x] for x in keys[:n]],
               [codes[x] for x in keys[n:]]]
        if sorted(new[0]) != sorted(new[1]):
            return False
        if new == colors:
            return True
        colors = new
    raise AssertionError('Pair refinement bound')


def main():
    expected_types = [1, 2, 3, 9, 20, 75, 262, 1117]
    expected_raw = [1, 3, 11, 45, 197, 903, 4279, 20793]
    expected_pairs = [0, 0, 0, 0, 0, 0, 0, 5]
    found_pairs = None
    for n in range(3, 11):
        chords, representatives, raw = enumerate_unlabelled(n)
        graphs = adjacencies(n, chords, representatives)
        signatures, rounds = exact_color_refinement(n, graphs)
        grouping = defaultdict(list)
        for mask, sig in zip(representatives, signatures):
            grouping[sig].append(mask)
        collisions = [sorted(v) for v in grouping.values() if len(v) > 1]
        collisions.sort()
        count = sum(len(v) * (len(v) - 1) // 2 for v in collisions)
        assert (raw, len(representatives), count) == (
            expected_raw[n - 3], expected_types[n - 3], expected_pairs[n - 3]), n
        assert len(set(representatives)) == len(representatives)
        print(f'ORDER_{n} RAW_{raw} ISOMORPHISM_TYPES_{len(representatives)} '
              f'CR_CLASSES_{len(grouping)} COLLISION_PAIRS_{count} PASS')
        if n == 10:
            assert len(collisions) == 5 and all(len(v) == 2 for v in collisions)
            found_pairs = collisions
            by_mask = dict(zip(representatives, graphs))
            for j, (left, right) in enumerate(collisions, 1):
                assert left != right
                assert direct_pair_check(n, by_mask[left], by_mask[right])
                assert not any(left == right for _ in (0,))
                cl = [list(c) for k, c in enumerate(chords) if left >> k & 1]
                cr = [list(c) for k, c in enumerate(chords) if right >> k & 1]
                print(f'PAIR_{j} {left:#x} {right:#x} CHORDS {cl} | {cr} PASS')
    assert found_pairs is not None
    print('EXACT_ENUMERATION_AND_FIVE_PAIR_CLASSIFICATION_PASS')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
