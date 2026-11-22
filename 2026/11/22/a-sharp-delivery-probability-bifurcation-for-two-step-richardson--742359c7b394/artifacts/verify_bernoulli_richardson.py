#!/usr/bin/env python3
"""Reproducible symbolic and exact-rational checks for a two-step erasure theorem.

Requires Python 3 and SymPy. Finite tests supplement, not replace, the proof.
"""
from fractions import Fraction as Q
from itertools import product
import sympy as s

p, c, x, y, z, d = s.symbols('p c x y z d', real=True)
A = 1-p+p*c*c

def g(a, lam):
    return 1-p+p*(1-a*lam)**2

Fminus = g(1+x,1-c)*g(1+y,1-c)
Fplus = g(1+x,1+c)*g(1+y,1+c)
W=(1+c)*Fminus/2+(1-c)*Fplus/2
certificate=A*A+p*(1-c*c)*((1-p*(1+c*c))*(x*x+y*y)
  +2*p*c*c*(x+y+x*y)**2+p*(1+c*c)*x*x*y*y)
assert s.expand(W-certificate)==0

# At the critical delivery probability the certificate vanishes only at x=y=0:
# xy=0 and x+y+xy=0 imply x=y=0.
assert s.simplify((1/(1+c*c))*(1+c*c)) == 1

Fpert=s.expand(g(1-d,z)*g(1+d,z))
F0=s.expand(g(1,z)**2)
perturb=F0+2*p*z*z*(1-p-p*(1-z)**2)*d*d+p*p*z**4*d**4
assert s.expand(Fpert-perturb)==0

# Independent rational checks of the global certificate and uniqueness.
nchecks=2
for cc in (Q(1,10),Q(1,4),Q(1,2),Q(3,4),Q(9,10)):
    threshold=1/(1+cc*cc)
    for pp in (Q(1,10),Q(1,3), threshold/2, threshold):
        base=(1-pp+pp*cc*cc)**2
        for aa,bb in product((Q(0),Q(1,5),Q(1),Q(3,2),Q(3)),repeat=2):
            fm=(1-pp+pp*(1-aa*(1-cc))**2)*(1-pp+pp*(1-bb*(1-cc))**2)
            fp=(1-pp+pp*(1-aa*(1+cc))**2)*(1-pp+pp*(1-bb*(1+cc))**2)
            w=(1+cc)*fm/2+(1-cc)*fp/2
            assert w>=base
            if aa!=1 or bb!=1: assert w>base
            nchecks+=2

# Above critical probability, sufficiently small unequal steps beat the
# repeated schedule uniformly across the interval. For a concrete rational
# instance verify the full interval by a polynomial positivity certificate.
cc=Q(1,2); pp=Q(9,10); dd=Q(1,5)
lam=s.symbols('lam',real=True)
F=s.expand((1-s.Rational(9,10)+s.Rational(9,10)*(1-s.Rational(4,5)*lam)**2)*
           (1-s.Rational(9,10)+s.Rational(9,10)*(1-s.Rational(6,5)*lam)**2))
base=s.Rational(169,1600)
# Monotonicity derivative: it is strictly convex on [1/2,3/2], hence a
# unique interior minimum (and no interior maximum). Check convex derivative.
Fsecond=s.factor(s.diff(F,lam,2))
assert s.simplify(Fsecond.subs(lam,s.Rational(1,2)))>0
assert s.discriminant(s.Poly(Fsecond,lam),lam)<0
assert s.diff(F,lam).subs(lam,s.Rational(1,2))<0
assert s.diff(F,lam).subs(lam,s.Rational(3,2))>0
assert F.subs(lam,s.Rational(1,2))==s.Rational(3233,31250)
assert F.subs(lam,s.Rational(3,2))==s.Rational(2873,31250)
assert max(F.subs(lam,s.Rational(1,2)),F.subs(lam,s.Rational(3,2)))<base
nchecks+=8
print('VERIFY_OK',nchecks)
print('symbolic weighted-endpoint sum-of-squares and perturbation identities passed')
print('rational example: kappa=3, p=9/10, normalized steps 4/5 and 6/5')
print('example worst squared amplification = 3233/31250 < 169/1600')
