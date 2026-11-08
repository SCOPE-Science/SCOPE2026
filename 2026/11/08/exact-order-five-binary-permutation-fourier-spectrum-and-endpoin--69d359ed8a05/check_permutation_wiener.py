#!/usr/bin/env python3
"""Exact arithmetic verification of the order-five binary permutation Fourier norm.
Standalone: Python >=3.10 standard library only.
The two enumeration methods use unrelated identities: permutations and Ryser subsets.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, combinations_with_replacement
from math import factorial

N = 5
MASK_COUNT = 1 << ((N - 1) ** 2)
EXPECTED = {0: 20200, 8: 29820, 16: 11640, 24: 3050,
            32: 600, 48: 200, 72: 25, 120: 1}


def by_matchings(bits):
    """Evaluate all 5! perfect-matchings as signed monomials."""
    ans = 0
    for perm in permutations(range(N)):
        parity = 0
        for i in range(1, N):
            j = perm[i]
            if j:
                parity ^= (bits >> (4 * (i - 1) + j - 1)) & 1
        ans += 1 if parity == 0 else -1
    return ans


def by_ryser(bits):
    """Independently evaluate inclusion-exclusion of column-subsets."""
    rowbits = [(bits >> (4 * i)) & 15 for i in range(4)]
    s = 0
    for subset in range(1, 1 << N):
        k = subset.bit_count()
        term = k  # Row 0 has all entries +1.
        for r in rowbits:
            term *= k - 2 * ((subset >> 1) & r).bit_count()
        s += term if ((N - k) & 1) == 0 else -term
    return s


def main():
    count_a = Counter()
    count_b = Counter()
    signed_a = Counter()
    for bits in range(MASK_COUNT):
        x = by_matchings(bits)
        y = by_ryser(bits)
        if x != y:
            raise AssertionError((bits, x, y))
        count_a[abs(x)] += 1
        count_b[abs(y)] += 1
        signed_a[x] += 1
    assert count_a == count_b == EXPECTED, (count_a, count_b)
    # Third count: quotient by permutations of four lower rows.
    # A multiset of four 4-bit row patterns has weight 4!/prod multiplicity!.
    weighted = Counter()
    for patterns in combinations_with_replacement(range(16), 4):
        bits = sum(r << (4 * i) for i, r in enumerate(patterns))
        multiplicities = Counter(patterns)
        weight = factorial(4)
        for v in multiplicities.values():
            weight //= factorial(v)  # factorial parts always divide sequentially here
        weighted[abs(by_ryser(bits))] += weight
    assert weighted == EXPECTED, weighted
    assert sum(count_a.values()) == MASK_COUNT
    assert sum(v * k * k for k, v in count_a.items()) == MASK_COUNT * 120
    first = Fraction(sum(k * v for k, v in count_a.items()), MASK_COUNT)
    zero = Fraction(count_a[0], MASK_COUNT)
    assert first == Fraction(33045, 4096), first
    assert zero == Fraction(2525, 8192), zero
    assert signed_a[120] == 1
    print('n=5 normalized 4x4 signs: 65536 EXACT classes')
    print('absolute_permanent:count', ' '.join(f'{k}:{count_a[k]}' for k in sorted(count_a)))
    print('first absolute moment / Fourier endpoint norm:', first)
    print('zero probability:', zero)
    print('second moment:', sum(k*k*v for k,v in count_a.items())//MASK_COUNT)
    print('full 25-bit Fourier zero count:', (1 << (2*N-1))*count_a[0])
    print('full 25-bit Fourier support size:', (1 << (N*N))-(1 << (2*N-1))*count_a[0])
    print('THREE_ENUMERATION_CERTIFICATES_PASS')


if __name__ == '__main__':
    main()
