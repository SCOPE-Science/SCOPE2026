#!/usr/bin/env python3
"""Finite checks for a directed-petal avalanche homotopy theorem.

All checks use Python's standard library. The general theorem is proved in RESULT.md,
not inferred from these finite tests.
"""
from collections import defaultdict
from itertools import product, combinations


def graph(lengths):
    assert len(lengths) >= 2 and all(q >= 3 for q in lengths)
    edges = {0: []}
    petals = []
    next_vertex = 1
    for length in lengths:
        vertices = list(range(next_vertex, next_vertex + length - 1))
        next_vertex += length - 1
        petals.append(vertices)
        edges[0].append(vertices[0])
        for a, b in zip(vertices, vertices[1:]):
            edges[a] = [b]
        edges[vertices[-1]] = [0]
    return edges, petals


def trajectory(lengths, extra_hub_grains=0):
    edges, petals = graph(lengths)
    k = len(lengths)
    c = tuple([k - 1 + extra_hub_grains] + [1] * (len(edges) - 1))
    seen = {}
    configurations, firing_sets = [], []
    while c not in seen:
        assert len(seen) < 2000, "Unexpectedly long trajectory"
        seen[c] = len(seen)
        configurations.append(c)
        active = frozenset(v for v in edges if c[v] >= len(edges[v]))
        firing_sets.append(active)
        new = list(c)
        for vertex in active:
            new[vertex] -= len(edges[vertex])
            for neighbor in edges[vertex]:
                new[neighbor] += 1
        c = tuple(new)
    return edges, petals, configurations, firing_sets, seen[c]


def expected_sets(lengths, petals):
    vertices = {0}
    for p in petals:
        vertices.update(p)
    out = []
    for t in range(max(lengths)):
        absent = {0} if t == 0 else {
            petals[i][t - 1] for i, length in enumerate(lengths) if t < length
        }
        out.append(frozenset(vertices - absent))
    return out


def verify_nerve(firing_sets):
    m = len(firing_sets)
    # A nonempty intersection of simplices is itself a simplex and hence contractible.
    # Check every proper subfamily, including the empty family only implicitly.
    assert not set.intersection(*(set(s) for s in firing_sets))
    for size in range(1, m):
        for family in combinations(firing_sets, size):
            assert set.intersection(*(set(s) for s in family))
    for q in range(m - 1):
        assert set.intersection(*(set(s) for s in firing_sets[:q + 1]))


def mod2_betti(facets):
    # Independent simplicial boundary-matrix calculation over GF(2).
    faces = defaultdict(list)
    full = set()
    for facet in facets:
        for dimp1 in range(1, len(facet) + 1):
            full.update(combinations(sorted(facet), dimp1))
    for face in sorted(full, key=lambda f: (len(f), f)):
        faces[len(face) - 1].append(face)
    ranks = {}
    for dimension in range(1, max(faces) + 1):
        indices = {face: idx for idx, face in enumerate(faces[dimension - 1])}
        pivots = {}
        for face in faces[dimension]:
            mask = 0
            for j in range(len(face)):
                mask ^= 1 << indices[face[:j] + face[j + 1:]]
            while mask:
                pivot = mask.bit_length() - 1
                if pivot in pivots:
                    mask ^= pivots[pivot]
                else:
                    pivots[pivot] = mask
                    break
        ranks[dimension] = len(pivots)
    return {d: len(faces[d]) - ranks.get(d, 0) - ranks.get(d + 1, 0)
            - (1 if d == 0 else 0) for d in faces if len(faces[d])
            - ranks.get(d, 0) - ranks.get(d + 1, 0) - (1 if d == 0 else 0)}


def main():
    cases = 0
    total_period_steps = 0
    for k in range(2, 6):
        for lengths in product(range(3, 8), repeat=k):
            edges, petals, configurations, sets, repeat_index = trajectory(lengths)
            target = expected_sets(lengths, petals)
            assert repeat_index == 0
            assert len(sets) == max(lengths)
            assert sets == target
            assert len(set(sets)) == max(lengths)
            assert sum(lengths) - 1 == sum(configurations[0])
            verify_nerve(sets)
            # One extra grain at the hub makes every vertex fire at time zero.
            _, _, _, higher_sets, _ = trajectory(lengths, extra_hub_grains=1)
            assert higher_sets[0] == frozenset(edges)
            cases += 1
            total_period_steps += len(sets)
    print("DYNAMICS_AND_NERVE_OK cases=%d period_steps=%d" % (cases, total_period_steps))
    samples = [(3, 3), (3, 4), (4, 4), (3, 3, 3), (3, 4, 4), (3, 3, 4, 5)]
    for lengths in samples:
        _, _, _, sets, _ = trajectory(lengths)
        betti = mod2_betti(sets)
        predicted = {max(lengths) - 2: 1}
        assert betti == predicted, (lengths, betti, predicted)
        print("DIRECT_GF2_OK lengths=%s reduced_betti=%s" % (lengths, betti))
    print("ALL_VERIFY_OK")


if __name__ == "__main__":
    main()
