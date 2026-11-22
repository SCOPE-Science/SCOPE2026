"""Finite checks for a two-point periodic quadrature theorem.

Run with: python verify.py
Tests are supplementary; the general minimax result has an analytic proof.
"""
from fractions import Fraction
from math import cos, pi, sin

checks = 0
for m in range(1, 41):
    # Exact coefficient-weight identity used by the Fejer certificate.
    triangular_weight = sum(m + 1 - k for k in range(1, m + 1))
    assert triangular_weight == m * (m + 1) // 2
    checks += 1

    # Uniform distribution over nonidentity cyclic shifts has exact
    # discrete Fourier moments -1/m in the target band.
    N = m + 1
    for k in range(1, N):
        real = sum(cos(2 * pi * k * j / N) for j in range(1, N)) / m
        imag = sum(sin(2 * pi * k * j / N) for j in range(1, N)) / m
        assert abs(real + 1 / m) < 2e-12, (m, k, real)
        assert abs(imag) < 2e-12, (m, k, imag)
        checks += 2

    # Phase quadrature: integrate a two-sample random-shift squared error
    # for several different coefficient vectors, using a sufficiently
    # fine deterministic mesh. This is a finite check of the covariance
    # normalization, not a proof for arbitrary copulas or coefficients.
    if m <= 16:
        grid_size = 8 * N
        for case in range(4):
            a = [Fraction((k * (case + 2) + 1) % 7 - 3, 5) for k in range(1, m + 1)]
            b = [Fraction((k * (case + 3) + 2) % 9 - 4, 7) for k in range(1, m + 1)]
            norm2 = float(sum(x*x + y*y for x,y in zip(a,b)))
            if norm2 == 0: continue
            total = 0.0
            for j in range(grid_size):
                x = j / grid_size
                f_x = sum(2**0.5 * (float(a[k-1]) * cos(2*pi*k*x) +
                                       float(b[k-1]) * sin(2*pi*k*x)) for k in range(1,m+1))
                for shift in range(1,N):
                    y = (x + shift/N) % 1
                    f_y = sum(2**0.5 * (float(a[k-1]) * cos(2*pi*k*y) +
                                           float(b[k-1]) * sin(2*pi*k*y)) for k in range(1,m+1))
                    total += ((f_x + f_y)/2)**2
            total /= grid_size * m
            expected = (m - 1) / (2*m) * norm2
            assert abs(total - expected) < 2e-10, (m,case,total,expected)
            checks += 1

# Explicit rational upper bound and equality rigidities.
for m in range(1,200):
    expected = Fraction(m - 1,2*m)
    assert expected == Fraction(1,2)*(1-Fraction(1,m))
    # Each Fejer weight is positive. Equal minimum cosine moments imply
    # the exact kernel expectation is zero.
    weights = [m + 1 - k for k in range(1,m+1)]
    assert all(w > 0 for w in weights)
    assert Fraction(m+1) - sum(Fraction(2*w,m) for w in weights) == 0
    checks += 3
print(f"PASS: {checks} supplementary finite checks")
