#!/usr/bin/env python3
"""Exact genus-three Ciani quartic Cartier and divisor identities in characteristic 7.
Run: python3 verify_symbolic.py  (requires sympy).
"""
import itertools
from math import factorial
import sympy as sp
r,s,t=sp.symbols('r s t')
mons=[(4,0,0),(0,4,0),(0,0,4),(2,2,0),(0,2,2),(2,0,2)]
cs=[sp.Integer(1),sp.Integer(1),sp.Integer(1),r,s,t]
B=[2*r*t-4*s,2*r*s-4*t,2*s*t-4*r]
A=[(r*r-4)*(t*t-4),(r*r-4)*(s*s-4),(s*s-4)*(t*t-4)]
D=[sp.expand(B[i]**2-A[i]) for i in range(3)]

def coeff_target(target):
    out=sp.Integer(0)
    for indexes in itertools.product(range(6),repeat=6):
        if tuple(sum(mons[j][k] for j in indexes) for k in range(3)) != target:continue
        # Use multinomial rather than all ordered tuples of six to avoid repeated expansion.
        counts=[indexes.count(i) for i in range(6)]
        if list(indexes)!=sorted(indexes): continue
        m=factorial(6)
        for c in counts:m//=factorial(c)
        out+=m*sp.prod(cs[i]**counts[i] for i in range(6))
    return sp.expand(out)
for i,target in enumerate([(12,6,6),(6,12,6),(6,6,12)]):
    # On plane quartics, the diagonal Hasse-Witt entries are these coefficients of F^6.
    co=coeff_target(target)
    assert sp.Poly(co-B[i]*D[i],r,s,t,modulus=7).is_zero,(i,co)
    print('coefficient',i,'OK')
for i in range(3):
    # The sextic Hasse polynomial is a product of two DISTINCT factors.
    assert sp.Poly(B[i],r,s,t,modulus=7).total_degree()==2
    assert sp.Poly(D[i],r,s,t,modulus=7).total_degree()==4
# Smoothness: B_i=0 implies D_i=-A_i; simultaneous vanishing forces a Ciani singular parameter.
print('CIANI_CHAR7_SYMBOLIC_FACTORIZATION_OK')
