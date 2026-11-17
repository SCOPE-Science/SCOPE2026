#!/usr/bin/env python3
"""Finite numerical corroboration of the circular spherical-tube Crofton law.

Requires Python 3, NumPy, SciPy. The analytic arguments are in RESULT.md.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import gammaln, ndtri


def mu(d):
    return math.exp(2*gammaln(d/2)-gammaln((d-1)/2)-gammaln((d+1)/2))


def density_constant(d):
    return 2*math.exp(gammaln(d/2)-gammaln((d-1)/2))/math.sqrt(math.pi)


def moments(d,r):
    assert d>=3 and r>1
    a=math.asin(1/r)
    c=density_constant(d)
    f=lambda t:c*math.sin(t)**(d-2)
    below=quad(lambda t:(1-r*math.sin(t))*f(t),0,a,epsabs=2e-12)[0]
    above=quad(lambda t:(r*math.sin(t)-1)*f(t),a,math.pi/2,epsabs=2e-12)[0]
    n=quad(lambda t:r*math.sin(t)*f(t),0,a,epsabs=2e-12)[0]+quad(f,a,math.pi/2,epsabs=2e-12)[0]
    deriv=quad(lambda t:math.sin(t)*f(t),0,a,epsabs=2e-12)[0]
    den=1+r*mu(d)
    return (above/den,2*n/den,below/den), n, deriv


def critical(d,r):
    _,n,deriv=moments(d,r)
    return deriv*(1+r*mu(d))-mu(d)*n


def optimum(d):
    return brentq(lambda r:critical(d,r),1+1e-7,1.5,xtol=2e-13)


def check():
    assert abs(mu(3)-math.pi/4)<1e-13
    assert abs(mu(4)-8/(3*math.pi))<1e-13
    comparisons=0
    for d in (3,4,5,6,10,20,40,100,200):
        r=optimum(d)
        p,n,deriv=moments(d,r)
        assert all(0<=v<=1 for v in p)
        assert abs(sum(p)-1)<3e-11
        assert abs(critical(d,r))<3e-10
        assert 1<r<1/mu(d)**2
        assert critical(d,max(1+1e-6,r-0.005))>0
        assert critical(d,r+0.005)<0
        assert abs(p[1]-2*n/(1+r*mu(d)))<1e-14
        assert p[1]>2*mu(d)/(1+mu(d))
        comparisons+=9
    # Existing elementary 3D circular-meridian formula for the shell probability.
    # In the source convention the tube radius is 1 and the center radius is R.
    for R in (1.05,1.3,2.0,4.0,8.0):
        a=1-0.5*math.sqrt(1-1/R**2)-0.5*R*math.asin(1/R)
        source_formula=a/(1+math.pi*R/4)
        assert abs(moments(3,R)[0][2]-source_formula)<2e-11
        comparisons+=1
    # Independent importance-weighted Haar simulations, conditioning on a hit.
    rng=np.random.default_rng(31917)
    for d,R in ((3,1.6),(4,1.3),(6,1.15),(10,1.07)):
        v=rng.standard_normal((240000,d))
        v/=np.linalg.norm(v,axis=1)[:,None]
        s=np.sqrt(1-v[:,-1]**2)
        halfwidth=1+R*s
        t=(2*rng.random(len(s))-1)*halfwidth
        c=R*s
        both=np.abs(t)<np.maximum(1-c,0)
        neither=np.abs(t)<np.maximum(c-1,0)
        one=~(both|neither)
        weights=halfwidth
        simulated=np.array([np.sum(weights*neither),np.sum(weights*one),np.sum(weights*both)])/sum(weights)
        truth=np.asarray(moments(d,R)[0])
        assert np.max(abs(simulated-truth))<0.007,(d,simulated,truth)
        comparisons+=3
    q=ndtri(.75)
    limloc=q*q/2
    limerror=q*math.exp(-q*q/2)/math.sqrt(2*math.pi)
    for d in (20,40,100,200):
        r=optimum(d)
        p=moments(d,r)[0]
        # Convergence is slow but monotone in the observed range.
        assert 0<d*(r-1)-limloc<0.016
        assert 0<d*(1-p[1])-limerror<0.012
        comparisons+=2
    print('PASS:',comparisons,'deterministic finite checks')
    print('Gaussian optimum:',limloc,limerror)
    for d in (3,4,10,40,200):
        r=optimum(d);print('dimension',d,'radius',format(r,'.12f'),'ball_probability',format(moments(d,r)[0][1],'.12f'))


if __name__=='__main__':
    check()
