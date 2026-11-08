#!/usr/bin/env python3
"""Finite arithmetic checks for the power-of-two Strehl–Franel coefficients."""
from math import comb

def valuation_two(n):
    if n == 0:
        raise ValueError("nonzero input required")
    return (n & -n).bit_length() - 1

def check(m):
    n = 1 << m
    d = n // 2
    c = [comb(n,j)**2 * comb(2*(n-j),n) for j in range(d+1)]
    assert len(c) == d+1 and c[-1] > 0
    assert all(z % 2 == 0 for z in c)
    assert valuation_two(c[0]) == 1
    assert valuation_two(c[-1]) == 2
    assert all(z % 4 == 0 for z in c[1:])
    g = [z//2 for z in c[::-1]]
    assert g[-1] % 2 == 1
    assert all(z % 2 == 0 for z in g[:-1])
    assert g[0] % 4 == 2
    return d

if __name__ == '__main__':
    degs = [check(m) for m in range(1,9)]
    print('VERIFY_OK checked_m=1..8 degrees=' + ','.join(map(str,degs)))
