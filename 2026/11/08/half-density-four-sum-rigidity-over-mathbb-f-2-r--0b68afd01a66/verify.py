"""Exact finite-case checks for restricted four-sums in binary vector spaces.
Python 3 standard library only. Tests are finite corroboration, not the infinite proof.
"""
from itertools import combinations
from collections import Counter


def four_sums(a):
    res = set()
    for w, x, y, z in combinations(a, 4):
        res.add(w ^ x ^ y ^ z)
    return res


def affine_hyperplane(a, r):
    s = set(a)
    for linear in range(1, 1 << r):
        for offset in (0, 1):
            if s == {x for x in range(1 << r) if ((linear & x).bit_count() % 2) == offset}:
                return True
    return False


def exceptional_direction(a, r):
    """A is the inverse image of an affinely independent four-set in V/<g>."""
    s = set(a)
    directions = []
    for g in range(1, 1 << r):
        if {x ^ g for x in s} != s:
            continue
        orbits = {min(x, x ^ g) for x in s}
        if len(orbits) != 4:
            continue
        values = list(orbits)
        if values[0] ^ values[1] ^ values[2] ^ values[3] not in (0, g):
            directions.append(g)
    return directions


def test_r4():
    full = set(range(16))
    histogram = Counter()
    classes = Counter()
    for combo in combinations(range(16), 8):
        a = set(combo)
        missing = full - four_sums(combo)
        hyper = affine_hyperplane(a, 4)
        special = exceptional_direction(a, 4)
        if hyper:
            assert len(missing) == 8
            assert missing == full - {0, *four_sums(combo)}
            assert not special
            classes['hyperplane'] += 1
        elif special:
            assert len(special) == 1
            assert missing == set(special), (combo, missing, special)
            classes['exception'] += 1
        else:
            assert not missing, (combo, missing)
            classes['covering'] += 1
        histogram[len(missing)] += 1
    assert histogram == {0: 12000, 1: 840, 8: 30}, histogram
    assert classes == {'hyperplane': 30, 'exception': 840, 'covering': 12000}, classes
    print('R4_OK sets=12870 missing_histogram=0:12000,1:840,8:30')


def test_r5():
    # Exhaustive verification of all 62 affine hyperplanes, with non-hyperplane
    # deterministic checks as a finite additional sanity test.
    from random import Random
    r = 5
    full = set(range(1 << r))
    seen = set()
    for linear in range(1, 1 << r):
        for offset in (0, 1):
            a = tuple(x for x in range(1 << r) if ((linear & x).bit_count() % 2) == offset)
            assert len(full - four_sums(a)) == 16
            seen.add(a)
    assert len(seen) == 62
    rng = Random(16807)
    checked = 0
    while checked < 2000:
        a = rng.sample(range(1 << r), 16)
        if affine_hyperplane(a, r):
            continue
        assert four_sums(a) == full
        checked += 1
    print('R5_OK affine_hyperplanes=62 sampled_nonhyperplanes=2000')


if __name__ == '__main__':
    test_r4()
    test_r5()
    print('VERIFY_OK')
