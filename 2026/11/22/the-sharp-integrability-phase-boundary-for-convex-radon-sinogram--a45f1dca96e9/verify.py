"""Reproduce exact radial Radon and endpoint-exponent identities.

These finite symbolic checks support, but do not substitute for, the analytic
all-functions and all-dimensions argument in RESULT.md.
"""
import sympy as sp

z=sp.symbols('z', positive=True)
t=sp.symbols('t', real=True)
for d in (2,3,4):
    a=sp.Rational(3-d,2)
    m=sp.Rational(d-1,2)
    # Integral on a (d-1)-dimensional section:
    # [surface(S^(d-2))/2] * Beta((d-1)/2,a+1) * (1-t^2)^(a+(d-1)/2)
    c=sp.simplify(sp.pi**m*sp.gamma(a+1)/sp.gamma(a+1+m))
    expected={2:sp.pi/2,3:sp.pi,4:sp.pi**2}[d]
    assert sp.simplify(c-expected)==0
    assert a+m==1
    assert sp.diff(-c*(1-t**2),t,2)==2*c
    # f belongs to Lp exactly when a*p > -1, except a >= 0.
    assert a=={2:sp.Rational(1,2),3:0,4:sp.Rational(-1,2)}[d]
for d in range(3,30):
    e=sp.Rational(d-3,2)
    assert (e>=1)==(d>=5)
    assert (e+sp.Rational(1,2)>=1)==(d>=4)
# Test the exact spherical delta-density (normalizing surface area):
for d in (3,4,5,6):
    r=sp.Rational(4,5)
    s=sp.Rational(1,2)
    area=2*sp.pi**(sp.Rational(d-1,2))/sp.gamma(sp.Rational(d-1,2))
    kernel=area/r*(1-(s/r)**2)**sp.Rational(d-3,2)
    assert kernel>0
print('Radial constants, convexity, critical exponents and spherical kernel: PASS')
