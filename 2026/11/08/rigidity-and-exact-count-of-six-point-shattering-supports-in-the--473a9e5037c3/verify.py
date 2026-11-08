"""Finite exhaustive certificate for six-column 3-uniform disjointness traces.

Uses all 3-subset queries, rather than a compressed trace criterion.
Python 3 standard library; run: python verify.py
"""
from itertools import combinations, combinations_with_replacement
from math import comb, factorial

M = 6
TRACES = set(range(1 << M))


def all_traces(supports, n):
    masks = set()
    for query in combinations(range(n), 3):
        query_set = set(query)
        hit = 0
        for i, support in enumerate(supports):
            if query_set.intersection(support):
                hit |= 1 << i
        masks.add(hit)
    return masks


def every_multiplicity_vector(num_types, total=M):
    return combinations_with_replacement(range(num_types), total)


def classify(num_extras, ground_size):
    pair_types = list(combinations(range(num_extras), 2))
    found = []
    tested = 0
    for pattern in every_multiplicity_vector(len(pair_types)):
        supports = [frozenset((i, M + pair_types[j][0], M + pair_types[j][1]))
                    for i, j in enumerate(pattern)]
        tested += 1
        if all_traces(supports, ground_size) == TRACES:
            found.append(pattern)
    return pair_types, tested, found


def main():
    pairs3, tested3, found3 = classify(3, 12)
    assert tested3 == 28 and not found3
    pairs4, tested4, found4 = classify(4, 13)
    assert tested4 == 462 and len(found4) == 4
    # Every successful edge multiset is precisely three doubled spokes,
    # with an arbitrary choice of the hub among four extra coordinates.
    for pattern in found4:
        edges = [pairs4[j] for j in pattern]
        candidates = [v for v in range(4) if all(v in e for e in edges)]
        assert len(candidates) == 1
        hub = candidates[0]
        assert sorted([edges.count(tuple(sorted((hub, w))))
                       for w in range(4) if w != hub]) == [2, 2, 2]
    # Construct all 64 traces by genuine three-subset queries.
    e = [frozenset((i, 6 + i // 2, 9)) for i in range(6)]
    assert len(set().union(*e)) == 10
    assert all_traces(e, 13) == TRACES
    assert 13 * comb(12, 3) * comb(9, 6) * factorial(6) // 8 == 21621600
    assert factorial(13) // (factorial(3)*2**3*factorial(3)) == 21621600
    assert comb(286, 6) == 721005537967
    print('ALL_KNESER_SIX_THRESHOLD_CHECKS_PASS')
    print('n12_reduced_cases=', tested3, 'n13_reduced_cases=', tested4,
          'n13_successes=', len(found4), 'orbit_count=1',
          'actual_query_traces=', len(all_traces(e, 13)))


if __name__ == '__main__':
    main()
