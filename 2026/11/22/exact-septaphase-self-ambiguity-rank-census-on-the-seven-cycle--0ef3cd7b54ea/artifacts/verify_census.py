#!/usr/bin/env python3
"""Exact, exhaustive septaphase self-ambiguity census on the seven-cycle.

All arithmetic uses integers modulo seven. No numerical zeros are inferred from a tolerance.
"""
from collections import Counter, defaultdict
from itertools import product

P = 7
EXPECTED = {7: 49, 37: 14406, 39: 18522, 41: 24696, 43: 59976}
EXPECTED_DEGREE = {
    0: {7: 1}, 1: {7: 6}, 2: {7: 42}, 3: {43: 294},
    4: {43: 2058}, 5: {39: 6174, 43: 8232},
    6: {37: 14406, 39: 12348, 41: 24696, 43: 49392},
}
EXPECTED_PROFILES = {
    (6, 0, 0, 0, 0, 0, 0): 59976,
    (6, 0, 0, 1, 1, 0, 0): 8232,
    (6, 0, 0, 2, 2, 0, 0): 2058,
    (6, 0, 1, 0, 0, 1, 0): 8232,
    (6, 0, 1, 1, 1, 1, 0): 4116,
    (6, 0, 2, 0, 0, 2, 0): 2058,
    (6, 1, 0, 0, 0, 0, 1): 8232,
    (6, 1, 0, 1, 1, 0, 1): 4116,
    (6, 1, 1, 0, 0, 1, 1): 4116,
    (6, 1, 1, 1, 1, 1, 1): 14406,
    (6, 2, 0, 0, 0, 0, 2): 2058,
    (6, 6, 6, 6, 6, 6, 6): 49,
}

def polynomial_degree(values):
    """Highest nonzero finite difference (valid in characteristic 7, length 7)."""
    diffs = list(values)
    deg = 0
    for j in range(P):
        if diffs[0] != 0:
            deg = j
        diffs = [(diffs[i+1] - diffs[i]) % P for i in range(len(diffs)-1)]
    return deg

def main():
    counts = Counter()
    profiles = Counter()
    degrees = defaultdict(Counter)
    count = 0
    for tail in product(range(P), repeat=P-1):
        a = (0,) + tail
        rowzeros = [0] * P
        for delay in range(P):
            for frequency in range(P):
                residues = [(a[(x + delay) % P] - a[x] - frequency*x) % P
                            for x in range(P)]
                # A sum of seven seventh roots vanishes iff every root appears once.
                if len(set(residues)) == P:
                    rowzeros[delay] += 1
        assert rowzeros[0] == 6
        assert all(rowzeros[t] == rowzeros[P-t] for t in range(1, P))
        rank = P*P - sum(rowzeros)
        counts[rank] += 1
        profiles[tuple(rowzeros)] += 1
        degrees[polynomial_degree(a)][rank] += 1
        count += 1
    assert count == P**(P-1) == 117649
    assert counts == EXPECTED, (counts, EXPECTED)
    assert profiles == EXPECTED_PROFILES, (profiles, EXPECTED_PROFILES)
    assert {k: dict(v) for k, v in degrees.items()} == EXPECTED_DEGREE
    print('SEPTAPHASE_P7_EXACT_PASS total=117649')
    print('ranks=' + str(sorted(counts.items())))
    print('profiles=' + str(sorted(profiles.items())))
    print('degrees=' + str(sorted((d, sorted(v.items())) for d, v in degrees.items())))

if __name__ == '__main__':
    main()
