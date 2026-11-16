#!/usr/bin/env python3
"""Exact tests of the constructive formulas in the accompanying theorem.
All claims beyond the finite sample rely on the mathematical proof.
"""
import sympy as sp
X=sp.Symbol('X')
PERIODS=(2,3,4,6,8,9,10,12,18,20,24,25,32,36,40,50,54,72,96,100)

def witness(N):
    f=sp.factorint(N)
    if len(f)==1:
        return sp.Poly(sum(X**j for j in range(N)),X),N-1
    if len(f)!=2 or 2 not in f:
        raise ValueError('period outside theorem domain')
    p=next(z for z in f if z!=2)
    q=2**(f[2]-1)*p**(f[p]-1)
    phi=sp.cyclotomic_poly(2*p,X)
    h=(1+X**p)*sum(X**j for j in range(p-1))+sp.Rational(1,2)*X**(p-1)*phi
    fpoly=sp.expand(sum(X**r for r in range(q))*h.subs(X,X**q)*2)
    return sp.Poly(fpoly,X),N-q-1

def main():
    passes=0
    for N in PERIODS:
        pol,degree=witness(N)
        assert pol.degree()==degree,(N,pol.degree(),degree)
        assert all(c>0 and c.q==1 for c in pol.all_coeffs()),N
        assert sp.rem(pol.as_expr(),sp.cyclotomic_poly(N,X),X)==0,N
        for extra in range(3):
            more=sp.Poly(sp.expand(pol.as_expr()*sum(X**j for j in range(extra+1))),X)
            assert more.degree()==degree+extra
            assert all(c>0 for c in more.all_coeffs())
            assert sp.rem(more.as_expr(),sp.cyclotomic_poly(N,X),X)==0
            passes+=1
    print('PASS: {} exact positive-tap divisibility and length checks on {} periods'.format(passes,len(PERIODS)))
if __name__=='__main__': main()
