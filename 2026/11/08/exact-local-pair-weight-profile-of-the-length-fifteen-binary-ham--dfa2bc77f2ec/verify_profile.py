#!/usr/bin/env python3
"""Exact finite enumeration of the local pair-weight profile of Hamming(15)."""
from functools import lru_cache
from fractions import Fraction
from math import factorial

N = 15
FULL = (1 << N) - 1
EXPECTED = (1642251264, 2567162880, 1512023040, 434319360, 65617920, 5492736, 153600)
CODE_COUNTS = (17106784, 26741280, 15750240, 4524160, 683520, 57216, 1600)

@lru_cache(maxsize=None)
def completions(mask, prev, last):
    if mask == FULL:
        return (0,) * (int((prev ^ last) == 1) + int((last ^ 1) == 2)) + (1,)
    result = [0] * 16
    unused = FULL ^ mask
    while unused:
        bit = unused & -unused
        unused -= bit
        nxt = bit.bit_length()
        shift = int((prev ^ last) == nxt)
        for i, count in enumerate(completions(mask | bit, last, nxt)):
            result[i + shift] += count
    while result and result[-1] == 0:
        result.pop()
    return tuple(result)

def score(columns):
    assert len(columns) == N and sorted(columns) == list(range(1, N + 1))
    return sum((columns[i] ^ columns[(i + 1) % N]) == columns[(i + 2) % N]
               for i in range(N))

def main():
    got = completions(3, 1, 2)
    assert got == EXPECTED, (got, EXPECTED)
    assert sum(got) == factorial(13)
    assert all(x % 96 == 0 for x in got)
    actual_codes = tuple(x // 96 for x in got)
    assert actual_codes == CODE_COUNTS
    assert sum(actual_codes) == factorial(15) // 20160
    assert Fraction(sum(i * v for i, v in enumerate(actual_codes)), sum(actual_codes)) == Fraction(15, 13)
    assert Fraction(sum(i * (i - 1) * v for i, v in enumerate(actual_codes)), sum(actual_codes)) == Fraction(150, 143)
    zero = (1, 2, 4, 3, 5, 7, 6, 8, 9, 10, 11, 12, 14, 13, 15)
    six = (1, 2, 3, 4, 5, 8, 13, 6, 10, 12, 11, 7, 9, 14, 15)
    assert score(zero) == 0 and score(six) == 6
    print('VERIFY_OK', actual_codes, 'states', completions.cache_info().currsize)

if __name__ == '__main__':
    main()
