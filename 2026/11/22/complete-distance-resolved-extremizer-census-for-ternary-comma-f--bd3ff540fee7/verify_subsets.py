#!/usr/bin/env python3
"""Exhaustive ternary triple-code census by unordered subsets.

Uses only the Python standard library. The universe has 27 words, and no
necklace or rotation reduction is assumed for this independent check.
"""
from itertools import combinations, permutations, product

WORDS = tuple(''.join(t) for t in product('012', repeat=3))

def valid(code, distance):
    lookup = set(code)
    if any(sum(x != y for x, y in zip(a, b)) < distance
           for a, b in combinations(code, 2)):
        return False
    return all(a[1:] + b[:1] not in lookup and a[2:] + b[:2] not in lookup
               for a in code for b in code)

def transform(code, permutation, reverse):
    words = (''.join(permutation[int(x)] for x in w) for w in code)
    return frozenset(w[::-1] if reverse else w for w in words)

def compute(distance, largest_k):
    hist = {}
    maxima = set()
    for k in range(0, largest_k + 1):
        valid_sets = (frozenset(c) for c in combinations(WORDS, k)
                      if valid(c, distance))
        result = set(valid_sets)
        hist[k] = len(result)
        if result:
            maxima = result
    assert hist[largest_k] == 0
    seen = set()
    orbits = []
    group = tuple(product(permutations('012'), (False, True)))
    for code in sorted(maxima, key=lambda c: sorted(c)):
        if code in seen:
            continue
        orbit = {transform(code, p, rev) for p, rev in group}
        assert orbit <= maxima
        seen.update(orbit)
        orbits.append((len(orbit), tuple(sorted(code))))
    print('distance', distance, 'histogram', hist)
    print('maxima', len(maxima), 'symmetry_orbits', len(orbits))
    print('orbit_sizes', sorted(s for s, _ in orbits))
    for s, rep in orbits:
        print('orbit', s, ','.join(rep))
    return hist, sorted(s for s, _ in orbits)

if __name__ == '__main__':
    two, sizes_two = compute(2, 5)
    three, sizes_three = compute(3, 4)
    assert two == {0: 1, 1: 24, 2: 174, 3: 336, 4: 132, 5: 0}
    assert sizes_two == [6, 6] + [12] * 10
    assert three == {0: 1, 1: 24, 2: 66, 3: 12, 4: 0}
    assert sizes_three == [2, 4, 6]
    print('ALL CHECKS PASSED')
