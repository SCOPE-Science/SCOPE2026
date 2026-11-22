#!/usr/bin/env python3
"""Reproduce finite checks for a weighted Bergman composition-difference boundary law.
The infinite-parameter assertions require the proof in RESULT.md, not this script.
Requires scipy, sympy and numpy.
"""
import math
import warnings
import numpy as np
import sympy as sp
from scipy.integrate import quad, IntegrationWarning

x,y,c=sp.symbols('x y c', real=True)
w=x+sp.I*y
z=1-w
phi=1-c*w
rho=sp.expand(1-z*sp.conjugate(z))
rhophi=sp.expand(1-phi*sp.conjugate(phi))
assert sp.simplify(rhophi-(c*rho+c*(1-c)*(x*x+y*y)))==0
assert sp.simplify(sp.beta(sp.Rational(3,2),sp.Rational(5,2)).rewrite(sp.gamma)-sp.pi/sp.Integer(16))==0

checks=2

def angular_density(r, alpha, c, gamma, beta, eps):
    p=alpha+2
    vmax=2/r-1
    def vfun(v):
        cost=r*(v+1)/2
        sine=math.sqrt(max(0.0,1-cost*cost))
        w=r*(cost+1j*sine)
        z=1-w
        phi=1-c*w
        psi=phi+eps*(c*w)**gamma
        R=1-abs(phi)**2
        S=1-abs(psi)**2
        B=1-phi*psi.conjugate()
        # exact squared norm of kernel difference, robust here at finite radii
        if min(R,S)<=0: raise ArithmeticError('symbol left disk')
        G=R**(-p)+S**(-p)-2*(B**(-p)).real
        if G < -1e-6*max(R**(-p),S**(-p)):
            raise ArithmeticError('negative squared kernel norm beyond rounding')
        G=max(0,G)
        # two conjugate arcs, using v=(1-|z|^2)/r^2
        return (alpha+1)/math.pi*(r*r*v)**alpha*abs(z)**2*r**(2*beta)*G*r*r/sine
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore',category=IntegrationWarning)
        edges=sorted(set([0,1,4,16,min(50,vmax*.8),vmax]))
        return sum(quad(vfun,a,b,epsabs=2e-11,epsrel=2e-6,limit=400)[0]
                   for a,b in zip(edges[:-1],edges[1:]) if a<b)

cases=[(0.0,0.5,2.5,0.0,.01),
       (1.0,0.5,2.5,0.0,.01),
       (0.0,0.7,2.25,0.25,.01),
       (0.0,0.5,2.2,0.0,.01)]
for alpha,c,gamma,beta,eps in cases:
    D=2*(abs(eps)**2)*c**(2*gamma-alpha-4)/(math.pi*(1-c)**3)
    for r in [.05,.02]:
        actual=angular_density(r,alpha,c,gamma,beta,eps)
        predicted=D*r**(2*(gamma+beta)-6)
        ratio=actual/predicted
        print(f'alpha={alpha}, c={c}, gamma={gamma}, beta={beta}, r={r}, local_ratio={ratio:.8f}')
        assert .94<ratio<1.06,(alpha,c,gamma,beta,r,ratio)
        checks+=1

# Beta-integral normalization for alpha=0,1,2 and rational kappa.
v=sp.symbols('v',positive=True)
for a in [0,1,2]:
    p=a+2
    kap=sp.Rational(1,2)
    integral=sp.integrate(v**a/(v+kap)**(p+2),(v,0,sp.oo))
    expected=2/(sp.Integer(a+1)*p*(p+1)*kap**3)
    assert sp.simplify(integral-expected)==0,(a,integral,expected)
    checks+=1
print('PASS',checks,'supplementary checks')
