#!/usr/bin/env python3
"""Independent numerical consistency tests for the sine-exponential threshold theorem."""
import math
from scipy.optimize import brentq

def crit(b):
    k=math.pi/(2*b)
    x=brentq(lambda z:(1-z)*math.tan(k*z)-b/math.pi,0,b*(1-1e-9),xtol=1e-14)
    return x,x+(x-1)*math.tan(k*x)**2

def disp(x,a,b):
    return 1-(1-a)*math.cos(math.pi*x/(2*b))**2-x

n=0
for b in [0.02,0.05,0.1,0.23,0.5,0.77,0.95]:
    x,ac=crit(b)
    assert 0<x<b/2 and 0<ac<b
    assert abs(disp(x,ac,b))<1e-12
    for factor,count in [(0.1,2),(0.5,2),(0.99,2),(1.0,1),(1.05,0)]:
        a=factor*ac
        if count==2:
            left=brentq(lambda v:disp(v,a,b),0,x)
            right=brentq(lambda v:disp(v,a,b),x,b)
            assert 0<left<x<right<b
            k=math.pi/(2*b)
            dl=(1-a)*k*math.sin(2*k*left)
            dr=(1-a)*k*math.sin(2*k*right)
            assert 0<dl<1<dr
        elif count==1: assert abs(disp(x,a,b))<1e-12
        else:
            assert all(disp(b*j/1000,a,b)>0 for j in range(1001))
        n+=1
    # Squared sine left and exponential right: no right equilibrium
    for c in [.03,.3,.9]:
        for j in range(1,50):
            y=b+(1-b)*j/50
            assert c*math.expm1((y-b)/(1-b))/math.expm1(1)-y<0
print('PASS',n,'parameter regimes; independent root brackets, stability, and exponential-branch checks')
