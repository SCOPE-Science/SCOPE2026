"""Reproduce algebraic and numerical checks for a two-sign Brownian-bridge integral design.

Run: python verify.py
Requires numpy, scipy, sympy, mpmath.
Analytic inequalities in the accompanying proof are required for all-parameter conclusions.
"""
from math import pi, asin, sqrt, log, exp
import random
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.integrate import quad
from scipy.special import ndtr

count = 0
r,h,c,w = sp.symbols('r h c w', real=True)
L = (1+2*h-c)/(1-c*c)
M = h*(1+c)/(1-c*c)
transformed = (L*w-M)/(4*sp.pi*(w+h)**2)
original = ((1+h)*w/(1+c)+h*(w-1)/(1-c))/(4*sp.pi*(w+h)**2)
assert sp.simplify(original-transformed) == 0
count += 1
critical = sp.factor(sp.diff((L*w-M)/(w+h)**2,w)*(w+h)**3)
assert sp.factor(critical - (L*h+2*M-L*w)) == 0
count += 1
h0=(1-r)**2/(4*r)
center_cert=sp.factor((1+2*h0-r)-h0*(3+2*h0+r))
assert sp.simplify(center_cert-(1-r)*(1+r)**2*(3*r-1)/(8*r*r)) == 0
count += 1
c0=sp.Rational(3,5)*r
L0=sp.factor(L.subs({h:h0,c:c0}));M0=sp.factor(M.subs({h:h0,c:c0}))
small_cert=sp.factor(8*(L0*h0+M0)-3*L0**2)
expected=-25*(6*r**3-r**2-14*r+5)*(6*r**3+r**2-14*r-5)/(4*r*r*(3*r-5)**2*(3*r+5)**2)
assert sp.factor(small_cert-expected)==0
count += 1

mp.mp.dps=65
f=lambda x:(mp.pi/2+mp.asin(x))*(1-x)**mp.mpf('1.5')/(x*mp.sqrt(1+x))-1
rho=mp.findroot(f,(mp.mpf('.5'),mp.mpf('.6')))
t= rho/(1+rho)
cor=2*mp.asin(rho)/mp.pi
value=rho/(mp.pi*(1+rho)**2*(1+cor))
risk=mp.mpf(1)/12-value
assert mp.mpf('.53')<rho<mp.mpf('.55')
assert mp.mpf('.63')<12*value<mp.mpf('.65')
assert abs(f(rho))<mp.mpf('1e-58')
count+=3

def objective(s,t):
    corr=sqrt(s*(1-t)/(t*(1-s)))
    cs=2*asin(corr)/pi
    a=sqrt(s*(1-s))/2
    b=sqrt(t*(1-t))/2
    return (2/pi)*(a*a+b*b-2*cs*a*b)/(1-cs*cs)

def quadrant_objective(s,t):
    """Independent numerical Gaussian-quadrant integration without sign-projection formula."""
    corr=sqrt(s*(1-t)/(t*(1-s)))
    a=sqrt(s*(1-s))/2
    b=sqrt(t*(1-t))/2
    coeff=((a-corr*b)/(1-corr*corr),(b-corr*a)/(1-corr*corr))
    sig=sqrt(1-corr*corr)
    result=0
    for i in (-1,1):
        for j in (-1,1):
            prob=.25+i*j*asin(corr)/(2*pi)
            def first(x):return x*exp(-x*x/2)/sqrt(2*pi)*ndtr(j*corr*x/sig)
            def second(x):return x*exp(-x*x/2)/sqrt(2*pi)*ndtr(i*corr*x/sig)
            moment_x=quad(first,0,12,epsabs=2e-12)[0] if i==1 else quad(first,-12,0,epsabs=2e-12)[0]
            moment_y=quad(second,0,12,epsabs=2e-12)[0] if j==1 else quad(second,-12,0,epsabs=2e-12)[0]
            result+=(coeff[0]*moment_x+coeff[1]*moment_y)**2/prob
    return result

pairs=[(.12,.91),(.20,.40),(.40,.70),(.01,.98),(.35,.65),(.49,.51)]
for s,t0 in pairs:
    assert abs(objective(s,t0)-quadrant_objective(s,t0))<3e-11
    count+=1

rng=random.Random(981725)
for i in range(1500):
    s,t0=sorted((rng.uniform(.001,.999),rng.uniform(.001,.999)))
    if t0-s<1e-5:continue
    assert objective(s,t0)<=float(value)+8e-13
    count+=1
for i in range(1,600):
    rr=i/600
    hh=(1-rr)**2/(4*rr)
    cc=2*asin(rr)/pi
    ww=hh*(3+2*hh+cc)/(1+2*hh-cc)
    if rr>=1/3:assert ww<=1+1e-12
    else:
        lower=3*rr/5
        ll=(1+2*hh-lower)/(1-lower*lower)
        mm=hh*(1+lower)/(1-lower*lower)
        assert ll*ll/(16*pi*(ll*hh+mm)) <1/(6*pi)
    count+=1

print('All checks passed:',count)
print('optimal correlation:',mp.nstr(rho,45))
print('optimal first/second sites:',mp.nstr(t,45),mp.nstr(1-t,45))
print('explained variance:',mp.nstr(value,45))
print('Bayes mean-square risk:',mp.nstr(risk,45))
print('variance fraction explained:',mp.nstr(12*value,45))
print('One-bit fraction:',mp.nstr(mp.mpf(3)/(2*mp.pi),30))
print('Full-value two-site fraction:',mp.nstr(mp.mpf(8)/9,30))
