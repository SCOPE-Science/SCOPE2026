#!/usr/bin/env python3
"""Exact finite-cylinder difference-set certificates; Python 3 standard library only.
Run: python verify_differences.py
"""
from functools import lru_cache
from fractions import Fraction

@lru_cache(None)
def translations(m, n):
    if m == 0 or n == 0:
        return (0,)
    offset = (2**m - 1) * 3**(n-1)
    return tuple(sorted(set(translations(m-1, n)) |
                        {offset + x for x in translations(m, n-1)}))

def first_missing_positive_difference(m, n):
    a = translations(m, n)
    # Binary polynomial of the translation set. Shifting right by b
    # and bitwise-OR over b records all nonnegative differences a-b.
    packed = bytearray(a[-1]//8 + 1)
    for x in a:
        packed[x//8] |= (1 << (x%8))
    word = int.from_bytes(packed, 'little')
    differences = 0
    for b in a:
        differences |= word >> b
    # Since bit 0 is present, the carry in differences+1 skips every
    # consecutive 1 bit and lands at the first absent difference.
    first_gap = ((differences + 1) & -(differences + 1)).bit_length() - 1
    return len(a), a[-1], first_gap

assert first_missing_positive_difference(9,9) == (48620,5028751,3163277)
assert first_missing_positive_difference(11,5) == (4368,247687,92381)

def Q99(p): return 3163277*(p*(1-p))**9
def Q115(p): return 92381*p**11*(1-p)**5
assert Q99(Fraction(1,4)) < 1 < Q99(Fraction(13,50))
assert Q99(Fraction(2,3)) > 1
assert Q115(Fraction(2,3)) > 1
assert Q115(Fraction(6,7)) > 1 > Q115(Fraction(9,10))
# Thus unique alpha in (1/4,13/50) and unique high-branch beta
# in (6/7,9/10); monotonicity proves all interior weights.
print('PASS: two exact cylinder certificates and six rational endpoint inequalities')
