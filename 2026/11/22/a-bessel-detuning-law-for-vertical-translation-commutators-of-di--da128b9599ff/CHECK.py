"""Supplementary finite identities and near-critical numerical checks.

Requires Python 3, NumPy and SciPy; these checks are not a proof of the infinite
series or its limiting law. Execute: python CHECK.py
"""
from math import factorial, log, pi, sqrt, cos, exp
import numpy as np
from scipy.integrate import quad
from scipy.special import iv, ive

checks=0
for a in [0.1, 0.3, 0.7]:
    for n in [2,3,7,53,4096]:
        x=a*log(n)
        for theta in [0.0,0.13,0.8,pi]:
            column=sum(2*x**(2*k)*(1-cos(k*theta))/factorial(k)**2
                       for k in range(1,80))
            bessel=2*(iv(0,2*x)-iv(0,2*x*np.exp(0.5j*theta)).real)
            assert abs(column-bessel)<1e-9*max(1.,abs(column)),(a,n,theta)
            checks+=1
for x in [0.1,0.5,2.,4.]:
    den=sum(x**(2*k)/factorial(k)**2 for k in range(60))
    second=sum(k*k*x**(2*k)/factorial(k)**2 for k in range(60))/den
    assert abs(second-x*x)<1e-10*max(1.,x*x)
    checks+=1

def scaled_norm(a, epsilon, theta, N=20000):
    c=a+0.5+epsilon
    n=np.arange(2,N+1,dtype=float)
    x=a*np.log(n)
    # Exact finite n contributions via two independent Bessel arguments.
    prefix=2*np.sum(n**(-2*c)*(iv(0,2*x)-iv(0,2*x*np.exp(0.5j*theta)).real))
    q=cos(theta/2)
    def tail_integrand(t):
        z=2*a*t*np.exp(0.5j*theta)
        normalized=ive(0,2*a*t)-(ive(0,z)*np.exp(-2*a*t*(1-q))).real
        return 2*exp(-2*epsilon*t)*normalized
    tail=quad(tail_integrand,log(N),max(1000.,log(N)+50/epsilon),
              epsabs=1e-9,epsrel=1e-9,limit=500)[0]
    # Tail integral is an approximation to the tail SUM, not a certificate.
    return sqrt(epsilon)*(prefix+tail)

a=0.3
for v in [0.5,2.,8.]:
    epsilon=0.01
    measured=scaled_norm(a,epsilon,epsilon*v)
    predicted=(1/sqrt(a))*(1/sqrt(2)-((2-1j*a*v)**(-0.5)).real)
    assert abs(measured-predicted)<.025*max(.01,predicted),(v,measured,predicted)
    checks+=1
print('PASS:',checks,'finite/computational checks; asymptotic proof is analytic.')
