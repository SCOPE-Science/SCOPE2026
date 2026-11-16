#!/usr/bin/env python3
"""Independent complete census using cyclic first differences and real coordinates."""
from itertools import product
from collections import Counter

# 2 Re(zeta^e), 2 Im(zeta^e)/sqrt(3), for e=0,...,5.
RE = (2, 1, -1, -2, -1, 1)
IM = (0, 1, 1, 0, -1, -1)
mask_counts = Counter()
support_counts = Counter()
for free_diffs in product(range(6), repeat=6):
    # All cyclic first-difference strings must have sum zero modulo 6.
    diffs = ((-sum(free_diffs)) % 6,) + free_diffs
    values = [0] * 7
    for t in range(1, 7):
        values[t] = (values[t-1] + diffs[t]) % 6
    mask = 0
    for x in range(1, 4):
        exps = [sum(diffs[(t-j) % 7] for j in range(x)) % 6 for t in range(7)]
        if sum(RE[e] for e in exps) == 0 and sum(IM[e] for e in exps) == 0:
            mask |= 1 << (x-1)
    mask_counts[mask] += 1
    support_counts[7 if all(v == 0 for v in values) else 43-2*mask.bit_count()] += 1
assert sum(mask_counts.values()) == 6**6
assert mask_counts == {0: 41868, 1: 1512, 2: 1512, 4: 1512,
                       3: 84, 5: 84, 6: 84}
assert support_counts == {7: 1, 39: 252, 41: 4536, 43: 41867}
print('PASS: independent first-difference census', dict(sorted(support_counts.items())))
