#!/usr/bin/env python3
"""Exact checks for a two-half three-branch interval transfer operator."""
import sympy as s
from sympy import Rational as Q
x,y,L=s.symbols('x y L')
def transfer_pair(fL, fU):
    lower=s.expand(fU.subs(x,1-y))
    upper=s.expand((fL.subs(x,(y-Q(1,2))/2)+fL.subs(x,(Q(3,2)-y)/2))/2)
    return lower,upper

def vector_to_pair(d, v):
    return (sum(v[j]*x**j for j in range(d+1)),
            sum(v[d+1+j]*x**j for j in range(d+1)))

def coeffs_poly(f,d):
    z=s.Poly(f,y)
    return [z.nth(j) for j in range(d+1)]

for d in range(8):
    n=2*(d+1)
    columns=[]
    for j in range(n):
        vec=[s.Integer(int(i==j)) for i in range(n)]
        fL,fU=vector_to_pair(d,vec)
        p,q=transfer_pair(fL,fU)
        columns.append(s.Matrix(coeffs_poly(p,d)+coeffs_poly(q,d)))
    M=s.Matrix.hstack(*columns)
    m=d//2
    expected=L**(2*(d-m))
    for k in range(m+1):
        expected*=L**2-Q(1,4**k)
    assert s.factor(M.charpoly(L).as_expr()-expected)==0,(d,M.charpoly(L).as_expr(),expected)
    assert n-M.rank()==d-m,(d,M.rank())
    assert n-(M*M).rank()==2*(d-m),(d,(M*M).rank())
    invariant=s.zeros(n,1); invariant[0]=1; invariant[d+1]=1
    assert M*invariant==invariant

phi=x-Q(1,2)
p1=transfer_pair(phi,phi)
p2=transfer_pair(*[z.subs(y,x) for z in p1]); assert p2==(Q(-1,4),Q(1,4)),p2
p3=transfer_pair(Q(-1,4),Q(1,4)); assert p3==(Q(1,4),Q(-1,4)),p3
C0=s.integrate(phi**2,(x,0,1))
C1=s.integrate((p1[0].subs(y,x))*phi,(x,0,Q(1,2)))+s.integrate((p1[1].subs(y,x))*phi,(x,Q(1,2),1))
C2=s.integrate(Q(-1,4)*phi,(x,0,Q(1,2)))+s.integrate(Q(1,4)*phi,(x,Q(1,2),1))
assert (C0,C1,C2)==(Q(1,12),Q(-7,96),Q(1,16)),(C0,C1,C2)
print('VERIFY_OK degrees_0_through_7=8 exact_charpolys=8 zero_Jordan_blocks=8 correlations=3 flip_plateau=1')
