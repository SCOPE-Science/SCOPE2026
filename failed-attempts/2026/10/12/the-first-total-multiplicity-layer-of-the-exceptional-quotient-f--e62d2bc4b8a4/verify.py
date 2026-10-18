#!/usr/bin/env python3

LIMIT = 200000

def factorization(n):
    x = n
    out = {}
    p = 2
    while p * p <= x:
        while x % p == 0:
            out[p] = out.get(p, 0) + 1
            x //= p
        p = 3 if p == 2 else p + 2
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out

def omega(n):
    return sum(factorization(n).values())

def sigma(n):
    ans = 1
    for p, e in factorization(n).items():
        ans *= (p ** (e + 1) - 1) // (p - 1)
    return ans

def phi(n):
    ans = n
    for p in factorization(n):
        ans = ans // p * (p - 1)
    return ans

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

hits = []
tested = 0
for n in range(2, LIMIT):
    if n % 2 == 0 and omega(n) <= 3:
        tested += 1
        if sigma(n) == 4 * phi(n):
            hits.append(n)

assert hits == [14, 418], hits
assert sigma(14) == 4 * phi(14) == 24
assert sigma(418) == 4 * phi(418) == 720

pairs = []
for d in range(1, 49):
    if 48 % d != 0:
        continue
    e = 48 // d
    if d >= e:
        continue
    p, q = d + 7, e + 7
    if is_prime(p) and is_prime(q):
        pairs.append((d, e, p, q))

assert pairs == [(4, 12, 11, 19)], pairs

print(
    "VERIFY_OK",
    f"range=2..{LIMIT-1}",
    f"low_multiplicity_even_tested={tested}",
    f"hits={hits}",
    f"factor_pair={pairs[0]}",
)
