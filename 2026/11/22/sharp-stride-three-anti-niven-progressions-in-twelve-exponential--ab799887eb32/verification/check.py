#!/usr/bin/env python3
"""Exact certificate for twelve even-base anti-Niven progressions (Python standard library)."""
from math import gcd, isqrt
DATA = [(2, 10, 17, 8, 1787, 9, 197), (3, 28, 37, 10, 29761, 21, 1101), (4, 82, 115, 34, 779899, 57, 9627), (5, 244, 365, 122, 21789929, 165, 89669), (6, 730, 797, 68, 425253467, 489, 583337), (7, 2188, 2381, 194, 11403451217, 1461, 5214197), (8, 6562, 6589, 28, 283764365395, 4377, 43250169), (9, 19684, 19699, 16, 7632959143513, 13125, 387794499), (10, 59050, 59429, 380, 207226615515947, 39369, 3509400929), (11, 177148, 177437, 290, 5568255320120801, 118101, 31432964261), (12, 531442, 531713, 272, 150172303709698451, 354297, 282575683301), (13, 1594324, 1594429, 106, 4052832216735449353, 1062885, 2542039609749)]
def digit_sum(n, b):
    total=0
    while n:
        n,r=divmod(n,b)
        total += r
    return total

def primes_up_to(n):
    flags=bytearray(b"\x01")*(n+1)
    flags[0]=flags[1]=0
    for p in range(2,isqrt(n)+1):
        if flags[p]:
            flags[p*p::p]=b"\x00"*((n-p*p)//p+1)
    return [p for p in range(2,n+1) if flags[p]]

def main():
    primes=primes_up_to(max(K+2*b for k,b,H,K,n,L,U in DATA))
    total=0
    for k,b,H,K,n,L,U in DATA:
        assert b == 3**k+1 and 2 <= k <= 13
        h = H-b
        assert 1 <= h <= b-2
        assert digit_sum(H,b)==K==h+1 and K%3!=0
        assert U == b*b+(h+2)*b+h
        assert n == H*b*b+(b-2)*b+(b-3)
        assert L == 2*3**(k-1)+3
        assert gcd(n,K+2*b-5)==1
        assert gcd(U+3,K+3)==1
        assert all(U%p!=0 and (U+2)%p!=0 for p in primes if p<=K+2*b and p!=3)
        assert digit_sum(n+3*(L-1),b)==K+3
        for j in range(L):
            x=n+3*j
            assert gcd(x,digit_sum(x,b))==1,(k,j)
        total += L
    assert total == 1594356
    print(f"VERIFY_OK bases={len(DATA)} terms={total}")
if __name__ == '__main__': main()
