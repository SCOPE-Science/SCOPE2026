"""Solve 7-torsion on E_lam via Tate normal form to get concrete params (a:b:c).
E: y^2 + (1-c)xy - b y = x^3 - b x^2 with 7-torsion at (0,0) (Kubert). Take b,c params s.t. j matches Hesse member, then map back? Simpler: directly solve division: parametrize E_lam in Weierstrass form and use numerical 7-division roots, then convert to Hesse coords and to (a:b:c) with sigma-translation=O? Note t=(a:b:c) IS sigma(O) per ker M(O) computation. So any order-7 point gives valid Sklyanin params (a:b:c) with abc!=0 generically.
"""
import numpy as np
lam = 2.0
# Weierstrass model of x^3+y^3+1-3 lam x y=0 (z=1): use sage-free transform:
# Standard: Hesse X^3+Y^3+Z^3=3 lam XYZ has j = 27 lam^3(8+... ) use numeric period lattice instead.
# Periods of E: integrate dx/y over cycles numerically? Heavy. Alternative: solve 7P=O directly with chord-tangent but robust line parametrization via SVD nullspace fix.
import sys
sys.path.insert(0,"output/artifacts")
from torsion7 import third, add, mul, peq, F, O, grad
# diagnose third(): test doubling P+P and P+Q distinct on the real curve y from cubic
P=np.array([1.0,2.0,3.0],dtype=complex)
print("F(P)=",F(P))
Q=add(P,O); print("P+O-P dist:",peq(Q,P))
R=add(P,P); print("2P=",R,"check on curve F=",F(R))
S=add(P,R); print("3P=",S,"F=",F(S))
print("order of P: ", [peq(mul(k,P),O) for k in [1,2,3,7]])
