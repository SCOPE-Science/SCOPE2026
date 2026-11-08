#!/usr/bin/env python3
"""Three exact finite checks of the 16-regular parity support theorem."""
from math import isqrt, pi, log

N = 5000
# Dynamic programming in the partition definition, not using eta identities.
b = bytearray(N + 1)
b[0] = 1
for part in range(1, N + 1):
    if part % 16:
        for n in range(part, N + 1):
            b[n] ^= b[n - part]

# Direct Jacobi triangular-pair theta coefficient computation.
theta = bytearray(N + 1)
for i in range(isqrt(2 * N) + 2):
    t = i * (i + 1) // 2
    if t > N:
        break
    for j in range(isqrt(N // 2) + 2):
        s = t + 2 * j * (j + 1)
        if s > N:
            break
        theta[s] ^= 1

# Prime sieve and factor-exponent characterization, independent from b and theta.
M = 8 * N + 5
spf = list(range(M + 1))
for p in range(2, isqrt(M) + 1):
    if spf[p] == p:
        for q in range(p * p, M + 1, p):
            if spf[q] == q:
                spf[q] = p

def criterion(n):
    m = 8 * n + 5
    seen = 0
    while m > 1:
        p = spf[m]
        e = 0
        while m % p == 0:
            m //= p
            e += 1
        if e & 1:
            if p % 8 != 5 or e % 4 != 1:
                return 0
            seen += 1
    return int(seen == 1)

for n in range(N + 1):
    if b[n] != theta[n] or b[n] != criterion(n):
        raise AssertionError(('mismatch', n, b[n], theta[n], criterion(n)))

# Direct signed ordered two-squares formula for 0 <= n <= 400.
for n in range(401):
    m = 8 * n + 5
    r = 0
    for x in range(-isqrt(m), isqrt(m) + 1):
        yy = m - x * x
        y = isqrt(yy)
        if y * y == yy:
            r += 1 if y == 0 else 2
    pairs = sum(1 for i in range(isqrt(2 * n) + 2) for j in range(isqrt(n // 2) + 2) if i * (i + 1) // 2 + 2 * j * (j + 1) == n)
    assert r == 8 * pairs, (n, r, pairs)

print('PASS: exact 16-regular parity, triangular-pair parity and prime-exponent test agree for n=0..5000 (5001 indices).')
print('PASS: signed ordered two-square count equals eight times triangular-pair count for n=0..400 (401 indices).')
for x in (100, 500, 1000, 2000, 5000):
    actual = sum(b[:x+1])
    pred = (pi*pi/4)*x/log(x)
    print(f'N({x})={actual}; first-order benchmark={pred:.5f}; ratio={actual/pred:.6f}')
