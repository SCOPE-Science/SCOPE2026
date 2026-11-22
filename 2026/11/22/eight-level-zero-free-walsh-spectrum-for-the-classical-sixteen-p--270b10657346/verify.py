"""Exact self-contained verification of the affine-plane Walsh convolution theorem.

Run: python3 verify.py
Uses Python integer arithmetic and exhaustive 16-bit transforms; no external packages.
"""
from collections import Counter
from itertools import combinations
from math import gcd

DIM = 4
V = 1 << DIM
GROUP = 1 << V


def planes_from_triples():
    # A quadruple is an affine plane iff its four distinct points XOR to zero.
    found = set()
    for a, b, c in combinations(range(V), 3):
        d = a ^ b ^ c
        if d > c:
            found.add((1 << a) | (1 << b) | (1 << c) | (1 << d))
    return sorted(found)


def planes_from_directions():
    found = set()
    for a in range(1, V):
        for b in range(a + 1, V):
            span = (0, a, b, a ^ b)
            for x in range(V):
                found.add(sum(1 << (x ^ z) for z in span))
    return sorted(found)


def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for j in range(0, len(a), 2 * h):
            for k in range(j, j + h):
                x, y = a[k], a[k + h]
                a[k], a[k + h] = x + y, x - y
        h *= 2
    return a


def monomial_mask(variables):
    return sum(1 << x for x in range(V)
               if all((x >> i) & 1 for i in variables))


def binary_rank(rows):
    pivots = {}
    for x in rows:
        while x:
            k = x.bit_length() - 1
            if k not in pivots:
                pivots[k] = x
                break
            x ^= pivots[k]
    return len(pivots)


def run():
    blocks = planes_from_triples()
    assert blocks == planes_from_directions(), 'Independent block constructions differ'
    assert len(blocks) == 140
    assert all(b.bit_count() == 4 for b in blocks)
    assert binary_rank(blocks) == 11  # Exactly the full RM(2,4) code

    a = [0] * GROUP
    for b in blocks:
        a[b] = 1
    spectrum = fwht(a)
    expected = {-20: 896, -10: 14336, -4: 26880, 6: 17920,
                12: 1120, 28: 3840, 70: 512, 140: 32}
    assert dict(Counter(spectrum)) == expected
    assert 0 not in spectrum

    quad = [monomial_mask(j) for j in combinations(range(DIM), 2)]
    cubic = [monomial_mask(j) for j in combinations(range(DIM), 3)]
    quartic = monomial_mask(range(DIM))
    assert len(quad) == 6 and len(cubic) == 4
    assert binary_rank(quad + cubic + [quartic]) == 11
    assert binary_rank(blocks + [monomial_mask(())] +
                       [monomial_mask((i,)) for i in range(DIM)]) == 11
    # Each frequency has a representative modulo the 32 affine Boolean functions.
    reduced = Counter()
    detail = Counter()
    for q in range(64):
        qmask = 0
        for j in range(6):
            if (q >> j) & 1:
                qmask ^= quad[j]
        for c in range(16):
            cmask = qmask
            for j in range(4):
                if (c >> j) & 1:
                    cmask ^= cubic[j]
            for d in (0, 1):
                t = cmask ^ (quartic if d else 0)
                val = spectrum[t]
                reduced[val] += 1
                detail[(d, c == 0, val)] += 1
    assert len(reduced) == 8
    assert all(32 * reduced[value] == multiplicity
               for value, multiplicity in expected.items())
    assert {v: reduced[v] for v in sorted(reduced)} == {
        -20: 28, -10: 448, -4: 840, 6: 560, 12: 35,
        28: 120, 70: 16, 140: 1}
    # Quadratic rank pattern; cubic-line and quartic-point classification.
    assert {v: detail[(0, True, v)] for v in (140, 12, -20)} == {
        140: 1, 12: 35, -20: 28}
    assert {v: detail[(0, False, v)] for v in (28, -4)} == {
        28: 120, -4: 840}
    assert {v: sum(detail[(1, z, v)] for z in (True, False))
            for v in (70, 6, -10)} == {70: 16, 6: 560, -10: 448}

    common_denominator = 420
    assert all(common_denominator % abs(e) == 0 for e in spectrum)
    numer_unreduced = fwht([common_denominator // e for e in spectrum])
    assert all(x % 8192 == 0 for x in numer_unreduced)
    kernel_numer = [x // 8192 for x in numer_unreduced]
    # This is 3360 times the exact inverse-convolution kernel.
    assert fwht(kernel_numer) == [3360 // e for e in spectrum]
    expected_kernel = {-415: 1, -255: 1, -9: 448, -3: 840,
                       0: 63628, 7: 448, 24: 140, 25: 30}
    assert dict(Counter(kernel_numer)) == expected_kernel
    assert Counter((i.bit_count(), k) for i, k in enumerate(kernel_numer) if k) == {
        (0, -255): 1, (4, 24): 140, (6, -9): 448,
        (8, -3): 840, (8, 25): 30, (10, 7): 448,
        (16, -415): 1}
    assert kernel_numer[0] == -255
    norm_numer = sum(abs(x) for x in kernel_numer)
    assert norm_numer == 14468
    assert gcd(norm_numer, 3360) == 4
    print('PASS: 140 affine planes; 2048 reduced signing classes')
    print('PASS: signed Walsh spectrum:', sorted(expected.items()))
    print('PASS: all 65536 multipliers nonzero; minimum absolute value 4')
    print('PASS: exact inverse kernel spectrum:', sorted(expected_kernel.items()))
    print('PASS: inverse l1/linfty norm = 3617/840')


if __name__ == '__main__':
    run()
