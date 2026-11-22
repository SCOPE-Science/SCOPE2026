#!/usr/bin/env python3
"""Exact finite corroboration of seven-adic derangement residue fibres.

Run with the Python 3 standard library: python3 verify.py
"""
from collections import Counter
from math import factorial

P = 7
F_MOD = (1, 0, 1, 5, 2, 5, 6)
FP_MOD = (1, 5, 4, 1, 5, 1, 3)
EXPECTED = (2, 3, 3, 0, 0, 3, 3)
checks = 0


def falling(x, j):
    prod = 1
    for t in range(j):
        prod *= x - t
    return prod


def falling_derivative(x, j):
    result = 0
    for deleted in range(j):
        term = 1
        for t in range(j):
            if t != deleted:
                term *= x - t
        result += term
    return result


# Independent finite falling-factorial polynomial evaluations of local values.
for a in range(P):
    val = sum((-1)**j * falling(a, j) for j in range(P)) % P
    derivative = sum((-1)**j * falling_derivative(a, j) for j in range(2*P)) % P
    assert val == F_MOD[a], (a, val, 'value')
    assert derivative == FP_MOD[a], (a, derivative, 'derivative')
    assert derivative != 0
    checks += 3

# Independent recurrence produces every term in an entire period.
for k in range(1, 6):
    modulus = P**k
    period = 2*modulus
    observed = Counter()
    prev = 1
    for n in range(period):
        if n == 0:
            value = 1
        else:
            value = (n*prev + (-1)**n) % modulus
        prev = value
        observed[value] += 1
    assert sum(observed.values()) == period
    checks += 1
    for r in range(modulus):
        assert observed[r] == EXPECTED[r % P], (k, r, observed[r])
        checks += 1
    assert len(observed) == 5 * P**(k-1)
    checks += 1

# Independently test index-period reduction for the first four prime-power levels.
for k in range(1, 5):
    modulus = P**k
    period = 2*modulus
    vals = [0]*period
    vals[0] = 1
    for n in range(1, period):
        vals[n] = (n*vals[n-1] + (-1)**n) % modulus
    for divisor in range(1, period):
        if period % divisor == 0:
            assert any(vals[i] != vals[(i+divisor)%period] for i in range(period)), (k, divisor)
            checks += 1

# Small-prime base-level image comparison, not a claim of higher-level coverage.
for q in (2, 3, 5):
    values = []
    v = 1
    for n in range(2*q):
        if n:
            v = (n*v + (-1)**n) % q
        values.append(v)
    assert set(values) == set(range(q)), (q, values)
    checks += 1

print(f'VERIFY_OK exact_assertions={checks} exponents=1..5 max_modulus=16807 local_table=7')
