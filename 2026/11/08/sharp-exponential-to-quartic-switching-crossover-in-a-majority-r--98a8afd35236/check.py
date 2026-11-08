#!/usr/bin/env python3
"""Independent numerical spot checks for sharp first-switch laws in a majority-reset spin ensemble.
Requires Python 3, NumPy and SciPy. The proof is analytic; these tests are finite checks.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.stats import binom
from scipy.special import ndtr, gamma as gamma_fn

RATE=0.7
OMEGA=math.sqrt(5.0)
P=math.pi/OMEGA

def binomial_majority(n, q):
    assert n % 2 == 1 and n>=1
    return float(binom.sf(n//2, n, q))

def exact_per_period(n, a, rate=RATE, omega=OMEGA):
    period=math.pi/omega
    integrand=lambda t: math.exp(-rate*t)*binomial_majority(n,a*math.sin(omega*t)**2)
    integral=quad(integrand,0,period,points=[period/2],epsabs=1e-12,epsrel=1e-11,limit=300)[0]
    return rate*integral/(-math.expm1(-rate*period))

def exp_sin_power(j, rate=RATE, omega=OMEGA):
    numer=math.comb(2*j,j)
    for k in range(1,j+1):
        numer += 2*(-1)**k*math.comb(2*j,j-k)*rate*rate/(rate*rate+4*k*k*omega*omega)
    return numer/(4**j)

def finite_poly_probability(n,a):
    # Direct independent finite polynomial/Fourier-Laplace formula, stable for small odd n.
    m=n//2
    value=0.
    for k in range(m+1,n+1):
        for j in range(n-k+1):
            value+=math.comb(n,k)*math.comb(n-k,j)*(-1)**j*a**(k+j)*exp_sin_power(k+j)
    return value

def fixed_prefactor(a,rate=RATE,omega=OMEGA):
    P=math.pi/omega
    return (2*rate*math.sqrt(a)*(1-a)/(omega*(1-2*a)**1.5)
            *math.exp(-rate*P/2)/(-math.expm1(-rate*P)))

def normal_crossover(lam):
    return quad(lambda y: ndtr(-2*lam-y*y),-12,12,epsabs=1e-13,epsrel=1e-12)[0]

def critical_prefactor(lam,rate=RATE,omega=OMEGA):
    P=math.pi/omega
    return rate*math.exp(-rate*P/2)/(omega*(-math.expm1(-rate*P)))*normal_crossover(lam)

def switch_laplace(n,a,s,rate=RATE,omega=OMEGA):
    P=math.pi/omega
    u=quad(lambda t: rate*math.exp(-(rate+s)*t)*binomial_majority(n,a*math.sin(omega*t)**2),
           0,P,points=[P/2],epsabs=1e-13,epsrel=1e-11)[0]/(-math.expm1(-(rate+s)*P))
    return u/(s/(rate+s)+u)

def run():
    checks=0
    for n in (1,3,5,7,9):
        for a in (.1,.2,.49):
            exact=exact_per_period(n,a)
            independent=finite_poly_probability(n,a)
            assert abs(exact-independent)<3e-10, (n,a,exact,independent)
            checks+=1
    f0=2**.25*gamma_fn(.75)/math.sqrt(math.pi)
    assert abs(normal_crossover(0)-f0)<1e-11;checks+=1
    # Fixed-detuning saddle: exact binomial integrates to sharp N^{-1} prefactor.
    a=.2
    I=-.5*math.log(4*a*(1-a))
    pref=fixed_prefactor(a)
    prev_err=float('inf')
    for n in (41,81,161,321,641):
        p=exact_per_period(n,a)
        ratio=n*p*math.exp(n*I)/pref
        err=abs(1-ratio)
        assert ratio>0 and err<prev_err+1e-8,(n,ratio,err,prev_err)
        prev_err=err;checks+=1
    assert prev_err<.008;checks+=1
    # Quartic critical saddle: the polynomial exponent is 1/4 (lambda fixed).
    for lam,tolerance in ((0.,.009),(.5,.03),(1.5,.03)):
        pref=critical_prefactor(lam)
        for n in (161,641,2561):
            a_n=.5-lam/math.sqrt(n)
            p=exact_per_period(n,a_n)
            ratio=n**.25*p/pref
            assert ratio>0 and abs(1-ratio)<(0.10 if n<2561 else tolerance),(lam,n,ratio)
            checks+=1
    # One-cycle renewal Laplace formula: scaled switching time tends to Exp(1).
    for a,n in ((.2,81),(.5,2561)):
        p=exact_per_period(n,a)
        for theta in (.5,1.,2.):
            transform=switch_laplace(n,a,theta*RATE*p)
            assert abs(transform-1/(1+theta))<(.035 if a==.5 else .0001),(a,n,theta,transform)
            checks+=1
    print('PASS:',checks,'independent finite and asymptotic numerical assertions')
    print('fixed case: a=0.2, rate=0.7, omega=sqrt(5), I=',I,'C=',fixed_prefactor(0.2))
    print('critical: F(0)=',f0, 'A(0)=',critical_prefactor(0))

if __name__=='__main__': run()
