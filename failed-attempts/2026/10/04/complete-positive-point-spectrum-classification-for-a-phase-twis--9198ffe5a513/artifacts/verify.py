#!/usr/bin/env python3
import math


def source_polynomial(k, ell, mu, q):
    x = k * ell
    s2 = math.sin(2.0 * mu)
    c2 = math.cos(2.0 * mu)
    c0 = -s2 * math.sin(x) ** 2
    c4 = c0
    c2coef = s2 * (1.0 + 3.0 * math.cos(2.0 * x))
    c1 = 2.0 * (2.0 * c2 * math.cos(x) - q) * math.sin(x)
    c3 = 2.0 * (2.0 * c2 * math.cos(x) + q) * math.sin(x)
    return c0 + c1 * k + c2coef * k * k + c3 * k ** 3 + c4 * k ** 4


def affine_polynomial(k, ell, mu, q):
    a = source_polynomial(k, ell, mu, 0.0)
    b = 2.0 * k * (k * k - 1.0) * math.sin(k * ell)
    return a + b * q


def close(a, b, tol=2e-11):
    return abs(a - b) <= tol * (1.0 + abs(a) + abs(b))


def main():
    ks = [0.23, 0.7, 1.0, 1.4, 2.8, 5.1]
    ells = [0.31, 0.9, 1.7, 2.4]
    mus = [0.13, 0.41, 0.88, 1.31]
    qs = [-2.0, -0.7, 0.0, 1.2, 2.0]
    for k in ks:
        for ell in ells:
            for mu in mus:
                for q in qs:
                    a = source_polynomial(k, ell, mu, q)
                    b = affine_polynomial(k, ell, mu, q)
                    assert close(a, b), (k, ell, mu, q, a, b)

    # At k=1, all Bloch dependence vanishes and the constant is exact.
    for ell in ells:
        for mu in mus:
            target = 4.0 * math.sin(2.0 * (mu + ell))
            for q in qs:
                got = source_polynomial(1.0, ell, mu, q)
                assert close(got, target), (ell, mu, q, got, target)

    # At k ell = n pi, the Bloch coefficient vanishes but the constant is
    # 4 k^2 sin(2 mu), nonzero for interior mu.
    for ell in [0.47, 1.11, 2.03]:
        for n in range(1, 6):
            k = n * math.pi / ell
            for mu in mus:
                target = 4.0 * k * k * math.sin(2.0 * mu)
                for q in qs:
                    got = source_polynomial(k, ell, mu, q)
                    assert close(got, target, 5e-10), (ell, n, mu, q, got, target)
                    assert abs(got) > 1e-8

    # Representative exceptional parameter pairs: mu+ell is a multiple of pi/2.
    exceptional = [
        (0.30, math.pi / 2.0 - 0.30),
        (2.00, math.pi - 2.00),
        (3.40, 3.0 * math.pi / 2.0 - 3.40),
    ]
    for ell, mu in exceptional:
        assert 0.0 < mu < math.pi / 2.0
        for q in qs:
            assert abs(source_polynomial(1.0, ell, mu, q)) < 2e-11

    # Representative nonexceptional parameters are not flat at k=1.
    for ell, mu in [(0.4, 0.4), (1.0, 0.3), (2.2, 0.7)]:
        vals = [source_polynomial(1.0, ell, mu, q) for q in qs]
        assert max(vals) - min(vals) < 2e-11
        assert abs(vals[0]) > 1e-6

    print('VERIFY_OK')


if __name__ == '__main__':
    main()
