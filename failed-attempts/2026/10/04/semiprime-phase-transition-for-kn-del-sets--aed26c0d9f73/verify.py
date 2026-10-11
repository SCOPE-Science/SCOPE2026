#!/usr/bin/env python3
from math import gcd

def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    p = 2
    while p * p <= n:
        if sieve[p]:
            start = p * p
            sieve[start:n+1:p] = b"\x00" * (((n-start)//p) + 1)
        p += 1
    return [i for i in range(2, n + 1) if sieve[i]]

P = primes_upto(997)
PSET = set(P)

def lcm(a,b):
    return a // gcd(a,b) * b

def actual(k,p,q):
    return p*q > k and (p*q-k) % lcm(p-1,q-1) == 0

def classified(k,p,q):
    if p == k and k in PSET:
        return (q-k) % (k-1) == 0 if k > 2 else True
    if p < q < k and p*q > k:
        return (k-q) % (p-1) == 0 and (k-p) % (q-1) == 0
    return False

checks = 0
for k in range(1,201):
    for i,p in enumerate(P):
        for q in P[i+1:]:
            if actual(k,p,q) != classified(k,p,q):
                raise AssertionError((k,p,q,actual(k,p,q),classified(k,p,q)))
            checks += 1

for k in (2,3,5,7):
    vals = []
    for i,p in enumerate(P):
        for q in P[i+1:]:
            if p*q > 5000:
                break
            if actual(k,p,q):
                vals.append(p*q)
    print(f"k={k} first_semiprimes={sorted(vals)[:12]}")

print(f"VERIFY_OK checks={checks}")
