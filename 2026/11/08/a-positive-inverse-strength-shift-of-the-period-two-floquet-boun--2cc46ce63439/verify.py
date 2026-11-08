#!/usr/bin/env python3
"""Supplementary arithmetic checks for the strong-predation two-cycle asymptotics.
Scientific proof and hypotheses are in RESULT.md; these finite checks do not replace it.
"""
import math
import mpmath as mp
mp.mp.dps=60

def p_of(t): return 2*t*mp.coth(t)
def p_prime(t): return 2*(mp.coth(t)-t/(mp.sinh(t)**2))
def p_double(t): return 4/(mp.sinh(t)**2)*(t*mp.coth(t)-1)
thstar=mp.findroot(lambda t:t*p_prime(t)-1,(mp.mpf('.7'),mp.mpf('1.1')))
pstar=p_of(thstar)
assert mp.mpf('2.5264677258538') < pstar < mp.mpf('2.5264677258539')
for t in [mp.mpf('0.2'),mp.mpf('.5'),mp.mpf('1'),mp.mpf('2')]:
 p=p_of(t)
 M=(1-p)**2-(2*t)**2
 assert abs(M-(1-2*t*p_prime(t)))<mp.mpf('1e-55')
 assert p_prime(t)>0 and p_double(t)>0
for p0 in [mp.mpf('2.1'),mp.mpf('2.4'),mp.mpf('2.8'),mp.mpf('3.5')]:
 t=mp.findroot(lambda a:p_of(a)-p0,(mp.mpf('.2'),mp.mpf('2')))
 dlim=2*t
 for q in [mp.mpf('100'),mp.mpf('10000'),mp.mpf('1000000')]:
  q0=p0*p0/(p0-2)
  if q<=q0:continue
  def q_of(d):
   u=d/2-mp.atanh(d/p0)
   return p0+d/mp.tanh(u)
  lo=mp.mpf('0'); hi=dlim
  for _ in range(250):
   md=(lo+hi)/2
   if q_of(md)>q: hi=md
   else: lo=md
  d=(lo+hi)/2
  x=mp.log((q-p0-d)/(p0+d)); y=x+d
  f=lambda z:z-p0+q/(1+mp.exp(z))
  assert abs(f(x)-y)<mp.mpf('1e-45')
  assert abs(f(y)-x)<mp.mpf('1e-45')
  mul=(1-(p0+d)+(p0+d)**2/q)*(1-(p0-d)+(p0-d)**2/q)
  assert abs(mul-((1-q*mp.exp(x)/(1+mp.exp(x))**2)*(1-q*mp.exp(y)/(1+mp.exp(y))**2)))<mp.mpf('1e-45')
  if q>=1000000:
   assert abs(mul-((1-p0)**2-dlim**2))<mp.mpf('.0005')
 print('p=',mp.nstr(p0,5),'infty_m=',mp.nstr((1-p0)**2-dlim**2,12))
print('VERIFY_OK analytic_identities=4 convexity=4 exact_period_two_equations=12 limit_multipliers=4 threshold=',mp.nstr(pstar,18))
# Verify the first finite-q correction to the Ricker-limit flip boundary.
pprime=p_prime(thstar)
pdouble=p_double(thstar)
cstar=4*(pstar**3-3*pstar**2+4*pstar-1)
slope=cstar/(2*(1+thstar*pdouble/pprime))

def theta_for(p):
 return mp.findroot(lambda t:p_of(t)-p,(mp.mpf('0.1'),mp.mpf('2')))
def d_from(p,q):
 high=2*theta_for(p); low=mp.mpf('0')
 for _ in range(225):
  md=(high+low)/2
  u=md/2-mp.atanh(md/p)
  qp=p+md/mp.tanh(u)
  if qp>q:high=md
  else:low=md
 return (high+low)/2
def mul_from(p,q):
 d=d_from(p,q)
 return (1-(p+d)+(p+d)**2/q)*(1-(p-d)+(p-d)**2/q)
for q in [mp.mpf('100'),mp.mpf('1000'),mp.mpf('10000'),mp.mpf('100000')]:
 critical=mp.findroot(lambda p:mul_from(p,q)+1,(pstar+slope/q*.8,pstar+slope/q*1.2))
 assert critical>pstar
 assert abs(q*(critical-pstar)-slope)<mp.mpf('50')/q
print('VERIFY_OK flip_curve_asymptotic=4 ricker_limit=1 positive_shift=1 slope=',mp.nstr(slope,18))
