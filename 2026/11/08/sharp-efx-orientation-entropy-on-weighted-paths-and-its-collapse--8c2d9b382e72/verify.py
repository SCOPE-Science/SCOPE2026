"""Independent exact enumeration checks for EFX orientations of weighted paths.

Run: python verify.py  (Python 3, standard library only)
An orientation bit 0 assigns the edge to its right endpoint; 1 to its left.
"""
from itertools import product
from math import comb
from random import Random


def direct_efx(bits, weights):
    """Check the literal EFX0 definition, all ordered agent pairs and removals."""
    m = len(weights)
    bags = [[] for _ in range(m + 1)]
    for e, bit in enumerate(bits):
        bags[e + (bit == 0)].append(e)
    for i in range(m + 1):
        own = sum(weights[e] for e in bags[i] if e == i or e == i - 1)
        for j in range(m + 1):
            if i == j:
                continue
            for removed in bags[j]:
                other = sum(weights[e] for e in bags[j]
                            if e != removed and (e == i or e == i - 1))
                if own < other:
                    return False
    return True


def sink_condition(bits, weights):
    """Independent locally stated characterization being verified."""
    m = len(weights)
    for j in range(1, m):
        if bits[j - 1] == 0 and bits[j] == 1:
            if not (2 <= j <= m - 2):
                return False
            if not (bits[j - 2] == 0 and bits[j + 1] == 1):
                return False
            if not (weights[j - 2] >= weights[j - 1] and
                    weights[j + 1] >= weights[j]):
                return False
    return True


def top_count(m):
    return sum(comb(m - 2 * k + 1, 2 * k + 1)
               for k in range(m // 4 + 1))


def check():
    direct_states = 0
    configurations = 0
    for m in range(1, 8):
        orientations = tuple(product((0, 1), repeat=m))
        for weights in product((1, 2, 3), repeat=m):
            configurations += 1
            count = 0
            for bits in orientations:
                a = direct_efx(bits, weights)
                b = sink_condition(bits, weights)
                assert a == b, ('characterization', m, weights, bits)
                count += a
                direct_states += 1
            assert m + 1 <= count <= top_count(m), ('bounds', m, weights)
            if len(set(weights)) == 1:
                assert count == top_count(m), ('uniform', m)
    rng = Random(20241021)
    for m in range(8, 12):
        for trial in range(16):
            weights = tuple(rng.randrange(1, 25) for _ in range(m))
            configurations += 1
            count = 0
            for bits in product((0, 1), repeat=m):
                a = direct_efx(bits, weights)
                b = sink_condition(bits, weights)
                assert a == b, ('long characterization', m, weights, bits)
                count += a
                direct_states += 1
            assert m + 1 <= count <= top_count(m)
    for m in range(1, 14):
        assert sum(direct_efx(bits, (1,) * m)
                   for bits in product((0, 1), repeat=m)) == top_count(m)
        assert sum(direct_efx(bits, tuple(range(1, m + 1)))
                   for bits in product((0, 1), repeat=m)) == m + 1
    assert [top_count(m) for m in range(1, 15)] == [
        2,3,4,6,10,17,28,45,72,116,188,305,494,799]
    for m in range(5, 201):
        assert top_count(m) == (2 * top_count(m-1) - top_count(m-2)
                                 + top_count(m-4)), ('recurrence', m)
    print('VERIFY_OK')
    print('weighted configurations:', configurations)
    print('direct weighted orientation states:', direct_states)
    print('uniform/strict monotone exact comparisons: m=1..13')
    print('exact recurrence checks: m=5..200')
    print('uniform counts m=1..14:', [top_count(m) for m in range(1, 15)])


if __name__ == '__main__':
    check()
