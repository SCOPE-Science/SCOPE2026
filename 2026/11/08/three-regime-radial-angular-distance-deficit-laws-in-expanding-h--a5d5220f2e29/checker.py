#!/usr/bin/env python3
"""Standalone numerical checks for a hyperbolic two-point distance-deficit limit.
This numerical program is not a proof of weak convergence or historical novelty.
Requires NumPy and SciPy; all random seeds are fixed for reproducibility.
"""
import math
import numpy as np
from scipy.special import betaln, gammaln, betainc
from scipy.integrate import quad

rng = np.random.default_rng(100712)

def analytic_laplace(d, alpha, s):
    a = (d-1)/2
    return math.exp(2*math.log(alpha/(alpha+s)) + betaln(a+s, a) - betaln(a,a))

def rate_product(d,s):
    k = (d-1)//2
    p = (2*k/(2*k+s))**2
    for j in range(k,2*k): p *= j/(j+s)
    return p

for d in (3,5,7,9):
    for s in (0.125,0.7,1.3):
        assert abs(analytic_laplace(d,d-1,s)-rate_product(d,s))<3e-14

# The three exponential clocks in dimension three have survival
# 4 exp(-t) - (3+2t) exp(-2t).
for t in (0.0,0.25,1.5,4,9):
    exact = 4*math.exp(-t) - (3+2*t)*math.exp(-2*t)
    assert 0 <= exact <= 1+1e-14

# Independent direct geometric sampling of point pairs in H^d, not via Beta variables.
def radial_sample(n,alpha,R):
    U=rng.random(n)
    return np.arccosh(1 + U*np.expm1(alpha*R)**2/(2*np.exp(alpha*R)))/alpha
    # cosh(alpha R)-1 = exp(alpha R)*(1-exp(-alpha R))^2/2

def geom_deficit(d,alpha,R,n):
    r=radial_sample(n,alpha,R); s=radial_sample(n,alpha,R)
    u=rng.standard_normal((n,d));v=rng.standard_normal((n,d))
    u /= np.linalg.norm(u,axis=1)[:,None]
    v /= np.linalg.norm(v,axis=1)[:,None]
    B=np.clip((1-np.einsum('ij,ij->i',u,v))/2,0,1)
    c=(1-B)*np.cosh(r-s)+B*np.cosh(r+s)
    assert np.min(c)>=1-1e-12
    return 2*R-np.arccosh(np.maximum(c,1))

def asymptotic_deficit(d,alpha,n):
    a=(d-1)/2
    return rng.exponential(1/alpha,n)+rng.exponential(1/alpha,n)-np.log(rng.beta(a,a,n))

N=85000
for d,alpha in [(2,.4),(3,.65),(3,1),(3,1.6),(5,4)]:
    T=geom_deficit(d,alpha,18,N)
    W=asymptotic_deficit(d,alpha,N)
    assert np.min(T)>-1e-10
    for q in (.15,.4,.7,.9):
        cutoff=np.quantile(W,q)
        err=abs(float(np.mean(T<=cutoff))-q)
        assert err<0.023, (d,alpha,q,err)
    print('geometry_vs_limit',d,alpha,'mean',round(float(T.mean()),5),round(float(W.mean()),5))

# Numerically check the exact asymptotic tail coefficients using the
# convolution of an independent Gamma(shape=2,rate=alpha) and -log Beta(a,a).
def exact_tail(d,alpha,t):
    a=(d-1)/2
    norm=math.exp(betaln(a,a))
    def integrand(z):
        fz=math.exp(-a*z) * (-math.expm1(-z))**(a-1)/norm
        w=t-z
        return math.exp(-alpha*w)*(1+alpha*w)*fz
    integral=quad(integrand,0,t,epsabs=1e-15,epsrel=1e-12,limit=200)[0]
    return integral+betainc(a,a,math.exp(-t))

for d,alpha in [(3,.6),(3,1.),(3,1.6),(5,2.0)]:
    a=(d-1)/2
    t=28 if alpha<=1.6 else 19
    p=exact_tail(d,alpha,t)
    B=math.exp(betaln(a,a))
    if alpha<a:
        coefficient=alpha*math.exp(betaln(a-alpha,a)-betaln(a,a))
        asymp=coefficient*t*math.exp(-alpha*t)
        tol=.19
    elif alpha>a:
        coefficient=(alpha/(alpha-a))**2/(a*B)
        asymp=coefficient*math.exp(-a*t)
        tol=.12
    else:
        coefficient=a/(2*B)
        asymp=coefficient*t*t*math.exp(-a*t)
        tol=.19
    relative=p/asymp
    assert abs(relative-1)<tol,(d,alpha,relative)
    print('tail_ratio',d,alpha,round(relative,5))
print('HYPERBOLIC_RADIAL_ANGULAR_TAIL_PHASES_OK',N,5)
