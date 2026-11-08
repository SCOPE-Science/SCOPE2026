"""Exact finite checker for a three-plant capacity-constrained service network.

No numerical optimization or simulation is used. Run: python VERIFY.py
"""
from itertools import combinations_with_replacement, permutations
from collections import Counter
from math import comb

NPLANTS = 3


def is_connected(cols):
    """Bipartite connectivity; every pollinator in cols has a nonempty neighborhood."""
    seen = {0}
    for _ in range(3):
        for i in tuple(seen):
            for j in range(3):
                if any((c & (1 << i)) and (c & (1 << j)) for c in cols):
                    seen.add(j)
    return len(seen) == 3


def hall_support(cols, subset):
    """Hall inequalities for every nonempty subset of the three plants."""
    for plants in range(1, 8):
        count = sum(1 for j, c in enumerate(cols) if (subset & (1 << j)) and (c & plants))
        if count < plants.bit_count():
            return False
    return True


def assignment_support(cols, subset):
    """Independent, direct distinct-pollinator assignment verifier."""
    living = [j for j in range(len(cols)) if subset & (1 << j)]
    return any((cols[a] & 1) and (cols[b] & 2) and (cols[c] & 4)
               for a, b, c in permutations(living, 3))


def coefficients(cols):
    n = len(cols)
    ans = [0] * (n + 1)
    for S in range(1 << n):
        if S.bit_count() >= 3 and hall_support(cols, S):
            ans[S.bit_count()] += 1
    return tuple(ans)


def increment_profiles(cols, base):
    results = {}
    for j, neighborhood in enumerate(cols):
        for i in range(3):
            if neighborhood & (1 << i):
                continue
            new = list(cols)
            new[j] |= (1 << i)
            c = coefficients(new)
            results[(j, i)] = tuple(a - b for a, b in zip(c, base))
    return results


def coefficientwise_best(gains):
    return any(all(all(a >= b for a, b in zip(x, y)) for y in gains.values())
               for x in gains.values())


def canonical_under_plant_permutations(cols):
    return min(tuple(sorted(sum((1 << permutation[i]) for i in range(3) if c & (1 << i))
                            for c in cols)) for permutation in permutations(range(3)))


def run():
    expected = {
        3: (84, 44, 41, 40, 0),
        4: (210, 135, 132, 131, 0),
        5: (462, 336, 333, 332, 0),
        6: (924, 728, 725, 724, 0),
        7: (1716, 1428, 1425, 1400, 24),
    }
    exception_masks = []
    crossing_count = Counter()
    for n in range(3, 8):
        tallies = Counter()
        for cols in combinations_with_replacement(range(1, 8), n):
            tallies['all'] += 1
            if not is_connected(cols):
                continue
            tallies['connected'] += 1
            base = coefficients(cols)
            if not base[n]:
                continue
            tallies['matchable'] += 1
            gains = increment_profiles(cols, base)
            if not gains:  # The fully complete incidence graph offers no missing edge.
                continue
            if coefficientwise_best(gains):
                tallies['dominant'] += 1
                continue
            tallies['exceptional'] += 1
            assert n == 7
            exception_masks.append(cols)
            vectors = set(gains.values())
            a = (0, 0, 0, 4, 0, 0, 0, 0)
            b = (0, 0, 0, 3, 1, 0, 0, 0)
            c = (0, 0, 0, 5, 0, 0, 0, 0)
            z = (0,) * 8
            assert b in vectors
            assert vectors.issubset({a, b, c, z})
            assert (a in vectors) or (c in vectors)
            if c in vectors:
                crossing_count['2/3'] += 1
            else:
                crossing_count['1/2'] += 1
        got = tuple(tallies[k] for k in ['all', 'connected', 'matchable', 'dominant', 'exceptional'])
        assert got == expected[n], (n, got, expected[n])
        print('pollinators', n, 'all/connected/matchable/dominant/switch=', got)
    assert len(exception_masks) == 24
    assert crossing_count == {'1/2': 9, '2/3': 15}, crossing_count
    orbit_reps = {canonical_under_plant_permutations(x) for x in exception_masks}
    expected_reps = {
        (1, 1, 2, 4, 6, 6, 7),
        (1, 1, 2, 5, 6, 6, 6),
        (1, 1, 2, 6, 6, 6, 7),
        (1, 1, 3, 6, 6, 6, 6),
        (1, 1, 6, 6, 6, 6, 7),
    }
    assert orbit_reps == expected_reps, orbit_reps
    print('seven-pollinator exceptional graphs: 24; thresholds 1/2:9, 2/3:15; plant-unlabelled orbits:5')

    witness = (1, 1, 2, 4, 6, 6, 7)
    assert coefficients(witness) == (0, 0, 0, 26, 34, 21, 7, 1)
    gains = increment_profiles(witness, coefficients(witness))
    assert gains[(0, 1)] == (0, 0, 0, 4, 0, 0, 0, 0)
    assert gains[(2, 0)] == (0, 0, 0, 3, 1, 0, 0, 0)
    assert set(gains.values()) == { (0,)*8, gains[(0,1)], gains[(2,0)] }
    # Independent matching formulation, all survival masks and the full witness intervention set.
    test_graphs = [witness]
    for j, c in enumerate(witness):
        for i in range(3):
            if not c & (1 << i):
                new = list(witness); new[j] |= (1 << i)
                test_graphs.append(tuple(new))
    independent_cases = 0
    for cols in test_graphs:
        for S in range(1 << 7):
            assert hall_support(cols, S) == assignment_support(cols, S)
            independent_cases += 1
    print('independent Hall-vs-assignments:', independent_cases)
    print('VERIFIED')

if __name__ == '__main__':
    run()
