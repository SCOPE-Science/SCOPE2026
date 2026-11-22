#!/usr/bin/env python3
"""Self-contained symbolic and exact-rational checks for a mixed-Poisson model.
Requires SymPy (ordinary optional computational dependency). Proof for all n is in RESULT.md.
"""
import sympy as sp
z,t=sp.symbols('z t',real=True)
L=sp.symbols('L',positive=True)
w=L**5*(L**5+48)/(L**5+24)**2
b=576/(L**5+24)**2
q=1/(1+L); r=1-q
assert sp.factor(w+b-1)==0
f=L**5/(L**5+24)**2*(L**6+48*L+24*t**4)*sp.exp(-L*t)
assert sp.simplify(sp.integrate(f,(t,0,sp.oo))-1)==0
G=sp.factor(w*r/(1-q*z)+b*r**5/(1-q*z)**5)
assert sp.factor(G.subs(z,1)-1)==0
assert sp.factor(G-L**5/(L**5+24)**2*((L**6+48*L)/(L+1-z)+576/(L+1-z)**5))==0
D4=sp.factor((b/w)*r**4)
assert sp.simplify(D4-576/(L*(L+1)**4*(L**5+48)))==0
poly=sp.expand(L*(L+1)**4*(L**5+48)-144)
assert sp.Poly(poly,L).degree()==10
# At rate 1 an explicit negative logarithmic coefficient rules out infinite divisibility.
# This finite check is not used to infer the global cutoff.
GG=sp.factor(G.subs(L,1))
num,den=sp.fraction(GG)
R=sp.cancel(sp.diff(GG,z)/GG)
co=sp.Poly(sp.series(R,z,0,55).removeO(),z)
for n in range(1,55):
    v=co.nth(n-1)
    if v<0:
        print('theta=1 first negative n*nu_n:',n,v)
        break
else: raise AssertionError('Expected negative log coefficient not located in finite diagnostic')
# Verify exact positivity of the coefficient at an ID-side rational theta.
for h in [sp.Rational(1,10),sp.Rational(1,2)]:
    V=sp.factor(G.subs(L,h)); RR=sp.factor(sp.diff(V,z)/V)
    val=[]
    cv=sp.Poly(sp.series(RR,z,0,25).removeO(),z)
    for n in range(1,25):
        v=cv.nth(n-1)
        assert v>0
        val.append(v)
    print(f"rate {h}: exact first {len(val)} logarithmic coefficients positive")
assert sp.expand(poly.subs(L,0))==-144
print('critical polynomial degree:',sp.degree(poly,L))
print('critical root bracket:',sp.N(sp.nsolve(poly,sp.Rational(1,2)),18))
print('PASS: mixture weights, model Laplace transform, critical equation and exact rational coefficients')
