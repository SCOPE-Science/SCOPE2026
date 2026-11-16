#!/usr/bin/env python3
"""Independent exact convolution and collision checks for four geometric tones.
Run: python3 verify_geometric_first_resonance.py (Python >=3.9, stdlib only).
These finite checks corroborate, but do not replace, the proof for all bases.
"""
from collections import defaultdict
from itertools import product
from math import factorial


def factorial_multinomial(counts):
    ans = factorial(sum(counts))
    for x in counts:
        ans //= factorial(x)
    return ans


def compositions(total, n=4):
    if n == 1:
        yield (total,)
    else:
        for k in range(total + 1):
            for rest in compositions(total - k, n - 1):
                yield (k,) + rest


def diagonal(r):
    return sum(factorial_multinomial(v) ** 2 for v in compositions(r))


def direct_moment(base, r, coeffs):
    buckets = defaultdict(complex)
    for v in compositions(r):
        freq = sum(v[j] * base ** j for j in range(4))
        term = factorial_multinomial(v)
        for a, power in zip(coeffs, v):
            term *= a ** power
        buckets[freq] += term
    value = sum(abs(c) ** 2 for c in buckets.values())
    return round(value)


def expected_moment(base, coeffs):
    p = base + 1
    eta = [coeffs[j] ** base * coeffs[j + 1].conjugate() for j in range(3)]
    collision = 2 * p * (eta[0] * eta[1].conjugate() + eta[1] * eta[2].conjugate()).real
    collision += 2 * p * p * (eta[0] * eta[2].conjugate()).real
    return round(diagonal(p) + collision)


def main():
    count = 0
    for b in range(2, 7):
        p = b + 1
        for r in range(1, p):
            assert direct_moment(b, r, (1, 1, 1, 1)) == diagonal(r)
            count += 1
        # Frequencies are spaced enough for a non-aliased convolution.
        # All 256 exact Gaussian-unit phase arrays are tested when b <= 5.
        if b <= 5:
            for coeffs in product((1, -1, 1j, -1j), repeat=4):
                assert direct_moment(b, p, coeffs) == expected_moment(b, coeffs)
                count += 1
        # Exhaustive binary phases and exact sharp values.
        data = [direct_moment(b, p, c) for c in product((1, -1), repeat=4)]
        B = diagonal(p)
        assert min(data) == B - 2 * p * p
        assert max(data) == B + 2 * p * p + 4 * p
        count += 16
        # An exact combinatorial baseline and character-phase upper bound.
        assert direct_moment(b, p, (1, 1, 1, 1)) == B + 2 * p * p + 4 * p
        count += 1
    print(f'EXACT_FIRST_RESONANCE_CHECKS_PASS {count}')


if __name__ == '__main__':
    main()
