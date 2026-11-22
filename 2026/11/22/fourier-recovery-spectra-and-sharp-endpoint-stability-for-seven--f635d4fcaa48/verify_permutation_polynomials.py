#!/usr/bin/env python3
"""Exact arithmetic check for seven-point affine-plane Fourier directions."""
from itertools import permutations
from collections import Counter
from math import comb

P = 7
field = range(P)

def is_perm(vals):
    return len(set(vals)) == P

def paired_perm(coeff, slope):
    return is_perm([(coeff*pow(x, 4, P)+slope*x)%P for x in field])

# Independently enumerate all permutations and the polynomial family.
count_all = 0
nonlinear = set()
for f in permutations(field):
    if is_perm([(f[x]-x)%P for x in field]):
        count_all += 1
        nonlinear.add(f)

families = set()
for b in field:
    for slope in (2,3,4,5,6):
        families.add(tuple((b+slope*x)%P for x in field))
for eps in (1, -1):
    for a in field:
        for b in field:
            families.add(tuple((b+4*(x-a)+eps*pow((x-a)%P,4,P))%P for x in field))
assert count_all == 133 and len(families) == 133
assert families == nonlinear

permutation_slopes = {}
for A in range(1,P):
    Ds = tuple(D for D in field if paired_perm(A,D))
    permutation_slopes[A] = Ds
assert permutation_slopes == {1:(3,4),2:(1,6),3:(2,5),4:(2,5),5:(1,6),6:(3,4)}

# Three directions: 35 affine graphs, 98 non-affine graphs.
assert len(families.intersection(
    {tuple((b+c*x)%P for x in field) for b in field for c in (2,3,4,5,6)}
)) == 35

# Geometric inclusion-exclusion based on direction transversality.
triple_nonlines = count_all - 5*P
assert triple_nonlines == 98
pair_exact = 5040 - 6*triple_nonlines - 6*P
single_exact = P**P - 7*pair_exact - comb(7,2)*triple_nonlines - 7*P
hist = {7:8*P, 3:comb(8,3)*triple_nonlines,
        2:comb(8,2)*pair_exact, 1:8*single_exact}
hist[0] = comb(49,7)-sum(hist.values())
assert hist == {7:56,3:5488,2:123480,1:6324528,0:79447032}
print('orthomorphisms:', count_all)
print('quartic families:', 98)
print('polynomial coefficient table:', permutation_slopes)
print('blind-directions histogram:', dict(sorted(hist.items())))
print('Fourier-convolution-rank histogram:',
      {49-6*k:v for k,v in sorted(hist.items())})
print('total:',sum(hist.values()))
