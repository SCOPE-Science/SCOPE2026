#!/usr/bin/env python3
"""Independent exact-length counting check for asymptotic joint uniformity."""
from fractions import Fraction

def count(m,k,n):
    v=[[0]*k for _ in range(m)];v[0][0]=1
    for _ in range(n):
        z=[[0]*k for _ in range(m)]
        for r in range(m):
            for p in range(k):
                c=v[r][p]
                if c:
                    z[2*r%m][p]+=c
                    z[(2*r+1)%m][(p+1)%k]+=c
        v=z
    return v
for m,k in [(3,2),(6,2),(8,3),(10,4),(15,3),(24,3)]:
    for n in (12,24,48,80):
        v=count(m,k,n)
        err=max(abs(Fraction(c,2**n)-Fraction(1,m*k)) for row in v for c in row)
        if n==80: assert err < Fraction(1,10000),(m,k,err)
        if n in (12,80):print(f'm={m} k={k} n={n} max_error={float(err):.9g}')
print('PASS: direct exact enumerator converges to uniform residues in six parameter cases')
