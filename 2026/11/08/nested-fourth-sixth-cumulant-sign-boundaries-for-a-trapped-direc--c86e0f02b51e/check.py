#!/usr/bin/env python3
"""Deterministic algebraic verification of the two cumulant transition curves.

Requires Python 3 and SymPy.  Uses only stationary generator identities;
it is not a stochastic simulation or an external certification claim.
"""
from functools import lru_cache
from fractions import Fraction
import sympy as sp

d,g=sp.symbols('d g', nonnegative=True)
@lru_cache(None)
def M(p,q,n):
    if p==0 and q==0:
        return sp.Integer(int(n==0))
    gap=p+q+d*n*n+(2*g if n%2 else 0)
    return sp.cancel(((p*M(p-1,q,n+1)) if p else 0)+((q*M(p,q-1,n-1)) if q else 0))/gap

def iszero(x):
    assert sp.cancel(sp.together(x))==0, sp.factor(x)

R2=1/(1+d+2*g)
R4=(4*d+3)/((1+2*d)*(1+d+2*g)*(3+d+2*g))
R6=3*(36*d**3+8*d*d*g+93*d*d+18*d*g+68*d+10*g+15)/((1+d)*(1+2*d)*(1+d+2*g)*(3+d+2*g)*(5+d+2*g)*(3+9*d+2*g))
for j,formula in [(1,R2),(2,R4),(3,R6)]:
    iszero(M(j,j,0)-formula)

P=116*d**3+199*d*d+98*d+15-(32*d*d+40*d+8)*g-(16*d+12)*g*g
K4=sp.Rational(3,8)*(R4-2*R2**2)
K6=sp.Rational(5,16)*R6-sp.Rational(45,16)*R4*R2+sp.Rational(15,4)*R2**3
D6=4*(1+d)*(1+2*d)*(1+d+2*g)**3*(3+d+2*g)*(5+d+2*g)*(3+9*d+2*g)
iszero(K4-3*(2*g-7*d-3)/(8*(1+2*d)*(1+d+2*g)**2*(3+d+2*g)))
iszero(K6-15*P/D6)
g4=(7*d+3)/2
iszero(P.subs(g,g4)+8*(2*d+1)*(3*d+1)*(4*d+3))
iszero(K4.subs(g,g4))
iszero(K6.subs(g,g4)+15*(3*d+1)/(1024*(d+1)**2*(2*d+1)**3*(8*d+3)))

# Independent finite exact-rational stationary-generator matrix comparison.
# Assemble all monomial/Fourier unknowns at total degree <=6 and solve the
# upper-triangular linear system in ascending degree, rather than using M.
for dd,gg in [(sp.Rational(1,2),sp.Rational(1,3)),(sp.Rational(1,1),sp.Rational(2,1)),(sp.Rational(3,2),sp.Rational(9,1)),(sp.Rational(1,4),sp.Rational(11,4)),(sp.Rational(2,1),sp.Rational(0,1))]:
    variables=[]
    for order in range(7):
        for p in range(order+1):
            q=order-p
            for n in range(-order,order+1):
                variables.append((p,q,n))
    values={(0,0,n):sp.Integer(int(n==0)) for n in range(-6,7)}
    for order in range(1,7):
        states=[(p,order-p,n) for p in range(order+1) for n in range(-order,order+1)]
        mat=sp.zeros(len(states)); rhs=sp.zeros(len(states),1)
        for i,(p,q,n) in enumerate(states):
            mat[i,i]=order+dd*n*n+(2*gg if n%2 else 0)
            if p: rhs[i,0]+=p*values.get((p-1,q,n+1),sp.Integer(0))
            if q: rhs[i,0]+=q*values.get((p,q-1,n-1),sp.Integer(0))
        solved=mat.inv()*rhs
        values.update({k:sp.factor(solved[i]) for i,k in enumerate(states)})
    for j,formula in [(1,R2),(2,R4),(3,R6)]:
        iszero(values[(j,j,0)]-formula.subs({d:dd,g:gg}))
    for order,val in [(4,K4),(6,K6)]:
        if order==4:
            independent=sp.Rational(3,8)*(values[(2,2,0)]-2*values[(1,1,0)]**2)
        else:
            independent=sp.Rational(5,16)*values[(3,3,0)]-sp.Rational(45,16)*values[(2,2,0)]*values[(1,1,0)]+sp.Rational(15,4)*values[(1,1,0)]**3
        iszero(independent-val.subs({d:dd,g:gg}))
print('PASS: symbolic 2/4/6 moment identities, cumulant factorization, transition ordering and five exact-rational independent linear-system comparisons')
