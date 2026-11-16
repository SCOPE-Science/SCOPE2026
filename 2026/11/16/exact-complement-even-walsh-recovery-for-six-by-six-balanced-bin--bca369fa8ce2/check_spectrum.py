"""Independent exact verifier: column-first enumeration and vectorized Walsh transform.
Run with Python 3 plus NumPy: python check_spectrum.py
Memory use is roughly 410 MB; every arithmetic operation is integral.
"""
from itertools import combinations
import numpy as np

N = 6
D = 25
SIZE = 1 << D
col_patterns = [sum(1 << i for i in triple) for triple in combinations(range(N), 3)]
frequency_counts = np.zeros(SIZE, dtype=np.int32)
remaining = [3] * N
number_tables = 0

def enumerate_columns(col, block_mask):
    global number_tables
    if col == N:
        if all(k == 0 for k in remaining):
            frequency_counts[block_mask] += 1
            number_tables += 1
        return
    for pattern in col_patterns:
        if any((pattern >> r) & 1 and remaining[r] == 0 for r in range(N)):
            continue
        for r in range(N):
            remaining[r] -= (pattern >> r) & 1
        next_mask = block_mask
        if col:
            for r in range(1, N):
                if (pattern >> r) & 1:
                    next_mask |= 1 << (5*(r-1)+col-1)
        enumerate_columns(col+1, next_mask)
        for r in range(N):
            remaining[r] += (pattern >> r) & 1

enumerate_columns(0, 0)
assert number_tables == 297200
assert np.count_nonzero(frequency_counts) == number_tables
for bit in range(D):
    step = 1 << bit
    slabs = frequency_counts.reshape(-1, 2*step)
    left = slabs[:, :step].copy()
    right = slabs[:, step:].copy()
    slabs[:, :step] = left + right
    slabs[:, step:] = left - right

freq = np.arange(SIZE, dtype=np.uint32)
odd = np.zeros(SIZE, dtype=np.bool_)
for bit in range(D):
    odd ^= (freq >> bit & 1).astype(np.bool_)
assert np.all(frequency_counts[odd] == 0)
nonzero_even = frequency_counts[~odd]
assert len(nonzero_even) == (1 << 24)
assert np.all(nonzero_even % 32 == 16)
assert np.min(np.abs(nonzero_even)) == 16
assert np.sum(frequency_counts.astype(np.int64)**2, dtype=np.int64) == SIZE * number_tables
print('tables=297200 characters=33554432 zeros=16777216 all_even_residue=16_mod_32 min_nonzero=16 PASS')
