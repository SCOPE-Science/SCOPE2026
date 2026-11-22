#!/usr/bin/env python3
"""Exact algebraic checks for the marked Z15 K3-tail gluing curve.
The geometric proof of completeness and quotient types is in RESULT.md.
Requires Python 3 and sympy.
"""
import sympy as s
alpha,beta,u=s.symbols('alpha beta u')
f0=beta*(alpha**2+beta)
g0=alpha*(alpha**2+2*beta)
# alpha=0 and beta=1: two points with mu4 stabilizer.
assert s.solve(f0.subs({alpha:0,beta:1})-u*u,u)==[-1,1]
assert g0.subs({alpha:0,beta:1})==0
assert s.diff(g0,alpha).subs({alpha:0,beta:1})==2
# alpha=1 and g0=0: beta=-1/2; two points, mu2 stabilizer.
assert s.solve(g0.subs(alpha,1),beta)==[-s.Rational(1,2)]
assert s.solve((f0-u*u).subs({alpha:1,beta:-s.Rational(1,2)}),u)==[-s.I/2,s.I/2]
assert s.diff(g0,beta).subs({alpha:1,beta:-s.Rational(1,2)})==2
assert s.expand(f0.subs(alpha,0)-u*u)==beta**2-u**2
# Canonical cyclic quotient ADE resolutions: inverse Cartan endpoint entries.
for n,d in [(1,s.Rational(1,2)),(3,s.Rational(3,4))]:
 M=s.Matrix(n,n,lambda i,j: 2 if i==j else (-1 if abs(i-j)==1 else 0))
 assert M.inv()[0,0]==d
# Weighted degree, correction, and self-intersection.
H2=s.Rational(6*8,1*2*4*4*3)
correction=2*s.Rational(3,4)+2*s.Rational(1,2)
assert H2==s.Rational(1,2) and correction==s.Rational(5,2)
assert H2-correction==-2
print('PASS: 2 mu4 points, 2 mu2 points; endpoint inverse-Cartan corrections; rational (-2)-curve')
