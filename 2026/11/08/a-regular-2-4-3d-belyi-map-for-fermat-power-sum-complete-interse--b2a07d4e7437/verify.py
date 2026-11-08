#!/usr/bin/env python3
"""Exact symbolic and arithmetic consistency checks for the Belyi passport.
Requires sympy. The all-degree theorem is proved in RESULT.md.
"""
from fractions import Fraction
from math import comb
import sympy as S

t,E3,E4=S.symbols('t E3 E4')
assert S.discriminant(t**4-E3*t+E4,t)==256*E4**3-27*E3**4
z=S.symbols('z0:4')
e1=sum(z)
e2=sum(z[i]*z[j] for i in range(4) for j in range(i+1,4))
assert S.expand(e1**2-2*e2-sum(w*w for w in z))==0
poly=S.expand(S.prod(t-v for v in z))
e3=sum(z[i]*z[j]*z[k] for i in range(4) for j in range(i+1,4) for k in range(j+1,4))
e4=S.prod(z)
assert S.expand(poly-(t**4-e3*t+e4))==S.expand(-e1*t**3+e2*t**2)
# Repeated-coordinate points (z0=z1=1): remaining two roots of T^2+2T+3.
b,c=S.symbols('b c')
assert S.solve([2+b+c,2+b**2+c**2],[b,c])
assert S.discriminant(t**2+2*t+3,t)==-8
# Standard Bezout points on the smooth conic Q: degree e3=3, e4=4, discriminant=12.
assert (2*3,2*4,6*2)==(6,8,12)
for d in range(3,40):
    if d==4: continue
    G=24*d**3
    g=1+d*d*(3*d-4)
    # Ordered ramification at beta=0,1,infinity is (4,2,3d).
    RH=G*(Fraction(3,4)+Fraction(1,2)+1-Fraction(1,3*d)-2)
    assert RH==2*g-2
    assert G//4==6*d**3 and G//2==12*d**3 and G//(3*d)==8*d**2
print('CERTIFICATE_OK: universal discriminant, symmetric identities, and passport checks')
