#!/usr/bin/env python3
"""Exact small-degree certificate for two genus-six Artin--Schreier examples.

Requires Python 3 and SymPy.  The uniform Cartier and automorphism conclusions
are proved mathematically in the accompanying exposition; this checks the
coefficient equations for the two explicit curves over F_3.
"""
import sympy as sp

A, B, x = sp.symbols('A B x')

def finite_field_rank(mat, p=3):
    a = [[v % p for v in row] for row in mat]
    rank = 0
    for col in range(len(a[0])):
        piv = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if piv is None:
            continue
        a[rank], a[piv] = a[piv], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(v * inv) % p for v in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][col]:
                d = a[i][col]
                a[i] = [(v - d*w) % p for v,w in zip(a[i],a[rank])]
        rank += 1
    return rank

for a5, target_rank in [(0,2),(1,3)]:
    f = x**7 + a5*x**5 + x**2
    delta = sp.Poly(sp.expand(f.subs(x, A*x + B) - A**7*f), x)
    c = lambda j: delta.nth(j)
    # u=A^7 must lie in F_3^* and the AS coboundary h^3-h,
    # deg(h)<=2, must match every positive-degree coefficient.
    constraints = [A**14-1,c(5),c(4),c(6)+c(2)**3,c(3)+c(1)**3]
    gb = sp.groebner(constraints,B,A,order='lex',modulus=3)
    assert list(gb) == [B,A-1], (a5,list(gb))
    # In row order (dx,x dx,x^2 dx), the Cartier images of
    # (x^2 dx, y dx, xy dx) are (1,0,0),(-1,-a5,0),(0,0,-1).
    matrix = [[1,-1,0],[0,-a5,0],[0,0,-1]]
    assert finite_field_rank(matrix) == target_rank
    print(f'a5={a5} CARTIER_RANK={target_rank} A_NUMBER={6-target_rank} AUTOMORPHISM_BASE_MAP_IDENTITY_OK')
print('CERTIFICATE_OK')
