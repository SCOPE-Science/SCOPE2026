#!/usr/bin/env python3
"""Independent algebra and finite diagnostic checks for the stated two-pool model.

The universal classification is established in RESULT.md; floating computations here
are illustrative checks and are not used as proofs of quantification over parameters.
"""
import sympy as sp
import mpmath as mp
from fractions import Fraction

z, chi, t = sp.symbols('z chi t', positive=True, real=True)
E = sp.sinh(z) / (sp.cosh(z) + chi)
assert sp.simplify(sp.diff(E, z) - (1 + chi * sp.cosh(z)) / (sp.cosh(z) + chi)**2) == 0
assert sp.simplify(sp.diff(E,z,2) - sp.sinh(z) * (chi**2 - 2 - chi*sp.cosh(z)) / (sp.cosh(z) + chi)**3) == 0
assert sp.simplify(sp.limit(E/z,z,0) - 1/(1+chi)) == 0
u, a, center, sep = sp.symbols('u a center sep', real=True, positive=True)
sig = lambda w: 1/(1+sp.exp(-w))
assert sp.cancel((sig(u+sep)+sig(u-sep)-1-sp.sinh(u)/(sp.cosh(u)+sp.cosh(sep))).rewrite(sp.exp)) == 0

# Exact rational five-equilibrium certificate: choose z=log(9), chi=5, amplitude=5.
assert Fraction(5*20,43) > Fraction(9,4)
partial = sum((Fraction(9,4)**j / sp.factorial(j) for j in range(6)), sp.Rational(0))
assert partial > 9
assert Fraction(5,6)-1 < 0

mp.mp.dps=75

def ex(u,c):return mp.sinh(u)/(mp.cosh(u)+c)
def gain(u,c,A):return A*ex(u,c)-u
def crit(c):
    z0=mp.acosh(c-2/c)
    j=lambda x: x*(1+c*mp.cosh(x))-mp.sinh(x)*(mp.cosh(x)+c)
    lo=z0+mp.mpf('0.001')
    hi=max(z0+4,mp.mpf(40))
    assert j(lo)>0 and j(hi)<0
    for _ in range(300):
        mid=(lo+hi)/2
        if j(mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

# The five-root window and the absence of five roots outside it.
for c in [mp.mpf('2.01'), mp.mpf('3'), mp.mpf('5'), mp.mpf('9')]:
    zstar=crit(c)
    rstar=ex(zstar,c)/zstar
    amin=1/rstar
    amax=1+c
    assert amin<amax
    for A, expected in [(amin*mp.mpf('.9'),0),((amin+amax)/2,2),(amax*mp.mpf('1.1'),1)]:
        roots=[]
        grid=[mp.mpf(i)/50 for i in range(1,int(50*max(3,A))+1)]
        for u0,u1 in zip(grid,grid[1:]):
            if gain(u0,c,A)*gain(u1,c,A)<0:
                root=mp.findroot(lambda u:gain(u,c,A),(u0,u1))
                if not any(abs(root-v)<mp.mpf('1e-30') for v in roots): roots.append(root)
        assert len(roots)==expected,(c,A,len(roots),expected)

assert gain(mp.log(9),5,5)>0
assert gain(5,5,5)<0
r1=mp.findroot(lambda u:gain(u,5,5),(1,2))
r2=mp.findroot(lambda u:gain(u,5,5),(4,5))
assert 1<r1<2 and 4<r2<5
slope=lambda u: 5* (1+5*mp.cosh(u))/(mp.cosh(u)+5)**2-1
assert slope(0)<0 and slope(r1)>0 and slope(r2)<0
print('PASS: symbolic identities, exact five-equilibrium witness, and finite numerical phase/stability diagnostics')
print('Illustrative positive roots:',mp.nstr(r1,20),mp.nstr(r2,20))
