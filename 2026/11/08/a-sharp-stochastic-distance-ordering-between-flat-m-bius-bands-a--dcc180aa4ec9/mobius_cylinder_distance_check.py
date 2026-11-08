"""Reproducible numerical checks for geodesic-distance stochastic ordering.

Only numpy and scipy are needed. All coordinates are intrinsic flat strip coordinates.
"""
from math import sqrt, pi
import numpy as np
from scipy.integrate import quad


def triangular_cdf(z, b):
    z = max(0.0, min(1.0, z/(2*b)))
    return 1-(1-z)**2


def radius(x, r):
    return sqrt(max(0.0, r*r-x*x))


def exact_cdfs(a, b, r):
    # t=|x1-x2|, density 2(a-t)/a**2.
    def integrand(t, mobius):
        u, v = radius(t,r),radius(a-t,r)
        z=(u+v) if mobius else max(u,v)
        return 2*(a-t)/(a*a)*triangular_cdf(z,b)
    cuts=sorted({0., a, a/2, min(a,max(0.,r)), min(a,max(0.,a-r))})
    return tuple(sum(quad(lambda t:integrand(t, mob), lo, hi,
                          epsabs=2e-12, epsrel=2e-12)[0]
                     for lo,hi in zip(cuts[:-1],cuts[1:]))
                 for mob in (True,False))


def direct_simulation(a,b,N,seed):
    rng=np.random.default_rng(seed)
    x=rng.uniform(0,a,(N,2))
    y=rng.uniform(-b,b,(N,2))
    t=np.abs(x[:,0]-x[:,1])
    s=np.abs(y[:,0]-y[:,1])
    v=np.abs(y[:,0]+y[:,1])
    dm=np.sqrt(np.minimum(t*t+s*s, (a-t)**2+v*v))
    dc=np.hypot(np.minimum(t,a-t),s)
    return dm,dc


def main():
    for a,b in ((1.0,0.35),(1.0,1.0),(0.7,1.7),(3.0,0.24)):
        c=a/2
        R=sqrt(c*c+(2*b)**2)
        for r in np.linspace(0,R*1.1,31):
            fm,fc=exact_cdfs(a,b,float(r))
            assert -2e-11 <= fc <=1+2e-11 and fc <=fm+2e-11 and fm<=1+2e-11,(a,b,r,fm,fc)
            if r<=c+1e-12: assert abs(fm-fc)<1e-10
            if c+1e-6<r<R-1e-6: assert fm>fc+1e-10,(a,b,r,fm,fc)
        for eps in (1e-4,1e-5,1e-6):
            fm,fc=exact_cdfs(a,b,c+eps)
            coeff=(fm-fc)/(eps**1.5)
            target=4/(3*b*sqrt(a))
            assert abs(coeff/target-1)<0.07,(a,b,eps,coeff,target)
        dm,dc=direct_simulation(a,b,250000,20261104+int(1000*a)+int(100*b))
        for r in (c*.8,c+0.1*min(a,b),0.7*R):
            fm,fc=exact_cdfs(a,b,r)
            empirical_m=np.mean(dm<=r)
            empirical_c=np.mean(dc<=r)
            assert abs(empirical_m-fm)<0.007,(a,b,r,empirical_m,fm)
            assert abs(empirical_c-fc)<0.007,(a,b,r,empirical_c,fc)
        print('CASE',a,b,'means',float(dm.mean()),float(dc.mean()),'diam_c',R)
    print('MOBIUS_CYLINDER_CHECK_OK profiles=4 thresholds=124 samples=1000000')

if __name__=='__main__': main()
