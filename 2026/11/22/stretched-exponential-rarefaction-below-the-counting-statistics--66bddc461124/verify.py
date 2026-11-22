#!/usr/bin/env python3
"""Numerical checks for the exact equilibrium-age mixture in a first-passage-reset gas.

Requires NumPy and SciPy. The continuum proof is in RESULT.md; quadrature
is a finite consistency test, not an independent proof of the asymptotics.
"""
import math
import numpy as np
from scipy.special import erf, erfc, erfinv, logsumexp
from scipy.stats import binom


def exact_log_probability(N, ell=1., kappa=.7, nodes=18000):
    """Numerical exact-mixture evaluation in scaled age u=4Dt log N/L^2."""
    assert isinstance(N, int) and N >= 5
    assert ell > 0 and 0 < kappa < float(erf(ell))
    b = math.log(N)
    u = np.linspace(.01, 12., nodes)
    z = np.sqrt(b/u)
    eta = ell/np.sqrt(u)
    survivor = erf(z)
    log_survival = N*np.log(survivor)
    image_term = .5*(erf(2*z + eta) - erf(2*z - eta))
    conditional_p = np.clip((erf(eta) - image_term)/survivor, 0, 1)
    count_logcdf = binom.logcdf(math.floor(kappa*N), N, conditional_p)
    log_mu_ratio = logsumexp(log_survival) + math.log(u[1]-u[0])
    log_numerator = logsumexp(log_survival + count_logcdf) + math.log(u[1]-u[0])
    u_k = float((ell/erfinv(kappa))**2)
    asymptotic = math.sqrt(u_k/(math.pi*b))*N**(1.-1./u_k)
    return float(log_numerator-log_mu_ratio), asymptotic, float(math.exp(log_mu_ratio))


def main():
    results=[]
    for N in (100, 300, 1000, 3000, 10000):
        observed, predicted, normalized=exact_log_probability(N)
        assert observed < 0 and predicted > 0 and .5 < normalized < 2
        ratio=-observed/predicted
        results.append(ratio)
        print(f'N={N:5d}, -log(P)={-observed:.6f}, scale={predicted:.6f}, ratio={ratio:.6f}')
    assert all(results[i+1] < results[i] for i in range(len(results)-1))
    assert 1 < results[-1] < 1.12
    print('Passed deterministic exact-mixture consistency checks; no infinity claim from finite computation.')


if __name__ == '__main__':
    main()
