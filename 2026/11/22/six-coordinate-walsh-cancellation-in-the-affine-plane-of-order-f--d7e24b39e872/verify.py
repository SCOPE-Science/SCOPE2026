#!/usr/bin/env python3
"""Exact Walsh spectrum of rank-three affine geometry AG(2,4).

Run: python verify.py
Python standard library only, no external data.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb

N = 16
LENGTH = 1 << N

def gf4_mul(a, b):
    c = 0
    for j in range(2):
        if (b >> j) & 1:
            c ^= a << j
    if c & 8:
        c ^= 0b1110
    if c & 4:
        c ^= 0b0111
    assert 0 <= c < 4
    return c

def point_id(x, y):
    return 4*x + y

# First independent incidence construction: slope and intercept.
lines = []
for slope in range(4):
    for intercept in range(4):
        lines.append(frozenset(point_id(x, gf4_mul(slope, x) ^ intercept)
                               for x in range(4)))
for x in range(4):
    lines.append(frozenset(point_id(x, y) for y in range(4)))
assert len(set(lines)) == 20 and all(len(line) == 4 for line in lines)
line_masks = {sum(1 << i for i in line) for line in lines}

# Second incidence construction: one line per unordered pair via affine displacement.
independent_line_masks = set()
for a, b in combinations(range(N), 2):
    ax, ay = divmod(a, 4)
    bx, by = divmod(b, 4)
    dx, dy = ax ^ bx, ay ^ by
    line = {point_id(ax ^ gf4_mul(t, dx), ay ^ gf4_mul(t, dy))
            for t in range(4)}
    assert len(line) == 4 and a in line and b in line
    independent_line_masks.add(sum(1 << i for i in line))
assert independent_line_masks == line_masks
assert len(independent_line_masks) == 20
assert all(sum((line >> i) & 1 for line in line_masks) == 5 for i in range(N))
assert all(sum(((line >> i) & 1) and ((line >> j) & 1)
               for line in line_masks) == 1 for i,j in combinations(range(N),2))

collinear = {tuple(sorted(triple)) for line in lines
             for triple in combinations(line, 3)}
assert len(collinear) == 80
bases = [triple for triple in combinations(range(N), 3)
         if triple not in collinear]
assert len(bases) == 480
assert all(sum(i in triple for triple in bases) == 90 for i in range(N))
assert all(sum(i in triple and j in triple for triple in bases) == 12
           for i,j in combinations(range(N),2))

# Direct complete Walsh-Hadamard transform of basis incidence distribution.
walsh = [0] * LENGTH
for triple in bases:
    walsh[sum(1 << i for i in triple)] += 1
for bit in range(N):
    half = 1 << bit
    for left in range(0, LENGTH, 2*half):
        for offset in range(half):
            a,b = left+offset,left+offset+half
            u,v = walsh[a],walsh[b]
            walsh[a],walsh[b] = u+v,u-v
assert walsh[0] == 480

# Independent incidence-moment formula, calculated for every single frequency.
# Exactly 90 bases contain a given point, 12 contain a given pair.
zero_hist = Counter()
geometry_zero_hist = Counter()
for freq, val in enumerate(walsh):
    k = freq.bit_count()
    t = sum(comb((freq & lm).bit_count(), 3) for lm in line_masks)
    expected = 480-180*k+48*comb(k,2)-8*(comb(k,3)-t)
    assert val == expected, (freq,val,expected)
    if val == 0:
        zero_hist[k] += 1
        signature = tuple(sum((freq & lm).bit_count() == j for lm in line_masks)
                          for j in range(5))
        geometry_zero_hist[(k,signature)] += 1
        if k == 6:
            candidates = []
            for lm in line_masks:
                if (freq & lm) == lm:
                    ext = freq ^ lm
                    if ext.bit_count() != 2:
                        continue
                    # The line through the two exterior points meets the selected full line.
                    if any((ext & other) == ext and (other & lm).bit_count() == 1
                           for other in line_masks):
                        candidates.append(lm)
            assert len(candidates) == 1, freq

expected_zero_hist = {6:960,8:4230,10:960}
assert dict(zero_hist) == expected_zero_hist
# Weight ten signatures are complement-reflected; weight eight signatures symmetric.
assert {sig:n for (k,sig),n in geometry_zero_hist.items() if k == 8} == {
    (1,4,10,4,1):4080,(0,8,4,8,0):120,(2,0,16,0,2):30}
assert zero_hist[6] == 20 * (comb(12,2) - 3*comb(4,2)) == 960

abs_distribution = Counter(abs(v) for v in walsh)
assert dict(sorted(abs_distribution.items())) == {
  0:6150,4:10560,8:6960,12:10880,16:10320,20:9216,
  24:8960,28:960,40:96,48:40,76:960,84:160,
  168:240,300:32,480:2}
assert sum(abs_distribution.values()) == LENGTH
assert walsh.count(0) == 6150
assert min(abs(v) for v in walsh if v) == 4
assert sum(v!=0 for v in walsh) == 59386
assert all(walsh[freq ^ (LENGTH-1)] == -walsh[freq] for freq in range(LENGTH))

# Sharp projection norm: translation-average any projection onto the range;
# the unique translation-invariant projection has the multiplier 1_{W != 0}.
projection_kernel_numerator = [int(v!=0) for v in walsh]
for bit in range(N):
    half = 1 << bit
    for left in range(0,LENGTH,2*half):
        for offset in range(half):
            a,b = left+offset,left+offset+half
            u,v = projection_kernel_numerator[a],projection_kernel_numerator[b]
            projection_kernel_numerator[a],projection_kernel_numerator[b] = u+v,u-v
assert projection_kernel_numerator[0] == 59386
endpoint_norm = Fraction(sum(abs(x) for x in projection_kernel_numerator),LENGTH)
assert endpoint_norm == Fraction(558109,16384)
assert Fraction(max(abs(v) for v in walsh),min(abs(v) for v in walsh if v)) == 120
print('PASS: 20 independently verified lines, 480 bases, 65536 exact Walsh coefficients')
print('rank=59386; nullity=6150; first nullity degree=6 with 960 line-plus-transversal witnesses')
print('absolute-spectrum',sorted(abs_distribution.items()))
print('zero weights',sorted(zero_hist.items()))
print('zero degree-eight geometries', sorted((s,n) for (k,s),n in geometry_zero_hist.items() if k == 8))
print('sharp endpoint projection norm=',endpoint_norm,'; sharp positive-spectrum condition number=120')
