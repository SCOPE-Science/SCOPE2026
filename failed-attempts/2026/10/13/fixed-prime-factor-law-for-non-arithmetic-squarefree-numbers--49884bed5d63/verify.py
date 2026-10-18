#!/usr/bin/env python3
from math import isqrt, log, factorial

LIMIT = 2_000_000

# Smallest-prime-factor sieve.
spf = list(range(LIMIT + 1))
if LIMIT >= 1:
    spf[1] = 1
for p in range(2, isqrt(LIMIT) + 1):
    if spf[p] == p:
        for m in range(p*p, LIMIT + 1, p):
            if spf[m] == m:
                spf[m] = p

def factor(n):
    out = []
    while n > 1:
        p = spf[n]
        a = 0
        while n % p == 0:
            n //= p
            a += 1
        out.append((p, a))
    return out

def is_arithmetic_from_factorization(f):
    sigma = 1
    tau = 1
    for p, a in f:
        sigma *= (p**(a+1) - 1) // (p - 1)
        tau *= a + 1
    return sigma % tau == 0

counts = {r: 0 for r in range(2, 6)}
layers = {r: 0 for r in range(2, 6)}
checked_squarefree = 0

for n in range(2, LIMIT + 1):
    f = factor(n)
    squarefree = all(a == 1 for _, a in f)
    if not squarefree:
        continue
    checked_squarefree += 1
    r = len(f)
    direct = is_arithmetic_from_factorization(f)
    ore = True
    if n % 2 == 0:
        ore = any(p % 4 == 3 for p, _ in f if p != 2)
    assert direct == ore
    if r in layers:
        layers[r] += 1
        if not direct:
            counts[r] += 1

rows = []
for r in range(2, 6):
    x = LIMIT
    main = x * (log(log(x)) ** (r-2)) / (2**r * factorial(r-2) * log(x))
    ratio = counts[r] / main
    rows.append((r, counts[r], layers[r], ratio))

print(
    "VERIFY_OK",
    f"limit={LIMIT}",
    f"squarefree_checked={checked_squarefree}",
    "rows=" + repr(rows),
)
