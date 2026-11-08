#!/usr/bin/env python3
"""Exact Cartier coefficient checks for a cyclic trigonal genus-four family."""
import sympy as S
x,t=S.symbols('x t'); p=7
f=x**5+t*x**3+x

def modc(expr):
    return S.Poly(S.expand(expr),t,modulus=p).as_expr()

def coefficient(P,e):
    return modc(S.Poly(S.expand(P),x).coeff_monomial(x**e))

a0=coefficient(f**2,6)
M=S.Matrix(3,3,lambda i,j:coefficient(f**4,7*(i+1)-(j+1)))
expected=S.Matrix([[4*t,0,1],[0,(t*t+2)*(t*t+3),0],[1,0,4*t]])
assert a0 == t*t+2
assert all(modc(M[i,j]-expected[i,j])==0 for i in range(3) for j in range(3))
# The anti-invariant two-dimensional block has eigenvalues 4t +/- 1.
assert modc((4*t-1)*(4*t+1)-2*(t*t+3)) == 0
assert modc(S.factor(a0*M.det())-2*(t*t+2)**2*(t*t+3)**2)==0
assert modc(S.discriminant(f,x)-16*(t*t-4)**2)==0
# Invariant and anti-invariant direct sum; the pair that can vanish
# consists of the invariant forms dx/y, x dx/y^2.
assert S.Poly(t*t+2,t,modulus=7).gcd(S.Poly(t*t+3,t,modulus=7)).degree()==0
assert S.Poly(t*t+2,t,modulus=7).gcd(S.Poly(2*t,t,modulus=7)).degree()==0
# Exact Fitting ideals: rank<=2 uses cubic minors, rank<=3 uses determinant.
u=t*t+2; v=t*t+3; a=4*t+1; b=4*t-1
D=S.diag(u,u*v,a,b)
minors=[modc(D.extract(rows,cols).det()) for rows in __import__('itertools').combinations(range(4),3) for cols in __import__('itertools').combinations(range(4),3)]
nonzero=[S.Poly(z,t,modulus=7) for z in minors if z!=0]
g=nonzero[0]
for P in nonzero[1:]:g=g.gcd(P)
assert g.monic()==S.Poly(u*v,t,modulus=7).monic() # v invertible on smooth base
assert modc(D.det()-2*u*u*v*v)==0
print('TRIGONAL_GENUS4_CARTIER_PASS',a0,M.tolist())
