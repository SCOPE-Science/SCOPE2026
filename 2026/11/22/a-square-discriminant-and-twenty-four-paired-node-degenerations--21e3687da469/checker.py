"""Exact supplementary computation for a transverse conic in the Fermat cubic's dual.

Requires Python 3 and SymPy. This finite calculation witnesses nonemptiness of
an open transversality condition; the general discriminant theorem is proved
geometrically, not by finite enumeration.
"""
from itertools import product
from sympy import Add, Matrix, Poly, expand, gcd, prod, symbols

A,B,C,D=symbols('A B C D')
a,b,c,d=symbols('a b c d')
s,t=symbols('s t')

# For F = x0^3+x1^3+x2^3+x3^3, tangent coefficients obey
# sum_i epsilon_i sqrt(a_i^3)=0 (up to common scalar).
# Product over the eight sign choices modulo simultaneous sign.
P=Poly(prod(A+e*B+f*C+g*D for e,f,g in product([1,-1],repeat=3)),A,B,C,D)
assert all(all(e%2==0 for e in exponents) for exponents,coef in P.terms())
Ddual=Add(*(coef*a**(3*exp[0]//2)*b**(3*exp[1]//2)
             *c**(3*exp[2]//2)*d**(3*exp[3]//2)
             for exp,coef in P.terms()))
assert Poly(Ddual,a,b,c,d).total_degree()==12

# A concrete rank-three coefficient map (Veronese conic in dual P3).
coeffs=Matrix([[-1,-1,2],[2,3,3],[-2,2,-2],[2,-2,3]])
assert coeffs.rank()==3
monomials=Matrix([s**2,s*t,t**2])
L=list(coeffs*monomials)
R=expand(Ddual.subs(dict(zip((a,b,c,d),L)),simultaneous=True))
assert Poly(R,s,t).total_degree()==24
f=Poly(R.subs(s,1),t)
assert f.degree()==24
assert gcd(f,f.diff()).degree()==0
assert expand(R.subs({s:0,t:1}))!=0
print('PASS: dual degree 12; rank-three conic; 24 simple intersection parameters.')
print('Leading coefficient at infinity:',R.subs({s:0,t:1}))
