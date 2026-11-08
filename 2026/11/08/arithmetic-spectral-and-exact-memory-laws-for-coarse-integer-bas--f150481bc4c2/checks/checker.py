#!/usr/bin/env python3
"""Exact checker for arithmetic spectra and memory of integer circle maps.

Standalone: Python 3 with sympy (no input files). For finitely many q,b,
checks Q products, characteristic polynomials, and exact TV distances.
"""
from fractions import Fraction
from math import gcd
import sympy as sp


def counts(q, b):
    return [[sum(1 for t in range(b) if (b*j+t)%q==k) for k in range(q)] for j in range(q)]


def cycles(q,b):
    unseen=set(range(1,q)); out=[]
    while unseen:
        start=min(unseen); seq=[]; loc={}; k=start
        while k and k in unseen and k not in loc:
            loc[k]=len(seq);seq.append(k);unseen.remove(k);k=(b*k)%q
        if k in loc:
            out.append(tuple(seq[loc[k]:]))
    return out


def test():
    z=sp.Symbol('z')
    tested=0
    for q in range(2,14):
        for b in range(2,13):
            C=sp.Matrix(counts(q,b)); P=C/b
            assert all(sum(C.row(j))==b for j in range(q))
            assert all(sum(C.col(j))==b for j in range(q))
            r=b%q
            for j in range(q):
                tv=sum(abs(sp.Rational(C[j,k],b)-sp.Rational(1,q)) for k in range(q))/2
                assert tv==sp.Rational(r*(q-r),q*b),(q,b,j,tv)
            cs=cycles(q,b)
            M=sum(len(c) for c in cs)
            predicted=(z-1)*z**(q-1-M)
            for c in cs:
                L=len(c)
                predicted *= z**L-sp.Rational(1,b**L)
            assert sp.expand(predicted-P.charpoly(z).as_expr())==0,(q,b,cs)
            # Spectrum nontrivial must have modulus 0 or 1/b.
            tested+=1
    for q in range(2,12):
        for b in range(2,9):
            for c in range(2,9):
                assert sp.Matrix(counts(q,b))*sp.Matrix(counts(q,c)) == sp.Matrix(counts(q,b*c))
                # Because count matrices have raw counts: C_b C_c=C_bc.
    # Explicit nontrivial transient/cycle instance.
    assert set(cycles(6,2))=={(2,4)}
    print('PASS: exact stochasticity, TV and characteristic polynomials for',tested,'(q,b) pairs; all q<=11 semigroup products; q=6,b=2 mixed spectrum')

if __name__=='__main__':
    test()
