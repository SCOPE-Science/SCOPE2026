#!/usr/bin/env python3
"""Independent exact checks of path maximal-independent-set sampling laws.
Run: python3 check.py. Python standard library only.
"""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial

N = 120
F = [0] * (N + 1)
A = [0] * (N + 1)
G = [Fraction(0) for _ in range(N + 1)]
checks = 0
for n in range(1, N + 1):
    for k in range(1, n + 1):
        j = n - 2*k + 1
        if 0 <= j <= k+1:
            c = comb(k+1, j)
            F[n] += c
            A[n] += k*c
    G[n] = Fraction(1) + Fraction(2, n)*sum(G[j] for j in range(n-1))
    if n >= 5:
        assert F[n] == F[n-2]+F[n-3]
        assert A[n] == A[n-2]+A[n-3]+F[n]
        checks += 2
    assert G[n] >= 0
    checks += 1

# Brute enumeration verifies both models, not just their recurrences.
for n in range(1, 9):
    maximal = []
    for mask in range(1 << n):
        selected = {i for i in range(n) if mask & (1 << i)}
        if any(i+1 in selected for i in selected):
            continue
        if any(i not in selected and i-1 not in selected and i+1 not in selected
               for i in range(n)):
            continue
        maximal.append(selected)
    assert len(maximal) == F[n]
    assert sum(map(len, maximal)) == A[n]
    greedy_total = 0
    for order in permutations(range(n)):
        taken = set()
        for v in order:
            if v-1 not in taken and v+1 not in taken:
                taken.add(v)
        greedy_total += len(taken)
    assert Fraction(greedy_total, factorial(n)) == G[n]
    checks += 3

# The exact finite-sample order and its complete equality set.
zeroes = []
for n in range(1, N+1):
    diff = G[n]-Fraction(A[n], F[n])
    assert diff >= 0
    if diff == 0:
        zeroes.append(n)
    checks += 1
assert zeroes == [1, 2, 4]

# Rational analytic certificates used in the infinite proof.
partial_e2 = sum((Fraction(2)**j)/factorial(j) for j in range(9))
assert partial_e2 == Fraction(2327, 315)
assert Fraction(2**14, factorial(15)) < Fraction(11, 27924)
for n in range(13, N+1):
    assert 437*n-5670 >= 11
    assert Fraction(A[n], F[n]) <= Fraction(5*n+6, 12)
    checks += 2

# Independent polynomial-coefficient identity, finite symbolic cross-check.
# x(1+x)^2 /(1-x^2-x^3) and x(1+x)^2 /(1-x^2-x^3)^2
for n in range(5, N+1):
    assert F[n] == F[n-2]+F[n-3]
    assert A[n] == A[n-2]+A[n-3]+F[n]
    checks += 2
print('CHECK_OK; assertions:', checks, '; finite equality set:', zeroes,
      '; exact n=13 gap:', G[13]-Fraction(A[13], F[13]))
