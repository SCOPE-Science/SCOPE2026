#!/usr/bin/env python3
"""Independent finite-size verification of an antiferromagnetic three-color wheel theorem.

Uses only the Python standard library. The exhaustive checks are finite tests;
the all-size mathematical conclusion rests on the accompanying proof.
"""
from fractions import Fraction
from itertools import product
from math import isclose, log, sqrt

def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    a, b = 2, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def predicted(n, x):
    assert n >= 5 and x > 0
    if x < 2:
        if n % 2 == 0:
            return -x * (n // 2), 4, n // 2
        return 1 - x * ((n + 1) // 2), 2 * n, (n + 1) // 2
    if x == 2:
        return Fraction(-n), 2 * lucas(n), None
    if x < n:
        return n * (1 - x), 2, n
    if x == n:
        return n * (1 - x), 3, None
    return 2 * n - x * (n + 1), 1, n + 1

def run():
    checked = 0
    total_configs = 0
    for n in range(5, 11):
        # A compact, exact sufficient-statistics histogram for the full 3^(n+1) configurations.
        counts = {}
        for state in product(range(3), repeat=n + 1):
            hub, rim = state[0], state[1:]
            u = sum(rim[i] == rim[(i+1) % n] for i in range(n))
            u += sum(color == hub for color in rim)
            k = sum(color == 0 for color in state)
            counts[u, k] = counts.get((u, k), 0) + 1
            total_configs += 1
        values = (Fraction(1, 10), Fraction(3, 4), Fraction(3, 2), Fraction(2),
                  Fraction(5, 2), Fraction(3), Fraction(n - 1, 1), Fraction(n),
                  Fraction(n + 1, 1))
        for x in values:
            energies = [(Fraction(u) - x * k, freq, k) for (u,k), freq in counts.items()]
            best = min(z[0] for z in energies)
            deg = sum(freq for e, freq, k in energies if e == best)
            k_values = {k for e, freq, k in energies if e == best}
            expected_energy, expected_deg, expected_k = predicted(n,x)
            assert best == expected_energy, (n, x, best, expected_energy)
            assert deg == expected_deg, (n, x, deg, expected_deg)
            if expected_k is not None:
                assert k_values == {expected_k}, (n,x,k_values,expected_k)
            if x == 2:
                assert k_values == set(range((n+1)//2,n+1))
            if x == n:
                assert k_values == {n,n+1}
            checked += 1
        print(f"n={n}: {3**(n+1)} states; nine exact field checks PASS")
    a = (1+sqrt(5))/2
    n = 100
    assert isclose(log(2 * lucas(n))/(n+1),log(a),abs_tol=0.01)
    print(f"PASS: {checked} exact field checks, {total_configs} configurations "
          f"and Lucas entropy asymptotic; not an all-size proof")

if __name__ == '__main__':
    run()
