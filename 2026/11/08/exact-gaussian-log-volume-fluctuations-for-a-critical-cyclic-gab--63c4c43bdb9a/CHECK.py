#!/usr/bin/env python3
"""Numerical reproducibility checks for a finite Gabor log-volume identity.

Requires numpy. These finite checks corroborate, but do not replace, the
analytic probability argument and the one-dependent central limit theorem.
"""
import math
import numpy as np


def gabor_matrix(g):
    n = len(g)
    assert n % 2 == 0
    p = n // 2
    z = np.arange(n)
    return np.column_stack([
        np.exp(2j * np.pi * (2*l) * z / n) * np.roll(g, k)
        for k in (0, 1) for l in range(p)
    ])


def local_log_volume(g):
    p = len(g)//2
    v = np.stack((g[:p],g[p:]), axis=1)
    w = np.roll(v, 1, axis=0)
    w[0] = v[-1, ::-1]
    d = v[:, 0]*w[:, 1]-v[:, 1]*w[:, 0]
    return 2*p*math.log(p)+sum(np.log(abs(d)**2))


def main():
    rng = np.random.default_rng(20261105)
    count = 0
    for p in (3, 4, 5, 7, 11):
        for _ in range(50):
            n = 2*p
            g = (rng.standard_normal(n)+1j*rng.standard_normal(n))/math.sqrt(2*n)
            G = gabor_matrix(g)
            S = G@G.conj().T
            sign, logdet = np.linalg.slogdet(S)
            assert abs(sign-1) < 1e-6
            target = local_log_volume(g)
            assert abs(logdet-target) < 1e-7*max(1,abs(target))
            count += 1
    for p in (7, 24):
        nrep = 4000
        values = np.zeros(nrep)
        for j in range(nrep):
            g = (rng.standard_normal(2*p)+1j*rng.standard_normal(2*p))/math.sqrt(4*p)
            values[j] = local_log_volume(g)
        mean = p*(1-2*np.euler_gamma-2*math.log(2))
        var = p*(2*np.pi**2/3-3)
        # Loose Monte Carlo checks are deliberately not used as proof.
        assert abs(values.mean()-mean) < 0.2 * math.sqrt(var)
        assert abs(values.var(ddof=1)/var-1) < 0.1
        count += 2
    print('GAUSSIAN_CYCLIC_GABOR_VOLUME_CHECKS_PASSED', count)


if __name__ == '__main__':
    main()
