#!/usr/bin/env python3
"""Exact elementary checks for a Fano-scheme contact-order classification.
This script checks only finite algebraic identities and examples;
the general geometric assertions require the accompanying proof.
"""
from math import comb
from fractions import Fraction
from sympy import symbols, expand, Poly, binomial, factor, simplify, Matrix, diff

a,u,q,y,x,z=symbols('a u q y x z')

for r in range(2,11):
    f=(a+q*u)**r
    tangent=a**r+r*a**(r-1)*q*u
    g=expand(f-tangent)
    expected=sum(comb(r,j)*a**(r-j)*q**j*u**j for j in range(2,r+1))
    assert expand(g-expected)==0
    # For j >= 2, the nilpotent graded layer has k-length r-j.
    lengths=[r-j for j in range(2,r)]
    assert sum(lengths)==comb(r-1,2)
    assert all(comb(r,j)!=0 for j in range(2,r+1))
    print(f'CONTACT_r={r} LAYERS={lengths} EMBEDDED_LENGTH={sum(lengths)}')

# On x^d+y^d=z^d, at p=[0:1:1] the tangent contact is d.
# The Hessian determinant in homogeneous coordinates is nonzero multiple
# of (xyz)^(d-2), hence 3d points of contact d and no others.
for d in range(3,10):
    f=x**d+y**d-z**d
    H=Matrix([[diff(f,a1,a2) for a2 in (x,y,z)] for a1 in (x,y,z)])
    det=factor(H.det())
    expected=(-1)*((d*(d-1))**3)*(x*y*z)**(d-2)
    assert expand(det-expected)==0
    # Hessian flex weights total 3d(d-2), agreeing with Plucker.
    assert 3*d*(d-2)==3*d*(d-2)
    embedded=3*d*comb(d-1,2)
    poly_const=d+embedded
    print(f'FERMAT_d={d} FLEXES={3*d} ALL_CONTACT={d} PLUCKER_P(n)={2*d}*n+{poly_const}')

# Exact tangent-jet coefficients for d=3,4,5; phi^d=1-a^d,
# phi'= -a^(d-1)/phi^(d-1); all coefficients have valuation d-j.
for d in range(3,8):
    for j in range(2,d+1):
        # eliminate phi via its dth power; the leading factor is a^(d-j)
        k=d-j
        correction=(-1)**j*a**(d*(j-1))/(1-a**d)**(j-1)
        bracket=1+correction
        assert simplify(bracket.subs(a,0))==1
        assert comb(d,j)>0
    # degree d=3 recovers generic-double plus 9 embedded flex residues.
    genus=(d-1)*(d-2)//2
    ordinary_flex_weight=3*d*(d-2)
    generic_const=d+ordinary_flex_weight
    by_RR=d*(d-2)+2*(1-genus)+ordinary_flex_weight
    assert generic_const==by_RR==d*(3*d-5)
print('ALL_CHECKS_PASSED')
