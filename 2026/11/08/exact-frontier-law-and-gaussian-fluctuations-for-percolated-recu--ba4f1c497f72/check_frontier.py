#!/usr/bin/env python3
"""Exact finite-state checks for the root-component frontier theorem.

No external dependencies are required for exact tests. Optional NumPy is used
only for the explicitly non-probative Monte Carlo diagnostic.
"""
from fractions import Fraction
from math import comb
from itertools import product


def joint_law(n, p):
    assert 1 <= n and 0 < p < 1
    q = 1 - p
    law = {(1, 0): Fraction(1)}
    for j in range(1, n):
        nxt = {}
        for (c, b), mass in law.items():
            for key, t in [((c, b), 1 - Fraction(c, j)),
                           ((c + 1, b), p * Fraction(c, j)),
                           ((c, b + 1), q * Fraction(c, j))]:
                nxt[key] = nxt.get(key, Fraction(0)) + mass * t
        law = {k: v for k, v in nxt.items() if v}
    return law


def enumerate_original_trees(n, p):
    """Independent brute-force check using all recursive-tree parents and edge marks."""
    q = 1 - p
    law = {}
    for parents in product(*(range(i) for i in range(1, n))):
        for marks in product((0, 1), repeat=n - 1):
            root_member = [True] + [False] * (n - 1)
            c, b = 1, 0
            for i, (father, open_edge) in enumerate(zip(parents, marks), 1):
                if root_member[father]:
                    if open_edge:
                        root_member[i] = True
                        c += 1
                    else:
                        b += 1
            weight = Fraction(1)
            for i, edge in enumerate(marks, 1):
                weight *= (p if edge else q) / i
            law[(c, b)] = law.get((c, b), Fraction()) + weight
    return {key: x for key, x in law.items() if x}


def binomial_power_coeff(exponent, degree):
    """Taylor coefficients of (1-z)**exponent, rational exact."""
    c = [Fraction(1)]
    for k in range(1, degree + 1):
        c.append(c[-1] * (k - 1 - exponent) / k)
    return c


def pgf_coeff(degree, p, u, v):
    """Independent coefficient extraction from the theorem's closed OGF."""
    q = 1 - p
    r = 1 - q*v
    a = binomial_power_coeff(r-1, degree)
    h = binomial_power_coeff(r, degree)
    num = [r*u*x for x in a]
    den = [p*u*x for x in h]
    den[0] += r - p*u
    out = []
    for k in range(degree+1):
        out.append((num[k] - sum(den[i]*out[k-i] for i in range(1,k+1)))/den[0])
    return out


def exact_checks():
    count = 0
    for p in map(Fraction, ['1/5', '2/5', '1/2', '2/3', '4/5']):
        q = 1 - p
        expected_c = Fraction(1)
        for n in range(1, 23):
            if n > 1:
                expected_c *= 1 + p / (n - 1)
            law = joint_law(n, p)
            total = sum(law.values(), Fraction())
            assert total == 1
            count += 1
            expected_c_law = sum(c * v for (c, b), v in law.items())
            assert expected_c_law == expected_c
            count += 1
            eb = sum(b * v for (c, b), v in law.items())
            assert eb == q / p * (expected_c - 1)
            count += 1
            ez = sum((Fraction(b) - q / p * (c - 1)) * v for (c, b), v in law.items())
            assert ez == 0
            count += 1
            ez2 = sum((Fraction(b) - q / p * (c - 1)) ** 2 * v for (c, b), v in law.items())
            assert ez2 == q / p**2 * (expected_c - 1)
            count += 1
            if n <= 6:
                assert law == enumerate_original_trees(n, p)
                count += 1
    # Exact OGF coefficient comparisons, algebraically independent of the DP.
    for p in map(Fraction, ['1/5', '1/2', '3/4']):
        for u,v in [(Fraction(1,3), Fraction(2,5)),
                    (Fraction(3,5), Fraction(4,7)),
                    (Fraction(1), Fraction(1)),
                    (Fraction(1), Fraction(0))]:
            coeff = pgf_coeff(12, p, u, v)
            for n in range(1,14):
                law = joint_law(n,p)
                expect = sum(mass*u**c*v**b for (c,b),mass in law.items())
                assert coeff[n-1] == expect
                count += 1
    # Exact hitting-law enumeration on the event-mark subsequence. For k-1
    # successes, the last mark is 1; earlier positions have k-2 ones and b zeros.
    for p in map(Fraction, ['1/4', '1/2', '3/4']):
        q = 1-p
        for k in range(2, 9):
            for b in range(0, 7):
                count1 = Fraction(0)
                for v in product((0, 1), repeat=k+b-2):
                    if sum(v) == k-2:
                        count1 += p ** (k-1) * q ** b
                assert count1 == comb(k+b-2, b) * p**(k-1) * q**b
                count += 1
    return count


def numeric_diagnostic(reps=1800, n=60000, p=0.8):
    """Non-proof simulation: reports mean and second moment, not used in proof."""
    import numpy as np
    rng = np.random.default_rng(20261101)
    c = np.ones(reps, dtype=np.int64)
    b = np.zeros(reps, dtype=np.int64)
    for j in range(1, n):
        parent_is_in_cluster = rng.random(reps) < c / j
        accepted = parent_is_in_cluster & (rng.random(reps) < p)
        c += accepted
        b += parent_is_in_cluster & ~accepted
    z = (b - (1-p)/p * (c-1))/np.sqrt(c)
    return float(z.mean()), float(np.mean(z*z)), float((1-p)/p**2)

if __name__ == '__main__':
    n = exact_checks()
    print(f'PASS: {n} independent exact finite tests')
    try:
        print('Monte Carlo diagnostic: (mean, second moment, target)=', numeric_diagnostic())
    except ImportError:
        print('No NumPy: skipped optional diagnostic')
