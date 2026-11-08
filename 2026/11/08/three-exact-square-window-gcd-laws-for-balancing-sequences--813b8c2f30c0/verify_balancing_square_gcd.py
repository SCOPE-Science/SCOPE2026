#!/usr/bin/env python3
"""Exact integer regression checks for three balancing-family square-window GCD formulas."""
from math import gcd

MAX_K = 260
N_STARTS = 48
N = 2*MAX_K + N_STARTS + 10
B = [0, 1]
C = [1, 3]
c = [-1, 1]
for n in range(2, N + 1):
    B.append(6*B[-1] - B[-2])
    C.append(6*C[-1] - C[-2])
    c.append(6*c[-1] - c[-2])

def v_p(x, p):
    assert x != 0
    t = 0
    while x % p == 0:
        x //= p
        t += 1
    return t

for k in range(1, MAX_K + 1):
    targets = (("balancing", B, (gcd(k, B[k]) if k%2 else gcd(k, B[k])//2)),
               ("Lucas-balancing", C, gcd(k, B[k])),
               ("Lucas-cobalancing", c, gcd(k, 3*B[k]) if k%2 else gcd(k, B[k])))
    for title, seq, expected in targets:
        value = 0
        current = sum(seq[i]**2 for i in range(1, k + 1))
        for n in range(N_STARTS):
            value = gcd(value, current)
            current += seq[n+k+1]**2 - seq[n+1]**2
        assert value == expected, (title, k, value, expected)
    assert B[2*k] == 2*B[k]*C[k]
    assert B[2*k+1] == 2*B[k]*C[k+1] + 1
    assert C[k]*C[k] - 8*B[k]*B[k] == 1
    assert B[k] % 2 == k % 2
    assert C[k] % 16 == (3 if k%2 else 1)
    if k % 2 == 0:
        assert v_p(B[k],2) == v_p(k,2)
        assert v_p(B[k]*C[k+1]-k,2) == v_p(k,2)+3
        assert v_p(B[k]*C[k]-k,2) == v_p(k,2)+1
        assert v_p(B[k],3) >= v_p(k,3)+1

print(f'VERIFY_OK k=1..{MAX_K} starts=0..{N_STARTS-1} exact_window_gcd_cases={MAX_K*3*N_STARTS} recurrence_identities={MAX_K} dyadic_and_ternary_checks=PASS')
