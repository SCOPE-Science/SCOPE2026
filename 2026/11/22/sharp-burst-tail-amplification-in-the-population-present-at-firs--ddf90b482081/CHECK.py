#!/usr/bin/env python3
"""Numerical cross-checks for the joint first-target arrival/occupancy formula.
Requires only the Python 3 standard library. Run: python3 CHECK.py
No finite test proves any infinite-time or heavy-tail asymptotic.
"""
import math


def simpson(f, a, b, n=600):
    assert n % 2 == 0
    h = (b-a)/n
    return (h/3)*(f(a)+f(b)+4*sum(f(a+(2*j-1)*h) for j in range(1,n//2+1))
           +2*sum(f(a+2*j*h) for j in range(1,n//2)))


def rhs(t, z, birth, kill, death, probs):
    rate=kill+death
    def ell(u):return math.exp(-rate*u)
    def w(u):return death/rate*(1-ell(u))
    def psi(x):return sum(p*x**j for j,p in probs)
    def dpsi(x):return sum(p*j*x**(j-1) for j,p in probs)
    logF=birth*simpson(lambda u: psi(w(u)+z*ell(u))-1,0,t)
    arrival=birth*z*simpson(lambda u:kill*ell(u)*dpsi(w(u)+z*ell(u)),0,t)
    return math.exp(logF)*arrival


def ode_hit_pgf(t,z,birth,kill,death,probs,N=35,steps=2000):
    # Independent killed master equation for exponential single-particle targeting.
    # Jump births are +j; death -1 per live individual; absorption at rate n*kill.
    def deriv(p):
        y=[0.0]*(N+1)
        for n in range(N+1):
            y[n]-=(birth+(death+kill)*n)*p[n]
            if n+1<=N: y[n]+=death*(n+1)*p[n+1]
            for j,pj in probs:
                if n>=j:y[n]+=birth*pj*p[n-j]
        return y
    h=t/steps;p=[0.0]*(N+1);p[0]=1.0
    for _ in range(steps):
        k1=deriv(p)
        k2=deriv([v+h*k/2 for v,k in zip(p,k1)])
        k3=deriv([v+h*k/2 for v,k in zip(p,k2)])
        k4=deriv([v+h*k for v,k in zip(p,k3)])
        p=[v+h*(a+2*b+2*c+d)/6 for v,a,b,c,d in zip(p,k1,k2,k3,k4)]
    return kill*sum(n*p[n]*z**n for n in range(1,N+1))

checks=0
for probs in [[(1,1.0)],[(2,1.0)],[(1,.25),(3,.75)]]:
    for t in (.07,.28,.75,1.2):
        for z in (.2,.5,.8,1.0):
            calc=rhs(t,z,1.3,1.1,.7,probs)
            independent=ode_hit_pgf(t,z,1.3,1.1,.7,probs,steps=400)
            assert abs(calc-independent)<3e-8*max(.001,abs(calc)),(probs,t,z,calc,independent)
            checks+=1

# Size-biased early-arrival law with unequal burst weights.
probs=[(1,.5),(3,.5)]
mu=2.0
for z in (.2,.5,.9):
    t=.0001
    pgf=rhs(t,z,1.3,1.1,.7,probs)/(z*rhs(t,1.,1.3,1.1,.7,probs))
    target=(.5+1.5*z*z)/mu
    assert abs(pgf-target)<1e-3,(z,pgf,target)
    checks+=1

# Finite-mean/finite-second-moment boundary for a finite burst mixture.
# At t=0, the conditional expected pre-reaction count tends to E[J^2]/E[J].
def conditional_mean(t, probs):
    rate=1.1+.7
    def x(u):
        ell=math.exp(-rate*u);w=.7/rate*(1-ell)
        q=w+ell
        dpsi=sum(p*j*q**(j-1) for j,p in probs)
        d2psi=sum(p*j*(j-1)*q**(j-2) for j,p in probs if j>=2)
        return ell,dpsi,d2psi
    initial=1.3*simpson(lambda u: x(u)[0]*x(u)[1],0,t)
    a=simpson(lambda u:1.1*math.exp(-rate*u)*x(u)[0]*x(u)[2],0,t)
    q=.7/rate+1.1/rate*math.exp(-rate*t)
    den=1-sum(p*q**j for j,p in probs)
    return 1+initial+a/den
for probs in [[(1,1.0)],[(2,1.0)],[(1,.5),(3,.5)]]:
    limit=sum(p*j*j for j,p in probs)/sum(p*j for j,p in probs)
    assert abs(conditional_mean(.0001,probs)-limit)<.002
    checks+=1
print('PASS',checks,'independent forward-master-equation and early-limit numerical comparisons')
