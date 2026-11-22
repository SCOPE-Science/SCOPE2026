#!/usr/bin/env python3
"""Exact GF(2) certificates and finite-field checks for short cycles.

Run with Python 3; no third-party packages required.
"""

from collections import Counter


def bits(exponents):
    return sum(1 << e for e in exponents)


def pmul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        b >>= 1
    return out


def ppow(a, e):
    out = 1
    while e:
        if e & 1:
            out = pmul(out, a)
        a = pmul(a, a)
        e >>= 1
    return out


def pmod(a, f):
    d = f.bit_length() - 1
    while a.bit_length() - 1 >= d:
        a ^= f << (a.bit_length() - 1 - d)
    return a


def pgcd(a, b):
    while b:
        a, b = b, pmod(a, b)
    return a


def unique_primes(d):
    primes = []
    for p in range(2, d + 1):
        if d % p == 0:
            primes.append(p)
            while d % p == 0:
                d //= p
    return primes


def irreducible(f):
    d = f.bit_length() - 1
    if d < 1:
        return False
    z = 2
    for j in range(1, d + 1):
        z = pmod(pmul(z, z), f)
        if j in [d // p for p in unique_primes(d)]:
            if pgcd(f, z ^ 2) != 1:
                return False
    return z == pmod(2, f)


EXPS = {3: (1, 2), 6: (2, 4), 10: (2, 8)}
FACTOR_EXPONENTS = {
    'lin': [0, 1],
    'quad': [0, 1, 2],
    'quart': [0, 3, 4],
    'a5': [0, 1, 2, 4, 5],
    'b5': [0, 2, 3, 4, 5],
    'a10': [0, 2, 7, 9, 10],
    'b10': [0, 1, 3, 5, 8, 9, 10],
}
FACTORS = {s:bits(e) for s,e in FACTOR_EXPONENTS.items()}
FACTORIZATION = {
    3: {'lin':1, 'quad':2},
    6: {'lin':4, 'quad':2, 'quart':2},
    10: {'lin':4, 'quad':4, 'a5':2, 'b5':2, 'a10':2, 'b10':2},
}


def polynomial_numerator(u):
    exps = EXPS[u]
    k = max(exps)
    p = bits([k + 1] + [k - e for e in exps])
    q = 1 << k
    # Numerator of F_u(F_u(X)) + X, with F_u=P/Q.
    out = ppow(p, k + 1) ^ pmul(2, pmul(q, ppow(p, k)))
    for e in exps:
        out ^= pmul(ppow(p, k-e), ppow(q, e+1))
    return out


def check_symbolic():
    for u, pieces in FACTORIZATION.items():
        product = 1
        for name, exp in pieces.items():
            product = pmul(product, ppow(FACTORS[name], exp))
        assert polynomial_numerator(u) == product, f'composition identity {u}'
    for name, f in FACTORS.items():
        assert irreducible(f), f'irreducibility of {name}'
    assert bits([0,1]) == FACTORS['lin']
    assert bits([0,1,2]) == FACTORS['quad']
    # Fixed-point numerators: X+1, X^2+1, X^6+1.
    assert bits([0,2]) == ppow(FACTORS['lin'], 2)
    assert bits([0,6]) == pmul(ppow(FACTORS['lin'], 2), ppow(FACTORS['quad'],2))
    return len(FACTORIZATION), len(FACTORS)


def field_mul(a, b, f):
    n = f.bit_length()-1
    ans = 0
    while b:
        if b & 1:
            ans ^= a
        b >>= 1
        a <<= 1
        if a & (1 << n):
            a ^= f
    return ans


def field_pow(a, e, f):
    ans = 1
    while e:
        if e & 1:
            ans = field_mul(ans, a, f)
        a = field_mul(a, a, f)
        e >>= 1
    return ans


def field_trace(a, n, f):
    s = 0
    for _ in range(n):
        s ^= a
        a = field_mul(a, a, f)
    assert s in (0,1)
    return s


def smallest_irreducible(n):
    for f in range((1 << n)+1, 1 << (n+1), 2):
        if irreducible(f):
            return f
    raise AssertionError(f'No field polynomial for {n}')


def predicted(n, u):
    if u == 0:
        return (1 << (n-1), 0)
    if u in (3,6):
        fixed = n % 2
        two = (1 if n%4==2 else 0)
        if u == 6 and n%8 == 4:
            two = 2
        return (fixed, two)
    assert u == 10
    fixed = 1 if n%2 else (2 if n%4==2 else 0)
    two = 5 if n%10==5 else (10 if n%20==10 else 0)
    return (fixed, two)


def check_field(n):
    f = smallest_irreducible(n)
    q = 1 << n
    t1 = [a for a in range(1,q) if field_trace(a,n,f)==1]
    assert len(t1) == q//2
    for u in (0,3,6,10):
        if u >= q:  # The binary index must satisfy 0<=u<2^n.
            continue
        table = {}
        for a in t1:
            inv = field_pow(a, q-2, f)
            out = a
            for i in range(n):
                if (u >> i) & 1:
                    out ^= field_pow(inv, 1 << i, f)
            table[a] = out
        assert set(table.values()) == set(t1), (n,u,'not permutation')
        fixed = sum(table[a]==a for a in t1)
        two_points = sum(table[a] != a and table[table[a]] == a for a in t1)
        assert two_points % 2 == 0
        observed = (fixed, two_points//2)
        assert observed == predicted(n,u), (n,u,observed,predicted(n,u))
    return len(t1)


if __name__ == '__main__':
    print('GF(2) symbolic identities and irreducibility:', check_symbolic())
    total=0
    for n in range(1,16):
        count=check_field(n)
        total += count
        print(f'F_2^{n}: verified all {count} trace-one inputs')
    print('PASS: 15 extension degrees,',total,'trace-one inputs, each admissible map')
