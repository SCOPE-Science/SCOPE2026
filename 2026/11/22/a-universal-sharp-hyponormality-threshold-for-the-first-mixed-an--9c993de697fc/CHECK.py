#!/usr/bin/env python3
"""Finite exact-arithmetic and numerical cross-checks of a Bergman Toeplitz theorem.

No third-party packages are required. The accompanying proof, not this finite script,
controls all real Bergman weights and arbitrary finite-support test vectors.
"""
from fractions import Fraction as F
from math import sqrt
from random import Random

count = 0


def x(n, q):
    return F(0) if n < 0 else F(n + 1, 1) / (n + q + 1)


def A(n, q):
    return x(n, q) - x(n - 1, q)


def B(n, q):
    return x(n, q) ** 2 * x(n - 1, q) - x(n + 1, q) ** 2 * x(n, q)


def C(n, q):
    return 0.0 if n < 0 else sqrt(float(x(n, q) * x(n + 1, q))) * float(A(n + 2, q))


def P(n, q):
    return (6*n*n*q + 4*n*n + 9*n*q*q + 23*n*q + 12*n
            + 3*q*q*q + 15*q*q + 20*q + 8)


Q = [F(1, 101), F(2, 7), F(1), F(7, 3), F(25), F(401, 7)]
for q in Q:
    for n in range(400):
        lhs = 3*A(n, q) + B(n, q)
        rhs = q*P(n, q) / ((n+q)*(n+q+1)**2*(n+q+2)**2)
        assert lhs == rhs and lhs > 0
        assert A(n, q) == q/((n+q)*(n+q+1))
        assert A(n+2, q) < A(n, q)
        assert C(n, q) < float(A(n+2, q))
        assert C(n, q) + C(n-2, q) < 2*float(A(n, q))
        count += 5
        for t in [3., 3.5, 4., 11.]:
            diag = t*t*float(A(n, q)) + float(B(n, q))
            assert diag - t*(C(n, q) + C(n-2, q)) >= -1.e-12
            count += 1


def norm2(z):
    return sum(abs(t)**2 for t in z)


def operator_and_adjoint(values, a, b, q):
    # Include one extra endpoint to retain the entire image of a finite vector.
    N = len(values)
    out = [0j] * (N + 1)
    adj = [0j] * (N + 1)
    for n, z in enumerate(values):
        u = sqrt(float(x(n, q)))
        out[n+1] += a*u*z
        if n >= 1:
            v = float(x(n, q))*sqrt(float(x(n-1, q)))
            out[n-1] += b*v*z
            adj[n-1] += a.conjugate()*sqrt(float(x(n-1, q)))*z
        vplus = float(x(n+1, q))*sqrt(float(x(n, q)))
        adj[n+1] += b.conjugate()*vplus*z
    return out, adj


def band_form(values, a, b, q):
    s = 0j
    for n, z in enumerate(values):
        s += (abs(a)**2*float(A(n, q)) + abs(b)**2*float(B(n, q)))*abs(z)**2
        if n + 2 < len(values):
            # Matrix element <H e_n,e_{n+2}> = a conj(b) C_n.
            s += 2*(a*b.conjugate()*C(n, q)*z*values[n+2].conjugate()).real
    return s.real


rng = Random(847291)
for q in Q:
    for rep in range(120):
        a = complex(rng.uniform(-3,3), rng.uniform(-3,3))
        b = complex(rng.uniform(-1,1), rng.uniform(-1,1))
        v = [complex(rng.uniform(-1,1),rng.uniform(-1,1)) for _ in range(15)]
        Tv, Tstarv = operator_and_adjoint(v, a, b, q)
        delta = norm2(Tv)-norm2(Tstarv)
        test = band_form(v, a, b, q)
        assert abs(delta-test) <= 2e-10*(1+abs(delta)+abs(test))
        count += 1


# Explicit finite-support witnesses below the sharp ratio (positive q and large N).
for q in [F(1,7), F(1), F(17,3)]:
    for t in [F(0), F(1), F(2), F(14,5)]:
        N, L = 5000, 40
        d = sum(float(t*t*A(N+2*j, q) + B(N+2*j, q)) for j in range(L))
        cross = sum(2*float(t)*C(N+2*j, q) for j in range(L-1))
        assert d-cross < 0, (q, t, d-cross)
        count += 1

print(f"PASS: {count} supplementary checks; analytical proof required for universal quantifiers")
