#!/usr/bin/env python3
"""Exact finite checks for binary-digit-parity ordered representations.

Uses only Python standard-library integers. These tests do not establish
asymptotic estimates or monotonicity beyond the finite checked window.
"""
from math import comb, log


def multiply(a, b, degree):
    out = [0] * (degree + 1)
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b[:degree + 1 - i]):
            if y:
                out[i + j] += x * y
    return out


def counts(indicator, degree, k):
    v = [1] + [0] * degree
    for _ in range(k):
        v = multiply(v, indicator, degree)
    return v


def coefficient_with_factor(power, exponent, degree):
    """Return coefficients (1-z)^exponent * power, truncated."""
    if exponent >= 0:
        factor = [(-1)**j * comb(exponent, j)
                  for j in range(min(degree, exponent) + 1)]
    else:
        h = -exponent
        factor = [comb(h + j - 1, j) for j in range(degree + 1)]
    return multiply(power, factor, degree)


def run():
    degree = 320
    tau = [1 if j.bit_count() % 2 == 0 else -1 for j in range(degree + 1)]
    evil = [(1 + t) // 2 for t in tau]
    odious = [(1 - t) // 2 for t in tau]
    raw_sides = {}
    total_coefficients = 0
    total_bad = 0
    for k in (7, 8, 9, 10):
        powers = [[1] + [0] * degree]
        for ell in range(1, k + 1):
            powers.append(multiply(powers[-1], tau, degree))
        term = [coefficient_with_factor(powers[ell], 1-k+ell, degree)
                for ell in range(k + 1)]
        for sign, indicator, label in ((1, evil, 'evil'), (-1, odious, 'odious')):
            c = counts(indicator, degree, k)
            d = [c[0]] + [c[n] - c[n-1] for n in range(1, degree+1)]
            for n in range(degree+1):
                rhs = sum((sign ** ell) * comb(k, ell) * term[ell][n]
                          for ell in range(k+1))
                assert rhs == (1 << k) * d[n], (k, label, n)
                total_coefficients += 1
            failures = [n for n in range(1, degree+1) if d[n] <= 0]
            total_bad += len(failures)
            raw_sides[(label, k)] = failures[-1] if failures else None
            assert all(d[n] > 0 for n in range(40, degree + 1))
    alpha = log(3) / log(4)
    assert alpha < 4 / 5
    assert min((k - 2) * (1 - alpha) - 1 for k in (7, 8, 9, 10)) > 0
    assert raw_sides[('evil', 7)] == 25
    assert raw_sides[('odious', 7)] == 6
    print('VERIFY_OK exact_coefficient_equalities=' + str(total_coefficients)
          + ' finite_window=' + str(degree)
          + ' last_nonincreases=' + repr(raw_sides)
          + ' total_nonincreases=' + str(total_bad))


if __name__ == '__main__':
    run()
