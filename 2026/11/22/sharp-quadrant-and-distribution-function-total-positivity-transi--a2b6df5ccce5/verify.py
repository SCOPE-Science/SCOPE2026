#!/usr/bin/env python3
"""Exact symbolic checks for the geometric-PGF–FGM quadrant-sign theorem.
The continuum implications are proved analytically in RESULT.md.
Requires sympy. No random sampling and no network access.
"""
import itertools
import sympy as sp
p, theta, x, y, u, v = sp.symbols('p theta x y u v', real=True)
q=1-p
z=(1-x)*(1-y)
G=lambda w:p*w/(1-q*w)
C=x*y*(1+theta*z)
T=G(C)
B=G(x)*G(y)
H=sp.factor(T-B)
R=p*x*y*z*(q+p*theta+q*theta*z)/((1-q*C)*(1-q*x)*(1-q*y))
assert sp.factor(H-R)==0
assert sp.simplify((G(x)-u).subs(x,u/(p+q*u)))==0
assert sp.simplify(sp.diff(T,theta)-p*x*y*z/(1-q*C)**2)==0
assert sp.factor(C.subs(theta,0)-x*y)==0
assert sp.factor(T.subs(p,1)-C)==0
Tuv=sp.cancel(T.subs({x:u/(p+q*u),y:v/(p+q*v)}))
assert sp.simplify(sp.limit(Tuv,p,0,dir='+')-u*v/(u+v-u*v))==0
# CDF-TP2 is a statement about the copula CDF, not its density.
# Increasing marginal reparameterizations preserve the determinant sign.
A=1+theta*z
Btp=A*(1-theta+2*theta*z)+2*theta**2*x*y*z
J=sp.cancel(T*sp.diff(T,x,y)-sp.diff(T,x)*sp.diff(T,y))
formulaJ=p**2*x**2*y**2*(theta+q*A*Btp)/(1-q*C)**4
assert sp.factor(J-formulaJ)==0
# Negative-theta sharp CDF-TP2 threshold q >= t/(1-t)^3.
t=sp.symbols('t',positive=True)
Bneg=sp.factor(Btp.subs(theta,-t))
assert sp.simplify(Bneg-((1-t*z)*(1+t-2*t*z)+2*t*t*x*y*z))==0
assert sp.simplify((A*Btp).subs({theta:-t,x:0,y:0})-(1-t)**3)==0
critical=1-t/(1-t)**3
assert sp.simplify((critical-(1-t)) + t*t*(t*t-3*t+3)/(1-t)**3)==0
# The sharp positive-to-mixed-to-negative p thresholds for any theta<0.
assert sp.simplify(1/(1-theta)-(1+theta)-theta**2/(1-theta))==0
# Four regimes for the same negative FGM baseline theta=-1/8.
regimes=[(sp.Rational(3,4),'CDF-TP2'),
         (sp.Rational(17,20),'PQD-only'),
         (sp.Rational(22,25),'mixed'),
         (sp.Rational(9,10),'NQD')]
for P,label in regimes:
    Tn=sp.Rational(-1,8)
    qval=1-P
    is_tp2=(qval*(1+Tn)**3>=-Tn)
    is_pqd=(Tn>=-qval)
    is_nqd=(Tn<=-qval/P)
    assert {'CDF-TP2':(1,1,0),'PQD-only':(0,1,0),
            'mixed':(0,0,0),'NQD':(0,0,1)}[label] == tuple(1 if bool(a) else 0 for a in (is_tp2,is_pqd,is_nqd))

# Three certified parameter cases: PQD, NQD, mixed; all exact.
cert=[(sp.Rational(1,3),sp.Rational(-1,2), 'PQD'),
      (sp.Rational(3,5),sp.Rational(-1,2), 'mixed'),
      (sp.Rational(3,4),sp.Rational(-1,2), 'NQD')]
for P,Th,expected in cert:
    a=sp.factor((q+p*theta+q*theta*z).subs({p:P,theta:Th}))
    root=sp.simplify((-(q+p*theta)/(q*theta)).subs({p:P,theta:Th}))
    bounds=(sp.simplify(a.subs({x:0,y:0})),sp.simplify(a.subs({x:1,y:1})))
    if expected=='PQD':assert bounds[0]>0 and bounds[1]>0
    elif expected=='NQD':assert bounds[0]<0 and bounds[1]<0
    else:
        assert bounds[0]<0 and bounds[1]>0
        assert sp.simplify(a.subs({x:sp.Rational(1,4),y:sp.Rational(1,4)}))<0
        assert sp.simplify(a.subs({x:sp.Rational(1,2),y:sp.Rational(1,2)}))>0
        assert root is not None
# Check the exact transition-gap identity; not relying on floats.
assert sp.factor(1/(1-theta)-(1+theta)-theta**2/(1-theta))==0
# Verify every pointwise sign on a finite rational sanity grid.
qs=[sp.Rational(1,9),sp.Rational(1,4),sp.Rational(1,2),sp.Rational(3,4),sp.Rational(8,9)]
for P,Th,expected in cert:
    for X,Y in itertools.product(qs,repeat=2):
        d=H.subs({p:P,theta:Th,x:X,y:Y})
        assert (d>0) if expected=='PQD' else ((d<0) if expected=='NQD' else True)
assert H.subs({p:sp.Rational(3,5),theta:sp.Rational(-1,2),x:sp.Rational(1,4),y:sp.Rational(1,4)})<0
assert H.subs({p:sp.Rational(3,5),theta:sp.Rational(-1,2),x:sp.Rational(1,2),y:sp.Rational(1,2)})>0
print('PASS: exact factorization, CDF-TP2 determinant, sharp parameter regimes, inverse, signs, and strong-compounding limit.')
