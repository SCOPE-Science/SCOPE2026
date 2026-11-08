#!/usr/bin/env python3
"""Independent finite consistency test, NOT a proof of infinite assertions."""
from collections import Counter
from fractions import Fraction as F
from exact_profile import EXPECTED

N = 200_000

def digit_parity_base_three_halves(n):
    parity = 0
    while n:
        d = (2 * n) % 3
        parity ^= d & 1
        n = (2 * n - d) // 3
    return parity

x = bytearray(digit_parity_base_three_halves(n) for n in range(N+1))
y_direct = bytearray(x[i] ^ x[i+1] for i in range(N))
y_toeplitz = bytearray(N)
maprank = {2:0, 4:1, 7:2, 8:3}
for i in range(N):
    q, r = divmod(i, 9)
    if r in (0,3,6): y_toeplitz[i] = 0
    elif r in (1,5): y_toeplitz[i] = 1
    else: y_toeplitz[i] = y_toeplitz[4*q+maprank[r]]
assert y_direct == y_toeplitz
positions = [i for i in range(N) if y_direct[i] == 1]
lengths = [b-a for a,b in zip(positions,positions[1:])]
assert set(lengths) == set(range(1, 6))
counts = Counter(zip(lengths,lengths[1:]))
num = len(lengths)-1
for a in range(1,6):
    for b in range(1,6):
        expected = F(EXPECTED[a-1][b-1], 108)
        observed = F(counts[a,b], num)
        assert abs(observed - expected) < F(1, 100), (a,b,observed,expected)
print('INDEPENDENT_PREFIX_OK',N,'run_pairs',num)
print('observed_5x5:', tuple(tuple(counts[a,b] for b in range(1,6)) for a in range(1,6)))
