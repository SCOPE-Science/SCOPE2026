"""Reproducible independent checks of normal-intersection far-field asymptotics."""
import math
import numpy as np

def h_deriv(theta, eps):
    return -2*eps*np.sin(2*theta)

def calc_radius(t, p, eps):
    delta = p-t
    # a n(t)+b t(t) solves the two normal equations
    b = h_deriv(t,eps)
    a = (b*np.cos(delta)-h_deriv(p,eps))/np.sin(delta)
    return np.hypot(a,b)

def main():
    eps = 0.2
    rng=np.random.default_rng(89134)
    N=4_000_000
    counts=np.zeros(4,dtype=np.int64)
    thresholds=np.array([20.,40.,80.,160.])
    step=200000
    for _ in range(N//step):
        t=rng.random(step)*2*math.pi
        p=rng.random(step)*2*math.pi
        r=calc_radius(t,p,eps)
        counts += np.count_nonzero(r[:,None]>thresholds[None,:],axis=0)
    C=8*eps/math.pi**2
    print('smooth support h(theta)=1+eps*cos(2theta), eps',eps)
    print('curvature radius min',1-3*eps)
    print('exact predicted coefficient',C)
    for R,n in zip(thresholds,counts):
        prob=n/N
        ratio=(R*prob)/C
        se=(R/C)*np.sqrt(prob*(1-prob)/N)
        print('threshold',R,'count',n,'R*P',R*prob,'ratio',ratio,'se of ratio',se)
        assert abs(ratio-1)<0.15+4*se
    # Independently verify strictly positively curved constant-width h=1+eta*cos(3t).
    eta=0.1
    assert 1-8*eta>0
    def r_cw(t,p):
        b=-3*eta*np.sin(3*t)
        q=-3*eta*np.sin(3*p)
        a=(b*np.cos(p-t)-q)/np.sin(p-t)
        return np.hypot(a,b)
    t=rng.random(500000)*2*math.pi
    p=rng.random(500000)*2*math.pi
    rr=r_cw(t,p)
    assert np.all(np.isfinite(rr))
    print('constant-width third-harmonic support, max sampled intersection radius:',rr.max())
    print('NORMAL_INTERSECTION_CHECKS_OK')
if __name__=='__main__':main()
