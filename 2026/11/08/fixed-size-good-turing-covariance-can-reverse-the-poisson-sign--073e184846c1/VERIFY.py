#!/usr/bin/env python3
"""Exact finite-sample checks for Good--Turing/missing-mass covariance laws."""
from fractions import Fraction as F
from itertools import product
from math import comb, exp


def covariance_formula(probabilities, n):
    """Finite-alphabet occupancy-indicator formula, exact over rational masses."""
    m = len(probabilities)
    em = sum((p * (1 - p) ** n for p in probabilities), F(0))
    eg = sum((p * (1 - p) ** (n - 1) for p in probabilities), F(0))
    emg = sum((probabilities[i] * probabilities[j]
               * (1 - probabilities[i] - probabilities[j]) ** (n - 1)
               for i in range(m) for j in range(m) if i != j), F(0))
    return emg - em * eg


def brute_force(probabilities, n):
    """Independent expectation evaluation over every ordered sample word."""
    em = eg = emg = F(0)
    for sample in product(range(len(probabilities)), repeat=n):
        counts = [sample.count(i) for i in range(len(probabilities))]
        weight = F(1)
        for i in sample:
            weight *= probabilities[i]
        missing = sum((probabilities[i] for i, count in enumerate(counts)
                       if count == 0), F(0))
        singleton = F(sum(count == 1 for count in counts), n)
        em += weight * missing
        eg += weight * singleton
        emg += weight * missing * singleton
    return emg - em * eg


def uniform_formula(n, m):
    a = F(m - 1, m)
    b = F(m - 2, m)
    return F(m - 1, m) * (b ** (n - 1) - a ** (2 * n - 2))


def core_tail_formula(n, q, m):
    """Aggregate the diagonal, core--rare, and rare--rare contributions."""
    r = (1 - q) / m
    em = q * (1 - q) ** n + m * r * (1 - r) ** n
    eg = q * (1 - q) ** (n - 1) + m * r * (1 - r) ** (n - 1)
    emg = 2 * m * q * r * (1 - q - r) ** (n - 1)
    emg += m * (m - 1) * r ** 2 * (1 - 2 * r) ** (n - 1)
    return emg - em * eg


def limit_formula(n, q):
    return q ** 2 * (1 - q) ** n * (1 - (1 - q) ** (n - 1))


def run():
    checks = 0
    for n in range(2, 6):
        for alphabet in range(2, 6):
            weights = [1 + (13 * i + 7 * alphabet) % 5 for i in range(alphabet)]
            ps = [F(w, sum(weights)) for w in weights]
            assert covariance_formula(ps, n) == brute_force(ps, n)
            checks += 1
    for n in range(2, 7):
        for m in range(2, 11):
            ps = [F(1, m)] * m
            assert covariance_formula(ps, n) == uniform_formula(n, m)
            assert uniform_formula(n, m) < 0
            checks += 2
    q = F(1, 2)
    m = 10
    ps = [q] + [(1 - q) / m] * m
    assert covariance_formula(ps, 3) == F(5801, 12800000)
    assert brute_force(ps, 3) == F(5801, 12800000)
    assert core_tail_formula(3, q, m) == F(5801, 12800000)
    checks += 3
    for n in range(2, 11):
        limit = limit_formula(n, q)
        assert limit > 0
        errors = [abs(core_tail_formula(n, q, m) - limit)
                  for m in (20, 100, 500)]
        assert errors[2] < errors[1] < errors[0]
        checks += 2
    for n in range(2, 8):
        for q in (F(1, 3), F(1, 2), F(2, 3)):
            c = limit_formula(n, q)
            assert c > 0
            bound_constant = 2 * n * (1 - q) + n * (n - 1) * (1 - q) ** 2
            sufficient_m = int(bound_constant / c) + 1
            assert core_tail_formula(n, q, sufficient_m) > 0
            checks += 2
    for t in (F(1, 2), F(3, 1), F(10, 1)):
        ps = [F(1, 2), F(1, 4), F(1, 4)]
        poisson_covariance = -sum(float(p * p) * exp(-2 * float(t * p))
                                  for p in ps)
        assert poisson_covariance < 0
        checks += 1
    print(f"PASS {checks} assertions; exact n=3 core+10 rare covariance = 5801/12800000")

if __name__ == '__main__':
    run()
