#!/usr/bin/env python3
"""Exact arithmetic spot checks for the nilradical module theorem.
Requires Python 3 and sympy. Finite checks are not the all-n proof.
"""
from math import factorial
from sympy import symbols, Rational, expand, diff, groebner, Poly, cancel
z,w=symbols('z w')
for n in range(2,11):
    c=lambda k:Rational(2**k*factorial(n),factorial(n-2*k)* (n*(n-1))**k * factorial(k)*factorial(k+1))
    G=expand(sum(c(k)*z**(n-2*k)*w**k for k in range(n//2+1)))
    R=expand(G+w*diff(G,w))
    U=diff(G,z)
    assert expand(2*R-(n+2)*G+z*U)==0
    g=G.subs(w,1)
    alpha=Rational(8,n*(n-1))
    assert expand((alpha-z**2)*diff(g,z,2)+(2*n+1)*z*diff(g,z)-n*(n+2)*g)==0
    assert Poly(g,z).gcd(Poly(diff(g,z),z)).degree()==0
    gb=groebner([G,U],z,w,order='lex')
    assert gb.is_zero_dimensional
    # Finite standard monomial enumeration using exact Groebner reduction.
    top=2*n-4
    standard=[]
    for a in range(2*n):
        for b in range(n):
            if a+2*b<=top and all(a<lm[0] or b<lm[1] for lm in [p.LM(order='lex').exponents for p in gb.polys]):
                standard.append((a,b))
    assert len(standard)==n*(n-1)//2,(n,len(standard))
    # First layer is z^0,...,z^(n-2), with w=0.
    assert expand(G.subs(w,0)-z**n)==0
    assert expand(U.subs(w,0)-n*z**(n-1))==0
    assert gb.reduce(w**n)[1]==0
    print('n=%d: ODE, gcd, Euler, colength, first layer, nilpotence PASS'%n)
print('finite exact checks PASS (n=2..10); all-n assertions use the paper proof')
