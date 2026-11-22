"""Check the exact bounded-heterogeneous-diffusion design formulas.

Requires numpy, scipy, and sympy. Results are reproducible with fixed seed.
"""
import numpy as np
from scipy.optimize import brentq, minimize
from scipy.integrate import quad
from sympy import symbols, simplify, diff


def design(lo, hi, mean):
    assert 0 < lo < mean < hi
    threshold = (2 * hi + lo ** 3 / hi ** 2) / 3
    if mean <= threshold:
        c = brentq(lambda a: (2*a + lo**3/a**2)/3 - mean, lo, hi)
        val = 2/(3*c) - lo**3/(6*c**4)
    else:
        c = np.sqrt((hi**3 - lo**3)/(3*(hi - mean)))
        val = 1/(2*hi) + 3*(hi-mean)**2/(2*(hi**3 - lo**3))
    profile = lambda x: np.clip(c * np.sqrt(1-x), lo, hi)
    return threshold, c, val, profile


def algebra_check():
    u, l, c = symbols('u l c', positive=True)
    mean1 = 2*c/3 + l**3/(3*c**2)
    value1 = 2/(3*c) - l**3/(6*c**4)
    mean2 = u - (u**3 - l**3)/(3*c**2)
    value2 = 1/(2*u) + (u**3-l**3)/(6*c**4)
    assert simplify(mean1.subs(c,u)-mean2.subs(c,u))==0
    assert simplify(value1.subs(c,u)-value2.subs(c,u))==0
    assert simplify(diff(value1,c)/diff(mean1,c)+1/c**2)==0
    assert simplify(diff(value2,c)/diff(mean2,c)+1/c**2)==0
    assert simplify(diff(3/(c**3-l**3),c)/diff(mean1,c)
                    +27*c**5/(2*(c**3-l**3)**3))==0
    print('PASS: exact branch identities, value derivatives and third-derivative jump')


def numerical_check():
    rng = np.random.default_rng(20261117)
    for run in range(16):
        lo = float(rng.uniform(.1, 1.))
        hi = float(rng.uniform(lo+.2, 4.))
        mean = float(rng.uniform(lo+.02*(hi-lo), hi-.02*(hi-lo)))
        _, c, val, profile = design(lo, hi, mean)
        breaks = [max(0., 1-(hi/c)**2), 1-(lo/c)**2]
        integ = quad(profile,0,1,points=breaks,epsabs=1e-10)[0]
        obj = quad(lambda x:(1-x)/profile(x),0,1,points=breaks,epsabs=1e-10)[0]
        assert abs(integ-mean)<1e-8, (run,integ,mean)
        assert abs(obj-val)<1e-8, (run,obj,val)
        n=220
        mid=(np.arange(n)+.5)/n
        w=(1-mid)/n
        result=minimize(lambda d: np.sum(w/d), np.repeat(mean,n),
            jac=lambda d:-w/d**2, bounds=[(lo,hi)]*n,
            constraints={'type':'eq','fun':lambda d:np.mean(d)-mean,
                         'jac':lambda d:np.ones(n)/n},
            method='SLSQP', options={'ftol':1e-12,'maxiter':1500})
        assert result.success, result.message
        assert abs(np.sum(w/result.x)-np.sum(w/profile(mid)))<5e-5
        assert np.sum(w/result.x)>=val-1e-6
    print('PASS: 16 random budget/functional quadratures and independent constrained discretizations')


if __name__ == '__main__':
    algebra_check()
    numerical_check()
    threshold, c, val, f = design(.5,1.5,1.2)
    assert abs(val-0.3748717948717949)<1e-12
    print('PASS: physical example, threshold', threshold, 'minimum time',val)
