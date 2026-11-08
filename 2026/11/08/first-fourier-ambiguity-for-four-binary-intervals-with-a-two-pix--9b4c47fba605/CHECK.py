#!/usr/bin/env python3
"""Exact finite certificate for four occupied pixel runs and three gaps,
all seven feature widths at least two. Python >=3.10, no dependencies.
"""
from collections import defaultdict
from itertools import combinations
from math import comb

START, END = 14, 22
A = '1110011000111110000011'
B = '1110000011111001100011'

def run_tuples(n):
    # Every ordered positive 7-composition of n with all components >= 2.
    r = n - 14
    for cuts in combinations(range(1, r + 7), 6):
        stops = (0,) + cuts + (r + 7,)
        t = tuple(2 + stops[i+1] - stops[i] - 1 for i in range(7))
        assert len(t) == 7 and min(t) >= 2 and sum(t) == n
        yield t

def word(t):
    a, gap, b, gap2, c, gap3, d = t
    return '1'*a + '0'*gap + '1'*b + '0'*gap2 + '1'*c + '0'*gap3 + '1'*d

def runvector(w):
    out = []
    for char in w:
        if not out or out[-1][0] != char: out.append([char, 1])
        else: out[-1][1] += 1
    return tuple(v for _, v in out)

def bit_autocorr(w):
    bit = sum((1 << j) for j, q in enumerate(w) if q == '1')
    return tuple((bit & (bit >> k)).bit_count() for k in range(len(w)))

def pair_autocorr(w):
    support = [j for j, char in enumerate(w) if char == '1']
    return tuple(sum(y-x == k for x in support for y in support) for k in range(len(w)))

def conv(x, y):
    z = [0] * (len(x)+len(y)-1)
    for i,a in enumerate(x):
        for j,b in enumerate(y): z[i+j] += a*b
    return z

def base_poly_coeffs(w): return [int(c) for c in w]

records = []
for n in range(START, END + 1):
    classes = defaultdict(list)
    total = 0
    fixed = 0
    for t in run_tuples(n):
        total += 1
        if t == t[::-1]: fixed += 1
        if t > t[::-1]: continue
        w = word(t)
        assert len(w) == n and runvector(w) == t
        classes[bit_autocorr(w)].append(w)
    r = n - 14
    assert total == comb(r+6, 6)
    assert fixed == comb(r//2+3, 3)
    unoriented = (total + fixed)//2
    assert sum(map(len, classes.values())) == unoriented
    nontrivial = [v for v in classes.values() if len(v) > 1]
    records.append((n,total,unoriented,len(classes),len(nontrivial)))
    if n < 22:
        assert not nontrivial
    else:
        assert len(nontrivial) == 1 and len(nontrivial[0]) == 2
        exceptional = nontrivial[0]
        actual = {min(w,w[::-1]) for w in exceptional}
        claimed = {min(w,w[::-1]) for w in (A,B)}
        assert actual == claimed

assert sum(t[2] for t in records) == 3270
assert sum(t[1] for t in records) == 6435
assert all(pair_autocorr(w) == bit_autocorr(w) for w in (A, B))
assert bit_autocorr(A) == bit_autocorr(B)
assert A != B and A != B[::-1]
assert runvector(A) == (3,2,2,3,5,5,2)
assert runvector(B) == (3,5,5,2,2,3,2)
# A common signed factor and reversal of the second factor yield the
# 0/1 indicator polynomials.  The identity is exact over the integers.
F = [1,0,0,-1,0,1]
G = [int(k in set(range(0,7)) | set(range(12,17))) for k in range(17)]
assert conv(F,G) == base_poly_coeffs(A)
assert conv(F,G[::-1]) == base_poly_coeffs(B)
print('CHECK_OK', 'raw_compositions=6435', 'reversal_classes=3270',
      'first_span=22', 'exceptional_unordered_pairs=1')
for n, raw, classes, fibers, nc in records:
    print('SPAN',n,'compositions',raw,'reversal_classes',classes,
          'autocorrelation_fibers',fibers,'ambiguous_fibers',nc)
