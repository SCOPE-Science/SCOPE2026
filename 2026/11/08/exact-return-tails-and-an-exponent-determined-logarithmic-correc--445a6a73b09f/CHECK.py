"""Numerical and algebraic checks of exact first-return law, not an infinite proof.
Run with Python 3 and mpmath, sympy installed: python CHECK.py
"""
from mpmath import mp
from sympy import Rational, symbols, series, expand, simplify

mp.dps = 65
u = symbols('u', positive=True)
for ell in (Rational(1, 3), Rational(1, 2), Rational(2, 3)):
    expr = (1+u)**(-ell)
    # w * (1-(1+1/w)**(-ell)) = ell - ell(ell+1)/(2w) + ...
    q = series(expr, u, 0, 3).removeO()
    assert simplify(q - (1-ell*u + ell*(ell+1)*u*u/2)) == 0

checks=0
for frac in ('0.333333333333333333333333333333333', '0.5', '0.6666666666666666666666666667'):
    ell = mp.mpf(frac)
    c = mp.findroot(lambda z:z-(1-z)**(1+ell), (mp.mpf('.3'),mp.mpf('.5')))
    d = 1-c
    assert mp.almosteq(d+d**(1+ell),1)
    g = lambda z:1+z-(1-z)**(1+ell)
    assert mp.almosteq(g(c),1)
    f = lambda z: z+(1+z)**(1+ell) if z < 0 else z-(1-z)**(1+ell)
    inverse = lambda t:mp.findroot(lambda v:v+v**(1+ell)-t,(t/(1+t**ell),t))
    invg=lambda t:mp.findroot(lambda z:g(z)-t,(t/(2+ell),t/2))
    delta=d
    for n in range(1,41):
        if n>1:
            delta=inverse(delta)
        x0=invg(delta)
        # threshold lies at boundary between r>n and r<=n, with an exception at exact equality.
        for factor,expect in ((mp.mpf('0.999999'),True),(mp.mpf('1.000001'),False)):
            x=x0*factor
            if x>=c: continue
            orbit=x
            survived=True
            for k in range(1,n+1):
                orbit=f(orbit)
                if abs(orbit)<c:
                    survived=False
                    break
            assert survived == expect,(frac,n,factor)
            checks+=1
        # reflection symmetry of finite forward dynamics away from the discontinuity
        if n<7:
            x=c*mp.mpf('0.6')
            assert abs(f(-x)+f(x))<mp.mpf('1e-50')
        # exact inverse-threshold values as finite probability
        assert 0<x0<c and mp.almosteq(g(x0),delta)
    # Stable subleading correction for n=400 and n=1200: residual is bounded.
    A=ell**(-1/ell)/((2+ell)*c)
    B=(1+ell)/(2*ell**2)
    delta=d
    for j in range(1,1201):
        delta=inverse(delta)
        if j in (400,1200):
            n=j+1
            x0=invg(delta)
            tail=x0/c
            residual=n*(tail/(A*n**(-1/ell))-1)-B*mp.log(n)
            assert abs(residual)<25,(frac,residual)
            checks+=1
print('PASS:',checks,'finite itinerary, inverse relation, symbolic coefficients, and tail-scale checks')
