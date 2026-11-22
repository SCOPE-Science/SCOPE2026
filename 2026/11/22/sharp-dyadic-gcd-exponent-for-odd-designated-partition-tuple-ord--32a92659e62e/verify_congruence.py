"""Reproducible finite diagnostics for odd-tuple designated-partition congruences.

The all-index theorem is proved independently by formal-power-series lifting
and the published theta-series identity; finite checks are not a substitute.
Run: python3 verify_congruence.py
"""
from math import comb


def divisors(n):
    return (d for d in range(1, n + 1) if n % d == 0)


def logarithmic_coefficients(N):
    # F(q)=prod_{d>=1}(1-q^d)^{-c(d)}.
    return [0] + [sum(d * (1 + (d % 2 == 0) + (d % 3 == 0) - (d % 6 == 0))
                            for d in divisors(n)) for n in range(1, N + 1)]


def power_coefficients(k, N, b):
    a = [1] + [0] * N
    for n in range(1, N + 1):
        t = k * sum(b[d] * a[n-d] for d in range(1, n+1))
        assert t % n == 0, (k, n, t)
        a[n] = t // n
    return a


def main():
    N = 160
    b = logarithmic_coefficients(N)
    f = power_coefficients(1, N, b)
    assert f[:4] == [1, 1, 3, 5]
    inv = power_coefficients(-1, N, b)
    assert inv[:8] == [1, -1, -2, 0, 1, 4, 0, 0]
    gap_checks = 0
    for n in range((N - 3)//4 + 1):
        assert inv[4*n + 3] == 0, n
        gap_checks += 1

    valuation_checks = 0
    sharpness_checks = 0
    for k in range(1, 130, 2):
        a = power_coefficients(k, N, b)
        s = ((k + 1) & -(k + 1)).bit_length() - 1
        bound = 1 << (s - 1)
        for j in range((N-3)//4 + 1):
            assert a[4*j+3] % bound == 0, (k, j, s)
            valuation_checks += 1
        first = k * (k+1) * (k+14) // 6
        assert a[3] == first and first % (2*bound) == bound, (k, first, bound)
        sharpness_checks += 1
    # Independent Euler-product construction for reciprocal F(q)^{-1}.
    M = 80
    direct = [1]+[0]*M
    for m in range(1, M+1):
        for d in (m, 2*m, 3*m):
            if d <= M:
                for n in range(M, d-1, -1):
                    direct[n] -= direct[n-d]
        d = 6*m
        if d <= M:
            for n in range(d, M+1):
                direct[n] += direct[n-d]
    assert direct == inv[:M+1]
    print('DESIGNATED_ODD_K_DYADIC_OK',
          'inverse_gap_tests', gap_checks,
          'coefficient_divisibility_tests', valuation_checks,
          'sharpness_tests', sharpness_checks,
          'independent_inverse_coefficients', M+1)


if __name__ == '__main__':
    main()
