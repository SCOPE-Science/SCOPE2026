"""Independent geometric/numerical corroboration for constant-width boundary-tail law.
Only numerical checks; the theorem requires the separate analytic proof.
"""
import numpy as np
from scipy.optimize import brentq
from scipy.special import ellipe

TWOPI=2*np.pi

def point(theta, lam):
    # h=1+(lam/8) cos(3theta), h'=-3(lam/8)sin(3theta)
    h=1+lam*np.cos(3*theta)/8
    dh=-3*lam*np.sin(3*theta)/8
    return np.array([h*np.cos(theta)-dh*np.sin(theta),h*np.sin(theta)+dh*np.cos(theta)])

def rho(theta,lam):
    return 1-lam*np.cos(3*theta)

def exact_probability(lam,eps,n=600):
    th=(np.arange(n)+0.5)*TWOPI/n
    acc=0.
    for theta in th:
        x=point(theta,lam)
        def fun(u): return np.linalg.norm(x-point(theta+np.pi+u,lam))-(2-eps)
        lo=brentq(fun,-np.pi,0,xtol=1e-13)
        hi=brentq(fun,0,np.pi,xtol=1e-13)
        # normal-angle arclength density for second endpoint, integrated exactly
        inner=(hi-lo)+(lam/3)*(np.sin(3*theta+3*hi)-np.sin(3*theta+3*lo))
        acc+=rho(theta,lam)*inner
    return acc/(n*TWOPI)

def coeff(lam):
    return 4*ellipe(lam*lam)/(np.pi*np.pi) # width 2

def check():
    # Algebraic exact local quadratic coefficient via symmetric finite differences
    for lam in [0.,.3,.7,.9]:
        for th in np.linspace(0,2*np.pi,17,endpoint=False):
            eps=2e-4
            x=point(th,lam)
            dplus=np.linalg.norm(x-point(th+np.pi+eps,lam))
            dminus=np.linalg.norm(x-point(th+np.pi-eps,lam))
            q=((2-dplus)+(2-dminus))/(2*eps**2)
            target=(rho(th,lam)*rho(th+np.pi,lam))/4
            assert abs(q-target) < 5e-6,(lam,th,q,target)
    for lam in [0,.3,.7,.9]:
        c=coeff(lam)
        for eps in [1e-3,2.5e-4]:
            p=exact_probability(lam,eps,n=480)
            ratio=p/(c*np.sqrt(eps))
            assert abs(ratio-1)<.015,(lam,eps,ratio)
    assert abs(coeff(0)-2/np.pi)<1e-13
    assert coeff(.8)<coeff(.3)<coeff(0)
    print('CONSTANT_WIDTH_HELLINGER_TAIL_CHECKS_OK',68+8+3)

if __name__=='__main__': check()
