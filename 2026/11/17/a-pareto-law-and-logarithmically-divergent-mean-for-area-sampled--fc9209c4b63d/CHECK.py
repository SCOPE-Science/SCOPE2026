#!/usr/bin/env python3
"""Independent algebraic and numerical checks of an exact area-period ensemble law."""
import sympy as sp
import mpmath as mp
x, y, k = sp.symbols('x y k', real=True)
F = x*x + y*y + k*x*x*y*y
vx = y*(1+k*x*x)
vy = -x*(1+k*y*y)
assert sp.simplify(sp.diff(F,x)*vx+sp.diff(F,y)*vy) == 0
assert sp.simplify(vx-sp.diff(F,y)/2) == 0
assert sp.simplify(vy+sp.diff(F,x)/2) == 0
mp.mp.dps=35
for kap in [mp.mpf('0.6'), mp.mpf('1.0'), mp.mpf('2.5')]:
 for A in [mp.mpf('0.2'),mp.mpf('1.1'),mp.mpf('3'),mp.mpf('15')]:
  z=kap*A*A
  T=4*mp.ellipk(-z)
  S=4/kap*((1+z)*mp.ellipk(-z)-mp.ellipe(-z))
  I=4*mp.quad(lambda xx:mp.sqrt((A*A-xx*xx)/(1+kap*xx*xx)),[0,A/2,A])
  assert mp.almosteq(S,I,rel_eps=mp.mpf('1e-25'))
  assert mp.almosteq(mp.diff(lambda a: 4/kap*((1+kap*a*a)*mp.ellipk(-kap*a*a)-mp.ellipe(-kap*a*a)),A),A*T,rel_eps=mp.mpf('1e-25'))
for R in [mp.mpf('1e3'),mp.mpf('1e5')]:
 z=R*R;B=R
 T=4*mp.ellipk(-z)
 S=4*((1+z)*mp.ellipk(-z)-mp.ellipe(-z))
 assert mp.mpf('0.8')<T/(4*mp.log(B)/B)<mp.mpf('1.3')
 assert mp.mpf('0.8')<S/(4*B*mp.log(B))<mp.mpf('1.1')
print('CUBIC_AREA_PARETO_IDENTITIES_OK')
