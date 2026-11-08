#!/usr/bin/env python3
"""Exact small-case checks for prime-relative Fuss--Catalan nondivisibility.

No external packages. Finite checks corroborate, but do not prove, the theorem.
"""
from math import comb, isclose, sin, cos, pi, log


def fuss(p, n):
    numerator = comb((p + 1) * n, n)
    denominator = p * n + 1
    assert numerator % denominator == 0
    return numerator // denominator


def digit_condition(p, n):
    previous = None
    while n:
        n, digit = divmod(n, p)
        if previous is not None and previous + digit >= p:
            return False
        previous = digit
    return True


def count_matrix(p, r):
    if r == 0:
        return 1
    values = [1] * p
    for _ in range(r - 1):
        values = [sum(values[j] for j in range(p - i)) for i in range(p)]
    return sum(values)


def count_spectral(p, r):
    assert r >= 1
    total = 0.0
    for j in range(p):
        half_angle = (2 * j + 1) * pi / (4 * p + 2)
        eig = (-1) ** j / (2 * sin(half_angle))
        coeff = (cos(half_angle) / sin(half_angle)) ** 2 / (2 * p + 1)
        total += coeff * eig ** (r - 1)
    return total


cases = {2: 10, 3: 6, 5: 4, 7: 3, 11: 2}
checked = 0
for p, max_r in cases.items():
    assert count_matrix(p, 1) == p
    for r in range(1, max_r + 1):
        m = p ** r
        count = 0
        for n in range(m):
            via_digits = digit_condition(p, n)
            via_fuss = (fuss(p, n) % p != 0)
            assert via_digits == via_fuss, (p, r, n)
            checked += 1
            count += via_fuss
        assert count == count_matrix(p, r), (p, r, count)
        approx = count_spectral(p, r)
        assert isclose(approx, count, rel_tol=1e-9, abs_tol=1e-6), (p, r, approx, count)
    for j in range(p):
        half_angle = (2*j + 1)*pi/(4*p+2)
        theta = 2*half_angle
        eigenvalue = (-1)**j/(2*sin(half_angle))
        vector = [cos((i+0.5)*theta) for i in range(p)]
        assert isclose(sum(z*z for z in vector), (2*p+1)/4, rel_tol=1e-9)
        for i in range(p):
            lhs = sum(vector[t] for t in range(p-i))
            assert isclose(lhs, eigenvalue*vector[i], rel_tol=1e-9, abs_tol=1e-9)
    rho = 1.0 / (2 * sin(pi / (4 * p + 2)))
    assert 1 < rho < p
    assert 0 < log(rho) / log(p) < 1
print('VERIFY_OK primes=' + ','.join(map(str, cases)))
print('index_checks=' + str(checked))
print('block_count_p2_r10=' + str(count_matrix(2, 10)))
print('block_count_p3_r6=' + str(count_matrix(3, 6)))
print('block_count_p5_r4=' + str(count_matrix(5, 4)))
print('digit_criterion=PASS matrix_count=PASS spectral_count=PASS eigenpairs=PASS dimension_bounds=PASS')
