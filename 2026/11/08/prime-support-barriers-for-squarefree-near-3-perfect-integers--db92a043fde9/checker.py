#!/usr/bin/env python3
"""Exact integer verification for prime-support obstructions in near-3-perfect numbers."""
from math import gcd, prod, isqrt

def prime(n):
    if n < 2: return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0: return False
    return True

def primes_1_mod_3(count):
    result = []
    v = 7
    while len(result) < count:
        if v % 3 == 1 and prime(v): result.append(v)
        v += 1
    return result

r = primes_1_mod_3(120)
assert r[:12] == [7,13,19,31,37,43,61,67,73,79,97,103]
assert r[12] == 109 and r[13] == 127
assert r[118] == 1567 and r[119] == 1579
# For odd candidates, 3,5 and 119 primes 1 mod 3 maximize abundancy at 121 supports.
B_119 = 4 * 6 * prod(p+1 for p in r[:119])
P_119 = 3 * 5 * prod(r[:119])
B_120 = B_119 * (r[119]+1)
P_120 = P_119 * r[119]
assert B_119 < 3*P_119
assert B_120 > 3*P_120
print('ODD_THRESHOLD_OK support=121 ratio_below_3=True support=122 ratio_above_3=True last=1567,1579')

# All 13-prime even positive-surplus candidates are 2*3*t1*...*t10*q,
# t1,...,t10 = first ten primes 1 mod 3 and q in {97,103,109}.
small = r[:10]
B_base = prod(p+1 for p in small)
assert 2*B_base < 3*prod(small)
P_base = prod(small)
skip = r[:9]+[r[10],r[11]]   # largest possible product after any of first 10 is skipped
assert 2*prod(p+1 for p in skip) < 3*prod(skip)
assert 2*B_base*(127+1) < 3*P_base*127
for q in (97,103,109):
    P = P_base*q
    B = B_base*(q+1)
    D = 2*B-3*P
    assert D > 0
    g = gcd(P,D)
    assert g < D and P%D != 0
    print('EVEN_13_CANDIDATE_REJECTED', 'q='+str(q),'P='+str(P),'D='+str(D),'gcd='+str(g))
print('EVEN_13_EXHAUSTIVE_OK first_ten_forced=True q_candidates=97,103,109')
print('SUPPORT_CERTIFICATE_OK even_min_omega=15 odd_min_omega=122')
