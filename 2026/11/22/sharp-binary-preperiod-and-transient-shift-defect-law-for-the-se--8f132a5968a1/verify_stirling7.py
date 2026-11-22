#!/usr/bin/env python3
"""Independent finite tests of the seventh Stirling-column shift theorem.
Uses standard-library integer arithmetic; it is not a proof for arbitrary depth.
"""
from collections import Counter
from fractions import Fraction
from math import comb


def stirling_mod(end, modulus):
    s = [1] + [0] * 7
    out = [0] * (end + 1)
    for n in range(1, end + 1):
        for j in range(7, 0, -1):
            s[j] = (s[j - 1] + j * s[j]) % modulus
        s[0] = 0
        out[n] = s[7]
    return out


def v2(a):
    if a == 0:
        return None
    return ((a & -a).bit_length() - 1)


def defect_v2(n, k, depth=40):
    # Compute 7! times the actual difference modulo a sufficiently high power.
    # Dividing out the exact factor 2^4 in 7! gives its valuation.
    modulus = 1 << (k + depth + 4)
    period = 1 << (k + 1)
    z = sum((-1) ** (7-j) * comb(7, j) * pow(j, n, modulus) *
            (pow(j, period, modulus) - 1) for j in range(1, 8)) % modulus
    if not z:
        raise AssertionError('valuation precision too small')
    return v2(z) - 4


def main():
    tests = 0
    assert Fraction(48+21*24+35*8, 5040) == Fraction(52, 315); tests += 1
    assert Fraction(7*48+105*24+105*8, 5040) == Fraction(11, 15); tests += 1
    assert Fraction(48**2+21*24**2+35*8**2, 5040) == Fraction(208, 63); tests += 1
    assert Fraction(7*48**2+105*24**2+105*8**2, 5040) == Fraction(248, 15); tests += 1
    for k in range(1, 12):
        modulus = 1 << k
        period = 1 << (k + 1)
        onset = max(7, k + 2 + (k % 2))
        seq = stirling_mod(onset + 3 * period + 20, modulus)
        for n in range(onset, onset + period + 20):
            assert seq[n] == seq[n + period], (k, n, 'period')
            tests += 1
        if onset > 7:
            assert seq[onset-1] != seq[onset-1+period], (k, 'sharp onset')
            tests += 1
        # Independently confirm the least period using the recurrent values.
        for d in [1 << i for i in range(k+1)]:
            assert any(seq[n] != seq[n+d] for n in range(onset, onset + period)), (k, d)
            tests += 1
        fibers = Counter(seq[n] for n in range(onset, onset + period))
        r = min(k, 2)
        for y in range(modulus):
            predicted = 1 + ((1 << r) if (y % (1 << r) == 0) else 0)
            assert fibers[y] == predicted, (k, y, fibers[y], predicted)
            tests += 1
        for n in range(7, k + 45):
            v = defect_v2(n, k)
            if n & 1:
                if n == k+3:
                    assert v >= k+1, (k, n, v)
                else:
                    assert v == min(k, n-3), (k, n, v)
            else:
                if n == k+4:
                    assert v >= k+3, (k, n, v)
                else:
                    assert v == min(k+2, n-2), (k, n, v)
            tests += 1
    print(f'PASS: {tests} exact integer assertions; k=1..11, ' 
          'periods, sharp onset, complete fibers, nonresonant and resonant checks.')


if __name__ == '__main__':
    main()
