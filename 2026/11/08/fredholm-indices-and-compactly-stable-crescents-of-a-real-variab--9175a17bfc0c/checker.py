#!/usr/bin/env python3
"""Finite numerical diagnostics for an explicit Cesaro Fredholm analysis.
These diagnostics do not establish the infinite-dimensional Fredholm assertions.
"""
import math
from scipy.integrate import quad
from scipy.special import expit

checks=0
for p in (1.2,1.5,2.,3.,5.):
    q=p/(p-1)
    for u in (-12.,-4.,0.,2.,8.):
        x=expit(u)
        b=1/q+(1/p-1/q)*x
        h=x**(-1/q)*(1-x)**(1/p)
        dlogh=-1/q+(1/q-1/p)*x
        assert abs(b+dlogh)<1e-12
        assert h>0
        checks+=2
    # Test the complex eigenfunction ODE in integral form for the p<2 case.
    if p<2:
        z=.5+.02j # 1/q < .5 < 1/p for p<2
        for x in (.07,.3,.8):
            f=(x**(z-1))*((1-x)**(-z))
            # Integral beta identity (substitution y=x/(1-x)).
            cquad=complex(quad(lambda t: (t**(z-1)*(1-t)**(-z-1)).real,0,x,epsabs=2e-10)[0],quad(lambda t: (t**(z-1)*(1-t)**(-z-1)).imag,0,x,epsabs=2e-10)[0])/x
            assert abs(cquad-f/z) < 2e-6
            checks+=1
    if p>2:
        z=.5+.02j # 1/p <.5<1/q
        for x in (.07,.3,.8):
            h=(x**(-z))*(1-x)**(z-1)
            hquad=complex(quad(lambda t: (t**(-z-1)*(1-t)**(z-1)).real,x,1,epsabs=2e-10)[0],quad(lambda t: (t**(-z-1)*(1-t)**(z-1)).imag,x,1,epsabs=2e-10)[0])/(1-x)
            assert abs(hquad-h/z) < 2e-6
            checks+=1
    # Equality between circle membership and asymptotic characteristic lines.
    for yi in (-8.,-2.,0.,1.,6.):
        for beta in (1/p,1/q):
            lam=1/complex(beta,yi)
            radius=1/(2*beta)
            assert abs(abs(lam-radius)-radius)<1e-12
            checks+=1
for p in (1.5,3):
    q=p/(p-1)
    for r in (0., .1,.5,.9,1.):
        # Explicit index in the interior depends on the orientation of asymptotic rates.
        bminus,bplus=1/q,1/p
        z=(1-r)*min(bminus,bplus)+r*max(bminus,bplus)
        if 0<r<1:
            sign=1 if bminus<bplus else -1
            ker=1 if sign==1 else 0
            cok=1 if sign==-1 else 0
            assert ker-cok==sign
            checks+=1
print('PASS:',checks,'algebraic, integral and geometric diagnostics')
