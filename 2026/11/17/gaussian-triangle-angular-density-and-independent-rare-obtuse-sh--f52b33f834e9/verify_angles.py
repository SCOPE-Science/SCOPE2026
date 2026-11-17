#!/usr/bin/env python3
"""Numerical corroboration of Gaussian-triangle angle and conditional-shape laws.

Run: python verify_angles.py
Dependencies: numpy, scipy. Checks are finite and not a substitute for proof.
"""
import math
import numpy as np
from scipy.integrate import dblquad
from scipy.special import betainc


def angular_density(alpha, beta, d):
    if not (0 < alpha < math.pi and 0 < beta < math.pi-alpha):
        return 0.0
    a,b,c=math.sin(alpha),math.sin(beta),math.sin(alpha+beta)
    return ((d-1)*2**(d-1)*3**(d/2)/math.pi
            *(a*b*c)**(d-1)/(a*a+b*b+c*c)**d)


def check_integrals():
    for d in (2,3,4,7):
        both,_=dblquad(lambda b,a:angular_density(a,b,d),0,math.pi,
                       lambda a:0,lambda a:math.pi-a,epsabs=2e-8,epsrel=2e-8)
        obt,_=dblquad(lambda b,a:angular_density(a,b,d),math.pi/2,math.pi,
                      lambda a:0,lambda a:math.pi-a,epsabs=2e-8,epsrel=2e-8)
        target=betainc(d/2,d/2,.25)
        assert abs(both-1)<5e-8, (d,both)
        assert abs(obt-target)<5e-8, (d,obt,target)
        print('quadrature',d,'mass',format(both,'.14f'),'one_obtuse',format(obt,'.14f'))


def check_factorization():
    rng=np.random.default_rng(20261108)
    for d in (2,5,17):
        a,b,c=rng.standard_normal((3,12000,d))
        x=b-a
        y=c-a
        z=(x+y)/math.sqrt(2)
        w=(x-y)/math.sqrt(2)
        U=np.sum(z*z,axis=-1)/3
        V=np.sum(w*w,axis=-1)
        T=U+V
        H=U/T
        J=np.sum(z*w,axis=-1)/(np.linalg.norm(z,axis=-1)*np.linalg.norm(w,axis=-1))
        Lx=np.sum(x*x,axis=-1)
        Ly=np.sum(y*y,axis=-1)
        Lc=np.sum((b-c)**2,axis=-1)
        r1=.5*T*(1+2*H+2*np.sqrt(3*H*(1-H))*J)
        r2=.5*T*(1+2*H-2*np.sqrt(3*H*(1-H))*J)
        r3=2*T*(1-H)
        assert max(np.max(np.abs(Lx-r1)),np.max(np.abs(Ly-r2)),np.max(np.abs(Lc-r3)))<1e-10
        assert np.array_equal((x*y).sum(axis=1)<0,H<.25)
        print('factorization',d,'maxerror',format(max(np.max(np.abs(Lx-r1)),np.max(np.abs(Ly-r2)),np.max(np.abs(Lc-r3))),'.3g'))


def check_tail():
    # Exact finite-d Beta-tail ratio for scaled obtuseness margin -> Exp(1).
    for d in (20,80,320,1000):
        den=betainc(d/2,d/2,.25)
        assert den>0
        errors=[]
        for t in (0.3,0.7,1.5,3.0):
            p=betainc(d/2,d/2,(1-3*t/d)/4)/den
            errors.append(abs(p-math.exp(-t)))
        print('conditional_exp_tail',d,'maxerr',format(max(errors),'.6g'))
        if d==1000:
            assert max(errors)<.012


if __name__=='__main__':
    check_integrals()
    check_factorization()
    check_tail()
    print('GAUSSIAN_TRIANGLE_ANGLE_SHAPE_LAWS_OK')
