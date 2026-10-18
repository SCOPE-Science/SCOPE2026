#!/usr/bin/env python3
"""Exact finite checks for local coordinate changes on reciprocal-plane germs.

The symbolic argument for arbitrary arrangement sizes is in RESULT.md.
This code is a finite cross-check, not an infinite proof.
"""
from fractions import Fraction
from math import comb, gcd


def solve_three(cols, rhs):
    rows = [[Fraction(cols[j][i]) for j in range(3)] + [Fraction(rhs[i])]
            for i in range(3)]
    for k in range(3):
        pivot = next(j for j in range(k,3) if rows[j][k])
        rows[k], rows[pivot] = rows[pivot], rows[k]
        p = rows[k][k]
        rows[k] = [x/p for x in rows[k]]
        for j in range(3):
            if j != k:
                factor = rows[j][k]
                rows[j] = [a-factor*b for a,b in zip(rows[j],rows[k])]
    return [r[3] for r in rows]


def poly_mult(a, b):
    c = [Fraction(0)] * (len(a) + len(b) - 1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] += x*y
    return c


def det_fraction(matrix):
    n = len(matrix)
    a = [[Fraction(x) for x in row] for row in matrix]
    d = Fraction(1)
    for k in range(n):
        pivot = next((i for i in range(k,n) if a[i][k]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            a[k],a[pivot]=a[pivot],a[k]
            d = -d
        p=a[k][k]
        d*=p
        for j in range(k+1,n):
            fac=a[j][k]/p
            for t in range(k+1,n):
                a[j][t]-=fac*a[k][t]
            a[j][k]=0
    return d


for n in range(4,12):
    # A Vandermonde family of lines, with no concurrent triples.
    ell = [(Fraction(1),Fraction(t),Fraction(t*t)) for t in range(n)]
    r=n-2
    for i in range(n):
        others=[j for j in range(n) if j!=i]
        basis=[ell[i], ell[others[0]], ell[others[1]]]
        coeffs={j:solve_three(basis,ell[j]) for j in others}
        L={j:coeffs[j][1:] for j in others}
        # No pair of binary restrictions has a common zero in projective P1.
        assert all(L[j][0]*L[k][1] != L[k][0]*L[j][1]
                   for j in others for k in others if j<k)
        # Products omitting one factor form a complete degree-r linear system.
        rows=[]
        for j in others:
            Q=[Fraction(1)]
            for k in others:
                if k!=j: Q=poly_mult(Q,L[k])
            assert len(Q)==r+1
            rows.append(Q)
        assert det_fraction(rows)
        # Direct Möbius identity with exact rational evaluations.
        for j in others:
            alpha=coeffs[j][0]
            found=False
            for u,v,w in [(1,2,3),(2,3,5),(1,7,11),(4,5,9)]:
                zden=L[j][0]*v+L[j][1]*w
                denom=alpha*u+zden
                if zden and denom:
                    y=Fraction(u,1)/denom
                    assert (1-alpha*y)!=0
                    assert y/(1-alpha*y)==Fraction(u,1)/zden
                    found=True
                    break
            assert found
    print(f"n={n}: all {n} germs, rank {n-1} Veronese basis, Möbius tests pass; "
          f"r={r}; class-group order={r}; index={r//gcd(r,2)}; "
          f"basepoints={comb(n,2)}; degree={comb(n-1,2)}")
print("SUCCESS: all exact rational checks passed; symbolic proof remains required.")
