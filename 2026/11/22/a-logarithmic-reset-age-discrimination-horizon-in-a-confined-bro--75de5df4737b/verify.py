#!/usr/bin/env python3
"""Standalone numerical checks for an exact Gaussian clock-discrimination identity."""
import math
import scipy.integrate as si
import scipy.special as sp
from scipy.stats import chi2,norm


def risk(n,k,delta,t):
    z=math.exp(-2*k*t); c=-math.expm1(-2*k*delta)
    if z==0: return 0.5
    if z==1: return 0.0
    q=1+c*z/(1-z)
    l=math.log(q)
    if l == 0.0: return 0.5
    h=l/math.expm1(l)
    return .5*(chi2.sf(n*q*h,n)+chi2.cdf(n*h,n))

def mean_risk(n,k,r,delta):
    # integrate on a time window centered at the logarithmic information horizon
    t0=math.log(n)/(4*k)
    return si.quad(lambda t:r*math.exp(-r*t)*risk(n,k,delta,t),0,max(30/r,t0+40/k),epsabs=1e-13,limit=500)[0]

def K(k,r,delta):
    p=r/(2*k); c=-math.expm1(-2*k*delta)
    return 2**(2*p-1)*sp.gamma((p+1)/2)/(math.sqrt(math.pi)*c**p)

def exact_finite_checks():
    # Cross-check the chi-square likelihood-threshold expression by direct
    # integration of the competing Gaussian radial densities.
    from scipy.stats import chi2
    for n in (1,2,3,8):
        for k,dt,t in ((1.,.7,.2),(.5,2.,1.5),(2.,.3,4.)):
            v0=1-math.exp(-2*k*t)
            v1=1-math.exp(-2*k*(t+dt))
            q=v1/v0
            threshold=n*v0*q*math.log(q)/(q-1)
            r0=si.quad(lambda u:chi2.pdf(u/v0,n)/v0,threshold,math.inf,
                       epsabs=1e-12)[0]
            r1=si.quad(lambda u:chi2.pdf(u/v1,n)/v1,0,threshold,
                       epsabs=1e-12)[0]
            assert abs((r0+r1)/2-risk(n,k,dt,t))<2e-8
            # Verify a Gaussian-affinity upper bound at the same parameters.
            z=math.exp(-2*k*t); c=1-math.exp(-2*k*dt)
            bound=.5*math.exp(-n*c*c*z*z/16)
            assert risk(n,k,dt,t)<=bound+1e-12
    for k,r,delta in ((1.,1.3,.7),(2.,1.,.3),(1.,2.,1.)):
        p=r/(2*k); c=1-math.exp(-2*k*delta)
        gaussconst=p*si.quad(lambda u:u**(p-1)*norm.sf(c*u/(2*math.sqrt(2))),
                              0,math.inf,epsabs=1e-12)[0]
        assert abs(gaussconst/K(k,r,delta)-1)<1e-7

def critical_test():
    k=1;delta=0.7;c=-math.expm1(-2*k*delta)
    for n in [100,1000,10000,100000]:
        for s in [-0.25,0,0.35]:
            t=math.log(n)/(4*k)+s
            if t<0: continue
            obs=risk(n,k,delta,t)
            pred=norm.cdf(-c*math.exp(-2*k*s)/(2*math.sqrt(2)))
            assert 0 <= obs <= 0.5
            if n >= 10000:
                assert abs(obs-pred) < .003, (n,s,obs,pred)
            print('critical',n,s,round(obs,9),round(pred,9))

def annealed_test():
    for k,r,delta in [(1,1.3,.7),(2,1,.3),(1,2,1)]:
        print('parameters',k,r,delta,'constant',K(k,r,delta))
        for n in [100,1000,10000,100000]:
            x=mean_risk(n,k,r,delta)
            y=x*n**(r/(4*k))
            assert 0 < x < 0.5
            if n >= 10000:
                assert abs(y/K(k,r,delta)-1) < .035, (n,y,K(k,r,delta))
            print('annealed',n,round(x,9),round(y,9))

if __name__=='__main__':
    exact_finite_checks();critical_test();annealed_test()
    print('PASS')
