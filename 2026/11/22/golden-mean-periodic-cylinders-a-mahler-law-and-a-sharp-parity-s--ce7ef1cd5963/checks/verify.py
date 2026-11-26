#!/usr/bin/env python3
"""Finite and high-precision checks of golden-mean unbordered counts.

This script checks finite instances only; the infinite statement follows from
shortest-border decomposition and meromorphic continuation in RESULT.md.
Python 3 standard library, no input files or network needed.
"""
from decimal import Decimal, getcontext
from itertools import product

LIMIT = 220
F = [0, 1]
for _ in range(2, LIMIT + 3):
    F.append(F[-1] + F[-2])
T = [0] * (LIMIT + 1)
for n in range(2, LIMIT + 1):
    T[n] = F[n - 1] - sum(T[k] * F[n - 2*k+1] for k in range(2, n//2+1))
    assert T[n] > 0

# Explicit independent enumeration of all admissible 2- through 15-bit words.
for n in range(2, 16):
    admissible = [bits for bits in product((0, 1), repeat=n)
                  if all(not (bits[i] and bits[i+1]) for i in range(n-1))]
    unbordered = 0
    for bits in admissible:
        least_period = next(p for p in range(1, n+1)
                            if all(bits[i] == bits[i+p] for i in range(n-p)))
        no_proper_border = not any(bits[:k] == bits[-k:] for k in range(1, n))
        assert (least_period == n) == no_proper_border
        if no_proper_border:
            assert bits[0] != bits[-1]
            assert not (bits[-1] and bits[0])
            unbordered += 1
    assert len(admissible) == F[n+2], (n, len(admissible), F[n+2])
    assert unbordered == 2*T[n], (n, unbordered, T[n])

# Check the coefficient form of (1-z-z^2)T(z)+T(z^2)=z^2.
for n in range(2, LIMIT+1):
    lhs = T[n] - T[n-1] - T[n-2] + (T[n//2] if n % 2 == 0 else 0)
    assert lhs == (1 if n == 2 else 0), (n, lhs)

getcontext().prec = 110
phi = (Decimal(1) + Decimal(5).sqrt()) / 2
q = 1/phi
s = q.sqrt()
series_at_q2 = sum(Decimal(T[n]) * (q*q)**n for n in range(2, LIMIT+1))
# Infinite tail bound: T[n] <= F[n-1] <= phi^(n-1), so
# sum_{n>LIMIT} T[n]*q^(2n) <= q^(LIMIT+2)/(1-q).
tail_bound = q**(LIMIT+2)/(1-q)
a = (q*q-series_at_q2)/(1+q*q)
p = 2*Decimal(5).sqrt()*q*q*a
k_even = p*q/(1-q**3)
k_odd = p/(s*(1-q**3))
assert 0 < a < 1 and 0 < p < 1 and 0 < k_even < k_odd
assert tail_bound < Decimal('1e-40')
# A high-n sanity test; not a substitute for the pole proof.
for n in (160, 180, 181, 201, 219):
    pn = 2*Decimal(T[n])/Decimal(F[n+2])
    scaled = (pn-p)*phi**(Decimal(n)/2)
    target = k_even if n % 2 == 0 else k_odd
    assert abs(scaled-target) < Decimal('1e-6'), (n, scaled, target)
print('PASS: complete admissible-word enumeration lengths 2..15')
print(f'PASS: {LIMIT-1} exact shortest-border/Mahler coefficient identities')
print('PASS: high-precision parity-correction asymptotic sanity tests')
print('t[2:17]=', T[2:17])
print('p_star =', p)
print('K_even =', k_even)
print('K_odd =', k_odd)
print('tail_bound_T_q2 =', tail_bound)
