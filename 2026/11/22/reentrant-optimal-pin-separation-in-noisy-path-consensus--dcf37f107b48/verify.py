#!/usr/bin/env python3
"""Exact and numerical checks for the finite-gain two-anchor path theorem.

Requires Python 3 with SymPy and NumPy; assertions raise on failure.
This script supplements the mathematical proof and is not an external audit.
"""
from fractions import Fraction
from itertools import combinations
import numpy as np
import sympy as sp

k, d, n, r, c, L, R = sp.symbols('k d n r c L R', positive=True)
V = (k*d + 1)/(k*(k*d + 2))
C = 1/(k*(k*d + 2))
segment = (d*d-1)/6 + ((d+1)*(2*d+1)/(3*d))*V + ((d*d-1)/(3*d))*C
full = (L*(L+1)+R*(R+1))/2 + segment + (L+R)*V
balanced = n/(2*k) + ((n-d)**2-1+sp.symbols('q'))/4 + (d*d-1)/6 + (3*d*n-2*d*d+2)/(6*(2+d*k))
q = sp.symbols('q')
assert sp.simplify(full - (n/(2*k) + ((n-d)**2-1+q)/4 +(d*d-1)/6 +(3*d*n-2*d*d+2)/(6*(2+d*k)) ).subs({n: L+R+d+1, q:(L-R)**2})) == 0
print('Exact finite-path trace formula: PASS')

J=(1-r)**2/sp.Integer(4)+r**2/sp.Integer(6)+r*(3-2*r)/(6*(2+c*r))
N=5*c*c*r**3-3*c*c*r**2+18*c*r*r-12*c*r+12*r-6
assert sp.simplify(sp.diff(J,r) - N/(6*(2+c*r)**2)) == 0
assert sp.factor(sp.diff(J,r,2)) == (5*c**3*r**3+30*c*c*r*r+60*c*r-12*c+24)/(6*(2+c*r)**3)
assert sp.factor(sp.diff(J,r,c))==r*(c*r*r+6*r-6)/(3*(2+c*r)**3)
assert sp.simplify(N.subs(c,6*(1-r)/r**2)-6*(2*r-3)*(7*r*r-14*r+6)/r**2)==0
rho=1-1/sp.sqrt(7)
cstar=(7+4*sp.sqrt(7))/3
assert sp.simplify(N.subs({r:rho,c:cstar}))==0
assert sp.simplify((c*r*r+6*r-6).subs({r:rho,c:cstar}))==0
assert sp.simplify(N.subs({r:sp.Rational(3,5),c:sp.Rational(5,3)}))==0
print('Cubic, convexity, mixed derivative, maximum and crossover: PASS')

def score(Nnodes,gap,gain):
    m=Nnodes-1-gap
    parity=m%2
    return (Fraction(Nnodes,2)/gain
          +Fraction((Nnodes-gap)**2-1+parity,4)
          +Fraction(gap*gap-1,6)
          +Fraction(3*gap*Nnodes-2*gap*gap+2,6)/(2+gap*gain))

for cc, expect in [(1,12),(6,13),(100,12)]:
    Nnodes=21
    gain=Fraction(cc,21)
    v=[(score(Nnodes,gap,gain),gap) for gap in range(1,Nnodes)]
    best=min(v)[0]
    winners=[gap for value,gap in v if value==best]
    assert winners==[expect],(cc,winners)
    runner_up=min(value for value,gap in v if value>best)
    print(f'21-path exact gain c={cc}: gap {expect}; runner-up-minus-best={runner_up-best}: PASS')

# Verify the rational trace formula by exact matrix inversion for every pair
# of distinct leaders on short paths, beyond balanced pairs.
for nn in range(2,10):
    base=sp.zeros(nn)
    for v in range(nn-1):
        base[v,v]+=1;base[v+1,v+1]+=1
        base[v,v+1]-=1;base[v+1,v]-=1
    for ii,jj in combinations(range(nn),2):
        dd=jj-ii
        left=ii;right=nn-1-jj
        kk=sp.Rational(3,7)
        A=base.copy();A[ii,ii]+=kk;A[jj,jj]+=kk
        v=(kk*dd+1)/(kk*(kk*dd+2))
        z=1/(kk*(kk*dd+2))
        formula=sp.Rational(left*(left+1)+right*(right+1),2) + (dd*dd-1)/sp.Integer(6) + v*(left+right+(dd+1)*(2*dd+1)/sp.Integer(3*dd)) + z*(dd*dd-1)/sp.Integer(3*dd)
        assert sp.simplify(sp.trace(A.inv())-formula)==0,(nn,ii,jj)
print('All short-path exact inverse traces: PASS')

# Independent floating-point experiment: predicted normalized maximizers
# for finite paths with gain c/n converge to the analytic root.
for cc in (sp.Rational(1,10),sp.Rational(5,3),sp.Rational(4),cstar,sp.Integer(20)):
    cfloat=float(cc)
    roots=sp.nroots(N.subs(c,cc),maxsteps=100)
    root=next(float(sp.re(z)) for z in roots if abs(float(sp.im(z)))<1e-9 and .5<float(sp.re(z))<2/3)
    nn=3001
    a=min(range(1,nn),key=lambda gap: float(score(nn,gap,Fraction(str(cfloat))/nn)))
    assert abs(a/nn-root)<.002,(cc,a/nn,root)
print('Five finite-size scaling confirmations: PASS')
print('All mathematical verification checks passed')
