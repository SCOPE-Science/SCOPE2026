#!/usr/bin/env python3
"""Independent finite checks for the Fourier spectrum of rooted cycle forests.

The analytic all-size arguments are in RESULT.md; finite checks alone do not
prove them. Uses only the Python 3 standard library.
"""
from fractions import Fraction
from itertools import product
from math import cos, isclose, pi, prod, sinh, sqrt


def enumerate_covariance(n, q):
    samples = []
    total = Fraction(0)
    for bits in product((0, 1), repeat=n):
        if all(bits):
            continue
        gaps = [i for i, bit in enumerate(bits) if bit == 0]
        sizes = [(gaps[(i + 1) % len(gaps)] - gaps[i]) % n or n
                 for i in range(len(gaps))]
        w = q ** len(gaps) * prod(sizes)
        total += w
        samples.append((bits, w))
    means = [sum(w * bits[i] for bits, w in samples) / total for i in range(n)]
    return [[sum(w * bits[i] * bits[j] for bits, w in samples) / total
             - means[i] * means[j] for j in range(n)] for i in range(n)]


def spectrum(n, q):
    q = float(q)
    t = 2.0 / (q + 2 + sqrt(q * (q + 4)))  # stable smaller resolvent root
    b = (1 - t) / (1 + t)
    H = (1 + t ** n) / (1 - t ** n)
    out = [b * H * 2 * t / (1 + t) ** 2
           - 2 * n * b * b * t ** n / (1 - t ** n) ** 2]
    for j in range(1, n):
        D = 1 - 2 * t * t * cos(2 * pi * j / n) + t ** 4
        out.append(b * H * (1 - b * (1 - t ** 4) / D))
    return out


def direct_fourier(row):
    n = len(row)
    return [sum(float(row[d]) * cos(2*pi*j*d/n) for d in range(n))
            for j in range(n)]


checks = 0
for n in range(3, 11):
    for q in (Fraction(1, 13), Fraction(1, 1), Fraction(7, 3)):
        C = enumerate_covariance(n, q)
        eig = spectrum(n, q)
        direct = direct_fourier(C[0])
        for j in range(n):
            assert isclose(eig[j], direct[j], abs_tol=3e-11, rel_tol=3e-10)
            checks += 1
            assert eig[j] > 0
            checks += 1
        assert eig[0] == min(eig)
        checks += 1
        assert isclose(max(eig), eig[n//2], abs_tol=1e-11)
        checks += 1
        assert all(eig[j] < eig[j+1] for j in range(1, n//2))
        checks += 1
        # exact cycle-edge sum/number-of-roots variance
        assert sum(C[0][j] for j in range(n)) > 0
        checks += 1

for q in (.08, 1., 5.):
    t = 2 / (q + 2 + sqrt(q * (q+4)))
    limit = (1+t)**2/(1+t*t)
    for n in (60, 120, 240):
        e = spectrum(n, q)
        assert abs(e[n//2]/e[0]-limit) < .02
        checks += 1

for u in (.5, 1., 3., 7.):
    limit = 2*sinh(u)/(sinh(u)-u)
    for n in (200, 500, 1000):
        e = spectrum(n, (u/n)**2)
        assert abs(e[n//2]/e[0]-limit) < .01
        checks += 1

for n in (80, 160, 320):
    q = .015/n**2
    e = spectrum(n, q)
    assert abs((e[n//2]/e[0])*(n*n*q)/12-1) < .02
    checks += 1

print('PASS: {} independent exact-enumeration/Fourier/limit assertions'.format(checks))
