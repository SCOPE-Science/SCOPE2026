#!/usr/bin/env python3
"""Reproducible diagnostics for a high-dimensional sphere-triangle asymptotic.

Dependencies: numpy, scipy, sympy. Execute: python verify.py
The analytical proof, not this finite checker, establishes asymptotics.
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.special import betainc, gammaln

z = sp.symbols('z', real=True)
f = (1-z)*(1+z)**2/2
g = (1+z)/sp.sqrt(2*(1-z))
assert sp.simplify(f.subs(z,sp.Rational(1,3))-sp.Rational(16,27)) == 0
assert sp.simplify(g.subs(z,sp.Rational(1,3))-2*sp.sqrt(3)/3) == 0
assert sp.simplify(sp.diff(sp.log(f),z,2).subs(z,sp.Rational(1,3))+sp.Rational(27,8)) == 0
pref = sp.Rational(3,2)/sp.pi * g.subs(z,sp.Rational(1,3)) * sp.sqrt(4*sp.pi/sp.Rational(27,8)) * f.subs(z,sp.Rational(1,3))**(-sp.Rational(3,2))
assert sp.simplify(pref-27*sp.sqrt(6)/(16*sp.sqrt(sp.pi)))==0


def scalar_weight(d,t):
    m = (d-3)/2
    c = math.exp(gammaln(d/2)-gammaln((d-1)/2)-0.5*math.log(math.pi))
    # P(unit sphere coordinate < -sqrt((1-t)/2))
    cap = 0.5*betainc((d-1)/2,0.5,(1+t)/2)
    return c*max(0.,1-t*t)**m*cap


def exact_prob_and_conditional(d):
    opts=dict(epsabs=1e-100,epsrel=1e-10,limit=300,points=[1/3])
    q=quad(lambda t:scalar_weight(d,t),-1,1,**opts)[0]
    mean=quad(lambda t:t*scalar_weight(d,t),-1,1,**opts)[0]/q
    var=quad(lambda t:(t-mean)**2*scalar_weight(d,t),-1,1,**opts)[0]/q
    return 3*q,mean,d*var


def predicted(d):
    return 27*math.sqrt(6)/(16*math.sqrt(math.pi*d))*(16/27)**(d/2)


p3,_,_=exact_prob_and_conditional(3)
p5,_,_=exact_prob_and_conditional(5)
assert abs(p3-0.5)<1e-11,(p3,'p3')
assert abs(p5-17/70)<1e-11,(p5,'p5')
results={}
for d in (20,40,80,160,256):
    p,mean,scaled_var=exact_prob_and_conditional(d)
    results[d]=(p/predicted(d),mean,scaled_var)
assert abs(results[20][0]-1)<0.07
assert abs(results[80][0]-1)<0.021
assert abs(results[256][0]-1)<0.012
assert abs(results[256][1]-1/3)<0.004
assert abs(results[256][2]-16/27)<0.003

rng=np.random.default_rng(48717)
n=180000
d=6
xx=rng.normal(size=(n,d));yy=rng.normal(size=(n,d));zz=rng.normal(size=(n,d))
for a in (xx,yy,zz):
    a/=np.linalg.norm(a,axis=1,keepdims=True)
score_x=np.einsum('ij,ij->i', yy-xx,zz-xx)
score_y=np.einsum('ij,ij->i', xx-yy,zz-yy)
score_z=np.einsum('ij,ij->i', xx-zz,yy-zz)
observed=np.mean((score_x<0)|(score_y<0)|(score_z<0))
target,_,_=exact_prob_and_conditional(d)
sigma=math.sqrt(target*(1-target)/n)
assert abs(observed-target)<5.5*sigma,(observed,target,sigma)
print('VERIFY_OK exact_cases=2 saddle_identities=4 asymptotic_quadratures=5 conditional_moments=5 sphere_mc=180000')
print('p3=',p3,'p5=',p5,'mc6=',observed,'analytic6=',target)
for d,(ratio,mean,scaled_var) in results.items():
    print('d=',d,'exact_over_predicted=',round(ratio,7),'conditional_mean=',round(mean,7),'d_conditional_variance=',round(scaled_var,7))
