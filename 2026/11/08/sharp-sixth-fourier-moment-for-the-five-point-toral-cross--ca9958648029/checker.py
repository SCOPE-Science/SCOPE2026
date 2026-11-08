#!/usr/bin/env python3
"""Exact integer-convolution checks for the five-frequency torus sixth moment.

Only the Python standard library is required. Mathematical proof of the
universal inequality and equality classification is in RESULT.md.
"""
from collections import defaultdict
from fractions import Fraction
from math import sqrt

# (frequency_x,frequency_y,exponent_A,exponent_X,exponent_Y).
terms = [(0,0,1,0,0),(1,0,0,1,0),(-1,0,0,1,0),
         (0,1,0,0,1),(0,-1,0,0,1)]
expanded = {(0,0,0,0,0):1}
for _ in range(3):
    nxt=defaultdict(int)
    for key, coeff in expanded.items():
        for t in terms:
            nxt[tuple(key[i]+t[i] for i in range(5))] += coeff
    expanded=dict(nxt)
by_freq=defaultdict(list)
for key,coef in expanded.items():
    by_freq[key[:2]].append((key[2:],coef))
moment=defaultdict(int)
for poly in by_freq.values():
    for powers1,c1 in poly:
        for powers2,c2 in poly:
            moment[tuple(powers1[i]+powers2[i] for i in range(3))]+=c1*c2
moment={k:v for k,v in moment.items() if v}
expected={(6,0,0):1, (4,2,0):30, (4,0,2):30,
          (2,4,0):90, (2,2,2):360, (2,0,4):90,
          (0,6,0):20, (0,4,2):180, (0,2,4):180,(0,0,6):20}
assert moment==expected, (moment,expected)
# On the energy-one slice, with all four arms equal, the exact moment is
# E(h)=(3*h-5)*(18*h*h-15*h-5)/4.
def E(h):
    return (3*h-5)*(18*h*h-15*h-5)/4
# Verify the polynomial at four distinct rational h (both are cubics).
for h in [Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(1)]:
    x2=(1-h)/4
    left=sum(coeff*h**(powers[0]//2)*x2**((powers[1]+powers[2])//2)
             for powers,coeff in expected.items())
    assert left==E(h), (h,left,E(h))
# Derivative: E'=3/2*(27h^2-45h+10), has exactly one root (0,1).
assert (27*Fraction(0)**2-45*Fraction(0)+10)>0
assert (27*Fraction(1)**2-45*Fraction(1)+10)<0
hstar=(15-sqrt(105))/18
M=Fraction(25,8)+Fraction(35,72)*sqrt(105)
assert 0<hstar<1 and abs(E(hstar)-M)<1e-12
assert E(hstar)>max(E(0),E(1))
print('FIVE_MODE_TORUS_L6_PASS moment_monomials=10 rational_tests=4 maximizer=unique')
print(f'optimal h={hstar:.15f} six_power_constant={M:.15f}')
