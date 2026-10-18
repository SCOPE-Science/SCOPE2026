#!/usr/bin/env python3
import math

phi=(1.0+math.sqrt(5.0))/2.0
gc=math.pi*math.pi/math.sqrt(5.0)
C=gc*(1.0-math.pi*math.pi/12.0)
rho=phi**-4

def A(n):
    x=phi**(-2*n)
    return (2.0*math.pi/math.sqrt(5.0))*(phi**(2*n)-phi**(-2*n))*math.tan(math.pi*x/2.0)

vals=[A(n) for n in range(1,9)]
if not all(vals[i] < vals[i+1] < gc for i in range(len(vals)-1)):
    raise AssertionError('threshold monotonicity')

scaled=[]
for n in range(2,9):
    d=gc-A(n)
    scaled.append(abs(d/(C*phi**(-4*n))-1.0))
if scaled[-1] > 2.0e-6:
    raise AssertionError(('leading asymptotic',scaled[-1]))

ratio_err=[]
for n in range(2,7):
    d0=gc-A(n)
    d1=gc-A(n+1)
    ratio_err.append(abs((d1/d0)/rho-1.0))
if ratio_err[-1] > 1.0e-5:
    raise AssertionError(('ratio asymptotic',ratio_err[-1]))

for n in range(1,7):
    g=0.5*(A(n)+A(n+1))
    if not (A(n) < g <= A(n+1)):
        raise AssertionError(('interval',n,g))

print('VERIFY_OK asymptotic_cases=%d max_scaled_rel=%.3e ratio_cases=%d max_ratio_rel=%.3e interval_cases=6' %
      (len(scaled),max(scaled),len(ratio_err),max(ratio_err)))
