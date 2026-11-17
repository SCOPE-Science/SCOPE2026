"""Finite diagnostics for sharp local radial Ky Fan stability; analytic proof is separate.
Uses only the Python standard library. Run: python check_radial.py
"""
import math
import random


def poisson_tail(j, x):
    # e^-x times the first j+1 terms of exp(x); upper gamma tail.
    return math.exp(-x) * sum(x ** k / math.factorial(k) for k in range(j + 1))


def moment(j, intervals):
    return sum(poisson_tail(j, a) - poisson_tail(j, b) for a, b in intervals)


def kyfan(n, intervals, degree_cutoff=25):
    return sum(sorted((moment(j, intervals) for j in range(degree_cutoff)),
                      reverse=True)[:n])


def q(n, x):
    return poisson_tail(n - 1, x)


def f(n, x):
    return n - math.exp(-x) * sum((n - j) * x ** j / math.factorial(j)
                                  for j in range(n))


def sharp_deficit(n, s, delta):
    return 2 * f(n, s) - f(n, s - delta) - f(n, s + delta)


def check():
    rng = random.Random(20261108)
    checks = 0
    for n in (2, 3, 4, 5):
        for s in (0.9, 1.8, 3.3, 5.0):
            gap = math.exp(-s) * s ** n / math.factorial(n)
            d = gap / 5
            assert 0 < d < gap / 2 and d < s
            checks += 1
            disk = [(0.0, s)]
            swapped = [(0.0, s - d), (s, s + d)]
            base = kyfan(n, disk)
            optimum = kyfan(n, swapped)
            deficit = sharp_deficit(n, s, d)
            assert abs((base - optimum) - deficit) < 2.e-9
            checks += 1
            assert deficit > 0
            checks += 1
            diag = [moment(j, swapped) for j in range(25)]
            assert min(diag[:n]) > max(diag[n:])
            checks += 1
            for trial in range(24):
                left = rng.uniform(0.0, s - d)
                right = s + rng.uniform(0.0, 4.0)
                other = [(0.0, left), (left + d, s), (right, right + d)]
                other_kyfan = kyfan(n, other)
                assert base - other_kyfan >= deficit - 2.e-9
                checks += 1
                diag2 = [moment(j, other) for j in range(25)]
                assert min(diag2[:n]) > max(diag2[n:]) - 2.e-10
                checks += 1
            for ratio in (0.05, 0.02, 0.01):
                eps = d * ratio
                quadratic_coefficient = math.exp(-s) * s**(n-1) / math.factorial(n-1)
                measured = sharp_deficit(n, s, eps) / eps**2
                assert abs(measured / quadratic_coefficient - 1) < 0.035
                checks += 1
    print(f'PASS: {checks} finite numerical diagnostic assertions')

if __name__ == '__main__':
    check()
