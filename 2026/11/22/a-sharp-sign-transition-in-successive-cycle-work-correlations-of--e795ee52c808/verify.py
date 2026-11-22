#!/usr/bin/env python3
"""Independent checks for the full-shift active-bath engine correlation theorem.
Requires Python 3.9+ and NumPy for the optional Gaussian-sample cross-check.
This script contains no external files or network calls.
"""
import math


def active_diagonal(a, b, tau, A2=1., gamma=1.):
    if abs(a-b) < 1.e-11:
        z = tau*math.exp(-2*a*tau)
    else:
        z = (math.exp(-(a+b)*tau)-math.exp(-2*a*tau))/(a-b)
    return 2*A2/gamma**2/(a+b) * (-math.expm1(-2*a*tau)/(2*a)-z)


def active_adjacent(a, b, tau, A2=1., gamma=1.):
    if abs(a-b) < 1.e-11:
        return A2/gamma**2 * tau*math.exp(-a*tau)*(-math.expm1(-2*a*tau))/(2*a)
    return A2/gamma**2 * (-math.expm1(-(a+b)*tau)) * (math.exp(-b*tau)-math.exp(-a*tau)) / (a*a-b*b)


def G(a,b,tau):
    if abs(a-b) < 1.e-11:
        return tau*(-math.expm1(-2*a*tau))/(2*a)
    return (-math.expm1(-(a+b)*tau)) * math.expm1((a-b)*tau)/(a*a-b*b)


def simpson(f, lo, hi, n=150):
    assert n%2==0
    h=(hi-lo)/n
    return h/3*(f(lo)+f(hi)+4*sum(f(lo+h*j) for j in range(1,n,2))+
                2*sum(f(lo+h*j) for j in range(2,n,2)))


def numerical_active_pair(a,b,tau,A2=1.,gamma=1.):
    c=A2/gamma**2
    diag=2*c*simpson(lambda u: simpson(lambda v: math.exp(-a*(2*tau-u-v))*math.exp(-b*(u-v)),0,u),0,tau)
    adj=c*simpson(lambda u: simpson(lambda v: math.exp(-a*(2*tau-u-v))*math.exp(-b*(tau+v-u)),0,tau),0,tau)
    return diag,adj


def work_covariance(a,b,tau,A2,sigma2,kappa=1.,gamma=1.,lag=1):
    h=math.exp(-a*tau)
    K=active_adjacent(a,b,tau,A2,gamma)
    return (kappa*kappa/2)*(K*K-h*h*sigma2*sigma2) if lag==1 else (kappa*kappa/2)*K*K*math.exp(-2*b*(lag-1)*tau)


def main():
    cases=[(.3,1.5,.8), (1.,.5,1.), (1.,2.,1.), (1.,1.,2.), (2.,.1,.75),(.2,.8,1.7)]
    for a,b,t in cases:
        d,k=numerical_active_pair(a,b,t)
        assert math.isclose(active_diagonal(a,b,t),d,rel_tol=4.e-5,abs_tol=4.e-6),(a,b,t,'diag',d,active_diagonal(a,b,t))
        assert math.isclose(active_adjacent(a,b,t),k,rel_tol=8.e-9,abs_tol=1.e-9),(a,b,t,'adj',k,active_adjacent(a,b,t))
        assert math.isclose(active_adjacent(a,b,t)*math.exp(a*t),G(a,b,t),rel_tol=5.e-11,abs_tol=5.e-11)
    for a,b in [(1.,.5),(1.,1.),(1.,2.),(.5,3.)]:
        last=0.
        for j in range(1,301):
            t=j/60
            value=G(a,b,t)
            assert value>last, (a,b,j,last,value)
            last=value
    # Cross-check the covariance formulas against independent multivariate Gaussian simulation.
    try:
        import numpy as np
    except ImportError:
        print('NumPy missing: optional Monte Carlo cross-check skipped')
    else:
        rng=np.random.default_rng(20261115)
        for a,b,t,A2,sigma2 in [(1.,.5,1.,.4,1.),(1.,.5,2.,3.,1.),
                                (1.,2.,1.,2.,1.),(1.,2.,1.,10.,1.),(1.,1.,3.,1.,1.)]:
            n=320000
            V=active_diagonal(a,b,t,A2)+(-math.expm1(-2*a*t))/a # gamma=kappa=kBT=1
            K=active_adjacent(a,b,t,A2)
            Q=np.array([[V,K,K*math.exp(-b*t)],
                        [K,V,K], [K*math.exp(-b*t),K,V]])
            B=rng.standard_normal((n,3))@np.linalg.cholesky(Q).T
            eps=rng.standard_normal((n,4))*math.sqrt(sigma2)
            Ys=B-math.exp(-a*t)*eps[:,:3]
            Ws=.5*(Ys**2-eps[:,1:4]**2)
            for lag in (1,2):
                x=Ws[:,0];y=Ws[:,lag]
                obs=np.mean((x-x.mean())*(y-y.mean()))
                target=work_covariance(a,b,t,A2,sigma2,lag=lag)
                stderr=math.sqrt((np.mean((x-x.mean())**2*(y-y.mean())**2)-obs**2)/n)
                assert abs(obs-target)<7*stderr+1.e-4,(a,b,t,A2,sigma2,lag,obs,target,stderr)
                print('mc:',(a,b,t,A2,sigma2),'lag',lag,'expected',round(target,7),'observed',round(obs,7),'SE',round(stderr,7))
    assert work_covariance(1,2,100,2,1,lag=1)<0
    assert work_covariance(1,2,2,20,1,lag=1)>0
    assert work_covariance(1,.5,.01,20,1,lag=1)<0
    assert work_covariance(1,.5,10,20,1,lag=1)>0
    for a,b,t,A2 in [(1,2,.6,1.),(1,1,1,1.),(1,.5,3,1.)]:
        assert work_covariance(a,b,t,A2,1,lag=2)>0
    print('PASS: analytical and independent numerical tests, 1200 monotonicity points, simulated Gaussian work covariance')

if __name__=='__main__': main()
