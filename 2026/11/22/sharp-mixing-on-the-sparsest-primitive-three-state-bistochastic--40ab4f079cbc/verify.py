#!/usr/bin/env python3
"""Standalone consistency checks for sparse three-state Markov mixing."""
from itertools import permutations, combinations
from fractions import Fraction
import sympy as sp

p,z=sp.symbols('p z')
P=sp.Matrix([[0,0,1],[p,1-p,0],[1-p,p,0]])
assert sp.simplify(P.charpoly(z).as_expr()-(z-1)*(z*z+p*z+2*p-1))==0
assert sp.factor((z*z+p*z+2*p-1).subs(z,-p/2)) == sp.factor(-(p*p-8*p+4)/4)
# A related published three-factor kernel is isospectral to the cube of P(p);
# this prior spectral relation is not a claim of novelty.
assert sp.factor(sp.trace(P**3)-1)==-p*(p*p-6*p+3)
assert sp.factor(P.det()**3)==(2*p-1)**3
pstar=4-2*sp.sqrt(3); lam=sp.sqrt(3)-2
J=sp.ones(3)/3; I=sp.eye(3)
Q=sp.simplify(P.subs(p,pstar));N=sp.simplify(Q-J-lam*(I-J))
assert N != sp.zeros(3)
assert sp.simplify(N*N)==sp.zeros(3)
assert sp.simplify(N*J)==sp.zeros(3)
for n in range(1,8):
    assert sp.simplify(Q**n - J - lam**n*(I-J)-n*lam**(n-1)*N)==sp.zeros(3)
perms = list(permutations(range(3)))
perm_supports = [frozenset((i,a[i]) for i in range(3)) for a in perms]
# Exhaustively identify all support graphs of 3x3 bistochastic matrices with five positive entries.
supports = set()
primitive = set()
for A,B in combinations(perm_supports,2):
    U=A|B
    if len(U)!=5:continue
    # Since the support has exactly two perfect matchings, their mixture
    # has all five cells positive for coefficients strictly in (0,1).
    possible=[S for S in perm_supports if S<=U]
    assert len(possible)==2
    supports.add(U)
    adj=sp.Matrix(3,3,lambda i,j:int((i,j) in U))
    if any(all(v>0 for v in list(adj**n)) for n in range(1,15)):
        primitive.add(U)
# All primitive supports are simultaneous-relabeling orbits of the displayed P(p).
canonical=frozenset([(0,2),(1,0),(1,1),(2,0),(2,1)])
conjugates=set()
for rel in perms:
    conjugates.add(frozenset((rel[i],rel[j]) for i,j in canonical))
assert primitive==conjugates,(primitive,conjugates)
assert len(supports)==9 and len(primitive)==6,(len(supports),len(primitive))
# Every nontrivial supporting permutation pair with >=2 different rows uses >=5 edges.
assert min(len(A|B) for A,B in combinations(perm_supports,2))==5
# Verify exact spectral radius formula against actual eigenvalues for 25 rational parameters.
for k in range(1,26):
    pp=sp.Rational(k,26)
    eig=P.subs(p,pp).eigenvals()
    vals=[v for v in eig if v!=1]
    target=(pp+sp.sqrt(pp**2-8*pp+4))/2 if pp<=pstar else sp.sqrt(2*pp-1)
    rho=max(abs(complex(v.evalf(40))) for v in vals)
    assert abs(rho-float(target))<1e-12,(pp,rho,target)
print('VERIFY_OK support_graphs=9 primitive_conjugates=6 exact_jordan_powers=7 spectral_test_parameters=25')
