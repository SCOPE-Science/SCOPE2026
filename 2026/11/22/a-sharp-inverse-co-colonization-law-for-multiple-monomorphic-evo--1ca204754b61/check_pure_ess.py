#!/usr/bin/env python3
"""Reproducible finite checks for Gaussian monomorphic ESS formulas.

Requires numpy and scipy. Finite sampling does not prove asymptotic claims.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ndtr


def mean_pure(n, mu):
    v = 1 + 2 * mu + 2 * mu * mu
    return n * quad(lambda z: math.exp(-z * z / 2) / math.sqrt(2 * math.pi)
                    * ndtr(z / math.sqrt(v)) ** (n - 1), -11, 11,
                    epsabs=2e-12, epsrel=2e-12)[0]


def simulate(n, mu, reps=200000):
    rng = np.random.default_rng(431726 + n * 100 + int(mu))
    hist = np.zeros(n + 1, dtype=np.int64)
    for remaining in range(reps, 0, -20000):
        batch = min(20000, remaining)
        a = rng.standard_normal((batch, n, n))
        # Row is the mutant index; column is the resident index.
        L = a.transpose(0, 2, 1) - np.diagonal(a, axis1=1, axis2=2)[:, None, :]
        L += mu * (a.transpose(0, 2, 1) - a)
        count = ((L < 0).sum(axis=1) == n - 1).sum(axis=1)
        hist += np.bincount(count, minlength=n + 1)
    return hist / reps


def main():
    for n in (2, 3, 4):
        assert abs(mean_pure(n, 0) - 1) < 1e-11
        for mu in (0, 2, 10, 40):
            freq = simulate(n, mu)
            exact_mean = mean_pure(n, mu)
            empirical_mean = sum(j * x for j, x in enumerate(freq))
            assert abs(empirical_mean - exact_mean) < 0.008
            if n == 2:
                rho = -mu * (1 + mu) / (1 + mu + mu * mu)
                exact_pair = .25 + math.asin(rho) / (2 * math.pi)
                assert abs(freq[2] - exact_pair) < 0.006
            if mu == 40:
                c = math.comb(n, 2) / (math.sqrt(2) * math.pi * 4 ** (n - 2))
                assert abs(sum(freq[2:]) - c / mu) < 0.007
            print(f"N={n} mu={mu} simulated={freq.round(5).tolist()} "
                  f"mean_exact={exact_mean:.8f} mean_sample={empirical_mean:.8f}")
    print("12 numerical/quadrature scenarios passed; none is an infinite proof")


if __name__ == "__main__":
    main()
