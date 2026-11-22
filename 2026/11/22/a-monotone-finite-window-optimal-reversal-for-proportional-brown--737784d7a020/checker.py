#!/usr/bin/env python3
"""Reproduce the finite-window optimal contraction of a Brownian jump diffusion.
Only the statistical model, independent checking, and deterministic numerics.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq, minimize_scalar

def weight_moments(b,tau):
    j=quad(lambda s:(tau-s)*math.exp(-b*s),0,tau,epsabs=1e-11)[0]
    m=quad(lambda s:s*(tau-s)*math.exp(-b*s),0,tau,epsabs=1e-11)[0]/j
    return j,m

def objective(b,tau):
    j,_=weight_moments(b,tau)
    return j/(b*(2-b))

def root_b(tau):
    return brentq(lambda b:weight_moments(b,tau)[1]-(1/(2-b)-1/b),1.0,4/3,xtol=1e-14)

def analytical_variance(a,tau,D=1.3,r=0.7):
    b=1-a
    return 4*D/(r*tau*tau)*objective(b,tau)

def check():
    tvals=[0.001,0.01,0.03,0.1,0.3,1,3,10,30,100,300]
    roots=[]; count=0
    for tau in tvals:
        b=root_b(tau)
        res=minimize_scalar(lambda z:objective(z,tau),bounds=(1.e-6,2-1.e-6),method='bounded',options={'xatol':1e-13})
        assert abs(res.x-b)<1.e-5, (tau,b,res.x)
        assert 1<b<4/3
        assert objective(b,tau) < objective(1,tau)
        assert abs(weight_moments(b,tau)[1]-(1/(2-b)-1/b))<1e-10
        roots.append(b)
        count+=4
        print(f'tau={tau:8.3f} optimal_a={1-b:+.10f} gain={1-objective(b,tau)/objective(1,tau):.8%}')
    assert all(roots[i]<roots[i+1] for i in range(len(roots)-1));count+=1
    assert abs((roots[0]-1)/(tvals[0]/6)-1)<0.01;count+=1
    assert abs((4/3-roots[-1])*(tvals[-1]*6)-1)<0.02;count+=1
    for a in [-.95,-.6,-.3333,-.1,0,.4,.8,.99]:
        for tau in [.1,1,5,30]:
            b=1-a
            k=.7*b
            D=1.3;r=.7;T=tau/r
            direct=4*D/(r*(1-a*a)*T*T)*(T/k-(1-math.exp(-k*T))/k**2)
            formula=analytical_variance(a,tau,D,r)
            assert abs(direct-formula)<2e-7*formula,(a,tau,direct,formula)
            count+=1
    # Symbolic stationary moment and autocovariance: L x = r(a-1)x, L x^2 = 2D+r(a^2-1)x^2.
    # Independent Monte Carlo: approximate the full finite-window variance of time integrals from random resets.
    rng=np.random.default_rng(20261115)
    r=1.0;D=1.0;T=3.0
    for a in [-0.7,-0.3,0.0,0.5]:
        # samples exact conditional-on-clock Gaussian path integrals via Brownian bridge each segment
        # Stationary start from series of Poisson cycles, with exponential backward age.
        n=22000
        vals=[]
        for _ in range(n):
            cur=0.0
            for k in range(80):
                e=rng.exponential(1/r)
                cur+= (a**k)*rng.normal(0,math.sqrt(2*D*e))
                if abs(a)**k<1e-8:break
            time=0.; area=0.
            while time<T:
                duration=min(rng.exponential(1/r),T-time)
                w=rng.normal(0,math.sqrt(2*D*duration))
                j=duration*.5*w+rng.normal(0,math.sqrt(D*duration**3/6))
                area+=duration*cur+j
                cur+=w
                time+=duration
                if time<T-1.e-12:cur*=a
            vals.append(area/T)
        empirical=np.var(vals,ddof=1)
        exact=analytical_variance(a,r*T,D,r)
        print('MonteCarlo',a,empirical,exact)
        assert abs(empirical-exact)/exact<0.09
        count+=1
    print('PASS',count,'assertions')
if __name__=='__main__':check()
