#!/usr/bin/env python3
"""Numerical checks for the entropy-process theorem. Python standard library only.
Run: python3 CHECK.py
"""
import math
import random


def log_transform(k, kap, T, q):
    d = 2.0 * math.sqrt(k*k + 4.0*kap*kap*q*(1-q))
    a = 2.0*k
    # Stable alternative to log(cosh(dT)+h*sinh(dT)).
    h = (a*a+d*d)/(2*a*d)
    logden = d*T + math.log((1+h)+(1-h)*math.exp(-2*d*T))-math.log(2)
    return (a*T-logden)/2.0


def riccati_log_transform(k, kap, D, T, q, n=8000):
    # Feynman-Kac ansatz exp(A(t)*y*y+B(t)) for an OU-square integral.
    u = (2*kap*kap/D)*q*(q-1)
    h = T/n
    A = B = 0.0
    def f(a,b):
        return (8*D*a*a-4*k*a+u,4*D*a)
    for _ in range(n):
        ka1,kb1=f(A,B)
        ka2,kb2=f(A+h*ka1/2,B+h*kb1/2)
        ka3,kb3=f(A+h*ka2/2,B+h*kb2/2)
        ka4,kb4=f(A+h*ka3,B+h*kb3)
        A +=h*(ka1+2*ka2+2*ka3+ka4)/6
        B +=h*(kb1+2*kb2+2*kb3+kb4)/6
    return B-0.5*math.log1p(-2*D*A/k)


def mean_sigma(k,kap,T):
    return 2*kap*kap*T/k


def var_sigma(k,kap,T):
    return 4*kap*kap*T/k+4*kap**4*T/k**3-kap**4*(-math.expm1(-4*k*T))/k**4


def effective_diffusion(D,k,kap,lam):
    return D/2+kap*kap*D/(2*k*(k+lam))


def test():
    ncheck=0
    for k,kap,D,T in [(1.0,.7,1.3,1.0),(.4,1.9,.9,2.3),(1.7,.2,2.0,.5),(.9,1.1,.6,3.0)]:
        for q in [0.,.1,.25,.37,.5,.63,.75,.9,1.]:
            ref=log_transform(k,kap,T,q)
            ode=riccati_log_transform(k,kap,D,T,q,n=5000)
            assert abs(ref-ode)<3e-10,(k,kap,q,ref,ode)
            assert abs(ref-log_transform(k,kap,T,1-q))<1e-13
            ncheck+=2
        for q in [0.,1.]:
            assert abs(log_transform(k,kap,T,q))<1e-14
            ncheck+=1
        # Numerical derivatives of log E(e^{-qS}) at q=0.
        h=0.00002
        f0=log_transform(k,kap,T,0)
        f1=log_transform(k,kap,T,h)
        fm1=log_transform(k,kap,T,-h)
        m=(fm1-f1)/(2*h)
        v=(f1+fm1-2*f0)/h**2
        assert abs(m-mean_sigma(k,kap,T))<1e-5
        assert abs(v-var_sigma(k,kap,T))<0.002,(v,var_sigma(k,kap,T))
        ncheck+=2
        # Verify derivative of independent OU-square covariance integral.
        sig2=D/k
        n=5000
        dt=T/n
        covsum=sum(2*sig2**2*math.exp(-4*k*(j+.5)*dt)*(T-(j+.5)*dt)*dt for j in range(n))
        a=2*kap*kap/D
        independent_var=2*a*sig2*T+a*a*2*covsum
        assert abs(independent_var-var_sigma(k,kap,T))<1e-6*max(1, var_sigma(k,kap,T))
        ncheck+=1
    # Check transport is sensitive to orientation flip rate.
    assert effective_diffusion(1.3,0.7,1.2,0.2)>effective_diffusion(1.3,0.7,1.2,2.0)
    ncheck+=1
    # Sampling the conditional Gaussian mixture from an OU path uses no flip-rate.
    # Its first two moments can be checked without simulating telegraph orientation.
    rng=random.Random(30719)
    k=1.;kap=.8;D=1.4;T=1.5;npath=18000;steps=120
    dt=T/steps
    e=math.exp(-2*k*dt)
    c=2*kap*kap/D
    acc=acc2=0.
    for j in range(npath):
        Y=rng.gauss(0,math.sqrt(D/k))
        area=0.
        for i in range(steps):
            yn=e*Y+math.sqrt((D/k)*(1-e*e))*rng.gauss(0,1)
            area+=(Y*Y+yn*yn)*dt/2
            Y=yn
        s=c*area+math.sqrt(2*c*area)*rng.gauss(0,1)
        acc+=s;acc2+=s*s
    mu=acc/npath; var=acc2/npath-mu*mu
    assert abs(mu-mean_sigma(k,kap,T))<0.14,(mu,mean_sigma(k,kap,T))
    assert abs(var-var_sigma(k,kap,T))<0.4,(var,var_sigma(k,kap,T))
    ncheck+=2
    print('PASS',ncheck,'independent exact-formula, ODE, covariance, symmetry, and Monte Carlo checks')

if __name__=='__main__': test()
