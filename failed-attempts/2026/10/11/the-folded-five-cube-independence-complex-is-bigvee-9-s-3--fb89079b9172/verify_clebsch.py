#!/usr/bin/env python3
"""Exhaustive acyclic-matching certificate for the folded five-cube."""
from collections import Counter, deque
from itertools import combinations


def main():
    labels = tuple(i for i in range(32) if i.bit_count() % 2 == 0)
    assert len(labels) == 16
    index = {x: j for j, x in enumerate(labels)}
    adjacency = [0] * 16
    for j, x in enumerate(labels):
        for coordinate in range(5):
            # Changing all coordinates except one has Hamming weight four.
            y = x ^ (31 ^ (1 << coordinate))
            adjacency[j] |= 1 << index[y]
    assert all(a.bit_count() == 5 for a in adjacency)
    assert all(not (adjacency[i] & (1 << i)) for i in range(16))
    assert all(bool(adjacency[i] & (1 << j)) == bool(adjacency[j] & (1 << i))
               for i in range(16) for j in range(16))
    assert sum(a.bit_count() for a in adjacency) == 80
    for i in range(16):
        for j in range(i + 1, 16):
            expected = 0 if adjacency[i] & (1 << j) else 2
            assert (adjacency[i] & adjacency[j]).bit_count() == expected

    # Exhaustive enumeration over all 2^16 subsets, with full membership test.
    simplices = {}
    for mask in range(1, 1 << 16):
        if all((adjacency[v] & mask) == 0
               for v in range(16) if mask & (1 << v)):
            simplices[mask] = mask.bit_count() - 1
    assert Counter(simplices.values()) == {0: 16, 1: 80, 2: 160, 3: 120, 4: 16}
    assert len(simplices) == 392
    maximal = [mask for mask in simplices
               if all((mask | (1 << i)) not in simplices
                      for i in range(16) if not (mask & (1 << i)))]
    assert Counter(simplices[mask] for mask in maximal) == {3: 40, 4: 16}
    for mask in simplices:
        assert all((mask ^ (1 << i)) in simplices
                   for i in range(16) if mask & (1 << i) and mask.bit_count() > 1)

    # A staged vertex-toggle matching. Each pair differs by one vertex;
    # formerly used faces are removed before proceeding to the next stage.
    unmatched = set(simplices)
    pairs = []
    for v in range(16):
        bit = 1 << v
        for lower in sorted(tuple(unmatched)):
            if lower & bit:
                continue
            upper = lower | bit
            if upper in unmatched:
                unmatched.remove(lower)
                unmatched.remove(upper)
                pairs.append((lower, upper))
    assert len(pairs) == 191
    assert Counter(simplices[m] for m in unmatched) == {0: 1, 3: 9}
    assert len(unmatched) == 10
    assert len(set(x for pair in pairs for x in pair)) == 2 * len(pairs)
    assert all((lo & hi) == lo and (hi.bit_count() == lo.bit_count() + 1)
               for lo, hi in pairs)

    # Orient every nonempty codimension-one face inclusion upwards,
    # except for matching edges, which are oriented downwards.
    upper_to_lower = {hi: lo for lo, hi in pairs}
    outgoing = {mask: [] for mask in simplices}
    indegree = {mask: 0 for mask in simplices}
    incidences = 0
    for upper in simplices:
        for v in range(16):
            if not (upper & (1 << v)):
                continue
            lower = upper ^ (1 << v)
            if lower not in simplices:
                continue  # Excludes empty face from ordinary CW matching.
            if upper_to_lower.get(upper) == lower:
                outgoing[upper].append(lower)
                indegree[lower] += 1
            else:
                outgoing[lower].append(upper)
                indegree[upper] += 1
            incidences += 1
    assert incidences == 1200
    queue = deque(mask for mask, d in indegree.items() if d == 0)
    visited = 0
    while queue:
        mask = queue.popleft()
        visited += 1
        for next_mask in outgoing[mask]:
            indegree[next_mask] -= 1
            if indegree[next_mask] == 0:
                queue.append(next_mask)
    assert visited == len(simplices), "The purported matching contains a closed V-path"

    # Exactly one critical 0-cell and nine critical 3-cells give the CW model
    # pt union nine 3-cells with constant attaching maps, hence wedge 9 S^3.
    assert sum((-1)**k * val for k, val in Counter(simplices.values()).items()) == -8
    print('CLEBSCH_MATCHING_VERIFIED: vertices=16 edges=40 faces=392 '
          'incidences=1200 pairs=191 critical=(one_0,nine_3) '
          'homotopy=wedge_9_S3')


if __name__ == '__main__':
    main()
