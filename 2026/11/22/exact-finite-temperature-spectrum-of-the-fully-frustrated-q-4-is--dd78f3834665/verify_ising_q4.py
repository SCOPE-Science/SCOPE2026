#!/usr/bin/env python3
"""Independent finite exact enumerations for the Q4 fully frustrated Ising cell.

All checks are deterministic integer arithmetic and use Python's standard library.
"""
from collections import Counter

EXPECTED = {-16:16, -12:1920, -8:8640, -4:13440, 0:17504,
            4:13440, 8:8640, 12:1920, 16:16}


def count_direct():
    # Graph of the cube: sixteen vertices, 32 coordinate edges.
    edges=[]
    for x in range(16):
        for j in range(4):
            y=x^(1<<j)
            if x<y:
                sign=1 if (x&((1<<j)-1)).bit_count()%2==0 else -1
                edges.append((x,y,sign))
    assert len(edges)==32
    histogram=Counter()
    for mask in range(1<<16):
        # Direct evaluation of Hamiltonian at each of the 65536 spin configurations.
        score=0
        for x,y,sign in edges:
            score+=sign*(1-2*((mask>>x)&1))*(1-2*((mask>>y)&1))
        histogram[score]+=1
    return dict(histogram)


def count_two_layers():
    # Independent transfer-polynomial construction on two 8-site cubes.
    # Precompute 3-cube layer scores; unlike count_direct, use 8-spin vectors
    # and a direct 256x256 transfer across the parity signed vertical bonds.
    lower=[]
    for mask in range(256):
        s=[1 if not(mask>>x)&1 else -1 for x in range(8)]
        q=0
        for j in range(3):
            for x in range(8):
                if (x>>j)&1:
                    continue
                q+=((-1) if (x&((1<<j)-1)).bit_count()%2 else 1)*s[x]*s[x^(1<<j)]
        lower.append((s,q))
    hist=Counter()
    for a,qa in lower:
        for b,qb in lower:
            bridge=sum(((-1) if x.bit_count()%2 else 1)*a[x]*b[x] for x in range(8))
            hist[qa+qb+bridge]+=1
    return dict(hist)


def check_geometric_and_spectral_facts():
    import math
    # Signed adjacency satisfies A^2=4 I, guaranteeing |-E|<=16 by Cauchy-Schwarz.
    A=[[0]*16 for _ in range(16)]
    for x in range(16):
        for j in range(4):
            y=x^(1<<j)
            A[x][y]=-1 if (x&((1<<j)-1)).bit_count()%2 else 1
    for x in range(16):
        for y in range(16):
            assert sum(A[x][z]*A[z][y] for z in range(16))==(4 if x==y else 0)
    # Each elementary square is frustrated (plaquette bond-sign product -1).
    for x in range(16):
        for i in range(4):
            for j in range(i+1,4):
                if (x>>i)&1 or (x>>j)&1:
                    continue
                a,b,c,d=x,x^(1<<i),x^(1<<i)^(1<<j),x^(1<<j)
                assert A[a][b]*A[b][c]*A[c][d]*A[d][a]==-1

if __name__=='__main__':
    check_geometric_and_spectral_facts()
    direct=count_direct()
    transfer=count_two_layers()
    assert direct==EXPECTED,(direct,EXPECTED)
    assert transfer==EXPECTED,(transfer,EXPECTED)
    assert sum(direct.values())==65536
    assert direct[16]==direct[-16]==16
    assert set(direct)==set(range(-16,17,4))
    # Exact finite-T partition sum: sum_E g(E) exp(-beta E).
    print('PASS: 16 spins, 32 signed edges, 24 frustrated squares, A^2=4I')
    print('PASS: all 65,536 configurations, two independent exact methods')
    print('Signed-score histogram:',sorted(EXPECTED.items()))
    print('Laurent polynomial coefficients (powers -4 through 4):', [EXPECTED[4*k] for k in range(-4,5)])
