#!/usr/bin/env python3
"""Numerical cross-checks for the normal-pair law of symmetric catenoid bands.
This is independent finite-precision corroboration, not a substitute for proof.
Requires numpy and scipy. Run: python checker.py
"""
import math
import numpy as np
from scipy.special import roots_legendre, eval_legendre
from scipy.integrate import quad
from scipy.optimize import brentq

def h(b): return b + 0.5*math.sinh(2*b)
def j(b): return (20*b+15*math.sinh(2*b)+3*math.sinh(4*b)+math.sinh(6*b)/3)/32
def f(s):
    a=math.sqrt(2*s); m=min(2.,a)
    t=math.sqrt(max(a*a-m*m,0.))
    return (2*m*t+2*a*a*math.asin(m/a)-(2/3)*(a**3-t**3))/(4*math.pi)
def numerical_prob(b,s,n=460):
    x,v=roots_legendre(n); a=math.tanh(b)
    z=a*x
    w=a*v/(1-z*z)**2/h(b)
    q=(1-b*b*s-z[:,None]*z[None,:])/np.sqrt((1-z[:,None]**2)*(1-z[None,:]**2))
    c=np.arccos(np.clip(q,-1,1))/math.pi
    return float(np.einsum('i,ij,j->',w,c,w,optimize=True))

def check():
    checks=0
    for b in (0.08,0.3,0.7,1.4):
        z,v=roots_legendre(440); a=math.tanh(b)
        w=a*v/(1-(a*z)**2)**2/h(b)
        assert abs(w.sum()-1)<1e-11
        checks+=1
        m=(0.5*math.sinh(2*b)-b)/h(b)
        assert abs(np.dot(w,(a*z)**2)-m)<1e-11
        checks+=1
        mu2=(3*m-1)/2
        assert abs(np.dot(w,eval_legendre(2,a*z))-mu2)<1e-11
        checks+=1
        c=j(b)/h(b)**2
        assert abs(quad(lambda zz: (1-zz*zz)**(-4),-a,a,epsabs=1e-11)[0]/h(b)**2-c)<1e-10
        checks+=1
    b0=brentq(lambda b:math.sinh(2*b)-4*b,0.2,2.)
    assert abs(b0-1.08865949248265)<1e-11
    checks+=1
    for s in (0.05,0.2,1.,2.,3.,8.):
        a=math.sqrt(2*s)
        val=quad(lambda u:(2-abs(u))*math.sqrt(max(0,2*s-u*u)), -min(2,a),min(2,a),epsabs=1e-10)[0]/(4*math.pi)
        assert abs(val-f(s))<2e-10,(s,val,f(s))
        checks+=1
    for b in (0.07,0.03):
        for s in (0.2,1,2,3):
            err=abs(numerical_prob(b,s)/b-f(s))
            assert err < (0.0015 if b==0.07 else 0.00035),(b,s,err)
            checks+=1
    # The two asymptotic ends of the explicit crossover profile.
    assert abs(f(1e-6)/(1e-6/2)-1)<0.0005
    assert abs(f(1e5)/(math.sqrt(2e5)/math.pi)-1)<3e-5
    checks+=2
    print('PASS',checks,'numerical comparisons')
    print('critical_halfheight',format(b0,'.14f'))
    print('critical_normal_latitude',format(math.tanh(b0),'.14f'))
    print('F(1)',format(f(1),'.14f'))
    print('F(2)',format(f(2),'.14f'))
    print('F(3)',format(f(3),'.14f'))

if __name__=='__main__':check()
