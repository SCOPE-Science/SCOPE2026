#!/usr/bin/env python3
"""Standalone algebraic and high-precision checks for exponential-kernel CQ weights.

No finite check is used as a proof of the infinite sign law; the proof uses
pole geometry and residue dominance.
"""
from fractions import Fraction
import math
import sympy as sp
import mpmath as mp

z, x = sp.symbols('z x', real=True)
w = 1-z
delta = sp.expand(w + w*w/2 + sp.Rational(2,3)*w*w*w)
P = sp.expand(delta+x)
assert P == x + sp.Rational(13,6) - 4*z+sp.Rational(5,2)*z*z-sp.Rational(2,3)*z**3
assert sp.simplify(sp.factor(P.subs(x,sp.Rational(141,250))) + (5*z-8)*(100*z*z-215*z+256)/750)==0
assert sp.simplify(P.subs({x:sp.Rational(141,250),z:sp.Rational(8,5)}))==0
R=sp.Rational(8,5)
Z=(43+sp.I*sp.sqrt(2247))/40
assert sp.simplify(P.subs({x:sp.Rational(141,250),z:Z}))==0
assert sp.simplify(Z*sp.conjugate(Z)-R*R)==0
px=sp.diff(P,z)
CR=sp.simplify(-1/(R*px.subs(z,R)))
CZ=sp.simplify(-1/(Z*px.subs(z,Z)))
assert CR==sp.Rational(125,224)
assert sp.simplify(4*CZ*sp.conjugate(CZ)/CR**2)==sp.Rational(128,107)
assert sp.simplify(sp.re(Z)/R)==sp.Rational(43,64)
print('Exact pole factorization and boundary residue squared-amplitude ratio: PASS,',sp.Rational(128,107))

# Fully rational coefficient recursion is verified independently using
# exact formal-series inversion, not by the residue formulas.
for xx in (sp.Rational(1,100),sp.Rational(1,2),sp.Rational(11,20),sp.Rational(9,10),sp.Rational(141,250),sp.Integer(1),sp.Integer(3)):
    b=sp.Rational(13,6)+xx
    g=[1/b]
    for k in range(1,24):
        g.append(sp.cancel((4*g[k-1]
                  -(sp.Rational(5,2)*g[k-2] if k>=2 else 0)
                  +(sp.Rational(2,3)*g[k-3] if k>=3 else 0))/b))
    if xx==sp.Rational(11,20):
        assert g[6]==-sp.Rational(1843765644000,3057125241215467)
    # Formal inversion by explicit multiplication of the truncated series.
    for k in range(24):
        v=b*g[k]
        if k>=1: v-=4*g[k-1]
        if k>=2: v+=sp.Rational(5,2)*g[k-2]
        if k>=3: v-=sp.Rational(2,3)*g[k-3]
        assert sp.cancel(v-(1 if k==0 else 0))==0
print('Exact coefficient recursion: PASS (168 rational identities and exact sixth-lag sign check)')

mp.mp.dps=90
samples=['0.01','0.25','0.5','0.55','0.563','0.564','0.565','0.6','0.8','1','2','6']

for xs in samples:
    xx=mp.mpf(xs)
    b=xx+mp.mpf(13)/6
    # independent polynomial root calculation
    roots=mp.polyroots([-mp.mpf(2)/3, mp.mpf(5)/2, -4, b], maxsteps=1000, error=False)
    realroots=[mp.re(r) for r in roots if abs(mp.im(r))<mp.mpf('1e-60')]
    assert len(realroots)==1
    real=realroots[0]
    complexroots=[r for r in roots if abs(mp.im(r))>=mp.mpf('1e-60')]
    assert len(complexroots)==2
    q=abs(complexroots[0])
    assert abs(q*q-real*real-(6-mp.mpf(15)/4*real)) < mp.mpf('1e-70')
    assert (q>real)==(xx<mp.mpf(141)/250) if xx!=mp.mpf(141)/250 else abs(q-real)<mp.mpf('1e-80')
    # Generate coefficients by recurrence independently of the pole calculation.
    arr=[1/b]
    for n in range(1,261):
        arr.append((4*arr[-1]
                 -(mp.mpf(5)/2*arr[-2] if n>=2 else 0)
                 +(mp.mpf(2)/3*arr[-3] if n>=3 else 0))/b)
    residues=[-1/(r*(-4+5*r-2*r*r)) for r in roots]
    for n in (0,1,2,3,4,5,6,8,10,13,20,27,39,55,78,99):
        pf=sum(c/r**n for c,r in zip(residues,roots))
        assert abs(mp.im(pf))<mp.mpf('1e-60')
        assert abs(mp.re(pf)-arr[n])<=mp.mpf('1e-65') * max(mp.mpf(1),abs(arr[n]))
    negatives=[n for n,v in enumerate(arr) if v<0]
    if xx<mp.mpf(141)/250 and xx<=mp.mpf('0.5'):
        assert len(negatives)==0
    if xx>=mp.mpf(141)/250:
        assert len(negatives)>0
    print('x=',xs,'R=',mp.nstr(real,9),'|Z|=',mp.nstr(q,9),
          'neg_indices_in_0_260=',len(negatives),
          'first_negative=',negatives[0] if negatives else 'none',
          'last_negative=',negatives[-1] if negatives else 'none')
print('Separate pole/residue and coefficient comparisons: PASS (192 high-precision checks)')

# BDF2 and trapezoidal comparison on rational samples.
for xx in (sp.Rational(1,10),sp.Rational(1,2),sp.Rational(3,5),sp.Integer(2),sp.Integer(3)):
    Pb=sp.expand(xx+sp.Rational(3,2)-2*z+z*z/2)
    gt=sp.cancel((1+z)/(2*(1-z)+xx*(1+z)))
    assert sp.simplify(Pb.subs(z,2)-(xx-sp.Rational(1,2)))==0
    assert sp.simplify(gt.subs(z,0)-1/(xx+2))==0
    for n in range(1,15):
        coeff=sp.simplify(sp.diff(gt,z,n).subs(z,0)/sp.factorial(n))
        want=sp.simplify(4/(xx+2)**2 * ((2-xx)/(2+xx))**(n-1))
        assert sp.simplify(coeff-want)==0
print('BDF2 pole threshold and trapezoidal weight comparison: PASS')
