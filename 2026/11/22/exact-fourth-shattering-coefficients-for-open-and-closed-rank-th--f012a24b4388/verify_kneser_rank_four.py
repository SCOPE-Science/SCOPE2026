#!/usr/bin/env python3
"""Exhaustive Venn-profile certificate for rank-four Kneser disjointness traces.

Python 3 standard library only. No numerical approximations.
"""
from collections import defaultdict
from itertools import combinations
from math import comb, factorial, prod

EXPECTED = {
    0: {(6, 3): 15, (7, 3): 2310, (8, 3): 32060,
        (9, 3): 105525, (10, 3): 129150, (11, 3): 69300},
    1: {(6, 3): 15, (7, 3): 4830, (8, 2): 560,
        (8, 3): 66780, (9, 2): 25200, (9, 3): 87885,
        (10, 1): 100800, (10, 3): 28350, (11, 1): 69300},
}

def census():
    # A nonzero four-bit mask records which of the four distinct sample
    # triples contain a ground point. Its multiplicity is the Venn-cell size.
    rows_left = [3] * 4
    multiplicities = [0] * 16
    buckets = defaultdict(int)
    profiles = [0]
    skipped_repeats = [0]
    profiles_at_nine = [0]
    total_ordered_at_nine = [0]
    full_orbits_at_nine = [set(), set()]

    def examine():
        # A sample is an unordered set of four DIFFERENT triples.
        for i in range(4):
            for j in range(i + 1, 4):
                if not any(multiplicities[m] and bool(m & (1 << i)) != bool(m & (1 << j))
                           for m in range(1, 16)):
                    skipped_repeats[0] += 1
                    return
        profiles[0] += 1
        point_signatures = [mask for mask in range(1, 16)
                            for _ in range(multiplicities[mask])]
        u = len(point_signatures)
        sample = [frozenset(p for p, mask in enumerate(point_signatures)
                            if mask & (1 << i)) for i in range(4)]
        assert all(len(s) == 3 for s in sample) and len(set(sample)) == 4
        ordered_on_u = factorial(u) // prod(factorial(multiplicities[m])
                                               for m in range(1, 16))
        if u <= 9:
            profiles_at_nine[0] += 1
            total_ordered_at_nine[0] += ordered_on_u * comb(9, u)
        for mode in (0, 1):
            least = None
            for ext in range(4):
                universe = range(u + ext)
                patterns = set()
                for choice in combinations(universe, 3):
                    center = frozenset(choice)
                    trace = sum(1 << i for i, edge in enumerate(sample)
                                if edge.isdisjoint(center)
                                or (mode == 1 and edge == center))
                    patterns.add(trace)
                if len(patterns) == 16:
                    least = ext
                    break
            if least is not None:
                buckets[mode, u, least] += ordered_on_u
                if u + least <= 9:
                    full_orbits_at_nine[mode].add(tuple(multiplicities))

    def generate(mask):
        if mask == 0:
            if rows_left == [0, 0, 0, 0]:
                examine()
            return
        covered = [j for j in range(4) if (mask >> j) & 1]
        bound = min(rows_left[j] for j in covered)
        for count in range(bound + 1):
            multiplicities[mask] = count
            for j in covered:
                rows_left[j] -= count
            generate(mask - 1)
            for j in covered:
                rows_left[j] += count
        multiplicities[mask] = 0

    generate(15)
    assert profiles[0] == 666, profiles[0]
    assert skipped_repeats[0] == 196, skipped_repeats[0]
    # 84 distinct three-subsets of a 9-set; all ordered 4-tuples.
    assert total_ordered_at_nine[0] == 84 * 83 * 82 * 81
    assert profiles_at_nine[0] == 634
    normalized = {}
    for mode in (0, 1):
        normalized[mode] = {}
        for (m, u, ext), count in buckets.items():
            if m == mode:
                assert count % 24 == 0
                normalized[mode][u, ext] = count // 24
        assert normalized[mode] == EXPECTED[mode], (mode, normalized[mode])
        assert sum(coef * comb(9, u) for (u, e), coef in normalized[mode].items()
                   if 9 >= u + e) == 1260
        assert len(full_orbits_at_nine[mode]) == 1
    for n, target_open, target_closed in [
        (7, 0, 0), (8, 0, 0), (9, 1260, 1260),
        (10, 280350, 607950), (11, 6059130, 15206730),
        (12, 40928580, 69535620),
    ]:
        vals = [sum(coef * comb(n, u) for (u, e), coef in normalized[m].items()
                    if n >= u + e) for m in (0, 1)]
        assert vals == [target_open, target_closed], (n, vals)
    print('EXHAUSTIVE VENN PROFILES: 666 distinct-edge cases')
    print('DISTINCTNESS FILTERED: 196 repeated-edge cases')
    print('ALL ORDERED FOUR-SUPPORTS AT n=9: 46,308,024')
    for mode in (0, 1):
        print(('OPEN', 'CLOSED')[mode], 'coefficient table:')
        for key, value in sorted(normalized[mode].items()):
            print(' ', key, value)
    print('EXACT ALL-n FOURTH-COEFFICIENT CERTIFICATE: PASS')

if __name__ == '__main__':
    census()
