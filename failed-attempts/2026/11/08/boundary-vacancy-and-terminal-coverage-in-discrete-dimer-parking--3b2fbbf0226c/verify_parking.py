#!/usr/bin/env python3
"""Exact finite verification of boundary--bulk moments for sequential dimer parking."""
from fractions import Fraction
from itertools import permutations
from math import factorial


def truncated_exp(c, m):
    if m < 0:
        return Fraction(0)
    return sum((Fraction((-c) ** j, factorial(j)) for j in range(m + 1)), Fraction(0))


def formula(n):
    assert n >= 2
    e = truncated_exp(1, n - 1)
    a = n * (1 - truncated_exp(2, n - 1)) - 2 * truncated_exp(2, n - 2)
    b = (Fraction(n) - Fraction(1, 2)) * (
        truncated_exp(1, n - 1) - truncated_exp(3, n - 1)
    ) - 3 * truncated_exp(3, n - 2)
    return e, a, b


def recurrence(max_n):
    a = [Fraction(0) for _ in range(max_n + 1)]
    e = [Fraction(0) for _ in range(max_n + 1)]
    b = [Fraction(0) for _ in range(max_n + 1)]
    e[1] = Fraction(1)
    for n in range(2, max_n + 1):
        a[n] = 2 + Fraction(2, n - 1) * sum(a[:n-1])
        e[n] = Fraction(1, n - 1) * sum(e[1:n-1])
        b[n] = Fraction(1, n - 1) * sum(
            b[j] + e[j] * (2 + a[n-j-2]) for j in range(1, n-1)
        )
    return a, e, b


def enumerate_edge_orders(n):
    """Each of the (n-1)! edge-priority orders is equiprobable."""
    count = 0
    total_e = total_a = total_b = 0
    for order in permutations(range(n-1)):
        taken = [False] * n
        for j in order:
            if not taken[j] and not taken[j+1]:
                taken[j] = taken[j+1] = True
        vacancy = int(not taken[0])
        occupied = sum(taken)
        count += 1
        total_e += vacancy
        total_a += occupied
        total_b += vacancy * occupied
    return Fraction(total_e, count), Fraction(total_a, count), Fraction(total_b, count)


def bound(n):
    return Fraction((2*n-1)*(1+3**n), 2*factorial(n)) + Fraction(
        3*n*3**(n-1) + n + 2*n*2**n, factorial(n)
    )


def main():
    checks = 0
    a, e, b = recurrence(100)
    for n in range(2, 101):
        triple = formula(n)
        for x, y in zip(triple, (e[n], a[n], b[n])):
            assert x == y, (n, x, y)
            checks += 1
        assert 0 <= e[n] <= 1 and 0 <= a[n] <= n
        checks += 1
    for n in range(2, 10):
        from_enumeration = enumerate_edge_orders(n)
        for x, y in zip(from_enumeration, formula(n)):
            assert x == y, (n, x, y)
            checks += 1
    zeros = {2,3,5}
    for n in range(2, 101):
        cov = b[n] - e[n] * a[n]
        assert (cov == 0) if n in zeros else (cov < 0)
        checks += 1
    assert b[4] - e[4] * a[4] == Fraction(-4,9)
    assert b[6] - e[6] * a[6] == Fraction(-77,225)
    assert bound(11) < Fraction(1,6)
    assert bound(12) < bound(11)
    checks += 4
    print(f'PASS: {checks} exact assertions; exhaustive edge orders n=2,...,9; recurrences n<=100')
    print(f'R_11={bound(11)} < 1/6; infinite negativity follows by termwise monotonicity')
    print(f'Cov_n at n=6: {b[6] - e[6]*a[6]}, n=10: {b[10] - e[10]*a[10]}')


if __name__ == '__main__':
    main()
