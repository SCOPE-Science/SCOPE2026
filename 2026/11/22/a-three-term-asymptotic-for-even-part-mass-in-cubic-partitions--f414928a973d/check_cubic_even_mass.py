#!/usr/bin/env python3
"""Independent finite checks for exact cubic-partition even-mass formulas.

This checker is diagnostic: it does not prove the infinite saddle-point theorem.
"""
from math import pi, sqrt


def partition_numbers(limit):
    p = [0] * (limit + 1)
    p[0] = 1
    for m in range(1, limit + 1):
        for n in range(m, limit + 1):
            p[n] += p[n - m]
    return p


def divisor_sums(limit):
    out = [0] * (limit + 1)
    for d in range(1, limit + 1):
        for m in range(d, limit + 1, d):
            out[m] += d
    return out


def exact_arrays(limit):
    p = partition_numbers(limit)
    a = [sum(p[j] * p[n - 2*j] for j in range(n//2 + 1))
         for n in range(limit + 1)]
    sig = divisor_sums(limit//2)
    even = [4 * sum(sig[j] * a[n - 2*j] for j in range(1, n//2 + 1))
            for n in range(limit + 1)]
    return a, even


def direct_colored_partitions(limit):
    count = [0] * (limit + 1)
    total_even = [0] * (limit + 1)
    count[0] = 1
    for m in range(1, limit + 1):
        colors = 2 if m % 2 == 0 else 1
        for _ in range(colors):
            for n in range(m, limit + 1):
                before = count[n-m]
                total_even[n] += total_even[n-m] + (m if m % 2 == 0 else 0) * before
                count[n] += before
    return count, total_even


def besseli(k, x):
    from math import factorial
    term = (x/2)**k / factorial(k)
    total = term
    for j in range(1, 5000):
        term *= (x*x/4)/(j*(j+k))
        total += term
        if abs(term) < 1e-15 * total:
            break
    return total


def bessel_prediction(n):
    C = pi*pi/4
    N = n - 1/8
    z = 2 * sqrt(C*N)
    i0, i1, i2 = (besseli(j, z) for j in (0, 1, 2))
    return (2*N/3)*(i0/i2) - sqrt(N/C)*(i1/i2) + 1/6


def three_term(n):
    return 2*n/3 - 2*sqrt(n)/(3*pi) + 1/12 - 1/(pi*pi)


def main():
    max_n = 1200
    a, even = exact_arrays(max_n)
    a2, e2 = direct_colored_partitions(125)
    for n in range(126):
        assert a[n] == a2[n], (n, 'count', a[n], a2[n])
        assert even[n] == e2[n], (n, 'weighted even', even[n], e2[n])
        assert 0 <= even[n] <= n*a[n]
    print('COLORED_PARTITION_COEFFICIENT_IDENTITY_OK', 126)
    for n in (100, 200, 400, 800, 1200):
        actual = even[n]/a[n]
        bpred = bessel_prediction(n)
        asym = three_term(n)
        print('N', n, 'exact', f'{actual:.12f}', 'Bessel', f'{bpred:.12f}',
              'BesselError', f'{actual-bpred:.9g}', 'threeTermError', f'{actual-asym:.9g}')
        assert abs(actual-bpred) < (0.02 if n < 400 else 0.0001)
        assert abs(actual-asym) < 0.12/sqrt(n)
    print('CUBIC_EVEN_MASS_ASYMPTOTIC_DIAGNOSTICS_OK')


if __name__ == '__main__':
    main()
