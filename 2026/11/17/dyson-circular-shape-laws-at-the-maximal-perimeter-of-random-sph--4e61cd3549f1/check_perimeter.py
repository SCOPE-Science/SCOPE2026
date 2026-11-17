#!/usr/bin/env python3
"""Numerical consistency check for maximal spherical-triangle perimeter tail.
Requires numpy and scipy. It is not an infinite-proof certificate.
"""
import numpy as np
from scipy.special import roots_legendre, gamma, betainc
from math import pi

def constant(d):
    a=(d-2)/2
    return np.sqrt(pi)*gamma(d/2)**2/(2*(d-2)*gamma((d-1)/2)*gamma((d-2)/2))*4**(-a)*gamma(1+1.5*a)/gamma(1+a/2)**3

def event_probability(d, eps, order=600):
    x,w=roots_legendre(order)
    b=(x+1)*pi/2
    w=w*pi/2
    B=b[:,None]
    D=b[None,:]
    S=np.sin(B)*np.sin(D)
    t=2*pi-eps-B-D
    z=(np.cos(np.clip(t,0,pi))-np.cos(B)*np.cos(D))/S
    alpha=(d-2)/2
    p=betainc(alpha,alpha,np.clip((1+z)/2,0,1))
    p=np.where(t<=0,1,np.where(t>=pi,0,p))
    f=gamma(d/2)/(np.sqrt(pi)*gamma((d-1)/2))*np.sin(b)**(d-2)
    wf=w*f
    return np.sum(p*wf[:,None]*wf[None,:])

def main():
    assert abs(constant(4)-3/(4*pi))<1.e-12
    assert abs(constant(6)-1/4)<1.e-12
    # Check the triangular Dyson integral in the exactly integrable cases alpha=0,1.
    xx,ww=roots_legendre(180)
    xx=(xx+1)*pi/2
    ww=ww*pi/2
    X=xx[:,None]
    Y=xx[None,:]
    # substitution y=(pi-x)*v, v in (0,1)
    t=(xx+1)/pi # unused variable is harmless
    for alpha in (0.,1.):
        X0=xx[:,None]
        Y0=(pi-X0)*((xx[None,:])/pi)
        W=ww[:,None]*(pi-X0)*(ww[None,:]/pi)
        val=np.sum(W*(np.sin(X0)*np.sin(Y0)*np.sin(X0+Y0))**alpha)
        exact=pi*pi/(2*8**alpha)*gamma(1+1.5*alpha)/gamma(1+alpha/2)**3
        assert abs(val-exact)<3.e-6,(alpha,val,exact)
    for d in (3,4,5,6,8):
        alpha=(d-2)/2
        c=constant(d)
        p=event_probability(d,0.002)
        ratio=p/(c*0.002**alpha)
        print(f'd={d} coefficient={c:.12f} p={p:.12g} asymptotic_ratio={ratio:.8f}')
        assert 0.998<ratio<1.003
    print('SPHERICAL_DYSON_PERIMETER_CHECKS_OK')

if __name__=='__main__':
    main()
