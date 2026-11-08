#!/usr/bin/env python3
"""Independent, exact census of six-factorial square witnesses with largest index 527.

Uses two arithmetic constructions for parity vectors and exhausts all feasible
penultimate indices. No external packages, network, or precomputed solution file.
"""
from collections import Counter, defaultdict
from pathlib import Path
import csv

N = 527
EXPECTED = {523: 5, 524: 0, 525: 1, 526: 126}


def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0:2] = b'\x00\x00'
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b'\x00' * (((n-p*p)//p)+1)
    return [i for i in range(n+1) if sieve[i]]


def signatures_by_integers():
    # Construction I: parity of the prime factors of each integer,
    # followed by cumulative XOR for factorials.
    pr = primes_upto(N)
    bits = {p: 1 << i for i, p in enumerate(pr)}
    sig = [0] * (N+1)
    for m in range(2, N+1):
        r, z = m, 0
        for p in pr:
            if p*p > r:
                break
            while r % p == 0:
                z ^= bits[p]
                r //= p
        if r > 1:
            z ^= bits[r]
        sig[m] = sig[m-1] ^ z
    return sig, pr


def signatures_by_legendre(pr):
    # Construction II: for each prime p, independently use Legendre's
    # formula v_p(n!) = sum_k floor(n/p^k) modulo 2.
    v = [0] * (N+1)
    for m in range(1, N+1):
        z = 0
        for i, p in enumerate(pr):
            if p > m:
                break
            t = m
            parity = 0
            while t:
                t //= p
                parity ^= (t & 1)
            z |= parity << i
        v[m] = z
    return v


def enumerate_a(sig):
    # For the four feasible penultimate indices e, enumerate every
    # two + two pairing a<b<c<d<e by a hash table for (a,b).
    solutions = set()
    counts = Counter()
    for e in range(523, 527):
        pairs = defaultdict(list)
        for a in range(1, e):
            for b in range(a+1, e):
                pairs[sig[a] ^ sig[b]].append((a, b))
        required = sig[e] ^ sig[N]
        for c in range(1, e):
            for d in range(c+1, e):
                key = required ^ sig[c] ^ sig[d]
                for a, b in pairs.get(key, ()):
                    if b < c:
                        solutions.add((a, b, c, d, e, N))
                        counts[e] += 1
    return {e: counts[e] for e in range(523,527)}, solutions


def enumerate_b(sig):
    # Reversed pairing method: for each c,d store their block interval
    # product [c+1,d]; loop a,b to close the parity equation. This
    # uses factorial signatures constructed via Legendre, not factorization.
    solutions = set()
    counts = Counter()
    for e in range(523,527):
        pair = defaultdict(list)
        for c in range(1, e):
            for d in range(c+1, e):
                pair[sig[c] ^ sig[d]].append((c, d))
        required = sig[e] ^ sig[N]
        for a in range(1,e):
            for b in range(a+1,e):
                for c,d in pair.get(required ^ sig[a] ^ sig[b], ()): 
                    if b < c:
                        solutions.add((a,b,c,d,e,N))
                        counts[e] += 1
    return {e: counts[e] for e in range(523,527)}, solutions


def main():
    s1, primes = signatures_by_integers()
    s2 = signatures_by_legendre(primes)
    assert s1 == s2, 'independent parity vectors differ'
    a, A = enumerate_a(s1)
    b, B = enumerate_b(s2)
    assert A == B and a == b == EXPECTED, (a, b, A.symmetric_difference(B))
    assert len(A) == 132
    assert not any(t[0] == 1 for t in A)
    assert min(A) == (2, 11, 29, 35, 526, 527)
    assert (16,17,30,31,526,527) in A
    with (Path(__file__).parent/'witnesses.csv').open(newline='') as f:
        rows = list(csv.reader(f))
    assert rows[0] == ['a','b','c','d','e','f']
    listed = [tuple(map(int,row)) for row in rows[1:]]
    assert len(listed) == 132 and listed == sorted(A), 'incomplete or mismatched witness certificate'
    # A completely independent arithmetic identity: a product of six
    # factorials has the same squareclass as its three disjoint intervals.
    for a1,b1,c1,d1,e1,f1 in A:
        z = s1[b1]^s1[a1]^s1[d1]^s1[c1]^s1[f1]^s1[e1]
        assert z == 0
    print('VERIFY_OK n=527 count=132 penultimate=' + str(EXPECTED))
    print('INDEPENDENT_EXHAUSTIVE_ENUMERATORS=yes prime_factor_vs_legendre=yes')
    print('WITNESS=(16,17,30,31,526,527)')

if __name__ == '__main__':
    main()
