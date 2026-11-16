"""Exact order-five derangement Walsh certificate; Python 3 standard library only.

Two independent checks: (a) gauge-normalized 2^11 signed permanents and
(b) complete length-2^20 fast Walsh-Hadamard transform of the indicator.
"""
from itertools import permutations
from collections import Counter
from fractions import Fraction

N = 5
EDGES = [(i, j) for i in range(N) for j in range(N) if i != j]
TREE = {(0, j) for j in range(1, N)} | {(i, 0) for i in range(1, N)} | {(1, 2)}
FREE = [e for e in EDGES if e not in TREE]
DERANGEMENTS = [p for p in permutations(range(N)) if all(p[i] != i for i in range(N))]
EXPECT = {0: 338, 2: 504, 4: 405, 6: 260, 8: 130,
          10: 240, 12: 90, 16: 60, 22: 20, 44: 1}
assert len(EDGES) == 20 and len(TREE) == 9 and len(FREE) == 11
assert len(DERANGEMENTS) == 44

# The monomials of the signed permanent, encoded by 11 free signs.
FREE_INDEX = {e: k for k, e in enumerate(FREE)}
FREE_MONOMIALS = [sum(1 << FREE_INDEX[(i, p[i])] for i in range(N)
                      if (i, p[i]) in FREE_INDEX)
                  for p in DERANGEMENTS]
hist_gauge = Counter()
for mask in range(1 << 11):
    value = sum(-1 if (mask & m).bit_count() & 1 else 1
                for m in FREE_MONOMIALS)
    hist_gauge[abs(value)] += 1
assert dict(hist_gauge) == EXPECT, (hist_gauge, EXPECT)
assert sum(hist_gauge.values()) == 2048

# Independent direct full Walsh transform in 20 off-diagonal coordinates.
M = 1 << 20
f = [0] * M
edge_index = {e: k for k, e in enumerate(EDGES)}
for p in DERANGEMENTS:
    word = 0
    for i in range(N):
        word ^= 1 << edge_index[(i, p[i])]
    assert f[word] == 0
    f[word] = 1
assert sum(f) == 44
step = 1
while step < M:
    span = 2 * step
    for begin in range(0, M, span):
        for j in range(begin, begin + step):
            a, b = f[j], f[j + step]
            f[j], f[j + step] = a + b, a - b
    step = span
hist_direct = Counter(map(abs, f))
assert hist_direct == {x: count * (1 << 9) for x, count in EXPECT.items()}
assert sum(hist_direct.values()) == M
assert sum(x * x * count for x, count in hist_direct.items()) == 44 * M

# Reinsert the five diagonal frequencies, unused by the derangement support.
zero_count = hist_direct[0] * (1 << 5)
rank = (M - hist_direct[0]) * (1 << 5)
assert (zero_count, rank) == (5537792, 28016640)
assert zero_count + rank == (1 << 25)
mean_abs = Fraction(sum(x * count for x, count in hist_direct.items()), M)
assert mean_abs == Fraction(1269, 256)
assert min(x for x in hist_direct if x > 0) == 2
assert Fraction(zero_count, 1 << 25) == Fraction(169, 1024)
assert Fraction(rank, 1 << 25) == Fraction(855, 1024)
print('DERANGEMENT_FIVE_EXACT_PASS')
print('gauge_2048_histogram', sorted(hist_gauge.items()))
print('all_20_binary_frequencies', M, 'diagonal_multiplier', 32)
print('zero_count', zero_count, 'rank', rank, 'min_positive', 2)
print('projection_endpoint_norm', mean_abs)
