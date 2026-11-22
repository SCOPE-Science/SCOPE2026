#!/usr/bin/env python3
"""Reproducible finite-state checks of paired-field Ising-trimer information.

All numerical checks are finite; the global and asymptotic theorems require
separate analytic arguments.
"""
from itertools import product
from math import exp, cosh, acosh, log, sqrt, isclose

A_CRIT = (23.0 + 4.0 * sqrt(55.0)) / 39.0

def fisher(x, y):
    data = []
    for spins in product((-1, 1), repeat=3):
        b = sum(spins[i] * spins[(i + 1) % 3] for i in range(3))
        m = sum(spins)
        data.append((b, m, x * b + y * m))
    shift = max(row[2] for row in data)
    raw = [exp(row[2] - shift) for row in data]
    norm = sum(raw)
    means = [sum(w * row[i] for w, row in zip(raw, data)) / norm for i in (0, 1)]
    bb = sum(w * (row[0] - means[0]) ** 2 for w, row in zip(raw, data)) / norm
    mm = sum(w * (row[1] - means[1]) ** 2 for w, row in zip(raw, data)) / norm
    bm = sum(w * (row[0] - means[0]) * (row[1] - means[1])
             for w, row in zip(raw, data)) / norm
    return bb, bm, mm

def information_formula(x, y):
    a, q = exp(4 * x), 2 * cosh(2 * y) - 1
    ixx = 48 * a * q / (a * q + 3) ** 2
    izz = 12 * (3 * a * a + a * q * q + 6 * a * q + 3 * a + 3) / ((q + 3) * (a * q + 3) ** 2)
    return ixx, izz

def polynomial(a, q):
    return (2 * a*a*q**4 + (21*a*a-6*a)*q**3 +
            (12*a**3+48*a*a-33*a)*q*q +
            (27*a**3+27*a*a-81*a)*q - 27*(a*a+a+1))

def optimal_q(a):
    if a >= A_CRIT:
        return 1.0
    lo, hi = 1.0, 2.0
    while polynomial(a, hi) <= 0:
        hi *= 2
    for _ in range(110):
        mid = (lo + hi) / 2
        if polynomial(a, mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

def det_from_formula(x, y):
    xx, zz = information_formula(x, y)
    return xx * zz

count = 0
for x in (-3.1, -1.8, -0.7, -0.15, 0, 0.09, 0.7):
    for y in (-3.2, -1.0, 0, 0.33, 1.3, 4.2):
        plus, cross, var = fisher(x, y)
        a, b = information_formula(x, y)
        assert isclose(plus, a, rel_tol=1e-10, abs_tol=1e-12)
        assert isclose(var, b, rel_tol=1e-10, abs_tol=1e-12)
        a0, q0 = exp(4*x), 2*cosh(2*y)-1
        assert isclose(cross, 48*a0*((exp(2*y)-exp(-2*y))/2)/(a0*q0+3)**2, rel_tol=1e-10, abs_tol=1e-12)
        opp = fisher(x, -y)
        assert isclose(opp[1], -cross, rel_tol=2e-10, abs_tol=1e-12)
        assert isclose((plus + opp[0]) * (var + opp[2]) / 4, det_from_formula(x, y), rel_tol=1e-10, abs_tol=1e-12)
        count += 1
for a in (0.001, 0.01, 0.1, 0.5, 0.99, 1.2, A_CRIT * 0.999):
    qopt = optimal_q(a)
    assert qopt > 1 and abs(polynomial(a, qopt)) < 1e-5 * max(1.0, qopt**4*a*a)
    yopt = 0.5 * acosh((qopt+1)/2)
    x = log(a)/4
    peak = det_from_formula(x, yopt)
    assert peak > det_from_formula(x, 0)
    for yy in (0, 0.1, 0.4, 1.0, 1.5, 3, 6):
        assert peak + 1e-11 >= det_from_formula(x, yy)
        count += 1
for a in (A_CRIT, A_CRIT*1.0001, 1.5, 3, 25):
    assert optimal_q(a) == 1.0
    x = log(a)/4
    for yy in (0.1, 0.5, 1.5, 4):
        assert det_from_formula(x, yy) < det_from_formula(x, 0)
        count += 1
for a in (1e-4, 1e-6, 1e-8):
    qopt = optimal_q(a)
    assert abs(a*qopt-3) < 0.04
    yopt = 0.5*acosh((qopt+1)/2)
    x = log(a)/4
    assert abs(det_from_formula(x, yopt) - 4) < 0.04
    assert abs(yopt+2*x-log(3)/2) < 0.04
    count += 1
print(f'PASS {count} independent finite-state and numerical consistency cases; critical a={A_CRIT:.15g}')
