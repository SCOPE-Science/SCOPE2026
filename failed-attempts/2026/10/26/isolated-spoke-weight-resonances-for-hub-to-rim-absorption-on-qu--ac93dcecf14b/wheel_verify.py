#!/usr/bin/env python3
"""Exact and numerical verification of a weighted-wheel quantum absorption formula.

Standard scientific dependencies: numpy, scipy, sympy.
"""
import math
import numpy as np
from scipy.linalg import eigh
import sympy as sp


def weighted_wheel(n, tau):
    A = np.zeros((n + 1, n + 1), dtype=float)
    for j in range(n):
        A[j, (j + 1) % n] = A[(j + 1) % n, j] = 1.0
        A[j, n] = A[n, j] = tau
    return A


def projected_dark_mass(n, tau, tol=1.e-9):
    A = weighted_wheel(n, tau)
    spectrum, U = eigh(A)
    i = 0
    bright_dim = 0
    darkmass = 0.0
    while i < n + 1:
        j = i + 1
        while j < n + 1 and abs(spectrum[j] - spectrum[i]) < tol:
            j += 1
        B = U[:, i:j]
        # The hub is index n, and the trap is rim index 0.
        trap = B[0, :]
        source = B[n, :]
        tnorm = np.dot(trap, trap)
        darkmass += np.dot(source, source)
        if tnorm > 1.e-12:
            bright_dim += 1
            darkmass -= (np.dot(source, trap) ** 2) / tnorm
        i = j
    return darkmass, bright_dim


def resonance(n, k):
    lam = 2.0 * math.cos(2 * math.pi * k / n)
    assert lam < -1.e-12
    tau = math.sqrt(lam * (lam - 2) / n)
    d = 1 if (n % 2 == 0 and k == n // 2) else 2
    survival = d * (lam - 2) / ((2 * d + 1) * lam - 2 * d)
    return lam, tau, survival


def exact_n_unit(n):
    A = sp.zeros(n + 1)
    for i in range(n):
        A[i, (i + 1) % n] = A[(i + 1) % n, i] = 1
        A[i, n] = A[n, i] = 1
    e0 = sp.eye(n + 1)[:, 0]
    K = sp.Matrix.hstack(*(A**j * e0 for j in range(n + 1)))
    rank = K.rank()
    B = sp.Matrix.hstack(*K.columnspace())
    # Standard Euclidean orthogonal projector to the Krylov bright space.
    source = sp.eye(n + 1)[:, n]
    coef = (B.T * B).inv() * (B.T * source)
    brightmass = (source.T * B * coef)[0]
    return rank, sp.factor(1 - brightmass)


def main():
    checks = 0
    # All resonant branches up to 39 rim sites; independent matrix diagonalization.
    for n in range(3, 40):
        ks = [k for k in range(1, n // 2 + 1)
              if math.cos(2 * math.pi * k / n) < -1.e-12]
        for k in ks:
            lam, tau, target = resonance(n, k)
            got, dim = projected_dark_mass(n, tau)
            assert abs(got - target) < 2.e-9, (n, k, target, got)
            assert dim == n // 2 + 1, (n, k, dim)
            checks += 2
            # Displacement away from the isolated resonance removes hub dark mass.
            for displacement in (-.01, +.01):
                if tau + displacement <= 0: continue
                perturbed, dimp = projected_dark_mass(n, tau + displacement)
                assert abs(perturbed) < 1.e-8, (n, k, perturbed)
                assert dimp == n // 2 + 2, (n, k, dimp)
                checks += 2
    # Generic non-resonant strengths, including values outside the resonant range.
    for n in range(3, 40):
        for tau in (0.1, 0.337, 3.7):
            if any(abs(tau - resonance(n, k)[1]) < 1.e-7 for k in range(1, n // 2 + 1)
                   if math.cos(2 * math.pi * k / n) < -1.e-12):
                continue
            got, dim = projected_dark_mass(n, tau)
            assert abs(got) < 1.e-8, (n, tau, got)
            assert dim == n // 2 + 2, (n, tau, dim)
            checks += 2
    # Exact integer linear algebra, independent of floating-point eigenvalue grouping.
    for n in range(3, 14):
        dim, survival = exact_n_unit(n)
        target = sp.Rational(2, 3) if n == 3 else sp.Rational(1, 2) if n == 8 else 0
        targetdim = n // 2 + 1 if n in (3, 8) else n // 2 + 2
        assert survival == target, (n, survival, target)
        assert dim == targetdim, (n, dim, targetdim)
        checks += 2
    print(f'PASS: {checks} independent checks, 37 wheel sizes, all resonance branches, detuning and exact Krylov ranks.')
    print('Exact unit-spoke special survival: n=3 -> 2/3, n=8 -> 1/2, others zero.')


if __name__ == '__main__':
    main()
