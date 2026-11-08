#!/usr/bin/env python3
"""Independent exact certificate for the support of four-agent random serial dictatorship.

Enumerates all multisets of strict rankings (rather than 24**4 labeled
profiles), quotients by object relabelings, and restores exact multiplicities
of labeled profiles. Uses Python's built-in arbitrary-precision integers.
"""
from collections import Counter, defaultdict
from csv import DictReader
from pathlib import Path
from fractions import Fraction
from itertools import combinations_with_replacement, permutations
from math import factorial

RANKINGS = tuple(permutations(range(4)))
INDEX = {order: j for j, order in enumerate(RANKINGS)}
AGENT_ORDERS = RANKINGS

EXPECTED = {
    1: 31104, 2: 20736, 3: 20736, 4: 53856,
    5: 48384, 6: 40032, 7: 45504, 8: 26568,
    9: 12672, 10: 15120, 11: 6336, 12: 5880,
    14: 4032, 16: 216, 18: 576, 24: 24,
}

def matching(preferences, priority):
    chosen = [-1] * 4
    remaining = set(range(4))
    for agent in priority:
        obj = next(v for v in preferences[agent] if v in remaining)
        chosen[agent] = obj
        remaining.remove(obj)
    assert not remaining
    return tuple(chosen)

def shape(profile):
    preferences = tuple(RANKINGS[j] for j in profile)
    outcomes = Counter(matching(preferences, priority) for priority in AGENT_ORDERS)
    assert sum(outcomes.values()) == 24
    return tuple(sorted(outcomes.values()))

def main():
    relabel = []
    for object_order in RANKINGS:
        relabel.append(tuple(INDEX[tuple(object_order[v] for v in ranking)] for ranking in RANKINGS))
    orbit_weights = defaultdict(int)
    n_anonymous = 0
    for anonymous in combinations_with_replacement(range(24), 4):
        n_anonymous += 1
        canonical = min(tuple(sorted(relabeling[j] for j in anonymous)) for relabeling in relabel)
        freq = Counter(anonymous)
        weight = factorial(4)
        for multiplicity in freq.values():
            weight //= factorial(multiplicity)  # integer at each step for n=4
        orbit_weights[canonical] += weight
    assert n_anonymous == 17550
    assert len(orbit_weights) == 762
    assert sum(orbit_weights.values()) == 331776
    histogram = Counter()
    spectra = Counter()
    full_support = []
    for canonical, weight in sorted(orbit_weights.items()):
        spectrum = shape(canonical)
        histogram[len(spectrum)] += weight
        spectra[spectrum] += weight
        if len(spectrum) == 24:
            full_support.append((canonical, weight))
    assert dict(histogram) == EXPECTED
    assert len(spectra) == 57
    assert full_support == [((0, 0, 0, 0), 24)]
    assert sum(histogram.values()) == 331776
    assert sum(k * v for k, v in histogram.items()) == 1839744
    assert Fraction(1839744, 331776) == Fraction(1597, 288)
    assert sum(v for k, v in histogram.items() if k >= 14) == 4848
    assert sorted(set(range(1, 25)) - set(histogram)) == [13, 15, 17, 19, 20, 21, 22, 23]
    directory = Path(__file__).resolve().parent
    with (directory / 'SUPPORT_HISTOGRAM.csv').open(encoding='utf-8', newline='') as handle:
        listed_histogram = {int(r['support_size']): int(r['labeled_preference_profiles'])
                            for r in DictReader(handle)}
    assert listed_histogram == dict(histogram)
    with (directory / 'SPECTRA.csv').open(encoding='utf-8', newline='') as handle:
        listed_spectra = {}
        for r in DictReader(handle):
            row = tuple(map(int, r['priority_order_multiplicities_ascending'].split()))
            assert sum(row) == 24 and len(row) == int(r['support_size'])
            assert row not in listed_spectra
            listed_spectra[row] = int(r['labeled_preference_profiles'])
    assert listed_spectra == dict(spectra)
    print('VERIFY_OK 17550 anonymous multisets, 762 symmetry classes, 331776 labeled profiles')
    for k, v in sorted(histogram.items()):
        print(f'{k}: {v}')
    print('SHAPES', len(spectra), 'MEAN', Fraction(1839744, 331776))
    return histogram, spectra

if __name__ == '__main__':
    main()
