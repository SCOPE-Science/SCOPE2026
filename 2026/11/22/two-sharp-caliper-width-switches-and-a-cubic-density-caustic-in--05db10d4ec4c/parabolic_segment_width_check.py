"""Reproducible checks for the directional-width bifurcation of parabolic segments.

Requirements: Python 3.10+, sympy, numpy, scipy.
Run: python parabolic_segment_width_check.py
All finite tests are diagnostics; the accompanying mathematical proof handles all parameters.
"""
import math
import random

import numpy as np
import sympy as sp
from scipy.optimize import brentq
from scipy.integrate import quad

T, A = sp.symbols('t a', positive=True)
P = T**3 + (2-4*A**2)*T + 4*A
F = (A*T + A**2 + T**2/4)/sp.sqrt(1+T**2)
assert sp.simplify(sp.diff(F,T)-P/(4*(1+T**2)**sp.Rational(3,2))) == 0
assert sp.simplify(P.subs(A,sp.sqrt(2))-(T-sp.sqrt(2))**2*(T+2*sp.sqrt(2)))==0
assert sp.simplify(F.subs({A:sp.sqrt(2),T:sp.sqrt(2)})-3*sp.sqrt(3)/2) == 0
assert sp.simplify(sp.diff(F,T,3).subs({A:sp.sqrt(2),T:sp.sqrt(2)})/6*27-3*sp.sqrt(6)/4)==0

Qmax = sp.together(16*(F**2-(2*A)**2))
Qmin = sp.together(16*(F**2-A**4))
nummax = sp.cancel(Qmax).as_numer_denom()[0]
nummin = sp.cancel(Qmin).as_numer_denom()[0]
rmax = sp.factor(sp.resultant(P,nummax,T))
rmin = sp.factor(sp.resultant(P,nummin,T))
assert sp.simplify(rmax/(1024*A**2*(4*A**2+1)**2)-(16*A**4-44*A**2-1)) == 0
assert sp.simplify(rmin/(256*A**4*(4*A**2+1)**2)-(16*A**6-56*A**4-12*A**2-1)) == 0

a_max = math.sqrt((11+5*math.sqrt(5))/8)
s_min = brentq(lambda s:16*s**3-56*s*s-12*s-1,3,4)
a_min = math.sqrt(s_min)
assert math.sqrt(2)<a_max<a_min<2

checks=0

def w(a,t):
    if t <= 2*a:
        return (a*t+a*a+t*t/4)/math.sqrt(1+t*t)
    return 2*a*t/math.sqrt(1+t*t)

def direct_width(a,th):
    # Direct maximization of linear functionals over the top chord and lower parabola.
    ux,uy=math.sin(th),math.cos(th)
    def support(x,y):
        top=a*abs(x)+a*a*y
        # The bottom parabola is a quadratic in the horizontal coordinate.
        candidates=[-a,a]
        if y < 0:
            candidates.append(max(-a,min(a,-x/(2*y))))
        low=max(x*s+y*s*s for s in candidates)
        return max(top,low)
    return support(ux,uy)+support(-ux,-uy)

rng=random.Random(23843)
for j in range(3000):
    a=math.exp(rng.uniform(math.log(.06),math.log(12)))
    th=rng.uniform(0,math.pi/2)
    assert abs(direct_width(a,th)-w(a,math.tan(th)))<2e-11*max(1,a*a)
    checks+=1

for a in [.15,.9,math.sqrt(2),1.45,1.6,a_max,1.8,a_min,2.1,5,30]:
    roots=sorted(float(z.real) for z in np.roots([1,0,2-4*a*a,4*a])
                 if abs(z.imag)<1e-9 and 0<z.real<2*a)
    candidate=[(0.,a*a), (math.inf,2*a)] + [(t,w(a,t)) for t in roots]
    mn=min(y for _,y in candidate); mx=max(y for _,y in candidate)
    for t in np.linspace(0,2*a,4000):
        assert mn-1e-10<=w(a,t)<=mx+1e-10
        checks+=1
    for th in np.linspace(math.atan(2*a),math.pi/2,301):
        assert mn-1e-10<=w(a,math.tan(th))<=mx+1e-10
        checks+=1
    expected=(2*a+a*math.sqrt(1+4*a*a)+.5*math.asinh(2*a))/math.pi
    integral=2/math.pi*quad(lambda th:w(a,math.tan(th)),0,math.pi/2,
                            points=[math.atan(2*a)],epsabs=1e-10)[0]
    assert abs(integral-expected)<2e-9*max(1,expected)
    checks+=1

for a, which in [(a_max,'max'),(a_min,'min')]:
    roots=sorted(float(z.real) for z in np.roots([1,0,2-4*a*a,4*a])
                 if abs(z.imag)<1e-9 and 0<z.real<2*a)
    target=2*a if which=='max' else a*a
    assert abs(w(a,roots[0 if which=='max' else 1])-target)<1e-10
    checks+=1

c=3*math.sqrt(6)/4
b=math.sqrt(2)
w0=3*math.sqrt(3)/2
for e in [1e-2,1e-3,1e-4,1e-5]:
    tleft=brentq(lambda t:w(b,t)-(w0-e),0,b,xtol=1e-13)
    tright=brentq(lambda t:w(b,t)-(w0+e),b,2*b,xtol=1e-13)
    probability=2/math.pi*(math.atan(tright)-math.atan(tleft))
    asymptotic=4/math.pi*(e/c)**(1/3)
    assert abs(probability/asymptotic-1)<.001
    checks+=1

K=4*2**(.75)/(3*math.sqrt(3))
for delta in [1e-2,1e-3,1e-4]:
    a=b+delta
    roots=sorted(float(z.real) for z in np.roots([1,0,2-4*a*a,4*a])
                 if abs(z.imag)<1e-9 and 0<z.real<2*a)
    split=w(a,roots[0])-w(a,roots[1])
    assert abs(split/(K*delta**1.5)-1)<.005
    checks+=1

print('PASS:',checks,'numerical checks and exact symbolic identities')
print('a_max=',a_max,'a_min=',a_min)
print('fold mass coefficient=',4/math.pi*c**(-1/3))
print('fold separation coefficient=',K)
