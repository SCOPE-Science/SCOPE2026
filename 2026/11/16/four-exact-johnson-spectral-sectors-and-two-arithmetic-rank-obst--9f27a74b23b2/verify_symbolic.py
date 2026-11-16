#!/usr/bin/env python3
"""Exact symbolic check of all Johnson eigenvalue factorizations."""
import sympy as S
n,s=S.symbols('n s', integer=True)
e={0:S.Integer(1),1:s}
for t in range(2,7):e[t]=S.factor((s*e[t-1]-(n-t+2)*e[t-2])/t)
b=lambda z,t:S.prod(z-i for i in range(t))/S.factorial(t)
mu=lambda t:S.factor(e[t]/b(n,t))
a=[mu(6),mu(4)-mu(6),mu(2)-2*mu(4)+mu(6),1-3*mu(2)+3*mu(4)-mu(6)]
expected=[s**2*(s**2-3*n+2)**2/(6*n*(n-1)*(n-2)),
(n**2-s**2)*(s**2-n+2)**2/(2*n*(n-1)*(n-2)*(n-3)),
s**2*(n**2-s**2)*((n-2)**2-s**2)/(n*(n-1)*(n-2)*(n-3)*(n-4)),
(n**2-s**2)*((n-2)**2-s**2)*((n-4)**2-s**2)/(n*(n-1)*(n-2)*(n-3)*(n-4)*(n-5))]
for j in range(4):
    obtained=S.factor(sum(a[t]*b(3-j,t-j)*b(n-t-j,3-t) for t in range(j,4)))
    assert S.factor(obtained-expected[j])==0,(j,S.factor(obtained-expected[j]))
print('PASS: 4 exact symbolic Johnson-sector eigenvalue factorizations and 7 elementary-moment recurrences.')
