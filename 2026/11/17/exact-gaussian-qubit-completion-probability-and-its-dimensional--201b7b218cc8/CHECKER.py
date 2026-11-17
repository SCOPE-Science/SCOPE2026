#!/usr/bin/env python3
"""Standard-library diagnostic checks for the exact square-complex-Wishart completion law."""
import cmath
from fractions import Fraction as Q
import math
import random

# Exact rational partial-fraction identity (dense rational test grid).
def original(t):
    return Q(6)*t*(t+1)/((2*t+1)**4*(t+2)**2)

def apart(t):
    return (-Q(28,81)/(2*t+1) + Q(4,9)/(2*t+1)**2
            + Q(4,9)/(2*t+1)**3 - Q(2,3)/(2*t+1)**4
            + Q(14,81)/(t+2) + Q(4,27)/(t+2)**2)

for m in range(0,80):
    t=Q(m+1,2*m+3)
    assert original(t)==apart(t)

exact=(24-28*math.log(2))/81
# Independent adaptive Simpson (finite interval with t = x/(1-x)).
def integral01(x):
    if x==1.0:
        return 0.0
    t=x/(1-x)
    return 6*t*(t+1)/((2*t+1)**4*(t+2)**2)/(1-x)**2

def simpson(n):
    h=1/n
    total=integral01(0)+integral01(1)
    for k in range(1,n):
        total+=(4 if k&1 else 2)*integral01(k*h)
    return total*h/3

assert abs(simpson(20000)-exact)<5e-10
assert abs(simpson(40000)-exact)<5e-10

# Check direct 2-by-2 Hermitian matrix inequality with genuine random Ginibre factors.
rng=random.Random(20261109)
def ginibre_wishart():
    Z=[[(rng.gauss(0,1)+1j*rng.gauss(0,1))/math.sqrt(2)
        for _ in range(2)] for _ in range(2)]
    a=abs(Z[0][0])**2+abs(Z[0][1])**2
    b=abs(Z[1][0])**2+abs(Z[1][1])**2
    z=Z[0][0]*Z[1][0].conjugate()+Z[0][1]*Z[1][1].conjugate()
    top=(a+b+math.sqrt((a-b)**2+4*abs(z)**2))/2
    return a/top,b/top,z/top

def completion():
    a,b,z=ginibre_wishart()
    c,d,w=ginibre_wishart()
    m=a+c-1; n=b+d-1; q=z+w
    return m+n>=0 and m*n>=abs(q)**2

N=25000
p=sum(completion() for _ in range(N))/N
sigma=math.sqrt(exact*(1-exact)/N)
assert abs(p-exact)<6*sigma
print('WISHART_COMPLETION_CHECK_OK', 'probability',format(exact,'.16f'),
      'direct_sample',format(p,'.6f'),'num_trials',N,'rational_checks',80)
