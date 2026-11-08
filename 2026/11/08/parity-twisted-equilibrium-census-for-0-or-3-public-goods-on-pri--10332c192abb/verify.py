#!/usr/bin/env python3
"""Exact finite checks for the 0-or-3 response game on circular ladders."""
from fractions import Fraction
from math import comb
from itertools import product

# Column bit 0 is the upper agent, bit 1 the lower agent.

def best_response_local(column_prev, column, column_next, layer):
    other_layer = 1 - layer
    active_neighbors = ((column_prev >> layer) & 1) + ((column_next >> layer) & 1) + ((column >> other_layer) & 1)
    return int(active_neighbors in (0, 3))


def is_equilibrium(columns):
    n = len(columns)
    return all(((columns[i] >> layer) & 1) == best_response_local(columns[(i - 1) % n], columns[i], columns[(i + 1) % n], layer)
               for i in range(n) for layer in (0, 1))


def brute_count(n):
    return sum(is_equilibrium(word) for word in product(range(4), repeat=n))


def circular_formula(n):
    total = Fraction(1)
    for q in range(0, n // 2 + 1, 2):
        rem = n - 2 * q
        if rem < 0 or rem % 3:
            continue
        r = rem // 3
        k = q + r
        if k > 0:
            total += Fraction(2 * n * comb(k, q), k)
    assert total.denominator == 1
    return int(total)


def build_six_state_transfer():
    # Single-rung symbols: 0 = (0,0), 1 = (1,0), 2 = (0,1).
    states = [(a, b) for a in range(3) for b in range(3) if a != b]
    def pair_to_column(p):
        return (0, 1, 2)[p]
    A = [[0] * 6 for _ in range(6)]
    for i, (a, b) in enumerate(states):
        for j, (bb, c) in enumerate(states):
            if b == bb and all(((pair_to_column(b) >> layer) & 1) == best_response_local(pair_to_column(a), pair_to_column(b), pair_to_column(c), layer) for layer in (0, 1)):
                A[i][j] = 1
    return states, A


def mul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def main():
    states, B = build_six_state_transfer()
    B2 = mul(B, B)
    B3 = mul(B2, B)
    B6 = mul(B3, B3)
    I = identity(6)
    assert all(B6[i][j] - 2 * B3[i][j] - B2[i][j] + I[i][j] == 0 for i in range(6) for j in range(6))
    # Exact trace agreement for long cycles, with no floating-point arithmetic.
    P = I
    for n in range(1, 101):
        P = mul(P, B)
        assert circular_formula(n) == 1 + trace(P), (n, circular_formula(n), 1+trace(P))
    # Direct evaluation of all 4^n independent labeled action profiles.
    checks = 0
    for n in range(3, 10):
        observed = brute_count(n)
        expected = circular_formula(n)
        assert observed == expected, (n, observed, expected)
        checks += 4 ** n
        print(f"n={n}: exact count={observed}, direct states={4**n}")
    # The exceptional one-equilibrium prism has exactly five rungs.
    assert [n for n in range(3, 101) if circular_formula(n) == 1] == [5]
    print(f"VERIFY_OK direct_profiles={checks} trace_comparisons=100 matrix_identity=6x6")


if __name__ == '__main__':
    main()
