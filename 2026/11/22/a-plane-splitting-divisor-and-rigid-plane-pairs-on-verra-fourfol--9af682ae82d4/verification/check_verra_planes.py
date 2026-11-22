#!/usr/bin/env python3
"""Exact checks for the plane-splitting Verra-fourfold theorem.

Requires SymPy. Symbolic tests validate the displayed witness and lattice data;
incidence geometry and genericity are established by the mathematical proof.
"""
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

u0, u1, u2, v0, v1, v2 = s.symbols("u0 u1 u2 v0 v1 v2")
F = ((u0**2 + 2*u0*u1)*v0**2 + 2*u2**2*v0*v1
     + (2*u0*u2+u1**2)*v0*v2 + (2*u0*u2+u1**2)*v1**2
     + (-u0**2+2*u0*u1)*v1*v2 + u2**2*v2**2)
p = {v0:0, v1:0, v2:1}
assert s.expand(F.subs(p) - u2**2) == 0
q0 = s.expand(s.diff(F,v0).subs(p))
q1 = s.expand(s.diff(F,v1).subs(p))
assert q0 == 2*u0*u2 + u1**2
assert q1 == -u0**2+2*u0*u1
assert q0.subs(u2,0) == u1**2
assert q1.subs(u2,0) == -u0**2+2*u0*u1
# Binary quadratic symmetric matrices on the line u2=0.
Q0 = s.Matrix([[0,0],[0,1]])
Q1 = s.Matrix([[-1,1],[1,0]])
s0,t0 = s.symbols("s t")
assert s.factor((s0*Q0+t0*Q1).det()) == -t0*(s0+t0)
# The H^0 map O(1) + O + O --> O(2) has full column rank five.
monomials = [u0**2,u0*u1,u0*u2,u1**2,u1*u2,u2**2]
columns = [2*u2*u0,2*u2*u1,2*u2*u2,-q0,-q1]
section_map=s.Matrix([[s.Poly(f,u0,u1,u2).coeff_monomial(m)
                       for f in columns] for m in monomials])
assert section_map.rank() == 5
# Chern classes of the rank-two normal bundle.
H=s.symbols("H")
assert s.expand(s.series((1+H)/(1+2*H),H,0,3).removeO()) == 1-H+2*H**2
# Integral intersection pairing and discriminant group.
M=s.Matrix([[0,0,2,1],[0,2,0,0],[2,0,0,0],[1,0,0,2]])
assert M.det() == -16
smith=smith_normal_form(M,domain=ZZ)
assert [abs(int(smith[i,i])) for i in range(4)] == [1,1,2,8]
# Fiberwise square incidence: P^35, fixed-point square codimension 3,
# two distinct points impose independent codimension 3 conditions each.
assert (35-3+2)==34
assert (35-6+4)==33
print("PASS: square fiber, normal map, nodal tangent cone, lattice")
