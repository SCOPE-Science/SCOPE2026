#!/usr/bin/env python3
"""Exact algebraic checker for five-atom zero-sum sixth-power norm inequalities.
Requires Python 3 and SymPy. Does not rely on numerical optimization.
"""
import itertools
from fractions import Fraction
import sympy as sp

u = sp.symbols('u1 u2 u3 u4', nonnegative=True)
raw = [0, u[0], u[0] + u[1], u[0] + u[1] + u[2], sum(u)]
mean = sum(raw) / 5
x = [z - mean for z in raw]
S = sum(z*z for z in x)
T = sum(z**6 for z in x)
LOW = sp.Poly(sp.expand(180*T - 11*S**3), *u)
HIGH = sp.Poly(sp.expand(41*S**3 - 80*T), *u)
assert len(HIGH.terms()) == 76
assert all(c >= 0 for _, c in HIGH.terms())
assert HIGH.coeff_monomial(u[1]**6) > 0
assert HIGH.coeff_monomial(u[2]**6) > 0
upper_edge = sp.factor(HIGH.as_expr().subs({u[1]:0, u[2]:0}))
assert upper_edge == sp.Rational(24,5)*u[0]**2*u[3]**2*(12*u[0]**2+11*u[0]*u[3]+12*u[3]**2)

square_terms = [
 (sp.Rational(48,5)*u[0]*u[1]*u[2]**2*(u[2]-u[1])**2),
 (sp.Rational(72,5)*u[0]*u[1]*u[2]*u[3]*(u[2]-u[1])**2),
 (sp.Rational(32,5)*u[1]**2*u[2]**2*(u[2]-u[1])**2),
 (sp.Rational(48,5)*u[1]**2*u[2]*u[3]*(u[2]-u[1])**2)
]
rem = sp.Poly(sp.expand(LOW.as_expr()-sum(square_terms)),*u)
assert all(c>=0 for _,c in rem.terms()), [(m,c) for m,c in rem.terms() if c<0]
# Compare both full coefficient maps with the supplied human-readable certificate.
from pathlib import Path
cert = Path(__file__).with_name("CERTIFICATE.tsv")
actual = {(name, tuple(exp)): str(coeff) for name,poly in (("P_hi",HIGH),("R",rem)) for exp,coeff in poly.terms()}
seen = {}
for line in cert.read_text(encoding="utf-8").splitlines():
 if not line or line.startswith("#"): continue
 name,*fields=line.split("\t")
 assert len(fields)==5
 exp=tuple(map(int,fields[:4]));coeff=fields[4]
 assert (name,exp) not in seen
 seen[(name,exp)]=coeff
assert seen==actual, "supplied coefficient certificate differs from exact expansion"
assert rem.coeff_monomial(u[0]**6)>0
assert rem.coeff_monomial(u[3]**6)>0
lower_edge = sp.factor(LOW.as_expr().subs({u[0]:0,u[3]:0}))
assert lower_edge == sp.Rational(8,5)*u[1]**2*u[2]**2*(9*u[1]**2-8*u[1]*u[2]+9*u[2]**2)
assert sp.expand(9*u[1]**2-8*u[1]*u[2]+9*u[2]**2-5*(u[1]**2+u[2]**2)-4*(u[1]-u[2])**2)==0

for witness,expected in [([4,-1,-1,-1,-1],sp.Rational(41,80)),([2,2,2,-3,-3],sp.Rational(11,180))]:
 assert sum(witness)==0
 val=sp.Rational(sum(z**6 for z in witness),sum(z*z for z in witness)**3)
 assert val==expected,(val,expected)
assert sp.Rational(41,80)/sp.Rational(11,180)==sp.Rational(369,44)

# Independent rational checks in the original zero-sum coordinates.
count=0
for zs in itertools.product(range(-2,3),repeat=4):
 q=(*zs,-sum(zs))
 if not any(q):continue
 ss=sum(z*z for z in q);tt=sum(z**6 for z in q)
 assert 180*tt-11*ss**3>=0
 assert 41*ss**3-80*tt>=0
 count+=1
print('EXACT_COEFFICIENTWISE_UPPER_CERTIFICATE_OK', len(HIGH.terms()))
print('EXACT_FOUR_SQUARE_LOWER_CERTIFICATE_OK',len(rem.terms()))
print('EXACT_EQUALITY_EDGE_FACTORIZATIONS_OK')
print('RATIONAL_ZERO_SUM_SAMPLE_INEQUALITIES_OK',count)
print('EXACT_BANACH_MAZUR_RATIO_OK 369/44')
print('ALL_FIVE_ATOM_SIXTH_POWER_CHECKS_PASSED')
