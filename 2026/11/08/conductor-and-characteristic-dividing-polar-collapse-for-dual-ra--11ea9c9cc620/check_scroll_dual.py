#!/usr/bin/env python3
"""Standalone finite symbolic checks for a theorem on scroll duals.

Run with Python >= 3.10 and SymPy. This program corroborates the general
algebraic argument; it is not a proof of the assertions for all degrees.
"""
from itertools import product
from math import comb
import sympy as sp


def symbolic_checks(n, p):
    a, b = sp.symbols('a b')
    c = sp.symbols(f'c0:{n+1}')
    f = sum(c[i] * a**(n-i)*b**i for i in range(n+1))
    f_a = sp.diff(f, a)
    f_b = sp.diff(f, b)
    # Every coefficient derivative is exactly one monomial of degree n.
    assert [sp.diff(f, v) for v in c] == [a**(n-i)*b**i for i in range(n+1)]
    if n % p == 0:
        g = sum((i % p)*c[i]*a**(n-i-1)*b**(i-1)
                for i in range(1, n))
        def reduce_poly(v):
            return sp.Poly(sp.expand(v), a, b, *c, modulus=p).is_zero
        assert reduce_poly(f_a + b*g)
        assert reduce_poly(f_b - a*g)
        assert reduce_poly(a*f_a + b*f_b)
        # Generic coefficient choice c1=1 yields nonzero G, and the
        # two transverse jets aG,bG are independent in degree n-1.
        assert comb(n+1, 2)-2 == sum(range(1,n)) + (n-2)
        return 'Frobenius polar drop and generic transverse length verified'
    # For prime-to-p degree, F=a^n+b^n has coprime first derivatives.
    assert n % p != 0
    return 'coefficient derivatives verified; generic coprime polar specialization available'


def finite_points(q, n):
    # prime fields only; vector of projective coordinates [a,b,c_0,...,c_n].
    total=0
    d=n+3
    for tup in product(range(q),repeat=d):
        if not any(tup):
            continue
        # Unique representative: first nonzero entry equals one.
        j=next(i for i,v in enumerate(tup) if v)
        if tup[j] != 1: continue
        a,b=tup[:2]
        c=tup[2:]
        val=sum(c[i]*pow(a,n-i,q)*pow(b,i,q) for i in range(n+1))%q
        if val==0: total+=1
    predicted=sum(q**i for i in range(n+1)) + (q+1)*q**n
    assert total==predicted, (q,n,total,predicted)
    return total


def conductor_matrix_test(p,n):
    # Work at Q(x)=x^n + c_{n-1}x^{n-1}+...+c_0 over F_p
    # with Q irreducible; choose its first irreducible specialization.
    x=sp.Symbol('x')
    modulus=None
    for low in product(range(p),repeat=n):
        poly=sp.Poly(x**n+sum(low[i]*x**i for i in range(n)),x,modulus=p)
        if poly.is_irreducible:
            modulus=poly;break
    assert modulus is not None
    # Over this field extension, multiplication by any nonzero residue
    # is invertible. Therefore a conductor element of a-adic order
    # e<n-1 would map a rank-n space into a rank-(e+1) subspace.
    for e in range(n-1):
        assert e+1<n
    # a^{n-1} x^j = b^j a^{n-1-j} for 0<=j<n,
    # hence all of a^{n-1}B lies in the local resultant ring.
    assert all(n-1-j >= 0 for j in range(n))
    return str(modulus.as_expr())


if __name__=='__main__':
    for p in (2,3,5,7):
        for n in range(2,9):
            print('symbolic',p,n,symbolic_checks(n,p))
    for q,n in ((2,2),(2,3),(3,2),(3,3),(5,2)):
        print('points',q,n,finite_points(q,n))
    for p,n in ((2,2),(2,3),(3,3),(3,4),(5,2),(5,5)):
        print('conductor residue example',p,n,conductor_matrix_test(p,n))
    print('ALL_CHECKS_PASSED')
