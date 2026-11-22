"""Standalone numerical checks of the Gaussian-mixture null-fiber theorem.
Requires Python 3, NumPy and SciPy. Proof is in RESULT.md; these are finite checks.
"""
from math import erf, sqrt, pi
import numpy as np
from scipy.integrate import quad
from scipy.special import ndtr

checks=0
def ck(cond, message):
    global checks
    checks+=1
    if not cond:
        raise AssertionError(message)

def weight(sig):
    q=0.5*erf(1/(2*sig))
    r=0.5*erf(3/(2*sig))
    return q/(q+r)

def density(x, center, sig):
    z=(x-center)/sig
    return np.exp(-0.5*z*z)/(sig*sqrt(2*pi))

def cdf(x, center, sig):
    return ndtr((x-center)/sig)

def f_dens(x, sig):
    return .5*(density(x,-1,sig)+density(x,1,sig))

def f_cdf(x,sig):
    return .5*(cdf(x,-1,sig)+cdf(x,1,sig))

def g_dens(x,sig):
    w=weight(sig)
    return (1-w)*density(x,0,sig)+.5*w*(density(x,-2,sig)+density(x,2,sig))

def g_cdf(x,sig):
    w=weight(sig)
    return (1-w)*cdf(x,0,sig)+.5*w*(cdf(x,-2,sig)+cdf(x,2,sig))

def integrate(fun):
    breaks=[-np.inf,-4,-3,-2.5,-2,-1.5,-1,-.5,0,.5,1,1.5,2,2.5,3,4,np.inf]
    return sum(quad(fun,a,b,epsabs=1e-12,epsrel=1e-12,limit=200)[0] for a,b in zip(breaks[:-1],breaks[1:]))

for s in [.10,.2,.4,1.,2.,5.]:
    w=weight(s)
    q=ndtr(1/(sqrt(2)*s)); r=ndtr(3/(sqrt(2)*s))
    A=2*q*(1-q)
    B=1-q-r+2*q*r
    ck(0.25 < w < 0.5, f'weight bound {s}')
    ck(abs((1-w)*A+w*B-.5)<1e-13, f'folded comparison {s}')
    ck(abs(integrate(lambda x:f_dens(x,s))-1)<2e-10,f'F mass {s}')
    ck(abs(integrate(lambda x:g_dens(x,s))-1)<2e-10,f'G mass {s}')
    theta=integrate(lambda y:f_cdf(y,s)*g_dens(y,s))
    i2=4*sum(quad(lambda y:f_cdf(y,s)*g_dens(y,s),a,b,epsabs=2e-13,limit=300)[0]
         for a,b in [(0,.5),(.5,1),(1,1.5),(1.5,2),(2,2.5),(2.5,3),(3,4),(4,np.inf)])-1
    ck(abs(theta-.5)<3e-10,f'theta {s} = {theta}')
    ck(abs(i2-.5)<5e-10,f'I2 {s} = {i2}')
    tv=0.5*integrate(lambda x:abs(f_dens(x,s)-g_dens(x,s)))
    bound=1-4*ndtr(-.5/s)
    ck(tv >= bound-3e-10,f'TV bound {s}: {tv} {bound}')
    print(f'sigma={s:5g} weight={w:.12f} theta={theta:.12f} I2={i2:.12f} TV={tv:.9f} TV_bound={bound:.9f}')
for s1,s2 in [(.1,.2),(.2,.4),(.4,1),(1,2),(2,5)]:
    ck(weight(s1)>weight(s2),f'checked decreasing numeric samples {s1},{s2}')
print('PASS', checks, 'numerical assertions')
