"""Numerical and algebraic checks for conditional two-edge direction laws."""
import numpy as np
from scipy.integrate import quad
from scipy.special import ellipk, ellipe
from scipy.optimize import brentq
from math import pi


def weight(n, s, t, psi):
    d = 1.0-s-t+s*t*np.sin(psi/2)**2
    return np.where(d>0,np.maximum(d,1e-300)**((n-5)/2),0.0)


def expected_cos(n,s,t):
    if n==4 and s+t>1:
        q=(s+t-1)/(s*t)
        return 1-2*q*ellipe(1-1/q)/ellipk(1-1/q)
    numer=quad(lambda phi: float(np.cos(phi)*weight(n,s,t,phi)),0,2*pi,epsabs=1e-11,points=[pi],limit=250)[0]
    denom=quad(lambda phi: float(weight(n,s,t,phi)),0,2*pi,epsabs=1e-11,points=[pi],limit=250)[0]
    return numer/denom


def sample(n,count,seed):
    rng=np.random.default_rng(seed)
    out=np.empty((count,3))
    for start in range(0,count,10000):
        m=min(10000,count-start)
        g=rng.standard_normal((m,n,2))
        q,_=np.linalg.qr(g)
        a,b=q[:,0,:],q[:,1,:]
        s=np.einsum('ij,ij->i',a,a)
        t=np.einsum('ij,ij->i',b,b)
        c=(a[:,0]**2-a[:,1]**2)*(b[:,0]**2-b[:,1]**2)+4*a[:,0]*a[:,1]*b[:,0]*b[:,1]
        out[start:start+m]=np.column_stack((s,t,c/(s*t)))
        # Gram determinant equals angular kernel, even for independent samples.
        u=a[:,0]*b[:,0]+a[:,1]*b[:,1]
        det=(1-s)*(1-t)-u*u
        angle_det=1-s-t+s*t*(1-out[start:start+m,2])/2
        assert np.max(np.abs(det-angle_det))<3e-12
        assert np.min(det)>=-3e-12
    return out


def run():
    for n in (4,5,6,8):
        print('n',n,'test conditional cos',expected_cos(n,.40,.37))
    assert expected_cos(4,.40,.37)>0
    assert abs(expected_cos(5,.40,.37))<1e-12
    assert expected_cos(6,.40,.37)<0
    assert expected_cos(8,.40,.37)<expected_cos(6,.40,.37)
    for n in (4,5,7):
        s,t=.68,.61
        zmax=1+2*(1-s-t)/(s*t)
        assert -1<zmax<1
        for z in np.linspace(-1,1,25):
            geom=((2-s-t)**2>=s*s+t*t+2*s*t*z)
            matrix=(1-s-t+(s*t/2)*(1-z)>=0)
            assert geom==matrix
        X=sample(n,130000,100+n)
        # one narrow band of lengths, compare measured conditional means.
        mask=(abs(X[:,0]-.4)<.035)&(abs(X[:,1]-.37)<.035)
        value=float(np.mean(X[mask,2])); target=expected_cos(n,.4,.37)
        assert sum(mask)>150, (n,sum(mask))
        assert abs(value-target)<.09, (n,value,target,sum(mask))
        print('empirical',n,sum(mask),value,'theoretical',target)
    # Independent elliptic evaluation of the unique four-edge alignment threshold.
    f=lambda q: 1.0-2*q*ellipe(1-1/q)/ellipk(1-1/q)
    root=brentq(f, .15, .20, xtol=1e-14)
    assert abs(root-.1738852340151234)<2e-12
    assert f(.15)>0 and f(.20)<0
    assert np.all(np.diff([f(q) for q in np.linspace(.02,.95,40)])<0)
    # Use the original angular integral, not elliptic functions, at four
    # sample length pairs lying on opposite sides of the threshold.
    for s,t in [(.515,.515),(.525,.525),(.55,.55),(.65,.65)]:
        q=(s+t-1)/(s*t)
        mean=expected_cos(4,s,t)
        assert (mean>0)==(q<root), (s,t,q,mean)
        print('four-edge crossover',s,t,q,mean)
    print('critical_q',root)
    print('STIEFEL_EDGE_ANGLE_CHECKS_OK')

if __name__=='__main__':
    run()
