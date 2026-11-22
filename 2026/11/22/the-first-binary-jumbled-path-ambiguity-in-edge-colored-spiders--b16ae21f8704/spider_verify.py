#!/usr/bin/env python3
"""Exact finite certificate for binary path-composition reconstruction of spiders.

Use: python3 spider_verify.py
Standard library only.  Every edge coloring is considered modulo only
permutations of equal-length arms; the two symbol names remain fixed.
"""
from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, product
from math import comb


def shapes(edges, arms, smallest=1):
    if arms == 0:
        if edges == 0:
            yield ()
        return
    for first in range(smallest, edges // arms + 1):
        for rest in shapes(edges - first, arms - 1, first):
            yield (first,) + rest


def shape_colorings(lengths):
    """One representative of every coloring modulo tree automorphisms."""
    choices = [list(product((0, 1), repeat=m)) for m in lengths]
    for arms in product(*choices):
        if arms == tuple(sorted(arms, key=lambda a: (len(a), a))):
            yield arms


def via_segments(arms):
    """Compute all path compositions from within-arm and across-arm segments."""
    counts = Counter()
    for arm in arms:
        for start in range(len(arm)):
            ones = 0
            for end in range(start, len(arm)):
                ones += arm[end]
                counts[(end - start + 1, ones)] += 1
    for i, j in combinations(range(len(arms)), 2):
        a, b = arms[i], arms[j]
        for h in range(1, len(a) + 1):
            for k in range(1, len(b) + 1):
                counts[(h + k, sum(a[:h]) + sum(b[:k]))] += 1
    return tuple(sorted(counts.items()))


def via_vertex_pairs(arms):
    """Independent generic graph traversal, one unique path per vertex pair."""
    graph = [[]]
    for arm in arms:
        previous = 0
        for bit in arm:
            vertex = len(graph)
            graph.append([])
            graph[previous].append((vertex, bit))
            graph[vertex].append((previous, bit))
            previous = vertex
    result = Counter()
    for source in range(len(graph)):
        stack = [(source, -1, 0, 0)]
        while stack:
            here, parent, distance, ones = stack.pop()
            if here > source:
                result[(distance, ones)] += 1
            for neighbor, bit in graph[here]:
                if neighbor != parent:
                    stack.append((neighbor, here, distance + 1, ones + bit))
    return tuple(sorted(result.items()))


def burnside_orbit_count(lengths):
    groups = Counter(lengths)
    ans = 1
    for length, multiplicity in groups.items():
        ans *= comb(2**length + multiplicity - 1, multiplicity)
    return ans


EXPECTED = {
    3: (1, 4, 4, 0),
    4: (2, 17, 17, 0),
    5: (4, 66, 66, 0),
    6: (7, 221, 221, 0),
    7: (11, 688, 688, 0),
    8: (17, 2034, 2034, 0),
    9: (25, 5788, 5786, 2),
}
PAIR_1 = (
    ((0, 1), (1, 0, 1), (0, 0, 1, 0)),
    ((1, 0), (0, 0, 1), (0, 1, 0, 1)),
)
PAIR_2 = (
    ((0, 1), (1, 1, 0), (1, 0, 1, 0)),
    ((1, 0), (0, 1, 0), (1, 1, 0, 1)),
)
EXPECTED_PAIRS = {frozenset(PAIR_1), frozenset(PAIR_2)}


def main():
    exceptional = set()
    for edges in range(3, 10):
        shape_count = coloring_count = profile_count = bad_count = 0
        for arm_count in range(3, edges + 1):
            for lengths in shapes(edges, arm_count):
                shape_count += 1
                observed = defaultdict(list)
                local = 0
                for arms in shape_colorings(lengths):
                    # Two algorithms agree for *every* canonical coloring.
                    sig = via_segments(arms)
                    assert sig == via_vertex_pairs(arms), (lengths, arms)
                    observed[sig].append(arms)
                    local += 1
                assert local == burnside_orbit_count(lengths), lengths
                coloring_count += local
                profile_count += len(observed)
                for classes in observed.values():
                    if len(classes) > 1:
                        bad_count += 1
                        assert len(classes) == 2
                        assert lengths == (2, 3, 4)
                        exceptional.add(frozenset(classes))
        got = shape_count, coloring_count, profile_count, bad_count
        assert got == EXPECTED[edges], (edges, got)
    assert exceptional == EXPECTED_PAIRS, exceptional
    assert via_segments(PAIR_1[0]) == via_segments(PAIR_1[1])
    assert via_segments(PAIR_2[0]) == via_segments(PAIR_2[1])
    assert sum(count for _, count in via_segments(PAIR_1[0])) == comb(10, 2)
    # The two collisions are exchanged by the global color complement.
    flip = lambda w: tuple(tuple(1 - b for b in arm) for arm in w)
    assert {flip(w) for w in PAIR_1} == set(PAIR_2)
    print('VERIFY_OK exhaustive_binary_spiders_edges_3_through_9; '
          '25_nine_edge_shapes; 5788_labeling_orbits; '
          '5786_topology_scoped_profiles; exactly_2_doubleton_fibers')


if __name__ == '__main__':
    main()
