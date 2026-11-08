#!/usr/bin/env python3
"""Finite, reproducible checks of the cyclotomic winding-cost theorem.

This program is supplementary: exhaustive tests are finite, not a proof of
asymptotic bounds or of global density.
"""
import cmath
import itertools
import math


def totient(n):
    return sum(math.gcd(j, n) == 1 for j in range(n))


def roots(n):
    return [cmath.exp(2j * math.pi * j / n) for j in range(n)]


def integer_vectors_with_l1_at_most(d, bound):
    vals = range(-bound, bound + 1)
    # Exact L1 feasibility pruning, no floating-point decisions here.
    def extend(prefix, left):
        if len(prefix) == d:
            yield tuple(prefix)
            return
        for a in range(-left, left + 1):
            yield from extend(prefix + [a], left - abs(a))
    yield from extend([], bound)


def finite_min(n, budget):
    u = roots(n)
    positives = []
    min_modulus = float('inf')
    for a in integer_vectors_with_l1_at_most(n, budget):
        z = sum(v * r for v, r in zip(a, u))
        # Potential cyclotomic relations are exact zero, up to roundoff.
        if abs(z) > 1e-9:
            min_modulus = min(min_modulus, abs(z))
    return min_modulus


def verify_pigeonhole(n, L):
    q = totient(n)
    assert q >= 4
    u = roots(n)[:q]
    K = ((L + 1) ** (q // 2)) // 2
    assert K * K < (L + 1)**q
    width = 2*q*L / K
    seen = {}
    for h in itertools.product(range(L + 1), repeat=q):
        z = sum(k*r for k, r in zip(h, u))
        # Square [-q L, q L]^2 is deliberately wider than needed.
        i = min(K - 1, max(0, int((z.real + q*L)/width)))
        j = min(K - 1, max(0, int((z.imag + q*L)/width)))
        cell = (i, j)
        if cell in seen:
            h0, z0 = seen[cell]
            assert h0 != h
            diff = abs(z-z0)
            assert diff < math.sqrt(2)*width*(1+1e-9)
            assert sum(abs(x-y) for x,y in zip(h,h0)) <= n*L
            assert diff > 1e-9  # independent powers give nonzero element
            return diff, sum(abs(x-y) for x,y in zip(h,h0))
        seen[cell] = (h,z)
    raise AssertionError('Pigeonhole collision was not found')


def main():
    for d in (3, 4, 6):
        for budget in range(1, 5):
            v = finite_min(d, budget)
            assert abs(v - 1) < 1e-8, (d, budget, v)
        print('LATTICE_MINIMUM_OK', d)

    for d, L in ((5, 17), (7, 6), (8, 17), (10, 17), (12, 17)):
        q = totient(d)
        v, budget = verify_pigeonhole(d, L)
        assert v >= budget ** (-(q - 2)/2) - 1e-8, (d, v, budget)
        print('PIGEONHOLE_AND_NORM_SANITY_OK', d, q, 'budget', budget,
              'normalized_size', round(v, 9))

    # Finite direct test of the conjugate-norm lower bound, with
    # small integer coefficient vectors. For exact algebraic norm the
    # accompanying proof, rather than floating-point code, is decisive.
    for d, budget in ((5, 4), (7, 3), (8, 4)):
        q = totient(d)
        v = finite_min(d, budget)
        assert v + 1e-8 >= budget ** (-(q-2)/2), (d, budget, v)
        print('FINITE_LOWER_BOUND_OK', d, budget, round(v, 10))
    print('CYCLOTOMIC_WINDING_CHECK_OK')


if __name__ == '__main__':
    main()
