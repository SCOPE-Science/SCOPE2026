#!/usr/bin/env python3
"""Finite diagnostic tests for the pendant-weight resonance theorem.

Uses only the Python standard library, exact finite-field controllability ranks,
and high-precision trigonometric eigenvector residuals via decimal-independent
floating point. These tests are diagnostics; the written proof proves the family.
"""
import math
from fractions import Fraction

PRIMES = (1000000007, 1000000009)


def exceptional_indices(n):
    # Exact integer inequalities for (0<lambda<1) or (2<lambda<4).
    return [ell for ell in range(1, n-2, 2)
            if 3*ell < n-2 or 2*ell > n-2]


def candidate_weight(n, ell):
    lam = 2-2*math.cos(math.pi*ell/(n-2))
    return lam*(2-lam)/(2*(1-lam))


def is_predicted_exception(n, t):
    return any(abs(candidate_weight(n, ell)-float(t)) < 5e-10
               for ell in exceptional_indices(n))


def finite_field_rank(n, t, prime):
    N = n + 1
    denom = t.denominator
    if denom % prime == 0:
        raise ValueError('Prime divides weight denominator')
    w = (t.numerator*pow(denom, -1, prime)) % prime
    neighbors = [[] for _ in range(N)]
    for i in range(n):
        neighbors[i].append(((i+1) % n, 1))
        neighbors[(i+1) % n].append((i, 1))
    neighbors[0].append((n, w))
    neighbors[n].append((0, w))
    basis = {}
    v = [0] * N
    v[1] = 1
    for step in range(N):
        q = v[:]
        while True:
            pivot = next((i for i, val in enumerate(q) if val % prime), None)
            if pivot is None:
                return step
            if pivot in basis:
                b = basis[pivot]
                alpha = q[pivot]
                q = [(x-alpha*y) % prime for x, y in zip(q, b)]
            else:
                scale = pow(q[pivot], -1, prime)
                basis[pivot] = [(x*scale) % prime for x in q]
                break
        nxt = [0]*N
        for i in range(N):
            nxt[i] = sum(wt*(v[i]-v[j]) for j, wt in neighbors[i]) % prime
        v = nxt
    return N


def residual(n, ell):
    theta = math.pi*ell/(n-2)
    lam = 2-2*math.cos(theta)
    t = candidate_weight(n, ell)
    # Set v0 = -sin(theta), vi=sin((i-1)*theta), v_leaf=t*v0/(t-lam).
    v = [0.0]*(n+1)
    v[0] = -math.sin(theta)
    for i in range(1, n):
        v[i] = math.sin((i-1)*theta)
    v[n] = t*v[0]/(t-lam)
    LV = [0.]*(n+1)
    for i in range(n):
        j = (i+1) % n
        LV[i] += v[i]-v[j]
        LV[j] += v[j]-v[i]
    LV[0] += t*(v[0]-v[n])
    LV[n] += t*(v[n]-v[0])
    return max(abs(LV[i]-lam*v[i]) for i in range(n+1)), abs(v[1]), t


def main():
    exact_cases = 0
    for n in range(3, 49):
        # Weights test generic and resonant rational values, both endpoints.
        for t in (Fraction(1), Fraction(1,2), Fraction(2), Fraction(1,3),
                  Fraction(3,2), Fraction(4,3), Fraction(7,5)):
            expected = n+1 if not is_predicted_exception(n, t) else None
            ranks = [finite_field_rank(n, t, p) for p in PRIMES]
            if t == 1:
                expected = n+1 - (2 if n % 8 == 6 else 0)
            if t == Fraction(1,2):
                expected = n+1 - (2 if n % 10 == 7 else 0)
            if expected is not None:
                assert all(r == expected for r in ranks), (n,t,ranks)
            else:
                assert all(r < n+1 for r in ranks), (n,t,ranks)
            exact_cases += 1
    analytic_cases = 0
    for n in range(3, 65):
        for ell in exceptional_indices(n):
            err, u1, t = residual(n, ell)
            assert t > 0 and err < 2e-10 and u1 < 1e-14, (n,ell,err,u1,t)
            analytic_cases += 1
    special = 0
    for n in range(3, 101):
        expected = (n % 8 == 6)
        assert is_predicted_exception(n, Fraction(1)) == expected, n
        assert is_predicted_exception(n, Fraction(1,2)) == (n % 10 == 7), n
        special += 2
    print('PASS', exact_cases, 'two-prime full Krylov-rank tests,',
          analytic_cases,'exceptional-mode residual tests,',special,
          'unweighted modular-size tests')

if __name__ == '__main__':
    main()
