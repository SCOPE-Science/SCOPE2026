#!/usr/bin/env python3
"""Supplementary finite Legendre recurrence checks (not an infinite proof)."""
import math
from scipy.special import gamma,zeta
for s in (1.2,1.4):
    alpha=s-0.5
    c=4**alpha*gamma(1-alpha)*math.sin(math.pi*alpha/2)/(math.sqrt(2*math.pi)*alpha*zeta(s))
    estimates=[]
    for h in (0.02,0.005,0.001):
        x=-math.sin(h)
        p0,p1=1.,x
        summ=p1/zeta(s)
        j=1
        for n in range(1,180001):
            p2=((2*n+1)*x*p1-n*p0)/(n+1)
            p0,p1=p1,p2
            if (n+1)%4==1:
                summ+=p1/(j+1)**s/zeta(s)
                j+=1
        estimate=-summ/h**alpha
        assert estimate>0 and math.isfinite(estimate)
        estimates.append(estimate/c)
    assert all(0<r<1 for r in estimates), estimates
    assert estimates[0]<estimates[1]<estimates[2], estimates
    print('s=',s,'ratios to sharp coefficient:',estimates)
print('6 finite asymptotic comparisons passed; the proof is analytic.')
