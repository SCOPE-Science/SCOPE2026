#!/usr/bin/env python3
"""Supplementary finite exact checks of the sampled resolvent circle and clock periods.

No finite test proves the functional-analytic or infinite-clock assertions.
"""
from fractions import Fraction as F
from math import factorial

count=0
for alpha in range(1, 15):
    for beta in range(-6, 7):
        for x in range(-25, 26):
            den=alpha**2+(beta-x)**2
            re=F(alpha,den)
            im=F(x-beta,den)
            center=F(1,2*alpha)
            assert (re-center)**2+im**2 == center**2
            count+=1

for n in range(1,15):
    period_units=factorial(n)  # period is 2*pi*period_units
    for j in range(1,n+1):
        assert period_units%factorial(j)==0
        count+=1
    if n<14:
        assert period_units%factorial(n+1)!=0
        count+=1

print(f"SAMPLED_RESOLVENT_EXACT_FINITE_OK {count}")
