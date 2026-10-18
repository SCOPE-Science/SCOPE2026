#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 80
N = 42
E = [0, 1]
for _ in range(2, 2 * N + 6):
    E.append(4 * E[-1] - E[-2])

pos = []
for n in range(2, N + 1):
    base = (E[2*n-1] - 1) // 2
    pos.append((base - 2*E[n-1], base + 2*E[n-1]))
assert pos[:4] == [(5, 9), (96, 112), (1425, 1485), (20160, 20384)]
for i, (lo, hi) in enumerate(pos[:-1]):
    assert 0 < lo < hi < pos[i+1][0]

neg = []
for m in range(2, N + 1):
    base = (E[2*m+1] + 1) // 2
    neg.append((base - 2*E[m+1], base + 2*E[m+1]))
assert neg[:3] == [(75, 135), (1344, 1568), (19855, 20691)]
assert 3 < 16 < neg[0][0]
for i, (lo, hi) in enumerate(neg[:-1]):
    assert lo < hi < neg[i+1][0]

sqrt3 = Decimal(3).sqrt()
lam = Decimal(2) + sqrt3
lam2 = lam * lam
p_lo, p_hi = pos[-2]
p_next_lo = pos[-1][0]
n_lo, n_hi = neg[-2]
n_next_lo = neg[-1][0]
within_pos = Decimal(p_hi) / Decimal(p_lo)
gap_pos = Decimal(p_next_lo) / Decimal(p_hi)
within_neg = Decimal(n_hi) / Decimal(n_lo)
gap_neg = Decimal(n_next_lo) / Decimal(n_hi)
assert abs(within_pos - Decimal(1)) < Decimal('1e-20')
assert abs(within_neg - Decimal(1)) < Decimal('1e-20')
assert abs(gap_pos - lam2) < Decimal('1e-18')
assert abs(gap_neg - lam2) < Decimal('1e-18')

print(
    'VERIFY_OK '
    f'positive_pairs={len(pos)} negative_pairs={len(neg)} '
    f'first_positive=5,9,96,112 first_negative=3,16,75,135 '
    f'within_pos={within_pos:.24f} gap_pos={gap_pos:.24f} '
    f'within_neg={within_neg:.24f} gap_neg={gap_neg:.24f} '
    f'lambda2={lam2:.24f}'
)
