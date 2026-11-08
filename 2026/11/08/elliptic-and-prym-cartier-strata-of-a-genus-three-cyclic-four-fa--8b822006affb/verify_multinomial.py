#!/usr/bin/env python3
"""Exact independent multinomial coefficient certificates for the genus-three family."""
from math import factorial


def coefficients(p):
    m=(p-1)//2
    terms={}
    # In (w^8+c*w^4+1)^m choose a powers of w^8, b of c*w^4.
    for a in range(m+1):
        for b in range(m-a+1):
            k=8*a+4*b
            c=factorial(m)//(factorial(a)*factorial(b)*factorial(m-a-b))
            poly=terms.setdefault(k,{})
            poly[b]=(poly.get(b,0)+c)%p
    return terms

def coeff(t,k,p):
    return {e:v for e,v in t.get(k,{}).items() if v%p}

for p,expect in [
    (7,[[{}, {},{1:3}],[{}, {1:6,3:1},{}],[{1:3},{},{}]]),
    (11,[[{},{},{0:5,2:10}],[{},{1:8,3:9,5:1},{}],[{0:5,2:10},{},{}]])]:
    t=coefficients(p)
    M=[[coeff(t,p*i-j,p) for j in range(1,4)] for i in range(1,4)]
    assert M==expect,(p,M,expect)
    print('MULTINOMIAL_MATRIX_PASS',p,M)
    # At the polynomial level det(H)=-A(c)^2 B(c), by antidiagonal form.
    assert all(not M[i][j] for i in range(3) for j in range(3) if (i,j) not in ((0,2),(1,1),(2,0)))
print('ALL_MULTINOMIAL_CHECKS_PASS')
