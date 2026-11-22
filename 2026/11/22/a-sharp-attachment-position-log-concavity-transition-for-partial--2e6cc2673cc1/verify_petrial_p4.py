#!/usr/bin/env python3
"""Exact finite checks for the four-vertex-branch partial-Petrial theorem."""
from collections import Counter
from math import comb


def rank_binary(rows, n):
    a = list(rows)
    pivot = 0
    for col in range(n):
        k = next((i for i in range(pivot, n) if (a[i] >> col) & 1), None)
        if k is None:
            continue
        a[pivot], a[k] = a[k], a[pivot]
        for j in range(n):
            if j != pivot and ((a[j] >> col) & 1):
                a[j] ^= a[pivot]
        pivot += 1
        if pivot == n:
            break
    return pivot


def direct(m, root_index):
    n = 4*m + 1
    base = [0]*n
    for i in range(m):
        off = 1 + 4*i
        edges = [(0, off+root_index)]+[(off+j, off+j+1) for j in range(3)]
        for u,v in edges:
            base[u] |= 1 << v
            base[v] |= 1 << u
    hist = Counter()
    for mask in range(1 << n):
        rows = [base[i] | (((mask >> i) & 1) << i) for i in range(n)]
        hist[rank_binary(rows, n)] += 1
    return hist


def polynomial(m, internal):
    # Coefficients of z^{3m} times the bracket in the theorem.
    b = 2 if internal else 0
    def power(a,b,k):
        return [comb(k,j)*a**(k-j)*b**j for j in range(k+1)]
    u=power(b,11,m)
    c=power(5,11,m)
    p=[0]*(m+3)
    for j,v in enumerate(u):
        p[j] += v
        p[j+1] += v
    for j in range(m+1):
        p[j+2] += 2*(c[j]-u[j])
    assert p[-1]==0
    return p[:-1]


def strict_defects(v):
    return [v[i]**2-v[i-1]*v[i+1] for i in range(1,len(v)-1)]


def run():
    for rooted in (False, True):
        for m in range(1,4):
            v=polynomial(m,rooted)
            direct_counts=direct(m,1 if rooted else 0)
            predicted={3*m+j: count for j,count in enumerate(v) if count}
            assert direct_counts == predicted, (m,rooted,direct_counts,predicted)
        print('DIRECT_GF2_RANK_ENUMERATION_PASS', 'internal' if rooted else 'endpoint', 'm=1..3')
    for m in range(1,7):
        ds=strict_defects(polynomial(m,True))
        assert all(d>0 for d in ds), (m,ds)
    for m in range(7,101):
        v=polynomial(m,True)
        assert v[1]**2-v[0]*v[2] < 0
        # Exact symbolic first-defect numerator identity.
        numerator=121*m*m+165*m+24
        assert 2**(2*m-3)*numerator-2**(m+1)*5**m == v[1]**2-v[0]*v[2]
    print('INTERNAL_SHARP_THRESHOLD_CHECK_PASS m=1..100')
    for m in range(1,101):
        v=[v for v in polynomial(m,False) if v]
        assert all(x>0 for x in strict_defects(v)),m
        if m >= 4:
            # Prove normalized exceptional defects with positive t=m-4 polynomials.
            t=m-4
            assert 625*t**4+8625*t**3+65150*t*t+246300*t+378723>0
            assert 25*t**3+300*t*t+812*t+1137>0
    print('ENDPOINT_STRICT_LOGCONCAVITY_CHECK_PASS m=1..100')
    assert polynomial(7,True)[:3]==[128,5056,242234]
    assert 5056**2-128*242234==-5442816
    print('BOUNDARY_CERTIFICATE_PASS 29 vertices defect=-5442816')
    print('VERIFY_OK')

if __name__=='__main__':
    run()
