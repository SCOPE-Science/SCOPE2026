"""Finite diagnostics for the log-periodic Bergman commutator theorem.

Requires NumPy and SciPy. These tests support, but cannot replace, the proof.
"""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.special import loggamma


def exact_coefficients(alpha, tau, b, count):
    """Absolute one-step commutator coefficients for n=0,...,count-1."""
    n = np.arange(count, dtype=float)
    q = n + alpha + 2.0
    R1 = np.exp(loggamma(q) - loggamma(q + 1j * tau))
    R2 = np.exp(loggamma(q) - loggamma(q + 2j * tau))
    w = np.sqrt((n + 1.0) / q)
    d = -1j * tau * w * (R1 / (q + 1j * tau) + b * R2 / (q + 2j * tau))
    return np.abs(d)


def threshold_root(tau, b, theta):
    lo, hi = tau * (1.0 - b), tau * (1.0 + b)
    def objective(x):
        return x - tau * abs(1.0 + b * np.exp(-1j * (theta + tau * np.log(x))))
    return float(brentq(objective, lo - 1.e-10, hi + 1.e-10, xtol=1.e-13))


def theoretical_trace(tau, b):
    theta = np.linspace(0., 2. * np.pi, 20001)
    return tau * np.trapezoid(np.abs(1.0 + b * np.exp(1j * theta)), theta) / (2. * np.pi)


def run():
    checks = 0
    cases = [(0., 1., .25), (2., .9, .2), (-.5, 2., .1),
             (1.5, .45, .28), (-.75, .7, .15)]
    for alpha, tau, b in cases:
        assert -1. < alpha and 0 < b < 1. / (1. + tau)
        checks += 1
        # Exact gamma-ratio recurrence in both frequencies.
        for v in [tau, 2. * tau]:
            for n in [0, 1, 3, 10, 101, 1000]:
                q = n + alpha + 2.
                r = np.exp(loggamma(q) - loggamma(q + 1j*v))
                r_next = np.exp(loggamma(q+1.) - loggamma(q+1.+1j*v))
                assert abs(r_next / r - q / (q + 1j*v)) < 3.e-11
                checks += 1
        coeff = exact_coefficients(alpha, tau, b, 60001)
        for n in [100, 1000, 10000, 50000]:
            model = tau * abs(1+b*np.exp(-1j*tau*np.log(n))) / n
            assert abs(coeff[n] - model) <= 25. / n**2
            checks += 1
        A, B = tau*(1-b), tau*(1+b)
        for angle in np.linspace(-2*np.pi, 2*np.pi, 33):
            x = threshold_root(tau, b, angle)
            assert A-1.e-10 <= x <= B+1.e-10
            assert abs(x-tau*abs(1+b*np.exp(-1j*(angle+tau*np.log(x))))) < 1.e-11
            checks += 2
        assert abs(threshold_root(tau, b, -tau*np.log(B))-B)<1.e-10
        assert abs(threshold_root(tau, b, np.pi-tau*np.log(A))-A)<1.e-10
        checks += 2
        for s in [.03, .01, .004, .001]:
            N = int(np.count_nonzero(coeff > s))
            expected = threshold_root(tau, b, tau*np.log(1/s))/s
            assert abs(N-expected) < 20., (alpha,tau,b,s,N,expected)
            checks += 1
        # The plain initial-order logarithmic mass has the prescribed trend.
        n = np.arange(1, 60001)
        model_trace = tau * np.sum(np.abs(1+b*np.exp(-1j*tau*np.log(n))) / n) / np.log(60001)
        assert abs(model_trace-theoretical_trace(tau,b)) < .2
        checks += 1
    print('PASS:', checks, 'finite diagnostics across', len(cases), 'parameter triples')
    print('Infinite-dimensional and uniqueness conclusions rely on the proof, not these checks.')


if __name__ == '__main__':
    run()
