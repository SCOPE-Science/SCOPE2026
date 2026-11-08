#!/usr/bin/env python3
"""Exact characteristic-seven Cartier-Manin and elimination certificate.

Requires SymPy; all polynomial identities are reduced in GF(7).
Run: python3 verify_strata.py
"""
import sympy as sp

p = 7
x, a, b, t = sp.symbols('x a b t')

def mod(expr, vars=(a,b)):
    return sp.Poly(expr, *vars, modulus=p).as_expr()

f = x**9 + a*x**7 + b*x**5 + a*x**3 + x
h = sp.Poly(sp.expand(f**3), x)
M = sp.Matrix(4, 4, lambda i,j:mod(h.nth(7*(i+1)-(j+1))))
u = 3*a
v = mod(3*a*a*b-a*a+3*b*b+3)
w = mod(3*a**3+3*a*b*b-a*b-a)
D = mod(u*w-v)
expected_M = sp.Matrix([[0,u,0,1],[w,0,v,0],[0,v,0,w],[1,0,u,0]])
assert all(mod(M[i,j]-expected_M[i,j])==0 for i in range(4) for j in range(4))
assert mod(M.det()-D**2)==0
assert mod(D-(2*a**4+2*a*a*b*b+a*a*b-2*a*a-3*b*b-3))==0

# In the Cartier basis the true operator is M^(1/7), hence its square,
# after applying the 49th power to all entries, is M^(7)*M.
# On D=0 the two rank-one blocks each compose with scalar E.
E = mod(1+u**7*w)
# On D=0, both Frobenius-twisted block products share exactly E.
A0=sp.Matrix([[u,1],[u*w,w]])
B0=sp.Matrix([[w,u*w],[1,u]])
A7=A0.applyfunc(lambda z:mod(z**7))
B7=B0.applyfunc(lambda z:mod(z**7))
upper=sp.Matrix([[1,u],[w**7,u*w**7]])
lower=sp.Matrix([[u*w**7,w**7],[u,1]])
assert all(mod((A7*B0-E*upper)[i,j])==0 for i in range(2) for j in range(2))
assert all(mod((B7*A0-E*lower)[i,j])==0 for i in range(2) for j in range(2))
g = sp.groebner([D,E],b,a,modulus=p,order='lex')
assert len(g.polys)==2
H1 = g.polys[0].as_expr()
H2 = g.polys[1].as_expr()
bpol = 3*a**20+2*a**18+2*a**14-a**12+3*a**10+3*a**8-2*a**6+a**4-3*a**2+1
P = a**22-3*a**20-2*a**16-3*a**12+a**10+a**8-3*a**4+2*a*a+2
assert mod(H1-(b+bpol))==0
assert mod(H2-P)==0
expected_factor=(a*a+3)**2*(a**4+3*a*a-1)*(a**6-a**4-2*a*a-3)*(a**8+3*a**6+3*a**4-3*a*a-2)
assert mod(P-expected_factor,vars=(a,))==0
U=sp.Poly(P,a,modulus=p)
assert U.sqf_part().degree()==20
assert sp.gcd(U,U.diff())==sp.Poly(a*a+3,a,modulus=p)
# For smoothness, disc of h(T)=T^4+a T^3+b T^2+a T+1 is nonzero.
q=t**4+a*t**3+b*t*t+a*t+1
disc=mod(sp.discriminant(q,t))
assert sp.gcd(U,sp.Poly(disc.subs(b,-bpol),a,modulus=p)).degree()==0
# Quick nontrivial witness checks: ordinary, rank-two, rank-zero smooth examples.
for aa,bb,dd,ee in [(0,0,4,1),(2,0,0,0),(-2,0,0,0)]:
    assert int(D.subs({a:aa,b:bb}))%7==dd
    assert int(E.subs({a:aa,b:bb}))%7==ee
    assert int(disc.subs({a:aa,b:bb}))%7!=0
print('CARTIER_STRATA_7_PASS', 4, 2, 0, U.degree(), U.sqf_part().degree(), 'smooth=20')
