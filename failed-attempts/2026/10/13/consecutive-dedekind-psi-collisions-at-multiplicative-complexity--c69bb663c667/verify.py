#!/usr/bin/env python3

LIMIT = 100000

def factorization(n):
    x = n
    out = {}
    p = 2
    while p*p <= x:
        while x % p == 0:
            out[p] = out.get(p, 0) + 1
            x //= p
        p = 3 if p == 2 else p + 2
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out

def omega(n):
    return sum(factorization(n).values())

def psi(n):
    if n == 1:
        return 1
    value = n
    for p in factorization(n):
        value = (value // p) * (p + 1)
    return value

hits = []
tested = 0
for n in range(1, LIMIT):
    if omega(n) <= 2 and omega(n+1) <= 2:
        tested += 1
        if psi(n) == psi(n+1):
            hits.append((n, n+1, psi(n)))

assert hits == [(4,5,6), (14,15,24)], hits
assert psi(4) == psi(5) == 6
assert psi(14) == psi(15) == 24

print(
    "VERIFY_OK",
    f"range=1..{LIMIT-1}",
    f"low_omega_pairs={tested}",
    f"hits={hits}",
)
