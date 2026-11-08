#!/usr/bin/env python3
"""Exact integer/rational polynomial consistency tests for quasi-Galois three-centre lines.
The uniform all-degree theorem additionally requires the argument in RESULT.md.
"""
from fractions import Fraction
from math import comb, factorial

def trim(p):
    p=list(p)
    while p and p[-1]==0: p.pop()
    return p

def remainder(a,b):
    a=trim(a); b=trim(b)
    assert b
    while len(a)>=len(b) and a:
        q=a[-1]/b[-1]; i=len(a)-len(b)
        for j,co in enumerate(b): a[j+i]-=q*co
        a=trim(a)
    return a

def monic_gcd(a,b):
    a=[Fraction(v) for v in a];b=[Fraction(v) for v in b]
    while b:
        a,b=b,remainder(a,b)
    return [v/a[-1] for v in a]

def h_coeffs(d):
    eps=(-1)**d
    return trim([Fraction(comb(d,k)+(eps if k in (0,d) else 0)) for k in range(d+1)])

for d in range(4,41):
    h=h_coeffs(d)
    derivative=[i*h[i] for i in range(1,len(h))]
    actual=monic_gcd(h,derivative)
    expected=[Fraction(1),Fraction(1),Fraction(1)] if d%3==1 else [Fraction(1)]
    assert actual==expected, (d, actual,expected)
    if d%2: assert len(h)==d and h[-1]==d
    else: assert len(h)==d+1 and h[-1]==2
for N in range(3,9):
    for d in (4,5,6,7,10,13):
        triad_lines=comb(N,3)*d*d
        rich_line_count=comb(N,2)+triad_lines
        if d%3==1:
            contacts=2*triad_lines
            group_order=factorial(N)*d**(N-1)
            stabilizer=3*factorial(N-3)*d**(N-3)
            assert group_order == contacts*stabilizer
        assert rich_line_count>comb(N,2)
print('GCD_ALL_DEGREES_4_TO_40_OK')
print('ORBIT_COUNTS_N_3_TO_8_OK')
print('CERTIFICATE_OK')
