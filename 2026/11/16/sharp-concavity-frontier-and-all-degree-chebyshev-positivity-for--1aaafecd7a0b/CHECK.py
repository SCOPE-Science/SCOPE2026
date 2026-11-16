#!/usr/bin/env python3
"""Standalone finite consistency checks for the arcsine-power circle-lift theorem.

The universal inequalities follow from the analytic proof, not these samples.
Requires sympy and mpmath.
"""
import sympy as sp
import mpmath as mp

u=sp.symbols('u', positive=True)
h3=u**3*sp.cos(u)/sp.sin(u)**3
assert sp.trigsimp(h3 + (u**3/sp.Integer(2))*sp.diff(sp.sin(u)**(-2),u)) == 0
assert sp.trigsimp(sp.diff(sp.cos(u),u,2)+sp.cos(u)) == 0
q=sp.series(h3,u,0,10).removeO().expand()
assert q.coeff(u,0)==1
assert q.coeff(u,2)==0
assert q.coeff(u,4)==-sp.Rational(1,15)
assert q.coeff(u,6)==-sp.Rational(4,189)
# The sine-power middle point expansion forces the sharp t=3 concavity boundary.
p=sp.symbols('p',real=True)
ht=sp.cos(u)*(u/sp.sin(u))**p
assert sp.simplify(sp.limit(sp.diff(ht,u,2),u,0)) == (p-3)/3

mp.mp.dps=50
count=5
for t in [0,mp.mpf('0.5'),1,mp.mpf('1.5'),2,mp.mpf('2.5'),3]:
 def h(x):return mp.cos(x)*(x/mp.sin(x))**t if x else mp.mpf('1')
 for j in range(1,20):
  x=(mp.pi/2)*j/20
  assert mp.diff(h,x,2)<0,(t,j)
  count+=1
 def g(theta):
  x=(mp.pi-theta)/2
  return h(x)
 total=mp.quad(g,[0,mp.pi])
 for n in range(1,13):
  moment=mp.quad(lambda theta:g(theta)*mp.cos(n*theta),[0,mp.pi])/total
  assert moment<0,(t,n,moment)
  count+=1
# The first cosine moments for the two exactly computable anchor weights.
def cosine_moment(t,n):
 def h(x):return mp.cos(x)*(x/mp.sin(x))**t if x else mp.mpf('1')
 def g(theta):return h((mp.pi-theta)/2)
 return mp.quad(lambda theta:g(theta)*mp.cos(n*theta),[0,mp.pi])/mp.quad(g,[0,mp.pi])
assert abs(cosine_moment(0,1)+mp.mpf(1)/3)<mp.mpf('1e-42')
assert abs(cosine_moment(1,1)-(1/(2*mp.log(2))-1))<mp.mpf('1e-42')
count+=2
print('PASS: {} finite symbolic and numerical checks; universal statements require analytic proof.'.format(count))
