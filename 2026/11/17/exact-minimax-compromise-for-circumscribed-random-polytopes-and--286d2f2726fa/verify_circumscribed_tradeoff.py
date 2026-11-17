"""Numerical cross-checks for minimax circumscribed-polytope sampling laws.

This script uses only the Python standard library; quadrature supports the
analytic proof but does not establish its continuum or asymptotic claims.
"""
import math

N = 16384
COS = [math.cos(2 * math.pi * (i + 0.5) / N * 2) for i in range(N)]


def mean(v):
    return math.fsum(v) / N


def case(t):
    radii = [1 + t * v for v in COS]
    A = mean(r ** (2 / 3) for r in radii)
    B = mean(r ** (1 / 3) for r in radii)
    ia, ib = A ** -3, B ** -3
    w = [r ** (1 / 3) for r in radii]
    delta = [r * ia - ib for r in radii]

    def value(z):
        zlist = [z * r * ia + (1 - z) * ib for r in radii]
        H = mean(w0 * a ** (1 / 3) for w0, a in zip(w, zlist))
        derivative = mean(w0 * b * a ** (-2 / 3) / 3
                          for w0, b, a in zip(w, delta, zlist))
        return H, derivative, zlist

    assert value(0)[1] > 0 and value(1)[1] < 0
    left, right = 0., 1.
    for _ in range(48):
        middle = (left + right) / 2
        if value(middle)[1] > 0:
            left = middle
        else:
            right = middle
    lam = (left + right) / 2
    H, dH, mix = value(lam)
    angular_prob = [w0 * a ** (1 / 3) / H for w0, a in zip(w, mix)]
    assert abs(mean(angular_prob) - 1) < 2e-12
    volume = mean(r * r * ia / (q * q) for r, q in zip(radii, angular_prob))
    width = mean(r * ib / (q * q) for r, q in zip(radii, angular_prob))
    assert abs(volume - width) < 1e-10
    assert abs(volume - H ** 3) < 1e-10
    assert abs(dH) < 1e-10
    Hhalf = value(0.5)[0]
    assert H ** 3 >= Hhalf ** 3 - 1e-12
    return lam, H ** 3, Hhalf ** 3


def main():
    assert case(0.15)[0] > 0.5
    assert abs(case(0.5)[0] - case(-0.5)[0]) < 2e-11
    for t in (0.08, 0.12, 0.2, 0.35, 0.6):
        lam, optimal, average = case(t)
        print('t=%.2f lambda=%.12f minimax=%.12f average=%.12f' %
              (t, lam, optimal, average))
    shift_coeff = (case(.08)[0] - 0.5) / .08**2
    gap_coeff = (case(.12)[1] - case(.12)[2]) / .12**6
    print('predicted shift coefficient', 5 / 96, 'numerical', shift_coeff)
    print('predicted gap coefficient', 25 / 55296, 'numerical', gap_coeff)
    assert abs(shift_coeff - 5 / 96) < 0.001
    assert abs(gap_coeff - 25 / 55296) < 0.00003
    print('CIRCUMSCRIBED_TRADEOFF_NUMERICAL_CHECKS_OK')


if __name__ == '__main__':
    main()
