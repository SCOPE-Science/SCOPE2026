#!/usr/bin/env python3
"""Exact modular certificates for a Fourier support theorem at cyclic order 14.

No external libraries or floating-point arithmetic are used.
A nonzero reduction modulo a prime of a cyclotomic determinant
certifies that the original complex determinant is nonzero.
"""
from itertools import combinations
N = 14
P = 1009
ROOT = 904
assert all(P % d for d in range(2, int(P**0.5)+1))
assert pow(ROOT, 14, P) == 1
assert pow(ROOT, 7, P) != 1 and pow(ROOT, 2, P) != 1
FOURIER = [[pow(ROOT, j*k, P) for k in range(N)] for j in range(N)]

def rank_matrix(a):
    a = [row[:] for row in a]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    lead = 0
    for col in range(cols):
        pivot = next((r for r in range(lead, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[lead], a[pivot] = a[pivot], a[lead]
        inv = pow(a[lead][col], P-2, P)
        for j in range(col, cols):
            a[lead][j] = a[lead][j]*inv % P
        for r in range(lead+1, rows):
            scale = a[r][col]
            if scale:
                for j in range(col, cols):
                    a[r][j] = (a[r][j]-scale*a[lead][j]) % P
        lead += 1
        if lead == rows:
            break
    return lead

def rank_minor(rows, columns):
    return rank_matrix([[FOURIER[r][c] for c in columns] for r in rows])

def disconnected(mask, bandwidth):
    """Support-induced graph with edges of circular distance <= bandwidth."""
    seen = mask & -mask
    prev = -1
    while seen != prev:
        prev = seen
        nxt = seen
        for j in range(N):
            if seen & (1 << j):
                for a in range(1, bandwidth+1):
                    nxt |= mask & (1 << ((j+a) % N))
                    nxt |= mask & (1 << ((j-a) % N))
        seen = nxt
    return seen != mask

def translate(mask, shift):
    shift %= N
    return ((mask << shift) | (mask >> (N-shift))) & ((1 << N)-1)

def orbits(masks):
    unseen = set(masks)
    reps = []
    while unseen:
        m = min(unseen)
        orb = {translate(m,s) for s in range(N)}
        assert orb <= set(masks)
        unseen -= orb
        reps.append(m)
    assert sum(len({translate(r,s) for s in range(N)}) for r in reps) == len(masks)
    return reps

# Exact exhaustive upper bound: all disconnected supports, modulo independently
# translating rows and columns of Fourier restrictions.
D4 = [mask for mask in range(1, 1<<N) if disconnected(mask,4)]
assert len(D4)==560
REP4 = orbits(D4)
assert len(REP4)==42
num=0
for s in REP4:
    columns=[j for j in range(N) if s & (1<<j)]
    for t in REP4:
        rows=[j for j in range(N) if not(t & (1<<j))]
        assert rank_minor(rows,columns)==len(columns),(s,t)
        num+=1
assert num==1764

# Exact sharpness: signal supported at even positions 2E.
# Its 7-point Fourier transform is supported precisely at {0,1,2,3}.
E=[0,1,4,5]
R=[4,5,6]
S=sum(1<<(2*e) for e in E)
T=sum(1<<k for k in [0,1,2,3,7,8,9,10])
assert disconnected(S,3) and disconnected(T,3)
# A kernel vector of the 3 x 4 matrix is nonzero in every entry;
# no remaining Fourier coefficient can vanish. Both assertions follow
# from the following nonzero minors in the complex seventh-root matrix.
Z7 = [[pow(ROOT, 2*r*e, P) for e in E] for r in range(7)]
assert all(rank_matrix([[Z7[r][j] for j in cols] for r in R])==3
           for cols in combinations(range(4),3))
assert all(rank_matrix([[Z7[r][j] for j in range(4)] for r in R+[extra]])==4
           for extra in range(4))
print('CHECK_OK prime=1009 order14_root=904 disconnected=560 translation_orbits=42 rank_pairs=1764 lower_minor_checks=8')
