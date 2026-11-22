#!/usr/bin/env python3
"""Exact local checks for the Heisenberg-invariant cubic fourfold."""
import sympy as s
from math import comb
A,B,U3,U4,U5,U6,U7,U8=s.symbols('A B U3 U4 U5 U6 U7 U8')
xs=[s.Integer(1),A-1,B,U3,U4,U5,U6,U7,U8]
x=xs
F=[3*(x[0]*x[1]*x[2]+x[3]*x[4]*x[5]+x[6]*x[7]*x[8]),
3*(x[0]*x[3]*x[6]+x[1]*x[4]*x[7]+x[2]*x[5]*x[8]),
3*(x[0]*x[4]*x[8]+x[1]*x[5]*x[6]+x[2]*x[3]*x[7]),
3*(x[0]*x[5]*x[7]+x[1]*x[3]*x[8]+x[2]*x[4]*x[6]),
s.Add(*(z**3 for z in x))]
vars=[A,B,U3,U4,U5,U6,U7,U8]
origin={v:0 for v in vars}
assert all(f.subs(origin)==0 for f in F)
J=s.Matrix([[s.diff(F[i],v).subs(origin) for v in [A,B]] for i in [0,4]])
assert J.det()!=0
assert s.Matrix([[s.diff(f,v).subs(origin) for v in vars] for f in F]).rank()==2

def homogeneous_part(poly,deg):
    p=s.Poly(s.expand(poly),*vars)
    return s.expand(sum(c*s.prod(v**e for v,e in zip(vars,mon))
                        for mon,c in p.terms() if sum(mon)==deg))
q=[homogeneous_part(F[i]/3,2) for i in [1,2,3]]
expected=[U3*U6-U4*U7,U4*U8-U5*U6,U5*U7-U3*U8]
assert all(s.expand(a-b)==0 for a,b in zip(q,expected))
M=s.Matrix([[U3,U4,U5],[U7,U6,U8]])
minor=[s.expand(M[:,[0,1]].det()),s.expand(M[:,[1,2]].det()),s.expand(-M[:,[0,2]].det())]
assert q==minor
assert homogeneous_part(F[0],1)==-3*B
assert homogeneous_part(F[4],1)==3*A
# The Segre projective variety is smooth: Jacobian rank is 2 at one rank-one
# point, and GL(2) x GL(3) is transitive on all nonzero rank-one matrices.
rep={U3:1,U4:0,U5:0,U6:0,U7:0,U8:0}
J2=s.Matrix([[s.diff(f,v).subs(rep) for v in [U3,U4,U5,U6,U7,U8]] for f in q])
assert J2.rank()==2
# Degree-d forms on Segre P^1 x P^2: (d+1)*binom(d+2,2).
for d in range(8):
    coeff = comb(d+3,3) + (2*comb(d+2,3) if d >= 1 else 0)
    assert (d+1)*comb(d+2,2) == coeff
print('PASS: point lies on the five cubics; rank-two linear elimination; three independent rank-one 2x3 minors; smooth Segre tangent cone; Hilbert series (1+2t)/(1-t)^4; multiplicity three')
