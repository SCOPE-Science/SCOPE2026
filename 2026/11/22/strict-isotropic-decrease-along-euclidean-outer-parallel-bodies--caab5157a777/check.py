#!/usr/bin/env python3
"""Exact symbolic and independent one-dimensional quadrature checks.
Run: python check.py (requires SymPy; SciPy for optional quadrature checks).
"""
from sympy import (symbols, Rational, pi, simplify, diff, expand, Poly,
                   factorial, sqrt, integrate, Rational as Q)
from math import pi as PI

a,b,t,z = symbols('a b t z', positive=True)
p = symbols('p', positive=True)
A = 4*a*b + 4*(a+b)*t + p*t*t
Mx = 4*a**3*b/3 + (4*a*a*b + 4*a**3/3)*t + (4*a*b + p*a*a)*t**2 + (4*b+8*a)*t**3/3 + p*t**4/4
My = Mx.xreplace({a:b,b:a})
J = Mx*My/A**4
# Both volume and separate moments are independently rebuilt from horizontal slices.
# In the upper rounded cap, s=y-b and x runs from -(a+sqrt(t^2-s^2)) to its opposite.
# The following five definite integrals follow from substituting s=t sin(theta).
S0=t
S1=pi*t**2/4                 # integral sqrt(t^2-s^2)
S2=2*t**3/3                 # integral (t^2-s^2)
S3=3*pi*t**4/16             # integral (t^2-s^2)^(3/2)
T1=t**3/3                   # integral s sqrt(t^2-s^2)
T2=pi*t**4/16               # integral s^2 sqrt(t^2-s^2)
A2 = 4*b*(a+t) + 4*(a*t + S1)
Mx2 = 4*b*(a+t)**3/3 + 4*(a**3*t+3*a*a*S1+3*a*S2+S3)/3
My2 = 4*(a+t)*b**3/3 + 4*(a*(b*b*t+b*t*t+t**3/3)+b*b*S1+2*b*T1+T2)
assert simplify(A2-A.subs(p,pi)) == 0
assert simplify(Mx2-Mx.subs(p,pi)) == 0
assert simplify(My2-My.subs(p,pi)) == 0

# Derivative certificate. R(t) = 4 A' Mx My - A(Mx' My + Mx My')
# Positive R means J'(t) = -R/A^5 < 0.
c=[
 Q(64,9)*a**4*b**4*(4-p),
 Q(64,9)*a**3*b**3*(p-1)*(a+b),
 Q(16,9)*a*a*b*b*((9*p-20)*(a*a+b*b)+(84*p-248)*a*b),
 Q(20,9)*a*b*(a+b)*(p*(a*a+b*b)+(12*p*p+10*p-144)*a*b),
 Q(2,9)*(2*p*(a**4+b**4)+(51*p*p+64*p-672)*(a**3*b+a*b**3)+(18*p**3+324*p-1536)*a*a*b*b),
 (a+b)/9*((27*p*p-256)*(a*a+b*b)+(54*p*p+36*p-640)*a*b),
 p/18*((9*p*p-88)*(a*a+b*b)+(36*p-112)*a*b),
]
R=4*diff(A,t)*Mx*My-A*(diff(Mx,t)*My+Mx*diff(My,t))
assert expand(R-t*sum(c[k]*t**k for k in range(7))) == 0
# At p0=157/50, every monomial of c[1..6] has positive coefficient;
# these coefficient functions are increasing in p>0. c0 uses p<4.
p0=Q(157,50)
assert p0 < pi < Q(22,7) < 4
for i in range(1,7):
    coeffs=Poly(expand(c[i].subs(p,p0)),a,b).coeffs()
    assert coeffs and all(q>0 for q in coeffs), (i,coeffs)
    derivative_coeffs=Poly(expand(diff(c[i],p).subs(p,p0)),a,b).coeffs()
    assert all(q>=0 for q in derivative_coeffs), (i,derivative_coeffs)
assert simplify(J.subs(t,0)-Q(1,144))==0
assert simplify(diff(J,t).subs(t,0))==0
assert simplify(diff(J,t,2).subs(t,0)/2-(p-4)/(288*a*b))==0
assert simplify((J.subs(t,1/z)*z**0).limit(z,0)-1/(16*p**2)) == 0
# Stronger large-radius expansion (coefficient at z^2).
Jinf=simplify((z**4*Mx.subs(t,1/z))*(z**4*My.subs(t,1/z))/(z**2*A.subs(t,1/z))**4)
large2=((9*p*p-88)*(a*a+b*b)+(36*p-112)*a*b)/(36*p**4)
assert simplify(diff(Jinf,z).subs(z,0))==0
assert simplify(diff(Jinf,z,2).subs(z,0)/2-large2)==0
# Algebraic scale and axis exchange checks.
h=symbols('h', positive=True)
assert simplify(J.subs({a:h*a,b:h*b,t:h*t})-J)==0
assert simplify(J-J.xreplace({a:b,b:a}))==0

# Independent numerical geometry: direct quadrature of horizontal rectangle/corner slices.
try:
    from scipy.integrate import quad
    import math
    trials=[(1.0,1.0,.05), (2.0,1.0,.3), (2.0,.2,.4),
            (.1,3.,5.), (10.,.03,.7), (.8,1.9,20.)]
    for aa,bb,tt in trials:
        mmx = 4*bb*(aa+tt)**3/3 + 4*quad(lambda s:(aa+math.sqrt(max(0,tt*tt-s*s)))**3,0,tt,epsabs=1e-10)[0]/3
        mmy = 4*(aa+tt)*bb**3/3 + 4*quad(lambda s:(bb+s)**2*(aa+math.sqrt(max(0,tt*tt-s*s))),0,tt,epsabs=1e-10)[0]
        area = 4*bb*(aa+tt) +4*quad(lambda s:aa+math.sqrt(max(0,tt*tt-s*s)),0,tt,epsabs=1e-10)[0]
        vals={a:aa,b:bb,t:tt,p:PI}
        for actual,target in [(mmx,float(Mx.subs(vals))), (mmy,float(My.subs(vals))), (area,float(A.subs(vals)))]:
            assert abs(actual-target) < 2e-9*(1+abs(target)), (aa,bb,tt,actual,target)
        # monotonic cross-check not used in proof
        js=[float(J.subs({a:aa,b:bb,t:s,p:PI})) for s in [0,tt,2*tt,100*tt]]
        assert all(js[j]>js[j+1] for j in range(3))
    print('PASS exact moment, seven derivative coefficients, endpoint expansions, independent quadrature (6 geometries).')
except ImportError:
    print('PASS exact moment, seven derivative coefficients and endpoint expansions (SciPy unavailable).')
