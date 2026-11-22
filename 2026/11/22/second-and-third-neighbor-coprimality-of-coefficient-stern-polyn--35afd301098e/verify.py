#!/usr/bin/env python3
"""Exact finite regression checks for coefficient-Stern polynomials (stdlib only).
The paper's universal coprimality assertion is proved in RESULT.md, not by this census.
"""
from math import gcd

LIMIT = 128
PRIMES = (1000003, 1000033, 1000037)

def stern_table(max_index):
    s = [0] * (max_index + 1)
    s[1] = 1
    for j in range(2, max_index + 1):
        if j % 2 == 0:
            s[j] = s[j // 2]
        else:
            s[j] = s[j // 2] + s[j // 2 + 1]
    return s

def trim(f):
    while len(f) > 1 and not f[-1]:
        f.pop()
    return f

def gcd_mod(f, g, p):
    f = trim([x % p for x in f])
    g = trim([x % p for x in g])
    while g != [0]:
        f, g = g, f
        inv = pow(f[-1], -1, p)
        while len(g) >= len(f) and g != [0]:
            t = g[-1] * inv % p
            offset = len(g) - len(f)
            for i, coeff in enumerate(f):
                g[i + offset] = (g[i + offset] - t * coeff) % p
            trim(g)
    return len(f) - 1

def multiply(f, g):
    out = [0] * (len(f) + len(g) - 1)
    for i, a in enumerate(f):
        for j, b in enumerate(g):
            out[i+j] += a*b
    return out

s = stern_table(LIMIT + 7)
P = [[1]]
for n in range(1, LIMIT + 4):
    P.append([s[n+1]] + P[-1])  # P_n = X P_{n-1} + s(n+1)

for n in range(LIMIT):
    assert P[n] == [s[n+1-j] for j in range(n+1)], n
    assert gcd(s[n+1], s[n+2]) == 1, n
    assert (s[n+1] == 1) == ((n+1)&n == 0), n
    for offset in (2, 3):
        remainder = P[n+offset][:(offset)]
        assert remainder == [s[n+offset+1-i] for i in range(offset)], (n, offset)
        assert any(gcd_mod(P[n], P[n+offset], p) == 0 for p in PRIMES), (n, offset)
    if n % 2 == 0 and n > 0:
        r = n//2
        rhs = multiply([1,1,1], [coeff if j%2==0 else 0 for i, coeff in enumerate(P[r-1]) for j in (2*i,2*i+1)][:2*r-1])
        rhs[0] += s[r+1]
        assert rhs == P[n], n
    if n%2 == 1:
        r=n//2
        u,v,w = s[r+1],s[r+2],s[r+3]
        a,b,c = s[n+2],s[n+3],s[n+4]
        assert (a,b,c) == (u+v,v,v+w), n
        assert b*b-4*a*c < 0 and a > 1 and gcd(gcd(a,b),c) == 1, n
print('VERIFIED: 128 indices; Stern identities, even positivity identity, odd quadratic arithmetic, and both polynomial gcds modulo an explicit prime.')
