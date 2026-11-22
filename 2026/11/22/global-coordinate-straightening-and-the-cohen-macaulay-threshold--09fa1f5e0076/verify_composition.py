#!/usr/bin/env python3
"""Exact coefficient/tangent and monomial checks for odd-degree composition collisions.

Scientific objects: two smooth polynomial-composition loci in a monic,
centered, zero-constant coefficient slice over characteristic zero.
This finite checker tests examples; the accompanying proof covers all odd degrees.
"""
from fractions import Fraction
from itertools import combinations_with_replacement
from math import comb


def rank(columns):
    matrix = [[Fraction(col[i]) for col in columns] for i in range(len(columns[0]))]
    piv = 0
    for j in range(len(columns)):
        k = next((r for r in range(piv, len(matrix)) if matrix[r][j]), None)
        if k is None:
            continue
        matrix[piv], matrix[k] = matrix[k], matrix[piv]
        q = matrix[piv][j]
        matrix[piv] = [v / q for v in matrix[piv]]
        for r in range(len(matrix)):
            if r != piv and matrix[r][j]:
                q = matrix[r][j]
                matrix[r] = [a - q*b for a, b in zip(matrix[r], matrix[piv])]
        piv += 1
        if piv == len(matrix):
            break
    return piv


def mul(a, b):
    z = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            z[i+j] += x*y
    return z


def tangent_test(m, coefficients):
    assert m % 2 == 1 and m >= 3
    d = (m-1)//2
    assert len(coefficients) == d
    # H(t) = t^m + sum_{j=0}^{d-1} c_j*t^(2*j+1)
    H = [0] * (m + 1)
    H[m] = 1
    for j, c in enumerate(coefficients):
        H[2*j+1] = c
    ambient_indices = list(range(1, 2*m-1))
    def vec(poly):
        return [poly[i] if i < len(poly) else 0 for i in ambient_indices]
    A = [vec([0]*k + [1]) for k in range(2, 2*m-1, 2)]
    B = [vec(mul(H, [0]*j + [1])) for j in range(0,m-1)]
    I = [vec(mul(H, [0]*j + [2])) for j in range(1,m-1,2)]
    assert len(A) == len(B) == 2*d
    assert len(I) == d
    assert rank(A) == rank(B) == 2*d
    assert rank(A+B) == 3*d
    assert rank(I) == d
    assert all(vec(mul(H,[0]*j+[1])) in B for j in range(0,m-1))
    # Every tangent of the intersection lies in both tangents.
    assert rank(A+I)==rank(A)
    assert rank(B+I)==rank(B)
    # The even-odd direct sum gives clean intersection.
    assert rank(A)+rank(B)-rank(A+B)==d
    print(f"TANGENT PASS: m={m}, W_lower={coefficients}, "
          f"dims={2*d},{2*d},{d}, sum={3*d}")


def hilbert_test(d):
    # Coordinates z_1,...,z_d, u_1,...,u_d, v_1,...,v_d;
    # ideal (u_i v_j) annihilates monomials containing u and v.
    for degree in range(5):
        survivors = 0
        for tup in combinations_with_replacement(range(3*d), degree):
            if not (any(d <= x < 2*d for x in tup)
                    and any(2*d <= x < 3*d for x in tup)):
                survivors += 1
        formula = 2*comb(degree+2*d-1,2*d-1)-comb(degree+d-1,d-1)
        assert survivors == formula, (d, degree, survivors, formula)
    print(f"HILBERT PASS: d={d}, five graded pieces")


def graph_inverse(m, top_coefficients):
    """Return H,b,low F from the (m-1) top coefficients of H^2+bH."""
    assert len(top_coefficients)==m-1
    top=dict(zip(range(m, 2*m-1), map(Fraction,top_coefficients)))
    H=[Fraction(0) for _ in range(m+1)]
    H[m]=Fraction(1)
    # Coefficients at t^(m+j) for j=m-2,...,1 reconstruct H.
    for j in range(m-2,0,-1):
        partial=mul(H,H)
        H[j]=(top[m+j]-partial[m+j])/2
    hh=mul(H,H)
    b=top[m]-hh[m]
    P=[hh[i] + (b*H[i] if i<len(H) else 0) for i in range(2*m+1)]
    assert all(P[i]==top[i] for i in range(m,2*m-1))
    assert P[0]==P[2*m-1]==0 and P[2*m]==1
    return H,b,dict((i,P[i]) for i in range(1,m))


def graph_test(m):
    d=(m-1)//2
    for vals in ([0]*(m-1), [j+1 for j in range(m-1)],
                 [0 if i%2 else i+2 for i in range(m-1)]):
        H,b,low=graph_inverse(m,vals)
        xs=dict(zip(range(m,2*m-1), vals))
        if all(xs[j]==0 for j in range(m,2*m-1,2)):
            assert all(H[j]==0 for j in range(2,m,2))
            assert b==0
            assert all(low[j]==0 for j in range(1,m,2))
    # A dense family of arbitrary even top-coefficient vectors.
    for k in range(3):
        xs=[0 if j%2 else (k+1)*(j+1) for j in range(m,2*m-1)]
        H,b,low=graph_inverse(m,xs)
        assert b==0 and all(low[i]==0 for i in range(1,m,2))
    print(f"GRAPH AND PARITY PASS: m={m}")


if __name__ == '__main__':
    for m in (3,5,7,9,11):
        d=(m-1)//2
        for c in ([0]*d, [1]*d, [j+1 for j in range(d)]):
            tangent_test(m,c)
    for m in (3,5,7,9,11):
        graph_test(m)
    for d in range(1,5):
        hilbert_test(d)
    print('ALL EXACT CHECKS PASS')
