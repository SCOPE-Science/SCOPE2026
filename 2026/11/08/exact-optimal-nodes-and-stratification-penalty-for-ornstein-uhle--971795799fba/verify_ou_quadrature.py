"""Numerical and exact-algebra consistency tests for OU Bayesian quadrature.
The analytic proof of all-n and asymptotic statements is in RESULT.md.
Run with: python verify_ou_quadrature.py (requires numpy, scipy, sympy).
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import brentq

checks = 0

def check(condition, explanation):
    global checks
    if not bool(condition):
        raise AssertionError(explanation)
    checks += 1

def b(x):
    # cancellation-safe near zero
    y=-math.expm1(-x)
    return 2*x - 2*y - y*y

def v(x):
    return 2*x - 4*math.tanh(x/2)

def design(n, lam):
    if n == 1:
        return [0.5]
    h=brentq(lambda h: n*h+2*math.log(math.cosh(lam*h/2))/lam-1,
             0,1,xtol=1e-15)
    a=h/2+math.log(math.cosh(lam*h/2))/lam
    check(abs((n-1)*h+2*a-1)<2e-13,'gap constraint')
    check(abs((1-math.exp(-lam*a))-math.tanh(lam*h/2))<1e-13,
          'stationary first-order condition')
    return [a+i*h for i in range(n)]

def local_variance(times, lam, scale):
    tt=np.sort(np.asarray(times))
    gaps=np.diff(tt)
    return scale/(lam*lam)*(b(lam*tt[0])+b(lam*(1-tt[-1]))+
                             sum(v(lam*float(g)) for g in gaps))

def schur_variance(times, lam, scale):
    tt=np.asarray(times)
    C=scale*np.exp(-lam*np.abs(tt[:,None]-tt[None,:]))
    k=scale/lam*(2-np.exp(-lam*tt)-np.exp(-lam*(1-tt)))
    varI=scale*(2/lam - 2*(-math.expm1(-lam))/(lam*lam))
    return varI-float(k@np.linalg.solve(C,k))

for lam in (0.5,1.,2.):
  for n in (1,2,3,4,8,16,40):
    tt=design(n,lam)
    check(abs(schur_variance(tt,lam,1.4)-local_variance(tt,lam,1.4))<2e-10,
          'design covariance direct Schur check')
    if n>=2:
      for j in range(3):
        rng=np.random.default_rng(4000+n*7+j)
        t=np.sort(rng.random(n))
        check(abs(schur_variance(t,lam,1.4)-local_variance(t,lam,1.4))<2e-10,
              'random locations covariance direct Schur check')

x=sp.symbols('x',real=True)
bs=2*x-3+4*sp.exp(-x)-sp.exp(-2*x)
vs=2*x-4*sp.tanh(x/2)
check(sp.simplify(sp.diff(bs,x)-2*(1-sp.exp(-x))**2)==0,'boundary derivative')
check(sp.simplify(sp.diff(vs,x)-2*sp.tanh(x/2)**2)==0,'bridge derivative')
check(sp.series(bs,x,0,5).removeO().coeff(x,3)==sp.Rational(2,3),'boundary cubic')
check(sp.series(vs,x,0,5).removeO().coeff(x,3)==sp.Rational(1,6),'bridge cubic')

u,w,z=sp.symbols('u w z',real=True)
Y=(1+w-u)**3
Z=(1+z-w)**3
m3=sp.integrate(sp.integrate(Y,(u,0,1)),(w,0,1))
m6=sp.integrate(sp.integrate(Y**2,(u,0,1)),(w,0,1))
m33=sp.integrate(sp.integrate(sp.integrate(Y*Z,(u,0,1)),(w,0,1)),(z,0,1))
check(m3==sp.Rational(3,2),'E[(1+V-U)^3]')
check(m6-m3*m3==sp.Rational(16,7),'variance of cubic gaps')
check(m33-m3*m3==-sp.Rational(307,336),'adjacent gap covariance')
check((m6-m3*m3+2*(m33-m3*m3))/36==sp.Rational(11,864),'CLT variance coefficient')

for lam in (0.5,1,2):
    for n in (100,1000):
        t=design(n,lam)
        vz=local_variance(t,lam,1)
        check(abs(n*n*vz-lam/6)<0.005,'optimal leading coefficient')
    rng=np.random.default_rng(400)
    n=1000
    t=(np.arange(n)+rng.random(n))/n
    vsamp=local_variance(t,lam,1)
    cc=sum((1+np.diff(n*t-np.arange(n)))**3)/(6*n)
    check(abs(n*n*vsamp-lam*cc)<0.02,'jitter cubic approximation')

print(f'PASS: {checks} checks. Cubic moments {m3}, {m6}, adjacent product {m33}; CLT variance 11/864.')
