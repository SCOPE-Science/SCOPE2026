#!/usr/bin/env python3
"""Finite checks for period-doubling run-reduced Abelian spectra.
All indices are zero-based. Python standard library only.
"""
from itertools import groupby

def tau(n):
    val, sign = 0, 1
    while n:
        val += sign * (n & 1)
        n >>= 1
        sign = -sign
    return val

def period_doubling(N):
    w = '0'
    while len(w) < N:
        w = ''.join('01' if b == '0' else '00' for b in w)
    return w[:N]

def runs_parikh(w):
    r = ''.join(k for k, _ in groupby(w))
    return (r.count('0'), r.count('1'))

N = 1 << 17
p = period_doubling(N)
assert all((int(c) == (((i+1 & -(i+1)).bit_length()-1) % 2)) for i,c in enumerate(p))
trans = [0] * N
for i in range(1,N):
    trans[i] = trans[i-1] + (p[i-1] != p[i])
for t in range(1,8):
    m = (4**t - 1)//3
    n = 2*m
    expected_zmin = (2*m-2*t)//3
    expected_zmax = (2*m+t)//3
    expected = {(z+1,z) for z in range(expected_zmin, expected_zmax)} | {(z,z) for z in range(expected_zmin+1, expected_zmax+1)}
    seen = set()
    seen_z = set()
    for i in range(N-n+1):
        r = 1 + trans[i+n-1]-trans[i]
        ones = (r + (p[i]=='1')) // 2
        seen.add((r-ones,ones))
        if i % 2:
            j = (i-1)//2
            if j+m < N:
                z = (2*m + tau(j+m)-tau(j))//3
                seen_z.add(z)
    assert seen == expected, (t, len(seen), sorted(seen ^ expected)[:6])
    assert seen_z == set(range(expected_zmin,expected_zmax+1)), t
    for i in range(min(2000,N-n+1)):
        assert runs_parikh(p[i:i+n]) == (lambda r,k:(r-k,k))(1+trans[i+n-1]-trans[i],(1+trans[i+n-1]-trans[i]+(p[i]=='1'))//2)
    print('t=%d m=%d length=%d zero_range=%d..%d classes=%d' % (t,m,n,expected_zmin,expected_zmax,len(seen)))
print('PASS: 7 exact spectra, independent run reductions on 14000 prefixes, prefix/digit identity.')
