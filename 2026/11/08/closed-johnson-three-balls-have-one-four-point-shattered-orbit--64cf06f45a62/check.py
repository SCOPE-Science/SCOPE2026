#!/usr/bin/env python3
"""Finite isomorphism-type certificate for radius-one Johnson 3-set balls.
Pure standard-library Python 3. No external data or dependencies.
"""
from itertools import combinations, permutations
from math import comb

PERMS = list(permutations(range(4)))
RELAB = [tuple(sum(((m >> i) & 1) << p[i] for i in range(4)) for m in range(16))
         for p in PERMS]


def orbit_signature(edges):
    """Complete invariant for unlabeled 3-uniform hypergraphs with four edges.

    Label all incident ground elements, list their four-edge incidence masks,
    and quotient by all 24 permutations of the four edges.
    """
    n = 1 + max(max(e) for e in edges)
    incidence = [sum((v in edge) << j for j, edge in enumerate(edges))
                 for v in range(n)]
    assert all(incidence)
    return min(tuple(sum(remap[mask] == j for mask in incidence)
                     for j in range(1, 16))
               for remap in RELAB)


def representative_types():
    """Generate ALL 4-distinct-triple support types on arbitrary ground sets.

    Any four triples can be ordered and its ground elements relabeled by first
    occurrence. Begin with (0,1,2); at each step a new triple uses old symbols
    and at most three consecutive fresh symbols. Quotient by complete incidence
    signatures. No finite ambient graph cutoff is assumed here.
    """
    states = {((0, 1, 2),)}
    counts = []
    for k in range(2, 5):
        next_states = set()
        for edges in states:
            size = 1 + max(max(e) for e in edges)
            for edge in combinations(range(size + 3), 3):
                fresh = {v for v in edge if v >= size}
                if edge in edges or fresh != set(range(size, size + len(fresh))):
                    continue
                next_states.add((*edges, edge))
        states = next_states
        counts.append(len(states))
    reps = {}
    for edges in sorted(states):
        reps.setdefault(orbit_signature(edges), edges)
    return counts, reps


def traces(n, support):
    return {sum((len(set(center) & set(query)) >= 2) << j
                for j, query in enumerate(support))
            for center in combinations(range(n), 3)}


def local_shattered_counts(n):
    triples = list(combinations(range(n), 3))
    root = triples[0]
    closed = [query for query in triples if len(set(query) & set(root)) >= 2]
    out = {}
    for k in range(1, 5):
        out[k] = sum(len(traces(n, S)) == (1 << k)
                     for S in combinations(closed, k))
    return out


def main():
    counts, reps = representative_types()
    assert counts == [7, 151, 6328], counts
    assert len(reps) == 66, len(reps)
    # For four query triples, at most 12 ground symbols occur. An arbitrary
    # center has size 3, so 3 additional fresh symbols suffice to simulate
    # every trace for all ambient n >= 15.
    yes = [edges for edges in reps.values()
           if len(traces(15, edges)) == 16]
    expected = ((0, 1, 2), (0, 1, 3), (0, 4, 5), (0, 4, 6))
    assert len(yes) == 1 and orbit_signature(yes[0]) == orbit_signature(expected)
    assert len(traces(7, expected)) == 16
    assert all(len(traces(15, edges)) != 16
               for edges in reps.values() if orbit_signature(edges) != orbit_signature(expected))
    # Small-parameter checks use graph-centered support enumeration,
    # independent of the isomorphism-type generation above.
    for n, expected_counts in [(5, {1: 7, 2: 15, 3: 0, 4: 0}),
                               (6, {1: 10, 2: 45, 3: 120, 4: 0}),
                               (7, {1: 13, 2: 78, 3: 286, 4: 18}),
                               (8, {1: 16, 2: 120, 3: 560, 4: 90}),
                               (9, {1: 19, 2: 171, 3: 969, 4: 270})]:
        got = local_shattered_counts(n)
        assert got == expected_counts, (n, got)
    # Each shattered four-support has a unique center realizing four 1 labels.
    # Thus the global fourth coefficient equals (number centers) times
    # the local count; check on n=7,8,9 against the structural formula.
    for n, local in [(7, 18), (8, 90), (9, 270)]:
        total = comb(n, 3) * local
        formula = n * comb(n - 1, 2) * comb(n - 3, 2) * comb(n - 5, 2)
        assert total == formula, (n, total, formula)
    # Small cases and explicit root witnesses.
    assert len(traces(5, [(0, 1, 2), (0, 1, 3)])) == 4
    assert len(traces(6, [(0, 1, 2), (0, 1, 3), (0, 1, 4)])) == 8
    print('ISOMORPHISM_ENUMERATION', counts, '66 types; 1 shattered type')
    print('JOHNSON_3_CLOSED_BALL_FOUR_SUPPORT_PASS')


if __name__ == '__main__':
    main()
