"""Numerical corroboration of late dwell-time Floquet windows.

The infinite-window theorem is proved analytically; finite tests here are not proof.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq


def constants(a, d):
    w = math.sqrt(1.0-a*a/4)
    k = math.sqrt((d+a/2)**2-1)
    eta = ((a*(a+2*d)/4)-1)/(w*k)
    sig = a-d+k
    mu = a-d-k
    R=math.hypot(1,eta)
    theta=math.atan(eta)
    return w,k,eta,sig,mu,R,theta


def tr_det(t,a,d):
    w,k,eta,sig,mu,R,theta=constants(a,d)
    return (math.exp(sig*t)*(math.cos(w*t)+eta*math.sin(w*t))+
            math.exp(mu*t)*(math.cos(w*t)-eta*math.sin(w*t)),
            math.exp(2*(a-d)*t))


def test(a,d,indices):
    w,k,eta,sig,mu,R,theta=constants(a,d)
    assert sig>0 and mu<0
    A0=np.array([[0.,-1.],[1.,a]])
    A1=np.array([[-2*d,-1.],[1.,a]])
    print('PARAM',a,d,'omega',w,'kappa',k,'sigma',sig,'eta',eta)
    for n in indices:
        t=(theta+math.pi/2+n*math.pi)/w
        tr,D=tr_det(t,a,d)
        # direct independent numerical matrix exponential trace for moderate half-period
        phi=expm(t*A1)@expm(t*A0)
        den=max(1.,abs(tr))
        assert abs(np.trace(phi)-tr)/den < 1e-7
        assert abs(np.linalg.det(phi)-D) < 1e-6 if t<9 else True
        assert D<1 and abs(tr)<1+D
        h=math.exp(-sig*t)/(w*R)
        # root target signs: left trace ~=(-1)^n, right opposite
        direction = (-1)**(n+1)
        def f(t_,side):
            tr_,D_=tr_det(t_,a,d)
            return tr_-side*(1+D_)
        lo=brentq(lambda z:f(z,-direction),t-3*h,t)
        hi=brentq(lambda z:f(z,direction),t,t+3*h)
        wl=hi-lo
        ratio=wl/(2*h)
        assert ratio>0.85 and ratio<1.15 if n>=5 else ratio>0.5
        print('WINDOW n',n,'center',round(t,8),'width',format(wl,'.12g'),'scaled_ratio',format(ratio,'.9g'))
    print('VERIFY_OK matrices_and_jury',len(indices),'exact_trace_vs_expm',len(indices),'finite_numerics_only')

if __name__=='__main__':
    test(0.1,11.0,[2,4,6,8,10])
    test(0.4,3.0,[2,4,6,8])
