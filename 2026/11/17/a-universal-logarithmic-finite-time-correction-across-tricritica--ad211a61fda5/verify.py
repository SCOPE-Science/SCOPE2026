#!/usr/bin/env python3
"""Scientific verification of an inverse-square tricritical scaling expansion.
Only symbolic identities and finite numerical samples; asymptotic uniformity is proved separately.
"""
import math
import sympy as sp

y=sp.symbols('y', positive=True)
R=(3*y-2)/(y-1)**2
assert sp.factor(y/(1-1/y)**2-y-2-R)==0
m, eps, x=sp.symbols('m eps x')
h=(1-2*m)/m
r=(1+eps)/m
G=m*(x-h)+1-m
assert sp.expand(r*x*(1-x)*G-(1+eps)*x*(1-x*x))==0
assert sp.simplify(R-3/y - (4*y-3)/(y*(y-1)**2)) == 0
print('exact_recurrence=1 exact_GAL_reduction=1')

def calculate(delta, x0=.4, s=1.2):
    eps=abs(delta)
    n=round(s/eps)
    a=(1+delta)**-2
    y=x0**-2
    for _ in range(n):
        y=a*(y+2+(3*y-2)/(y-1)**2)
    loga=-2*math.log1p(delta)
    an=math.exp(n*loga)
    base=eps*an/x0**2+2*eps*a*math.expm1(n*loga)/(a-1)
    correction=eps*y-base
    predicted=1.5*eps*an*math.log(1/eps)
    remaining=(correction-predicted)/eps
    return correction/(eps*an*math.log(1/eps)),remaining,eps*y

for delta in [0.01,0.003,0.001,0.0003,0.0001,-0.01,-0.003,-0.001,-0.0003,-0.0001]:
    coeff,rem,ey=calculate(delta)
    assert math.isfinite(coeff) and math.isfinite(rem)
    assert 0.3 < coeff < 5.5 and abs(rem) < 60
    print('delta=%+.4g coefficient=%.7f remainder_over_eps=%+.6f scaled_inverse_square=%.7f'%(delta, coeff, rem, ey))
# Critical case y_n - 2n -1.5 log n tends to a finite limit:
y=.4**-2
values=[]
for n in range(1,50001):
    y+=2+(3*y-2)/(y-1)**2
    if n in (5000,10000,20000,50000):
        values.append((n,y-2*n-1.5*math.log(n)))
print('critical_renormalized=',values)
assert max(abs(values[k][1]-values[-1][1]) for k in (1,2))<.003
print('VERIFY_OK exact_recurrence=1 GAL_reduction=1 signed_crossover_samples=10 critical_constant=1')
