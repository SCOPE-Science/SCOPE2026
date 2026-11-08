#!/usr/bin/env python3
"""Exact finite corroboration of the Dirichlet-inverse composite-gap theorem.

The computation constructs the inverse by convolution, independently of
prime-power formulas used in the mathematical proof.
"""
from math import isqrt


def least_prime_factors(limit):
    lp = list(range(limit + 1))
    for p in range(2, isqrt(limit) + 1):
        if lp[p] == p:
            for n in range(p * p, limit + 1, p):
                if lp[n] == n:
                    lp[n] = p
    return lp


def mu_jordan(limit, k, lp):
    mu = [0] * (limit + 1)
    jordan = [0] * (limit + 1)
    mu[1] = jordan[1] = 1
    for n in range(2, limit + 1):
        p = lp[n]
        m = n // p
        if m % p == 0:
            mu[n] = 0
            jordan[n] = p**k * jordan[m]
        else:
            mu[n] = -mu[m]
            jordan[n] = (p**k - 1) * jordan[m]
    return mu, jordan


def divisor_sums(limit, k):
    sigma = [0] * (limit + 1)
    for d in range(1, limit + 1):
        dk = d**k
        for multiple in range(d, limit + 1, d):
            sigma[multiple] += dk
    return sigma


def dirichlet_inverse_sigma(limit, sigma):
    # Convolution equation sum_{d | n} inv(d)*sigma(n//d) = [n=1].
    inv = [0] * (limit + 1)
    inv[1] = 1
    for d in range(1, limit + 1):
        fd = inv[d]
        if fd:
            for multiple in range(2 * d, limit + 1, d):
                inv[multiple] -= fd * sigma[multiple // d]
    return inv


def run(limit=10000, k_min=2, k_max=8):
    lp = least_prime_factors(limit)
    for k in range(k_min, k_max + 1):
        sigma = divisor_sums(limit, k)
        inv = dirichlet_inverse_sigma(limit, sigma)
        mu, jordan = mu_jordan(limit, k, lp)
        target = 4**k + 3
        seen = []
        best = None
        closest = []
        for n in range(2, limit + 1):
            value = inv[n] + mu[n] + jordan[n] + 3
            isprime = lp[n] == n
            if isprime:
                assert value == 0, (k, n, value)
            else:
                assert abs(value) >= target, (k, n, value, target)
                if abs(value) == target:
                    seen.append(n)
                if best is None or abs(value) < best:
                    best = abs(value)
                    closest = [n]
                elif abs(value) == best:
                    closest.append(n)
        assert seen == [4], (k, seen)
        assert best == target and closest == [4], (k, best, closest)
        assert inv[4] + mu[4] + jordan[4] + 3 == target
        print('PASS k=%d n=2..%d exact_composite_min=%d unique_minimizer=4' %
              (k, limit, target))
    print('VERIFY_OK k_range=%d..%d n_range=2..%d independent_convolution=yes exact_integer=yes' %
          (k_min, k_max, limit))

if __name__ == '__main__':
    run()
