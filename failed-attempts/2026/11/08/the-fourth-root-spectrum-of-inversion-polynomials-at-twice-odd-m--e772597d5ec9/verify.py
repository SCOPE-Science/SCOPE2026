#!/usr/bin/env python3
"""Independent direct enumeration of a fourth-root inversion-number identity."""
from math import gcd, isqrt

def inversion(a, n):
    perm = [(a*j) % n for j in range(n)]
    return sum(perm[j] > perm[k] for j in range(n) for k in range(j+1, n))

def jacobi(a, n):
    assert n > 0 and n % 2
    a %= n
    sign = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                sign = -sign
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            sign = -sign
        a %= n
    return sign if n == 1 else 0

count = 0
for q in range(3, 140, 2):
    evaluation = 0
    for a in range(1, 2*q, 2):
        if gcd(a, q) != 1:
            continue
        lhs = inversion(a, 2*q)
        rhs = inversion(a % q, q)
        assert (lhs - 2*rhs) % 4 == 0, (q, a, lhs, rhs)
        assert (-1)**(lhs//2) == jacobi(a, q), (q, a, lhs)
        evaluation += (-1)**(lhs//2)
        count += 1
    expected = sum(gcd(a, q) == 1 for a in range(1, q)) if isqrt(q)**2 == q else 0
    assert evaluation == expected, (q, evaluation, expected)
assert count == 3994
print('VERIFY_OK odd_moduli=69 multipliers=3994 mod4=PASS Jacobi=PASS fourth_root=PASS')
