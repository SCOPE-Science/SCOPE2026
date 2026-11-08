#!/usr/bin/env python3
"""Separate algebraic and numerical cross-checks for inverse-normal Gaussian importance stratification."""
import math
import numpy as np
import sympy as sp
from scipy.special import ndtri
from scipy.integrate import quad
from numpy.polynomial.legendre import leggauss

S=sp.symbols('s',positive=True)
z=sp.symbols('z',real=True)
a=S-sp.Rational(3,2)
poly=4*z**2-4*(S-1)*z**4+(S-1)**2*z**6
Gaussian_integral = sp.sqrt(2*sp.pi)*S**3*sp.sqrt(sp.pi)*(2/a**sp.Rational(3,2)-3*(S-1)/a**sp.Rational(5,2)+sp.Rational(15,8)*(S-1)**2/a**sp.Rational(7,2))
I = sp.pi/(4*sp.sqrt(2))*S**3*(7*S**2-18*S+15)/a**sp.Rational(7,2)
assert sp.simplify(Gaussian_integral-I)==0
P=7*S**3-41*S**2+67*S-45
assert sp.factor(sp.diff(sp.log(I),S) - 3*P/(S*(2*S-3)*(7*S**2-18*S+15)))==0
assert sp.expand(P.subs(S,sp.symbols('t')+sp.Rational(3,2)))==7*sp.symbols('t')**3-sp.Rational(19,2)*sp.symbols('t')**2-sp.Rational(35,4)*sp.symbols('t')-sp.Rational(105,8)
sstar=float(sp.nroots(P)[0]); assert 3.77<sstar<3.78
Istar=float(I.subs(S,sstar)); print('sstar',sstar,'Istar',Istar,'variance leading',Istar/12)

def f(u,s):
    z=ndtri(u)
    return (s**1.5)*z*z*np.exp((1-s)*z*z/2)

def approx_const(n,s,order):
    # Independent Gauss-Legendre integration of each conditional variance.
    xx,ww=leggauss(order)
    uu=(np.arange(n)[:,None]+(xx[None,:]+1)/2)/n
    vals=f(uu,s)
    weights=ww/2
    mean=np.sum(vals*weights[None,:],axis=1)
    vals_c=vals-mean[:,None]
    variances=np.sum(weights[None,:]*vals_c**2,axis=1)
    return n*np.sum(variances) # n^3 Var Q = n sum_i Var_i

for s in [1.6,2.,3.,sstar,4.,6.]:
    # independent quadrature of derivative L2 in z domain
    def deriv_integrand(z):
        return s**3 * math.sqrt(2*math.pi)*(2*z-(s-1)*z**3)**2 * math.exp(-(s-1.5)*z*z)
    integral=quad(deriv_integrand,-np.inf,np.inf,epsabs=2e-9,epsrel=2e-10)[0]
    expected=float(I.subs(S,s))
    assert abs(integral/expected-1)<1e-9,(s,integral,expected)
    seq=[approx_const(n,s,96) for n in [32,128,512]]
    print(f's={s:.9f} theoretical n^3var={expected/12:.9f} n=32/128/512:',*[round(x,9) for x in seq])
    assert seq[-1]>0
    if s>=2.5:
        assert abs(seq[-1]/(expected/12)-1)<0.09,(s,seq,expected/12)
    else:
        assert seq[0]<seq[1]<seq[2]<(expected/12)

# MC second moment; exact symbolic and numerical
J=3*S**3/(2*S-1)**sp.Rational(5,2)
assert sp.simplify(sp.diff(sp.log(J),S)-(S-3)/(S*(2*S-1)))==0
assert float(J.subs(S,3)-1)<float(J.subs(S,sstar)-1)
assert float(I.subs(S,sstar))<float(I.subs(S,3))
for s in [.7,1,1.5,3,sstar,8]:
    if s>.5:
        moment=quad(lambda z: s**3/math.sqrt(2*math.pi)*z**4*math.exp(-(s-.5)*z*z),-np.inf,np.inf)[0]
        assert abs(moment-float(J.subs(S,s)))<1e-9
print('MC optimal s=3; asymptotic stratified optimal s=3.771..; all checks PASS')
