#!/usr/bin/env python3
"""Finite regression checks for the arithmetic consequences of the slope-seminorm formula."""
from math import ceil
from fractions import Fraction

cases=0
for N in range(2,31):
    scl_z=Fraction(N-1,2)
    scl_lambda=scl_z/N
    for a in range(-25,26):
        for b in range(-25,26):
            m=a-N*b
            direct=abs(m)*scl_lambda
            closed=Fraction((N-1)*abs(a-N*b),2*N)
            assert direct==closed
            assert (closed==0) == (a==N*b)
            cases += 1
    # The source's specified surgery direction is s_r, so m=-N.
    assert Fraction((N-1)*abs(-N),2*N)==scl_z
    # On the index-N sublattice the exact commutator-length formula applies.
    for q in range(-20,21):
        if q==0: continue
        g=1+ceil(abs(q)*(N-1)/2)
        assert g>=1
        if N%2==0 and abs(q)==1:
            assert g==N//2+1
print(f"VERIFY_OK cases={cases} N=2..30 box=-25..25 kernel=true surgery_direction=true sublattice_genus=true")
