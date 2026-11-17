#!/usr/bin/env python3
"""Exact finite diagnostics for star heat Lipschitz norm (standard library)."""
from fractions import Fraction as F
from itertools import product

def star_direct(m, q, d):
    # Separate the constant, central-versus-leaf, and leaf-transverse spectral modes.
    s=q**(m+1)
    center=F(0)
    leaves=d[:]  # a representative with zero center
    leafmean=sum(leaves,F(0))/m
    grandmean=(center+sum(leaves,F(0)))/(m+1)
    center_new=grandmean + s*F(m,m+1)*(center-leafmean)
    leaf_new=[grandmean + q*(leaf-leafmean) + s*F(1,m+1)*(leafmean-center) for leaf in leaves]
    return [v-center_new for v in leaf_new]

def star_formula(m,q,d):
    s=q**(m+1)
    mean=sum(d,F(0))/m
    return [q*(v-mean)+s*mean for v in d]

rows=0; spectral=0
for m in range(1,10):
    for q in [F(1,2),F(2,3),F(3,4),F(4,5)]:
        s=q**(m+1)
        expected=F(2*(m-1),m)*q-F(m-2,m)*s
        max_ratio=F(0)
        for digits in product([-1,1],repeat=m):
            d=list(map(F,digits))
            a=star_direct(m,q,d)
            b=star_formula(m,q,d)
            assert a==b, (m,q,d,a,b)
            spectral+=1
            max_ratio=max(max_ratio,max(map(abs,a)))
        assert max_ratio==expected,(m,q,max_ratio,expected)
        rows+=1
assert rows==36
print('EXACT_SPECTRAL_HEAT_VS_EDGE_EVOLUTION_CHECKS_PASSED',spectral)
print('EXHAUSTIVE_SHARP_ROW_SUM_CHECKS_PASSED',rows)
print('ALL_STAR_HEAT_LIPSCHITZ_CHECKS_PASSED')
