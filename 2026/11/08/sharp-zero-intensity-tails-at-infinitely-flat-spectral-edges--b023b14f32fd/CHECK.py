#!/usr/bin/env python3
"""Finite numerical checks for compact-spectrum spectrogram-zero edge laws.
This checks examples, not the universal asymptotic theorem.
Dependencies: scipy, Python 3.
"""
from math import exp, pi
from scipy.integrate import quad


def upper_moments(beta, t):
    """The tilted variable is U=1-X, with S(x)=x^2 exp(-1/(1-x)^beta), x in (0,1)."""
    u0 = (beta / t) ** (1.0 / (beta + 1.0))
    phi0 = t*u0 + u0 ** (-beta)
    def moment(k):
        def fn(u):
            if not 0 < u < 1:
                return 0.0
            phi = t*u + u ** (-beta)
            return u**k * (1-u)**2 * exp(-(phi-phi0)-2*pi*(1-u)**2)
        return quad(fn, 0, 1, points=[u0], epsabs=1e-13,
                    epsrel=1e-11, limit=400)[0]
    a,b,c=(moment(k) for k in range(3))
    mean=b/a
    return mean,c/a-mean**2


def lower_moments(beta, t):
    def moment(k):
        def fn(x):
            if not 0 < x < 1:
                return 0.0
            return x ** (k+2)*exp(-t*x-2*pi*x*x-(1-x)**(-beta))
        return quad(fn, 0, 1, epsabs=1e-90, epsrel=1e-11, limit=400)[0]
    a,b,c=(moment(k) for k in range(3))
    mean=b/a
    return mean,c/a-mean**2


def mean_at_omega(omega, beta=1):
    # At small frequencies no exponential stabilization is needed.
    def moment(k):
        def fn(x):
            if not 0 < x < 1:
                return 0.0
            return x**(k+2)*exp(4*pi*omega*x-2*pi*x*x-(1-x)**(-beta))
        return quad(fn, 0, 1, epsabs=1e-13, epsrel=1e-12)[0]
    a,b,c=(moment(k) for k in range(3))
    return b/a, c/a-(b/a)**2


def main():
    for beta, tolerance in ((0.5,0.18),(1.0,0.05),(2.0,0.025)):
        t=3000.0
        mean,var=upper_moments(beta,t)
        u0=(beta/t)**(1/(beta+1))
        predicted_variance=u0/((beta+1)*t)
        assert abs(var/predicted_variance-1)<tolerance, (beta,var,predicted_variance)
        # A second independent asymptotic: the surviving right-hand zero mass
        # is exactly b-E[X] = E[U], of order u0.
        assert abs(mean/u0-1)<0.12, (beta,mean,u0)
        lower_mean, lower_var=lower_moments(beta,300.0)
        assert abs(lower_var/(3/300.0**2)-1)<0.03
        assert abs(lower_mean/(3/300.0)-1)<0.02

    # Derivative of the exponentially tilted mean equals 4*pi*variance:
    for omega in (-0.2,0,0.3):
        h=1e-4
        derivative=(mean_at_omega(omega+h)[0]-mean_at_omega(omega-h)[0])/(2*h)
        exact=4*pi*mean_at_omega(omega)[1]
        assert abs(derivative-exact)<5e-7, (omega,derivative,exact)
    print('EDGE_ZERO_TAIL_CHECKS_PASSED')

if __name__=='__main__':
    main()
