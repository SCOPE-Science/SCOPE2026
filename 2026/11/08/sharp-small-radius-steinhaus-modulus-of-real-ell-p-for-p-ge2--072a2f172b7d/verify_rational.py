#!/usr/bin/env python3
"""Finite exact-rational checks for scalar monotonicity and coefficient identity."""
from fractions import Fraction as F
count = 0
for p in (2, 4, 6):
    for k in range(-8, 9):
        for j in range(-8, 9):
            u, v = F(k, 7), F(j, 7)
            # At even integer p, |t|^(p-2)t equals t^(p-1).
            slack = (u**(p-1) - v**(p-1)) * (u-v) - F(1, 2**(p-2)) * (u-v)**p
            assert slack >= 0
            count += 1
    for s in (F(1, 8), F(1, 4), F(1, 2), F(3, 4)):
        d = 2*s
        assert 2*s**(p-1) == F(1,2**(p-2))*d**(p-1)
        count += 1
print('STEINHAUS_RATIONAL_GRID_OK', count)
