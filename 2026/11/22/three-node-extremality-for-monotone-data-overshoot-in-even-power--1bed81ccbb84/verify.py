"""Reproduce finite-grid examples for a sharp monotone-range theorem.

Usage: python verify.py
Dependencies: Python 3.9+, sympy, mpmath.
The finite-grid tests illustrate but do not replace the analytic all-grid proof.
"""
from fractions import Fraction as F
from math import isclose
import sympy as sp
import mpmath as mp

# The sharp three-node step profile and its stationary equation.
t, r = sp.symbols('t r', real=True)
for gamma in (2, 4, 6, 8):
    f = (1-t)*t**gamma/(t**gamma+(2-t)**gamma)
    critical = gamma*(1-r*r)-2*r*(1+r**gamma)
    transformed_derivative = sp.factor(sp.diff(f,t).subs(t, 2*r/(1+r)))
    critical_factor = r**(gamma-1)/(2*(1+r**gamma)**2)
    assert sp.simplify(transformed_derivative - critical*critical_factor) == 0
    # Symbolically verify the critical equation is equivalent to derivative zero
    logder = -1/(1-t)+2*gamma*(2-t)**gamma/(t*(2-t)*(t**gamma+(2-t)**gamma))
    assert sp.simplify(sp.diff(f,t)-f*logder) == 0
    rr = mp.findroot(lambda z: gamma*(1-z*z)-2*z*(1+z**gamma), (mp.mpf('.3'),mp.mpf('.7')))
    tt = 2*rr/(1+rr)
    dd = (1-tt)*rr**gamma/(1+rr**gamma)
    assert 0<rr<1 and 0<tt<1 and 0<dd<1
    print('gamma',gamma,'r',mp.nstr(rr,16),'t',mp.nstr(tt,16),'delta',mp.nstr(dd,16))

# Verify the original blended formula against cardinal step evaluation on rational cases.
def blend(n, gamma, x, data):
    x=F(x)
    if x.denominator==1 and 0<=x<=n: return F(data[int(x)])
    weights=[1/((x-i)**gamma*(x-i-1)**gamma) for i in range(n)]
    numer=sum(weights[i]*(data[i]*(i+1-x)+data[i+1]*(x-i)) for i in range(n))
    return numer/sum(weights)

def step(n,k): return [int(j>=k) for j in range(n+1)]

# Rational exact comparisons to a conservative rational majorant delta_2< 68/1000.
for gamma in (2,4,6,8):
    for n in range(2,13):
        for j in range(n):
            for q in range(1,29):
                x=F(j)+F(q,29)
                for k in range(1,n+1):
                    v=blend(n,gamma,x,step(n,k))
                    assert -F(68,1000) < v < 1+F(68,1000), (n,gamma,x,k,v)
print('Exact rational: 4 gamma values x 11 grid sizes x 28 evaluation offsets x every step: PASS')

# Construct the exact extremal step and reflected complement for gamma=2.
mp.mp.dps=50
rr=mp.findroot(lambda z: 2*(1-z*z)-2*z*(1+z*z),(.4,.6))
tt=2*rr/(1+rr)
dd=(1-tt)*rr**2/(1+rr**2)
w0=1/(tt**2*(tt-1)**2)
w1=1/((tt-1)**2*(tt-2)**2)
assert abs((tt-1)*w1/(w0+w1)+dd)<mp.mpf('1e-45')
print('Exact three-node step extremal profile: PASS')
