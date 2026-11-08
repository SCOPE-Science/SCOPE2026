#!/usr/bin/env python3
"""Independent numerical checks for finite-Zipf quorum inverse limits.
Requires Python 3, numpy and scipy. All random sampling uses a fixed seed.
This checks finite computations only; it does not prove asymptotic claims.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import zeta, exp1

COUNT = 0

def check(condition, message):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(message)

def integrals(s, theta):
    c = 1.0 - s
    def J(a):
        return quad(lambda t: t**(-1/s)*math.exp(-a*t)/s,
                    1., math.inf, epsabs=1e-12, epsrel=1e-11)[0]
    def JP(a):
        return -quad(lambda t: t**(1-1/s)*math.exp(-a*t)/s,
                     1., math.inf, epsabs=1e-12, epsrel=1e-11)[0]
    u = brentq(lambda u: 1. - c*J(c*u) - theta, 1.e-8, 200)
    a = c*u
    derivative = -c*c*JP(a)
    variance = c*c*quad(lambda t: t**(1-1/s)*math.exp(-a*t) *
                        (-math.expm1(-a*t))/s, 1., math.inf,
                        epsabs=1e-12, epsrel=1e-11)[0]
    D = (J(a)-math.exp(-a))/s
    B = -c*c*zeta(s)*D/derivative
    return u, derivative, variance, D, B, J, JP

def finite_root(s, theta, n):
    j = np.arange(1, n+1, dtype=float)
    w = j**(-s)
    w /= np.sum(w)
    root = brentq(lambda u: 1. - np.dot(w, np.exp(-n*u*w))-theta,
                  0., 200.)
    return root, w

# A closed-form integral at s=1/2 is checked independently of quadrature.
for a in [0.07, 0.31, 0.9, 2.]:
    lhs = quad(lambda x: x**(-0.5)*math.exp(-a*x**(-0.5)),0.,1.,epsabs=1e-12,epsrel=1e-12)[0]
    rhs = 2. * (math.exp(-a)-a*exp1(a))
    check(abs(lhs-rhs)<2e-11, 'J_{1/2} exponential-integral identity')

for s, theta in [(0.3,0.4),(0.5,0.3),(0.5,0.8),(0.7,0.4)]:
    u, derivative, var, D, B, J, JP = integrals(s,theta)
    check(u>0 and derivative>0 and var>0, 'positive inverse CLT parameters')
    a = (1-s)*u
    check(abs(D-(J(a)+a*JP(a)))<2e-10,'integration-by-parts D identity')
    errors = []
    for n in [1600,6400,25600]:
        root, w = finite_root(s,theta,n)
        check(abs(w.sum()-1)<1e-12, 'weight normalization')
        errors.append(abs((root-u)*n**(1-s)-B))
    check(errors[-1]<0.09 and errors[-1]<errors[0], 'first drift constant')

for s in [0.6, 0.75, 0.85]:
    c=1-s
    J = lambda a: quad(lambda t:t**(-1/s)*math.exp(-a*t)/s,1.,math.inf)[0]
    root_a = brentq(lambda a: J(a)-math.exp(-a), 0.001, 6.)
    theta0 = 1-c*math.exp(-root_a)
    u, derivative, var, D, B, J1, JP = integrals(s,theta0)
    Dprime = (JP(root_a)+math.exp(-root_a))/s
    B2 = c**4*zeta(s)**2*u*Dprime/(2*derivative)
    check(abs(D)<2e-10 and abs(B)<2e-9 and B2<0, 'unique sign-cancellation root')
    n1,n2=8000,128000
    r1,_=finite_root(s,theta0,n1)
    r2,_=finite_root(s,theta0,n2)
    b1=(r1-u)*n1**(2-2*s)
    b2=(r2-u)*n2**(2-2*s)
    check(abs(b2-B2)<abs(b1-B2) and abs(b2-B2)<0.12,
          'second exceptional drift coefficient')

# Bernoulli weighted-occupancy moments, by exact subset enumeration.
for n in [4,7,10]:
    s=0.65
    t=0.8
    _, w = finite_root(s,0.5,n)
    q = np.exp(-n*t*w)
    e1=0.; e2=0.; total=0.
    for mask in range(1<<n):
        bits=np.array([(mask>>j)&1 for j in range(n)])
        prob=np.prod(np.where(bits,1-q,q))
        mass=float(np.dot(w,bits))
        total+=prob;e1+=prob*mass;e2+=prob*mass*mass
    mean=float(np.dot(w,1-q))
    v=float(np.dot(w*w,q*(1-q)))
    check(abs(total-1)<1e-11,'subset probability normalization')
    check(abs(e1-mean)<1e-11,'finite occupancy expectation')
    check(abs(e2-e1*e1-v)<1e-11,'finite occupancy variance')

# Reproducible distributional check of inverse fluctuation scale.
seed=20260709
rng=np.random.default_rng(seed)
s,theta,n=0.5,0.30,1500
u,derivative,v,D,B,_,_=integrals(s,theta)
root,w=finite_root(s,theta,n)
obs=[]
for _ in range(900):
    times=rng.exponential(scale=1.0/(n*w))
    order=np.argsort(times)
    k=int(np.searchsorted(np.cumsum(w[order]),theta,side='right'))
    obs.append(math.sqrt(n)*(times[order[k]]-root))
obs=np.asarray(obs)
sigma=math.sqrt(v)/derivative
check(abs(float(obs.mean()))<0.14, 'inverse CLT simulated mean')
check(abs(float(obs.std(ddof=1))-sigma)<0.16, 'inverse CLT simulated SD')
print(f'PASS {COUNT} independent numerical assertions; seed={seed}')
print(f'Critical sample: s={s}, theta={theta}, Gaussian variance={sigma*sigma:.9f}')
