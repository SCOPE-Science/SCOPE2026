#!/usr/bin/env python3
"""Independent numerical checks for renewal-aged Glauber pair correlations."""
import numpy as np
from math import pi, sqrt, exp, log, lgamma
from scipy.special import ive
from scipy.integrate import quad

def correlation_integral(n, alpha, tau0):
    p = alpha - 1.0
    def age_survival(t):
        return 1.0 - p*t/(alpha*tau0) if t < tau0 else (tau0/t)**p/alpha
    def f(y):
        t = n*n*exp(y)
        # The large-argument asymptotic is used only beyond t=1e8.
        kernel = ive(n, 2*t) if t < 1e8 else exp(-n*n/(4*t))/sqrt(4*pi*t)
        return n * kernel * age_survival(t)
    return quad(f, -25, 30, epsabs=2e-12, epsrel=1e-10, limit=240)[0]

def mellin(n,p):
    return exp(log(2*n)+lgamma(2*p)+lgamma(n-p)-lgamma(p)-log(n+p)-lgamma(n+p))

for alpha in (1.2, 1.5, 2., 3.):
    p=alpha-1
    const=exp(p*log(4)+lgamma(p+0.5)-log(alpha)-0.5*log(pi))
    for n in (20,50,100):
        v=correlation_integral(n,alpha,1.)
        exact_upper=mellin(n,p)/alpha
        assert abs(exact_upper-v) < (2*np.e/n)**n/alpha*(1+p/(n-p)) + 5e-9*exact_upper, (alpha,n,v,exact_upper)
        assert abs(v*n**(2*p)/const-1) < 0.06, (alpha,n,v, const)
        print('PASS', 'alpha=',alpha,'n=',n,'pair=',round(v,12),'scaled=',round(v*n**(2*p),10),'lim=',round(const,10))
print('Numerical checks completed')
