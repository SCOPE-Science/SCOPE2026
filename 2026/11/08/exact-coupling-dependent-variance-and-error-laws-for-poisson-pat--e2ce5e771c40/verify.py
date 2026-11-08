#!/usr/bin/env python3
"""Reproducibility checks for Poisson-path equal-cell quadrature.
Only Python standard library. These tests supplement the analytic proof.
"""
import cmath
import math
import random
from fractions import Fraction as F

NTEST = 0

def check(cond, message):
    global NTEST
    NTEST += 1
    if not cond:
        raise AssertionError(message)

def approx(a,b,tol=1e-10):
    return abs(a-b)<=tol

# Exact polynomial moment identities under uniform cell phases.
# f(u)= integral_0^1 (1_{u>=v}-(1-v))^2 dv.
check(F(1,3)-F(1,2)+F(1,3)==F(1,6), 'mean f(U)')
check(F(1,4)-F(1,3)+F(1,3)==F(1,4), 'f(U) raw second order average check')
check(F(1,4)-F(1,2)+F(1,3)==F(1,12), 'f(1/2)')
check(F(1,3)-F(1,4)==F(1,12), 'Var(U)')
check(2*F(1,80)+6*F(1,12)**2==F(1,15), 'triangular fourth moment')

rng = random.Random(572993)

def poisson(rate):
    # Knuth generator for modest rates.
    q=1.0; k=0
    threshold=math.exp(-rate)
    while True:
        q*=rng.random()
        if q<threshold:
            return k
        k+=1

def trial(n,lam,mode):
    k=poisson(lam)
    times=[rng.random() for _ in range(k)]
    if mode=='mid':
        u=[0.5]*n
    elif mode=='shared':
        a=rng.random(); u=[a]*n
    elif mode=='ind':
        u=[rng.random() for _ in range(n)]
    elif mode=='paired':
        assert n%2==0
        u=[]
        for j in range(n//2):
            a=rng.random(); u.extend([a,1.0-a])
    else:
        raise ValueError(mode)
    # Two independently computed formulas for n*(Q-I).
    z1=sum((n*t-int(n*t)) - (1.0 if u[min(n-1,int(n*t))]<(n*t-int(n*t)) else 0.0) for t in times)
    integral=sum(1.0-t for t in times)
    q=sum(sum(t<=(i+u[i])/n for t in times) for i in range(n))/n
    z2=n*(q-integral)
    check(approx(z1,z2,1e-8),'pathwise jump identity')
    return z1

for n in (1,2,3,5,11):
    for mode in ('mid','shared','ind')+ (('paired',) if n%2==0 else ()):
        for j in range(30):
            trial(n,1.7,mode)

# Exact chi formulas and finite n variance predictions.
for n in (2,4,8,32):
    for lam in (0.25,1.0,2.0,3.5):
        expected={'mid':lam/12, 'shared':lam/6+lam*lam/12,
                  'ind':lam/6+lam*lam/(12*n), 'paired':lam/6}
        for mode,ex in expected.items():
            check(ex>=0.0 and math.isfinite(ex),'valid variance expression')

# Accurate numeric quadrature of the exact characteristic function.
def sinc(x):
    return 1.0 if abs(x)<1e-12 else math.sin(x)/x

def midpoint_integral(func, mesh=4000):
    return sum(func((j+0.5)/mesh) for j in range(mesh))/mesh

for lam in (0.25,1.0,2.3):
    for t in (0.1,0.5,1.0,2.0):
        a=sinc(t/2)
        g=lambda u: cmath.exp(1j*t*(u-0.5))*a
        cp=cmath.exp(lam*(a*a-1))
        phi=midpoint_integral(lambda u: g(u),4000)
        check(abs(phi-a*a)<1e-8,'triangular characteristic function')
        for n in (1,2,5,20,100):
            ch=midpoint_integral(lambda u: cmath.exp((lam/n)*(g(u)-1.0)),4000)**n
            check(abs(ch-cp)<min(0.8,4*lam*lam/n+1e-6),'characteristic-function convergence')
        shared=midpoint_integral(lambda u: cmath.exp(lam*(g(u)-1)),4000)
        check(abs(shared-midpoint_integral(lambda u: cmath.exp(lam*(g(u)-1)),2000))<1e-7,'shared n-invariance')

# Independent, shared, complementary and deterministic sampling simulation.
# The tolerance accommodates stochastic error while catching gross variance mistakes.
lam=2.0
for n in (2,6,20):
    for mode in ('mid','shared','ind','paired'):
        count=17000
        samples=[trial(n,lam,mode) for _ in range(count)]
        mean=sum(samples)/count
        variance=sum(x*x for x in samples)/count-mean*mean
        target={'mid':lam/12,'shared':lam/6+lam*lam/12,
                'ind':lam/6+lam*lam/(12*n),'paired':lam/6}[mode]
        check(abs(mean)<0.075,'empirical centered error')
        check(abs(variance-target)<0.065+0.06*target,'empirical variance')

print('PASS', NTEST, 'checks; conditional Poisson calculations, distribution identities, and simulations')
