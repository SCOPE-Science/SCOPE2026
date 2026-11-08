#!/usr/bin/env python3
"""Exact subset-sum and Walsh-PBH verification for a weighted hypercube."""
from collections import defaultdict
from itertools import combinations

BASE = (1, 3, 5, 7, 9, 20)
EXPECTED = {
    15: (8, 17, 28, 37),
    23: (9, 16, 29, 36),
    27: (10, 15, 30, 35),
    30: (12, 13, 32, 33),
    59: (20, 25),
    61: (21, 24),
}
ODD_CIRCUIT = (15, 23, 30, 59, 61)


def sign(x, a):
    return 1 if ((x & a).bit_count() % 2 == 0) else -1


def analyze(weights):
    d = len(weights)
    fibers = defaultdict(list)
    for a in range(1 << d):
        fibers[sum(w for i, w in enumerate(weights) if (a >> i) & 1)].append(a)
    return fibers


def is_full_rank_on_fibers(weights, chosen):
    fibers = analyze(weights)
    for indices in fibers.values():
        if len(indices) == 1:
            continue
        assert len(indices) == 2, "Applicable only for fibers of size at most two"
        a, b = indices
        # Two columns on selected rows are independent iff their relative
        # Walsh signs are not constant.
        ratios = {sign(x, a) * sign(x, b) for x in chosen}
        if len(ratios) != 2:
            return False
    return True


def check_base():
    fibers = analyze(BASE)
    assert len(fibers) == 44
    assert max(map(len, fibers.values())) == 2
    assert sum(len(a) == 2 for a in fibers.values()) == 20
    patterns = defaultdict(list)
    for s, indices in fibers.items():
        if len(indices) == 2:
            patterns[indices[0] ^ indices[1]].append(s)
    patterns = {k: tuple(sorted(v)) for k, v in patterns.items()}
    assert patterns == EXPECTED, (patterns, EXPECTED)
    parity_xor = 0
    for delta in ODD_CIRCUIT:
        parity_xor ^= delta
    assert parity_xor == 0
    assert len(ODD_CIRCUIT) % 2 == 1
    assert all((delta & 3) != 0 for delta in patterns)
    assert is_full_rank_on_fibers(BASE, (0, 1, 2))

    # Direct weighted-graph Laplacian action on the Walsh basis, no
    # numerical eigenvalue routines and no reliance on a prior log.
    lap_checks = 0
    for x in range(64):
        for a in range(64):
            left = sum(w * (sign(x, a) - sign(x ^ (1 << i), a))
                       for i, w in enumerate(BASE))
            right = 2 * sum(w for i, w in enumerate(BASE) if (a >> i) & 1) * sign(x, a)
            assert left == right
            lap_checks += 1

    pair_failures = 0
    for x, y in combinations(range(64), 2):
        assert not is_full_rank_on_fibers(BASE, (x, y))
        pair_failures += 1
    assert pair_failures == 2016
    return lap_checks, pair_failures


def check_extensions():
    weights = list(BASE)
    checks = 0
    for _ in range(3):
        weights.append(sum(weights) + 1)
        fibers = analyze(weights)
        assert max(map(len, fibers.values())) == 2
        assert is_full_rank_on_fibers(weights, (0, 1, 2))
        # Every collision difference is supported entirely in the original
        # six coordinates, and reproduces one of the original six patterns.
        differences = {ids[0] ^ ids[1] for ids in fibers.values() if len(ids) == 2}
        assert differences == set(EXPECTED)
        checks += sum(len(ids) == 2 for ids in fibers.values())
    return checks


if __name__ == '__main__':
    lap, pairs = check_base()
    ext = check_extensions()
    print('PASS: 44 exact spectral fibers; 20 double fibers; 6 difference masks')
    print('PASS: five-mask odd XOR obstruction and 3-vertex full PBH ranks')
    print(f'PASS: {lap} exact Laplacian/Walsh identities; {pairs} failing coordinate pairs')
    print(f'PASS: {ext} exact repeated fibers verified over dimensions 7, 8, 9')
