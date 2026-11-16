"""Numerical consistency checks for a reciprocal-Gamma Gaussian analytic boundary kernel.

Requires numpy and scipy. This verifies finite numerical consequences, not the
analytic convergence theorem or publication originality.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln


def moments_cont(s):
    def g(x, k):
        return x**k * math.exp(s*x - gammaln(2*x)) if x > 0 else 0.0
    return np.array([quad(lambda x: g(x, k), 0, 40, epsabs=2e-12,
                          epsrel=1e-11)[0] for k in range(3)])


def moments_disc(s, beta):
    h = 1.0/beta
    k = np.arange(1, int(40*beta)+1, dtype=float)
    x = h*k
    w = h*np.exp(s*x-gammaln(2*x))
    return np.array([np.dot(w, x**j) for j in range(3)])


def density(M):
    return (M[2]/M[0]-(M[1]/M[0])**2)/math.pi


def inverse_l_second(M):
    return (2*M[1]**2-M[0]*M[2])/M[0]**3


def run():
    checks=0
    for s in (-3.0, -1.0, 0.0, 1.0, 2.0):
        C=moments_cont(s)
        assert C[0]>0 and density(C)>0
        checks += 2
        for beta in (16,32,64):
            D=moments_disc(s,beta)
            pred=C[0]-1/(6*beta**2)
            assert abs(D[0]-pred) < 0.07/(beta**4)
            pred_rho=density(C)-inverse_l_second(C)/(6*math.pi*beta**2)
            assert abs(density(D)-pred_rho)< 0.35/(beta**4)
            checks += 2
    # Confirm the limiting tails numerically where quadrature is well conditioned.
    for t in (-8.0,-6.0,-5.0,2.0,3.0):
        rho=density(moments_cont(2*t))
        if t<0:
            assert abs(2*math.pi*t*t*rho-1)<0.14
        else:
            assert abs(4*math.pi*math.exp(-t)*rho-1)<0.004
        checks += 1
    print('PASS',checks,'finite numerical assertions')

if __name__ == '__main__':
    run()
