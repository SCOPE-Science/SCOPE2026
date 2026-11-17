#!/usr/bin/env python3
"""Reproduce the sharp cubic-interpolation variation design formulas.

Requires Python 3.10+, SymPy and NumPy. No network or external data.
"""
from fractions import Fraction
from math import isqrt
from itertools import product
import numpy as np
import sympy as sp

x, a, m = sp.symbols('x a m', real=True)
nodes = [-sp.Integer(1), m-a, m+a, sp.Integer(1)]
L = [sp.cancel(sp.prod((x-z) for j,z in enumerate(nodes) if j!=k) /
               sp.prod((nodes[k]-z) for j,z in enumerate(nodes) if j!=k))
     for k in range(4)]
assert sp.simplify(sum(L)-1)==0
for i,j in product(range(4),repeat=2):
    assert sp.simplify(L[i].subs(x,nodes[j]) - int(i==j))==0
S = [sp.factor(sum(L[k:])) for k in range(1,4)]
assert sp.simplify(S[0]-(1-L[0]))==0
assert sp.simplify(S[2]-L[3])==0
assert sp.simplify(S[1].subs({x:-x,m:-m})-(1-S[1]))==0
print('SYMBOLIC_CARDINAL_AND_JUMP_DECOMPOSITION_PASS')

# An elementary cubic fact: if the two derivative roots of
# p(x)=Ax^3+Bx^2+Cx+D are r_-<r_+, the difference between its two
# critical values is |A|(r_+-r_-)^3/2. Here the roots always lie in
# the indicated interpolation gaps, by Rolle's theorem.
q = 1+a+a*a
v_left  = 1 + 4*((1-m)**2+3*a*a)**sp.Rational(3,2)/(27*((1+m)**2-a*a))
v_right = 1 + 4*((1+m)**2+3*a*a)**sp.Rational(3,2)/(27*((1-m)**2-a*a))
v_mid = 4*q**sp.Rational(3,2)*(3*(1+a)**2+m*m)**sp.Rational(3,2)/(27*a*(1+a)**2*((1+a)**2-m*m))-1

# Recover each branch from the *independently constructed* Lagrange
# polynomials and the derivative-root discriminants.
for k,claimed in zip(range(3), [v_left,v_mid,v_right]):
    p = sp.Poly(S[k], x)
    A = p.all_coeffs()[0]
    d = sp.Poly(sp.diff(S[k],x), x)
    aa,bb,cc = d.all_coeffs()
    gap_sq = sp.factor((bb*bb-4*aa*cc)/(aa*aa))
    # For the end steps the variation is 1+|A|*(r_+-r_-)^3;
    # for the middle step it is |A|*(r_+-r_-)^3-1.
    Aabs = A if k == 0 else -A if k in (1,2) else A
    # The sign is fixed on the admissible domain. Check with a valid point.
    if float(Aabs.subs({a:sp.Rational(1,2),m:0})) < 0: Aabs=-Aabs
    positive_part = claimed - (1 if k!=1 else -1)
    expr = sp.factor(Aabs*Aabs*gap_sq**3 - positive_part**2)
    assert sp.simplify(expr)==0, (k,expr)
    assert float(positive_part.subs({a:sp.Rational(1,2),m:0}))>0
print('EXACT_ALL_THREE_BRANCH_IDENTITIES_PASS')

E = sp.simplify(v_left.subs(m,0))
F = sp.simplify(v_mid.subs(m,0))
E0=1+4*(1+3*a*a)**sp.Rational(3,2)/(27*(1-a*a))
F0=4*q**sp.Rational(3,2)/(3*sp.sqrt(3)*a*(1+a))-1
assert sp.simplify(E-E0)==0
assert sp.simplify(sp.powdenest(F-F0,force=True))==0
assert sp.simplify(sp.diff(E0,a) - 4*a*(11-3*a*a)*sp.sqrt(1+3*a*a)/(27*(1-a*a)**2))==0
assert sp.simplify(sp.diff(F0,a) - 2*sp.sqrt(3)*(a-1)*(a+2)*(2*a+1)*sp.sqrt(q)/(9*a*a*(1+a)**2))==0
# Exact factorization proving that moving the midpoint away from zero
# increases the middle-step variation for any fixed interior spacing.
ratio=sp.factor((v_mid+1)/(F0+1))
ratio0=((1+m*m/(3*(1+a)**2))**sp.Rational(3,2)/(1-m*m/(1+a)**2))
assert sp.simplify(sp.powdenest(sp.factor(ratio**2-ratio0**2),force=True))==0
assert float(ratio.subs({a:sp.Rational(1,2),m:sp.Rational(1,8)}))>0
print('SYMMETRIZATION_AND_STRICT_ONE_PARAMETER_MONOTONICITY_PASS')

