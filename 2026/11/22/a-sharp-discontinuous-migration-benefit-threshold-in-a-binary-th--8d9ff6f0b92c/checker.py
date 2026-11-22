#!/usr/bin/env python3
"""Deterministic checks for a two-patch three-season periodic growth theorem.

Requires Python 3 and SymPy. Numerical checks are diagnostics; the included
proof establishes the unrestricted parameter statements.
"""
import json
from fractions import Fraction
from pathlib import Path
from sympy import Matrix, symbols, diag, factor, simplify, sqrt, Rational, N

r, d = symbols('r d', real=True)
M = Matrix([[1-d, d], [d, 1-d]])
H = diag(r, 1)
L = diag(1, r)
P = M*L*M*L*M*H
T = factor(P.trace())
D = factor(P.det())
Q = (r*r+4*r-1)*d*d-(r*r+6*r-1)*d+3*r
checks = 0
assert simplify(T-(r+1)*(1-d)*(r-2*r*d+(r+1)**2*d*d)) == 0; checks += 1
assert simplify(D-r**3*(1-2*d)**3) == 0; checks += 1
assert simplify(r**4-T*r**2+D-r**2*d*(r-1)*Q) == 0; checks += 1
A = r*r+4*r-1
B = r*r+6*r-1
assert factor(B**2-12*r*A) == (r*r-4*r+1)*(r*r+4*r+1); checks += 1
rc = 2+sqrt(3)
dc = (3-sqrt(3))/2
assert simplify(Q.subs({r:rc,d:dc})) == 0; checks += 1
assert simplify(Q.diff(d).subs({r:rc,d:dc})) == 0; checks += 1
assert simplify(Q.subs(d,Rational(1,2))-(-r*r+4*r+1)/4) == 0; checks += 1
assert simplify(P.subs(d,0)-diag(r,r*r)) == Matrix.zeros(2); checks += 1
assert simplify(P.subs(d,1).trace()) == 0; checks += 1
assert simplify(P.subs(d,1).det()+r**3) == 0; checks += 1
# Check exact characteristic-factor signs against an independently computed
# two-by-two Perron root on a rational grid. This is not an infinity proof.
from math import sqrt as fsqrt
for rv in [Fraction(6,5),Fraction(2),Fraction(3),Fraction(4),Fraction(5),Fraction(7),Fraction(10)]:
 for i in range(101):
  dv=Fraction(i,100)
  R=Matrix([[Rational(rv.numerator,rv.denominator)]])
  p=P.subs({r:R[0],d:Rational(dv.numerator,dv.denominator)})
  tr=float(p.trace()); det=float(p.det());disc=max(0.0,tr*tr-4*det)
  pr=(tr+fsqrt(disc))/2
  q=float(Q.subs({r:R[0],d:Rational(dv.numerator,dv.denominator)}))
  diff=pr-float(rv*rv)
  if i>0 and abs(q)>1e-6:
   assert (diff>0)==(q<0), (rv,dv,pr,q)
  checks += 1
# At specified parameters, exact rational signs demonstrate a changed
# advantage when full migration is allowed but pooled mixing is not.
assert Q.subs({r:4,d:Rational(2,3)}) < 0; checks += 1
assert Q.subs({r:4,d:Rational(1,2)}) > 0; checks += 1
assert Q.subs({r:5,d:Rational(1,2)}) < 0; checks += 1
assert simplify((r*r+4*r-1)*Rational(1,4)-(r*r+6*r-1)*Rational(1,2)+3*r) == (-r*r+4*r+1)/4; checks += 1
report={
 'result':'PASS', 'symbolic_identities':10, 'checks_total':checks,
 'rational_grid':{'fitness_ratios':['6/5','2','3','4','5','7','10'],'rates':101},
 'scope':'finite and symbolic diagnostic verification; universal arguments in proof'
}
Path(__file__).with_name('verification_certificate.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(report, sort_keys=True))
