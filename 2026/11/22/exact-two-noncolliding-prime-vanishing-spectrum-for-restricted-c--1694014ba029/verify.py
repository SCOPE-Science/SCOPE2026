#!/usr/bin/env python3
"""Exhaustive small-support certificate for restricted coprime representations.

Requires Python 3 standard library only. All arithmetic is exact.
The infinite reduction invokes the stated inequalities in Salazar's
arXiv:2611.10059, Theorem 4.9; this program checks the finite remainder.
"""
from csv import DictReader
from math import factorial, gcd
from pathlib import Path


def primes_upto(m):
    is_prime = bytearray(b'\x01') * (m + 1)
    is_prime[0:2] = b'\x00\x00'
    for d in range(2, int(m ** .5) + 1):
        if is_prime[d]:
            is_prime[d*d::d] = b'\x00' * ((m - d*d)//d + 1)
    return [p for p in range(5, m + 1) if is_prime[p]]


def g(N, P):
    assert N % 2 == 0
    return sum(gcd(h*(N-h), 6*P) == 1 for h in range(1, N//2 + 1))


def cases():
    prime_list = primes_upto(1848)
    for n in range(13, 925):
        c = sum(n%q == 0 for q in prime_list if q <= n)
        if c > 3 or n >= (2*(c+2)+3)*(2**c*9 - 1) + 2:
            continue
        base = [h for h in range(1,n+1) if gcd(h*(2*n-h),6*n) == 1]
        full_mask = (1 << len(base)) - 1
        masks = [(0,0)]
        for q in prime_list:
            if q > 2*n: break
            if n%q == 0: continue
            mask = sum(1 << i for i,h in enumerate(base)
                       if h%q == 0 or (2*n-h)%q == 0)
            masks.append((q,mask))
        best = (len(base),0,0)
        for a,(q1,m1) in enumerate(masks):
            for q2,m2 in masks[a+1:]:
                missing = len(base) - (m1|m2).bit_count()
                if missing < best[0]: best = (missing,q1,q2)
        yield dict(n=n,c=c,base_survivors=len(base),minimum_survivors=best[0],
                   witness_q1=best[1],witness_q2=best[2])


def main():
    result = list(cases())
    cert = Path(__file__).with_name('small_support_certificate.csv')
    with cert.open(newline='',encoding='utf-8') as f:
        rows = [{k:int(v) for k,v in row.items()} for row in DictReader(f)]
    assert result == rows, ('certificate mismatch',len(result),len(rows))
    assert len(result) == 207
    from collections import Counter
    assert dict(sorted(Counter(row['c'] for row in result).items())) == {0:8,1:109,2:82,3:8}
    zeros = [2*row['n'] for row in result if row['minimum_survivors'] == 0]
    assert zeros == [26,28,34,40,46], zeros
    witnesses = {26:5*7*13,28:5*7*11,34:5*11*17,40:5*11*17,46:5*17*23}
    for N,P in witnesses.items():
        assert g(N,P) == 0, (N,P,g(N,P))
        primes = [p for p in primes_upto(P) if P%p == 0]
        assert sum((N//2)%p != 0 for p in primes) == 2, (N,P)
    print('RESTRICTED_COPRIME_J2_OK',len(result),'candidate_half_sums',
          'zero_even_sums',zeros,'witnesses',witnesses)

if __name__ == '__main__':
    main()
