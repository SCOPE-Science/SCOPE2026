#!/usr/bin/env python3
"""Exact independent labeled-component check of the maximal bipartite formula.
Run: python3 verify_bipartite_triangular_series.py
"""
from math import comb, factorial
from fractions import Fraction

MAX_N = 30
A = [0]*(MAX_N+1)  # labeled partitions into even cycles of length >= 4
A[0] = 1
for n in range(1,MAX_N+1):
    for ell in range(4,n+1,2):
        A[n] += comb(n-1,ell-1)*factorial(ell-1)//2*A[n-ell]

c = [Fraction(0) for _ in range(MAX_N//2+1)]
c[0] = Fraction(1)
for m in range(1,len(c)):
    c[m] = sum(c[:m-1],Fraction(0))/(4*m)
    assert c[m] == Fraction(A[2*m], factorial(2*m))

small = {2:{1:1},3:{2:3},4:{4:3},5:{4:75},
         6:{5:45,6:60},7:{6:3255},8:{7:1680,8:2835},
         9:{8:244755},10:{9:127575,10:219240}}
for n in range(2,MAX_N+1):
    coefficient_n = A[n]
    coefficient_n_minus_one = n*A[n-1]+comb(n,2)*A[n-2]
    for ell in range(3,n+1,2):
        coefficient_n_minus_one += comb(n,ell)*(factorial(ell)//2)*A[n-ell]
    if n%2==0:
        m=n//2
        expected_n = factorial(n)*c[m]
        expected_nm1 = factorial(n)*c[m-1]/2
    else:
        m=(n-1)//2
        expected_n = 0
        expected_nm1=factorial(n)*(c[m]+sum(c[:m],Fraction(0))/2)
    assert coefficient_n == expected_n
    assert coefficient_n_minus_one == expected_nm1
    observed={k:v for k,v in [(n-1,coefficient_n_minus_one),(n,coefficient_n)] if v}
    if n in small: assert observed == small[n],(n, observed,small[n])
    if n>=3 and n%2==1: assert set(observed)=={n-1}
    if n>=6 and n%2==0: assert set(observed)=={n-1,n}
print('VERIFY_OK exact_component_recurrence_and_series n=2..30',
      'odd_well_bicovered=PASS even_two_sizes=PASS')
