"""Reproducible numerical checks for a five-point projective cross-ratio tail.

This script tests, but does not replace, the accompanying analytic proof.
Requires NumPy and SciPy for quadrature and simulation.
"""
import math
import numpy as np
from scipy.integrate import quad

PI=math.pi

def cdf_interval(b,x):
    return (math.atan(b+x)-math.atan(b-x))/PI

def min_expectation(b):
    return quad(lambda x:(1-cdf_interval(b,x))**2,0,np.inf,epsabs=2e-9,limit=150)[0]

def double_tail_constant():
    return 4*quad(lambda b:min_expectation(b)/(PI**2*(1+b*b)**2),0,np.inf,epsabs=2e-8,limit=150)[0]

if __name__=='__main__':
    k=double_tail_constant()
    assert 0.3429 <k<0.3433, k
    # Exact conditional integration over the fifth Cauchy coordinate suppresses the
    # sampling noise from a very rare simultaneous-denominator collision.
    rng=np.random.default_rng(672019)
    n=800000
    b=np.tan(PI*(rng.random(n)-0.5))
    d=np.tan(PI*(rng.random(n)-0.5))
    e=np.tan(PI*(rng.random(n)-0.5))
    m=np.minimum(np.abs(d-b),np.abs(e-b))
    approximations=[]
    for t in [25.,100.,400.,1600.]:
        p=np.arctan2(m/t,1+b*b-(m/t)**2) if False else (np.arctan(b+m/t)-np.arctan(b-m/t))/PI
        # Cauchy CDF difference is nonnegative for b +/- m/t.
        estimate=float(t*np.mean(p))
        se=float(t*np.std(p,ddof=1)/math.sqrt(n))
        approximations.append((t,estimate,se))
        assert abs(estimate-k)<0.02, (t,estimate,k)
    assert abs(approximations[-1][1]-k)<0.008
    print('CONSTANT',f'{k:.12f}')
    for t,estimate,se in approximations:
        print('T',int(t),'tP',f'{estimate:.9f}','SE',f'{se:.9f}')
    print('PENTAGON_CROSSRATIO_CHECKS_OK')
