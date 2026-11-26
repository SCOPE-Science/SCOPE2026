#!/usr/bin/env python3
"""Exact, standalone check of Frobenius-stable maximal isotropic 2-torsion kernels.

Requires Python 3.10+ standard library only. No external files or packages.
"""
from itertools import combinations

N = 10
FULL = (1 << N) - 1


def even_subset(x):
    """Identify F2^8 with even subsets of [10] modulo the full subset.

    Choose the representative without element 9; element 8 restores parity.
    """
    assert 0 <= x < 256
    return x | ((x.bit_count() & 1) << 8)


def pairing(a, b):
    return ((a & b).bit_count() + (a.bit_count() & 1) * (b.bit_count() & 1)) & 1


def span(rows):
    result = 1
    for mask in range(1, 1 << len(rows)):
        x = 0
        for i, row in enumerate(rows):
            if (mask >> i) & 1:
                x ^= row
        result |= 1 << x
    return result


def lagrangians_rref():
    """All isotropic 4-dimensional subspaces via UNIQUE reduced row echelon bases."""
    result = set()
    inspected = 0
    for pivots in combinations(range(8), 4):
        choices = [(i, j) for i in range(4)
                   for j in range(pivots[i]+1, 8) if j not in pivots]
        for bits in range(1 << len(choices)):
            inspected += 1
            rows = [1 << p for p in pivots]
            for k, (i, j) in enumerate(choices):
                if (bits >> k) & 1:
                    rows[i] |= 1 << j
            if any(pairing(rows[i], rows[j]) for i in range(4)
                   for j in range(i+1, 4)):
                continue
            result.add(span(rows))
    assert inspected == 200787, inspected  # Gaussian binomial [8 choose 4]_2
    assert len(result) == 2295 == 3*5*9*17
    return result


def lagrangians_by_extension():
    """Independent enumeration using isotropic-line extensions and set deduplication."""
    layers = [{1}]
    assert [even_subset(x) for x in range(256)]
    for dimension in range(1, 5):
        next_layer = set()
        for U in layers[-1]:
            members = [i for i in range(256) if (U >> i) & 1]
            for v in range(1, 256):
                if (U >> v) & 1:
                    continue
                if any(pairing(v, u) for u in members):
                    continue
                W = U
                for u in members:
                    W |= 1 << (u ^ v)
                next_layer.add(W)
        layers.append(next_layer)
    assert [len(S) for S in layers] == [1, 255, 5355, 11475, 2295]
    return layers[-1]


def partitions(n, largest=None):
    if n == 0:
        yield ()
        return
    for k in range(min(n, n if largest is None else largest), 0, -1):
        for suffix in partitions(n-k, k):
            yield (k,) + suffix


def permutation_from_partition(shape):
    permutation = list(range(10))
    beginning = 0
    for length in shape:
        for j in range(length):
            permutation[beginning+j] = beginning+(j+1) % length
        beginning += length
    assert beginning == 10
    return permutation


def permutation_map(permutation):
    action = []
    for vector in range(256):
        image = 0
        subset = even_subset(vector)
        for i in range(10):
            if (subset >> i) & 1:
                image |= 1 << permutation[i]
        if (image >> 9) & 1:
            image ^= FULL
        action.append(image & 255)
    assert len(set(action)) == 256
    return action


def count_fixed(lags, permutation):
    images = permutation_map(permutation)
    fixed_torsion = sum(images[v] == v for v in range(256))
    fixed_kernel = 0
    for U in lags:
        members = [v for v in range(256) if (U >> v) & 1]
        fixed_kernel += all((U >> images[v]) & 1 for v in members)
    return fixed_torsion, fixed_kernel


# Each triple is (cycle lengths of Frobenius on the ten ramification points,
# number of fixed two-torsion points, number of stable Lagrangian kernels).
EXPECTED = [
    ((10,), 1, 1), ((9,1), 1, 0), ((8,2), 2, 1), ((8,1,1), 2, 1),
    ((7,3), 1, 0), ((7,2,1), 2, 2), ((7,1,1,1), 4, 6),
    ((6,4), 2, 1), ((6,3,1), 2, 0), ((6,2,2), 4, 7),
    ((6,2,1,1), 4, 3), ((6,1,1,1,1), 8, 3),
    ((5,5), 1, 5), ((5,4,1), 2, 0), ((5,3,2), 2, 0),
    ((5,3,1,1), 4, 0), ((5,2,2,1), 4, 0),
    ((5,2,1,1,1), 8, 0), ((5,1,1,1,1,1), 16, 0),
    ((4,4,2), 4, 11), ((4,4,1,1), 4, 11), ((4,3,3), 2, 3),
    ((4,3,2,1), 4, 0), ((4,3,1,1,1), 8, 0),
    ((4,2,2,2), 8, 7), ((4,2,2,1,1), 8, 7),
    ((4,2,1,1,1,1), 16, 15), ((4,1,1,1,1,1,1), 32, 15),
    ((3,3,3,1), 4, 0), ((3,3,2,2), 4, 9),
    ((3,3,2,1,1), 8, 9), ((3,3,1,1,1,1), 16, 45),
    ((3,2,2,2,1), 8, 0), ((3,2,2,1,1,1), 16, 0),
    ((3,2,1,1,1,1,1), 32, 0), ((3,1,1,1,1,1,1,1), 64, 0),
    ((2,2,2,2,2), 16, 151), ((2,2,2,2,1,1), 16, 39),
    ((2,2,2,1,1,1,1), 32, 39), ((2,2,1,1,1,1,1,1), 64, 135),
    ((2,1,1,1,1,1,1,1,1), 128, 135),
    ((1,1,1,1,1,1,1,1,1,1), 256, 2295),
]


def run():
    by_rref = lagrangians_rref()
    by_extension = lagrangians_by_extension()
    assert by_rref == by_extension
    assert len(EXPECTED) == 42
    assert [e[0] for e in EXPECTED] == list(partitions(10))
    for shape, n_torsion, n_kernels in EXPECTED:
        permutation = permutation_from_partition(shape)
        assert count_fixed(by_rref, permutation) == (n_torsion, n_kernels), shape
        # Conjugating the labels preserves both counts. Test nontrivial relabellings.
        for offset in (1, 3, 7):
            p = [(i + offset) % 10 for i in range(10)]
            inverse = [p.index(i) for i in range(10)]
            conjugate = [p[permutation[inverse[i]]] for i in range(10)]
            assert count_fixed(by_rref, conjugate) == (n_torsion, n_kernels), shape
    print('GENUS4_HYPERELLIPTIC_2295_LAGRANGIAN_42_FROBENIUS_TYPES_VERIFIED_OK')


if __name__ == '__main__':
    run()
