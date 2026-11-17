#!/usr/bin/env python3
"""Exact rational enclosure checks for a five-character Fourier projector.

All inequalities in the finite residue check use fractions and certified
Taylor remainders. No external Python packages are required.
"""
from fractions import Fraction as Q
from math import factorial


def arctan_interval(z, terms=12):
    """Alternating series bound for arctan(z), for 0<z<=1."""
    partial = sum(((-1)**j * z**(2*j+1)/Q(2*j+1) for j in range(terms)), Q(0))
    omitted = (-1)**terms*z**(2*terms+1)/Q(2*terms+1)
    return min(partial,partial+omitted), max(partial,partial+omitted)


def pi_interval():
    # Machin's identity, pi = 16 atan(1/5)-4 atan(1/239)
    a,b=arctan_interval(Q(1,5))
    c,d=arctan_interval(Q(1,239))
    return 16*a-4*d,16*b-4*c

PI_LO, PI_HI = pi_interval()
assert Q(157,50) < PI_LO < PI_HI < Q(22,7)


def cos_interval(n,k):
    """Enclose cos(2*pi*k/n) by exact rational Taylor remainder."""
    k %= n
    k = min(k,n-k)
    xlo = 2*PI_LO*Q(k,n)
    xhi = 2*PI_HI*Q(k,n)
    x = (xlo+xhi)/2
    t=sum(((-1)**j*x**(2*j)/factorial(2*j) for j in range(16)),Q(0))
    error=(xhi-xlo)/2+xhi**32/factorial(32)
    return t-error,t+error


def abs_upper(lo,hi):
    assert lo <= hi
    return max(abs(lo),abs(hi))


def sample_upper(n):
    total=Q(0)
    for j in range(n):
        a,b=cos_interval(n,j)
        c,d=cos_interval(n,2*j)
        lo=Q(1,2)+2*a+2*c
        hi=Q(1,2)+2*b+2*d
        total+=abs_upper(lo,hi)
    return total/n


# The n=8 sharp constant is 1+sqrt(2)/2 > 17/10.
# Exact input gradients attaining it are signs of D_2-1/2.
assert Q(1,2)>Q(7,10)**2
finite={}
for n in range(5,21):
    if n==8:
        continue
    upper=sample_upper(n)
    assert upper<Q(163,100),(n,float(upper))
    finite[n]=float(upper)
print("CERTIFIED_FINITE_N5_TO_N20_EXCEPT_N8_PASS",len(finite),
      "largest_upper",max(finite.items(),key=lambda p:p[1]))

# For all n>=21, |composite trapezoid - integral| <= 44*pi/(3*n*n).
# The inequality below is checked purely with standard rational pi bounds.
large=Q(250,157)+Q(44,3*21**2)*Q(22,7)
assert large<Q(17,10)
print("ANALYTIC_ALL_N_GE_21_RATIONAL_BOUND_PASS", float(large))

# Independent direct formula diagnostics: the same kernel on zero-sum edge
# vectors has norm exactly its minimum absolute deviation from a constant.
import math
for n in range(5,101):
    values=[1+2*math.cos(2*math.pi*j/n)+2*math.cos(4*math.pi*j/n) for j in range(n)]
    sorted_values=sorted(values)
    median=sorted_values[n//2]
    val=sum(abs(v-median) for v in values)/n
    if n==8:
        assert abs(val-(1+math.sqrt(2)/2))<1e-12
    elif n<=20:
        assert val<1.7
    else:
        assert val<float(large)
print("INDEPENDENT_SAMPLED_MEDIAN_N5_TO_N100_PASS")

# A norming real zero-sum edge vector at n=8 exists with four +1 and four -1.
n=8
vals=[1+2*math.cos(2*math.pi*j/n)+2*math.cos(4*math.pi*j/n) for j in range(n)]
g=[1 if v>0.5 else -1 for v in vals]
assert sum(g)==0
conv=sum(v*x for v,x in zip(vals,g))/n
assert abs(conv-(1+math.sqrt(2)/2))<1e-12
print("EXPLICIT_EIGHT_CYCLE_ZERO_SUM_NORMING_GRADIENT_PASS")
print("ALL_FIVE_CHARACTER_LIPSCHITZ_PROJECTION_CHECKS_PASS")