def sqrt_interval(z, digits=42):
    """Exact rational endpoints enclosing sqrt of nonnegative Fraction."""
    if not isinstance(z,Fraction): z=Fraction(z)
    scale=10**digits
    low=isqrt((z.numerator*scale*scale)//z.denominator)
    return Fraction(low,scale),Fraction(low+1,scale)

def diff_interval(r):
    """Guaranteed rational lower/upper bounds for E(r)-F(r)."""
    r=Fraction(r); q=1+r+r*r
    sl,su=sqrt_interval(1+3*r*r)
    tl,tu=sqrt_interval(3*q)
    # E = 1 + 4(1+3a^2)s / (27(1-a^2));
    # F = 4q*sqrt(3q)/(9a(1+a)) - 1.
    El=1+4*(1+3*r*r)*sl/(27*(1-r*r))
    Eu=1+4*(1+3*r*r)*su/(27*(1-r*r))
    Fl=4*q*tl/(9*r*(1+r))-1
    Fu=4*q*tu/(9*r*(1+r))-1
    return (El-Fu, Eu-Fl)

lo=Fraction(4801369262,10**10);hi=Fraction(4801369264,10**10)
assert diff_interval(lo)[1]<0
assert diff_interval(hi)[0]>0
print('RATIONAL_ROOT_ENCLOSURE_PASS',float(lo),float(hi))

# Independently integrate |p'| on its exact intervals, using the
# derivative's real critical roots and no branch formulas.
def poly_variation(data,m0,a0):
    xs=np.array([-1.,m0-a0,m0+a0,1.]); c=np.polyfit(xs,np.asarray(data,dtype=float),3)
    dc=np.polyder(c); z=np.roots(dc)
    pts=np.array(sorted([-1.,1.]+[v.real for v in z if abs(v.imag)<1e-10 and -1.<v.real<1.]))
    return float(np.abs(np.diff(np.polyval(c,pts))).sum())

def branch_float(m0,a0):
    q=1+a0+a0*a0
    e0=1+4*((1-m0)**2+3*a0*a0)**1.5/(27*((1+m0)**2-a0*a0))
    e2=1+4*((1+m0)**2+3*a0*a0)**1.5/(27*((1-m0)**2-a0*a0))
    e1=4*q**1.5*(3*(1+a0)**2+m0*m0)**1.5/(27*a0*(1+a0)**2*((1+a0)**2-m0*m0))-1
    return (e0,e1,e2)

rng=np.random.default_rng(24052004)
count=0
for _ in range(400):
    a0=float(rng.uniform(.025,.97));m0=float(rng.uniform(-.99*(1-a0),.99*(1-a0)))
    vals=[poly_variation([int(j>=k) for j in range(4)],m0,a0) for k in [1,2,3]]
    wanted=branch_float(m0,a0)
    assert np.allclose(vals,wanted,rtol=2e-8,atol=2e-8),(vals,wanted)
    d=rng.normal(size=3)
    y=np.r_[0.,np.cumsum(d)]
    assert poly_variation(y,m0,a0) <= max(wanted)*sum(abs(d))+1e-7
    count+=1
print('INDEPENDENT_CRITICAL_POINT_AND_RANDOM_DATA_PASS',count)

astar=float(sp.nsolve(E0-F0,.48,prec=65))
opt=float(E0.subs(a,astar))
print('OPTIMAL_INTERIOR_PARAMETER',format(astar,'.14f'))
print('SHARP_VARIATION_GAIN',format(opt,'.14f'))
print('EQUISPACED_GAIN',float(max(E0.subs(a,sp.Rational(1,3)), F0.subs(a,sp.Rational(1,3)))))
print('CHEBYSHEV_LOBATTO_GAIN',float(max(E0.subs(a,sp.Rational(1,2)), F0.subs(a,sp.Rational(1,2)))))
print('ALL_FOUR_NODE_VARIATION_CHECKS_PASS')
